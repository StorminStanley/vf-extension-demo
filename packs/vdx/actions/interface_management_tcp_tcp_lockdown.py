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


def interface_management_tcp_tcp_lockdown(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    management = ET.SubElement(interface, "management")
    if kwargs.pop('delete_management', False) is True:
        delete_management = config.find('.//*management')
        delete_management.set('operation', 'delete')
        
    name_key = ET.SubElement(management, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    tcp = ET.SubElement(management, "tcp")
    if kwargs.pop('delete_tcp', False) is True:
        delete_tcp = config.find('.//*tcp')
        delete_tcp.set('operation', 'delete')
        
    tcp_lockdown = ET.SubElement(tcp, "tcp_lockdown")
    if kwargs.pop('delete_tcp_lockdown', False) is True:
        delete_tcp_lockdown = config.find('.//*tcp_lockdown')
        delete_tcp_lockdown.set('operation', 'delete')
        
    tcp_lockdown.text = kwargs.pop('tcp_lockdown')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_management_tcp_tcp_lockdown_act(Action):
    def run(self, name, delete_tcp, delete_interface, delete_name, delete_management, delete_tcp_lockdown, tcp_lockdown, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_management_tcp_tcp_lockdown(name=name, delete_name=delete_name, delete_management=delete_management, delete_tcp=delete_tcp, host=host, tcp_lockdown=tcp_lockdown, delete_tcp_lockdown=delete_tcp_lockdown, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    