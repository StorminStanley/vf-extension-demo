#!/usr/bin/env python2
"""YANG StackStorm Action Auto-Generation
"""
import inspect
import re
import yaml
from autocode.brocade_rbridge import brocade_rbridge
from autocode.brocade_interface import brocade_interface

ITEMS = list()
ITEMS.extend(inspect.getmembers(brocade_rbridge, predicate=inspect.ismethod))
ITEMS.extend(inspect.getmembers(brocade_interface, predicate=inspect.ismethod))
for item in ITEMS:
    if item[0] is '__init__':
        continue

    source = inspect.getsource(item[1])
    args = re.findall('kwargs.pop\(\'([_A-z]+)\'', source) # pylint: disable=anomalous-backslash-in-string,line-too-long
    args.remove('callback')
    args = list(set(args))
    args.extend(['host', 'username', 'password'])
    if 'timeout' in args:
        args.pop(args.index('timeout'))
        args.append('timeout_ag')
    params = dict()
    code_params = list()
    count = 0
    for arg in args:
        if 'delete_' not in arg:
            params[arg] = dict(
                type='string',
                description='Auto generated parameter.',
                required=True,
                position=count
            )
            code_params.append("%s=%s" % (arg, arg))
            count += 1
        else:
            params["%s" % arg] = dict(
                type='boolean',
                description='Auto generated parameter.',
                required=False,
                position=count
            )
            count += 1
            code_params.append("%s=%s" % (arg, arg))

    ss_action = dict(
        name=item[0],
        runner_type='python-script',
        description='Auto generated action.',
        enabled=True,
        entry_point='%s.py' % item[0],
        parameters=params
    )
    source = source.split('\n')
    code_params = list(set(code_params))
    for count, line in enumerate(source):
        source[count] = line[4:]
        source[count] = source[count].replace('return callback(config)',
                                              "return callback(config, mgr=kwargs.pop('mgr'))")
        source[count] = source[count].replace('self._callback', '_callback')
        if count == 0:
            source[count] = line[4:-16]
            source[count] += '**kwargs):'


    source = '\n'.join(source)

    code = """import sys
from ncclient import manager
from ncclient import xml_
import ncclient
from st2actions.runners.pythonrunner import Action
from xml.etree import ElementTree as ET



def _callback(call, handler='edit_config', target='running', source='startup', mgr=None):
    try:
        call = ET.tostring(call)
        if handler == 'get':
            call_element = xml_.to_ele(call)
            return ET.fromstring(str(mgr.dispatch(call_element)))
        if handler == 'edit_config':
            mgr.edit_config(target=target, config=call)
        if handler == 'delete_config':
            mgr.delete_config(target=target)
        if handler == 'copy_config':
            mgr.copy_config(target=target, source=source)
    except (ncclient.transport.TransportError,
            ncclient.transport.SessionCloseError,
            ncclient.transport.SSHError,
            ncclient.transport.AuthenticationError,
            ncclient.transport.SSHUnknownHostError) as error:
        logging.error(error)
        raise DeviceCommError


%s
class %s_act(Action):
    def run(self, %s):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.timeout = 600
        %s(%s, callback=_callback, mgr=mgr)
        return 0
    """ % (source,
           item[0],
           ', '.join(args),
           item[0],
           ', '.join(code_params))
    code = code.replace('timeout', 'agtimeout')
    with open("actions/%s.yaml" % item[0], 'w+') as yaml_file:
        yaml_file.write("---\n" + yaml.dump(ss_action, default_flow_style=False))

    with open("actions/%s.py" % item[0], 'w+') as py_file:
        py_file.write(code)
print 'Done'
