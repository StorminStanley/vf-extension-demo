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


def interface_port_channel_switchport_port_security_port_sec_violation(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    switchport = ET.SubElement(port_channel, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    port_security = ET.SubElement(switchport, "port-security")
    if kwargs.pop('delete_port_security', False) is True:
        delete_port_security = config.find('.//*port-security')
        delete_port_security.set('operation', 'delete')
        
    port_sec_violation = ET.SubElement(port_security, "port-sec-violation")
    if kwargs.pop('delete_port_sec_violation', False) is True:
        delete_port_sec_violation = config.find('.//*port-sec-violation')
        delete_port_sec_violation.set('operation', 'delete')
        
    port_sec_violation.text = kwargs.pop('port_sec_violation')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_switchport_port_security_port_sec_violation_act(Action):
    def run(self, delete_switchport, port_sec_violation, name, delete_port_channel, delete_port_sec_violation, delete_interface, delete_name, delete_port_security, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_switchport_port_security_port_sec_violation(name=name, delete_name=delete_name, delete_switchport=delete_switchport, delete_port_sec_violation=delete_port_sec_violation, delete_port_channel=delete_port_channel, host=host, delete_port_security=delete_port_security, port_sec_violation=port_sec_violation, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    