import sys
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


def rbridge_id_ipv6_ipv6_global_cmds_nd_global_dad_global_dad_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_global_cmds = ET.SubElement(ipv6, "ipv6-global-cmds", xmlns="urn:brocade.com:mgmt:brocade-ipv6-nd-ra")
    if kwargs.pop('delete_ipv6_global_cmds', False) is True:
        delete_ipv6_global_cmds = config.find('.//*ipv6-global-cmds')
        delete_ipv6_global_cmds.set('operation', 'delete')
        
    nd_global = ET.SubElement(ipv6_global_cmds, "nd-global")
    if kwargs.pop('delete_nd_global', False) is True:
        delete_nd_global = config.find('.//*nd-global')
        delete_nd_global.set('operation', 'delete')
        
    dad = ET.SubElement(nd_global, "dad")
    if kwargs.pop('delete_dad', False) is True:
        delete_dad = config.find('.//*dad')
        delete_dad.set('operation', 'delete')
        
    global_dad_time = ET.SubElement(dad, "global-dad-time")
    if kwargs.pop('delete_global_dad_time', False) is True:
        delete_global_dad_time = config.find('.//*global-dad-time')
        delete_global_dad_time.set('operation', 'delete')
        
    global_dad_time.text = kwargs.pop('global_dad_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_ipv6_global_cmds_nd_global_dad_global_dad_time_act(Action):
    def run(self, rbridge_id, global_dad_time, delete_global_dad_time, delete_nd_global, delete_dad, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_ipv6_global_cmds_nd_global_dad_global_dad_time(delete_nd_global=delete_nd_global, username=username, rbridge_id=rbridge_id, host=host, global_dad_time=global_dad_time, delete_dad=delete_dad, delete_rbridge_id=delete_rbridge_id, delete_global_dad_time=delete_global_dad_time, password=password, callback=_callback, mgr=mgr)
        return 0
    