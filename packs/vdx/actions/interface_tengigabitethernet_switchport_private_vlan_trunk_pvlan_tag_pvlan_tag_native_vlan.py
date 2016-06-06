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


def interface_tengigabitethernet_switchport_private_vlan_trunk_pvlan_tag_pvlan_tag_native_vlan(**kwargs):
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
        
    private_vlan = ET.SubElement(switchport, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    trunk = ET.SubElement(private_vlan, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    pvlan_tag = ET.SubElement(trunk, "pvlan-tag")
    if kwargs.pop('delete_pvlan_tag', False) is True:
        delete_pvlan_tag = config.find('.//*pvlan-tag')
        delete_pvlan_tag.set('operation', 'delete')
        
    pvlan_tag_native_vlan = ET.SubElement(pvlan_tag, "pvlan-tag-native-vlan")
    if kwargs.pop('delete_pvlan_tag_native_vlan', False) is True:
        delete_pvlan_tag_native_vlan = config.find('.//*pvlan-tag-native-vlan')
        delete_pvlan_tag_native_vlan.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_private_vlan_trunk_pvlan_tag_pvlan_tag_native_vlan_act(Action):
    def run(self, delete_switchport, delete_pvlan_tag_native_vlan, name, delete_trunk, delete_private_vlan, delete_interface, delete_name, delete_tengigabitethernet, delete_pvlan_tag, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_private_vlan_trunk_pvlan_tag_pvlan_tag_native_vlan(name=name, delete_trunk=delete_trunk, delete_switchport=delete_switchport, username=username, delete_name=delete_name, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_private_vlan=delete_private_vlan, delete_pvlan_tag_native_vlan=delete_pvlan_tag_native_vlan, delete_interface=delete_interface, delete_pvlan_tag=delete_pvlan_tag, password=password, callback=_callback, mgr=mgr)
        return 0
    