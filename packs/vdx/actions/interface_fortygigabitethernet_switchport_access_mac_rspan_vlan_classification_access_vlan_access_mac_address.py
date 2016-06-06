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


def interface_fortygigabitethernet_switchport_access_mac_rspan_vlan_classification_access_vlan_access_mac_address(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    switchport = ET.SubElement(fortygigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    access_mac_rspan_vlan_classification = ET.SubElement(switchport, "access-mac-rspan-vlan-classification")
    if kwargs.pop('delete_access_mac_rspan_vlan_classification', False) is True:
        delete_access_mac_rspan_vlan_classification = config.find('.//*access-mac-rspan-vlan-classification')
        delete_access_mac_rspan_vlan_classification.set('operation', 'delete')
        
    access = ET.SubElement(access_mac_rspan_vlan_classification, "access")
    if kwargs.pop('delete_access', False) is True:
        delete_access = config.find('.//*access')
        delete_access.set('operation', 'delete')
        
    vlan = ET.SubElement(access, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
    access_vlan_id_key.text = kwargs.pop('access_vlan_id')
    if kwargs.pop('delete_access_vlan_id', False) is True:
        delete_access_vlan_id = config.find('.//*access-vlan-id')
        delete_access_vlan_id.set('operation', 'delete')
            
    access_mac_address = ET.SubElement(vlan, "access-mac-address")
    if kwargs.pop('delete_access_mac_address', False) is True:
        delete_access_mac_address = config.find('.//*access-mac-address')
        delete_access_mac_address.set('operation', 'delete')
        
    access_mac_address.text = kwargs.pop('access_mac_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_switchport_access_mac_rspan_vlan_classification_access_vlan_access_mac_address_act(Action):
    def run(self, delete_switchport, delete_vlan, delete_access_vlan_id, name, access_mac_address, delete_fortygigabitethernet, delete_access_mac_rspan_vlan_classification, delete_access, delete_access_mac_address, access_vlan_id, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_switchport_access_mac_rspan_vlan_classification_access_vlan_access_mac_address(delete_access=delete_access, name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_switchport=delete_switchport, username=username, access_vlan_id=access_vlan_id, delete_access_vlan_id=delete_access_vlan_id, delete_vlan=delete_vlan, host=host, delete_access_mac_rspan_vlan_classification=delete_access_mac_rspan_vlan_classification, delete_name=delete_name, access_mac_address=access_mac_address, delete_access_mac_address=delete_access_mac_address, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    