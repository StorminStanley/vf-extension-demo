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


def protocol_udld_hello(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    udld = ET.SubElement(protocol, "udld", xmlns="urn:brocade.com:mgmt:brocade-udld")
    if kwargs.pop('delete_udld', False) is True:
        delete_udld = config.find('.//*udld')
        delete_udld.set('operation', 'delete')
        
    hello = ET.SubElement(udld, "hello")
    if kwargs.pop('delete_hello', False) is True:
        delete_hello = config.find('.//*hello')
        delete_hello.set('operation', 'delete')
        
    hello.text = kwargs.pop('hello')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_udld_hello_act(Action):
    def run(self, delete_hello, delete_udld, hello, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_udld_hello(delete_hello=delete_hello, username=username, delete_protocol=delete_protocol, delete_udld=delete_udld, host=host, hello=hello, password=password, callback=_callback, mgr=mgr)
        return 0
    