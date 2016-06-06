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


def interface_tengigabitethernet_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id(**kwargs):
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
        
    access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
    if kwargs.pop('delete_access_mac_group_vlan_classification', False) is True:
        delete_access_mac_group_vlan_classification = config.find('.//*access-mac-group-vlan-classification')
        delete_access_mac_group_vlan_classification.set('operation', 'delete')
        
    access = ET.SubElement(access_mac_group_vlan_classification, "access")
    if kwargs.pop('delete_access', False) is True:
        delete_access = config.find('.//*access')
        delete_access.set('operation', 'delete')
        
    vlan = ET.SubElement(access, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    access_mac_group_key = ET.SubElement(vlan, "access-mac-group")
    access_mac_group_key.text = kwargs.pop('access_mac_group')
    if kwargs.pop('delete_access_mac_group', False) is True:
        delete_access_mac_group = config.find('.//*access-mac-group')
        delete_access_mac_group.set('operation', 'delete')
            
    access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
    if kwargs.pop('delete_access_vlan_id', False) is True:
        delete_access_vlan_id = config.find('.//*access-vlan-id')
        delete_access_vlan_id.set('operation', 'delete')
        
    access_vlan_id.text = kwargs.pop('access_vlan_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id_act(Action):
    def run(self, delete_switchport, delete_vlan, access_mac_group, delete_access_vlan_id, name, delete_access_mac_group, delete_access_mac_group_vlan_classification, delete_access, access_vlan_id, delete_interface, delete_name, delete_tengigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id(delete_access=delete_access, name=name, delete_name=delete_name, username=username, delete_switchport=delete_switchport, delete_access_mac_group_vlan_classification=delete_access_mac_group_vlan_classification, access_vlan_id=access_vlan_id, delete_access_vlan_id=delete_access_vlan_id, delete_vlan=delete_vlan, delete_tengigabitethernet=delete_tengigabitethernet, delete_access_mac_group=delete_access_mac_group, host=host, delete_interface=delete_interface, access_mac_group=access_mac_group, password=password, callback=_callback, mgr=mgr)
        return 0
    