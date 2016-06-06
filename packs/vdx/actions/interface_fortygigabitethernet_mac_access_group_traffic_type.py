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


def interface_fortygigabitethernet_mac_access_group_traffic_type(**kwargs):
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
            
    mac = ET.SubElement(fortygigabitethernet, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
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
            
    mac_direction_key = ET.SubElement(access_group, "mac-direction")
    mac_direction_key.text = kwargs.pop('mac_direction')
    if kwargs.pop('delete_mac_direction', False) is True:
        delete_mac_direction = config.find('.//*mac-direction')
        delete_mac_direction.set('operation', 'delete')
            
    traffic_type = ET.SubElement(access_group, "traffic-type")
    if kwargs.pop('delete_traffic_type', False) is True:
        delete_traffic_type = config.find('.//*traffic-type')
        delete_traffic_type.set('operation', 'delete')
        
    traffic_type.text = kwargs.pop('traffic_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_mac_access_group_traffic_type_act(Action):
    def run(self, name, mac_access_list, delete_fortygigabitethernet, delete_mac_access_list, delete_access_group, delete_name, traffic_type, delete_traffic_type, delete_interface, delete_mac_direction, mac_direction, delete_mac, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_mac_access_group_traffic_type(traffic_type=traffic_type, delete_traffic_type=delete_traffic_type, name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_name=delete_name, delete_access_group=delete_access_group, delete_mac_access_list=delete_mac_access_list, mac_direction=mac_direction, host=host, delete_mac_direction=delete_mac_direction, mac_access_list=mac_access_list, delete_interface=delete_interface, username=username, delete_mac=delete_mac, password=password, callback=_callback, mgr=mgr)
        return 0
    