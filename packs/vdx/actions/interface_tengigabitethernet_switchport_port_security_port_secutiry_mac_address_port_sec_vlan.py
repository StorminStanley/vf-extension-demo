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


def interface_tengigabitethernet_switchport_port_security_port_secutiry_mac_address_port_sec_vlan(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    tengigabitethernet = ET.SubElement(interface, "tengigabitethernet")
    if kwargs.pop('delete_tengigabitethernet', False) is True:
        delete_tengigabitethernet = config.find('.//*tengigabitethernet')
        delete_tengigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(tengigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    switchport = ET.SubElement(tengigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    port_security = ET.SubElement(switchport, "port-security")
    if kwargs.pop('delete_port_security', False) is True:
        delete_port_security = config.find('.//*port-security')
        delete_port_security.set('operation', 'delete')
        
    port_secutiry_mac_address = ET.SubElement(port_security, "port-secutiry-mac-address")
    if kwargs.pop('delete_port_secutiry_mac_address', False) is True:
        delete_port_secutiry_mac_address = config.find('.//*port-secutiry-mac-address')
        delete_port_secutiry_mac_address.set('operation', 'delete')
        
    mac_address_key = ET.SubElement(port_secutiry_mac_address, "mac-address")
    mac_address_key.text = kwargs.pop('mac_address')
    if kwargs.pop('delete_mac_address', False) is True:
        delete_mac_address = config.find('.//*mac-address')
        delete_mac_address.set('operation', 'delete')
            
    port_sec_vlan = ET.SubElement(port_secutiry_mac_address, "port-sec-vlan")
    if kwargs.pop('delete_port_sec_vlan', False) is True:
        delete_port_sec_vlan = config.find('.//*port-sec-vlan')
        delete_port_sec_vlan.set('operation', 'delete')
        
    port_sec_vlan.text = kwargs.pop('port_sec_vlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_port_security_port_secutiry_mac_address_port_sec_vlan_act(Action):
    def run(self, delete_switchport, delete_mac_address, name, delete_port_secutiry_mac_address, delete_interface, delete_name, mac_address, port_sec_vlan, delete_tengigabitethernet, delete_port_security, delete_port_sec_vlan, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_port_security_port_secutiry_mac_address_port_sec_vlan(port_sec_vlan=port_sec_vlan, name=name, delete_name=delete_name, delete_switchport=delete_switchport, delete_port_sec_vlan=delete_port_sec_vlan, mac_address=mac_address, password=password, delete_mac_address=delete_mac_address, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_port_security=delete_port_security, delete_interface=delete_interface, username=username, delete_port_secutiry_mac_address=delete_port_secutiry_mac_address, callback=_callback, mgr=mgr)
        return 0
    