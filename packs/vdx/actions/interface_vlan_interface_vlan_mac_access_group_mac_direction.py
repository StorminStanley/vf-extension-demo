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


def interface_vlan_interface_vlan_mac_access_group_mac_direction(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface_vlan = ET.SubElement(config, "interface-vlan", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface_vlan', False) is True:
        delete_interface_vlan = config.find('.//*interface-vlan')
        delete_interface_vlan.set('operation', 'delete')
        
    interface = ET.SubElement(interface_vlan, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    vlan = ET.SubElement(interface, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    name_key = ET.SubElement(vlan, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    mac = ET.SubElement(vlan, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
    if kwargs.pop('delete_mac', False) is True:
        delete_mac = config.find('.//*mac')
        delete_mac.set('operation', 'delete')
        
    access_group = ET.SubElement(mac, "access-group")
    if kwargs.pop('delete_access_group', False) is True:
        delete_access_group = config.find('.//*access-group')
        delete_access_group.set('operation', 'delete')
        
    mac_access_list_key = ET.SubElement(access_group, "mac-access-list")
    mac_access_list_key.text = kwargs.pop('mac_access_list')
    if kwargs.pop('delete_mac_access_list', False) is True:
        delete_mac_access_list = config.find('.//*mac-access-list')
        delete_mac_access_list.set('operation', 'delete')
            
    mac_direction = ET.SubElement(access_group, "mac-direction")
    if kwargs.pop('delete_mac_direction', False) is True:
        delete_mac_direction = config.find('.//*mac-direction')
        delete_mac_direction.set('operation', 'delete')
        
    mac_direction.text = kwargs.pop('mac_direction')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_mac_access_group_mac_direction_act(Action):
    def run(self, delete_vlan, name, delete_interface_vlan, delete_mac_access_list, delete_interface, delete_name, mac_direction, delete_mac_direction, mac_access_list, delete_access_group, delete_mac, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_mac_access_group_mac_direction(name=name, delete_name=delete_name, delete_vlan=delete_vlan, delete_mac=delete_mac, delete_access_group=delete_access_group, delete_mac_access_list=delete_mac_access_list, delete_interface_vlan=delete_interface_vlan, delete_mac_direction=delete_mac_direction, host=host, mac_access_list=mac_access_list, mac_direction=mac_direction, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    