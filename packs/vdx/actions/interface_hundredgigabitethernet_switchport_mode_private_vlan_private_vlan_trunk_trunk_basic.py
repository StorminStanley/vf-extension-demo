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


def interface_hundredgigabitethernet_switchport_mode_private_vlan_private_vlan_trunk_trunk_basic(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    switchport = ET.SubElement(hundredgigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    mode = ET.SubElement(switchport, "mode")
    if kwargs.pop('delete_mode', False) is True:
        delete_mode = config.find('.//*mode')
        delete_mode.set('operation', 'delete')
        
    private_vlan = ET.SubElement(mode, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    private_vlan_trunk = ET.SubElement(private_vlan, "private-vlan-trunk")
    if kwargs.pop('delete_private_vlan_trunk', False) is True:
        delete_private_vlan_trunk = config.find('.//*private-vlan-trunk')
        delete_private_vlan_trunk.set('operation', 'delete')
        
    trunk_basic = ET.SubElement(private_vlan_trunk, "trunk-basic")
    if kwargs.pop('delete_trunk_basic', False) is True:
        delete_trunk_basic = config.find('.//*trunk-basic')
        delete_trunk_basic.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_switchport_mode_private_vlan_private_vlan_trunk_trunk_basic_act(Action):
    def run(self, delete_switchport, name, delete_private_vlan, delete_interface, delete_name, delete_trunk_basic, delete_hundredgigabitethernet, delete_mode, delete_private_vlan_trunk, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_switchport_mode_private_vlan_private_vlan_trunk_trunk_basic(name=name, delete_name=delete_name, delete_switchport=delete_switchport, username=username, delete_mode=delete_mode, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_trunk_basic=delete_trunk_basic, host=host, delete_private_vlan=delete_private_vlan, delete_interface=delete_interface, delete_private_vlan_trunk=delete_private_vlan_trunk, password=password, callback=_callback, mgr=mgr)
        return 0
    