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


def interface_tengigabitethernet_ip_acl_interface_ip_access_group_traffic_type(**kwargs):
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
            
    ip_acl_interface = ET.SubElement(tengigabitethernet, "ip-acl-interface", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
    if kwargs.pop('delete_ip_acl_interface', False) is True:
        delete_ip_acl_interface = config.find('.//*ip-acl-interface')
        delete_ip_acl_interface.set('operation', 'delete')
        
    ip = ET.SubElement(ip_acl_interface, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    access_group = ET.SubElement(ip, "access-group")
    if kwargs.pop('delete_access_group', False) is True:
        delete_access_group = config.find('.//*access-group')
        delete_access_group.set('operation', 'delete')
        
    ip_access_list_key = ET.SubElement(access_group, "ip-access-list")
    ip_access_list_key.text = kwargs.pop('ip_access_list')
    if kwargs.pop('delete_ip_access_list', False) is True:
        delete_ip_access_list = config.find('.//*ip-access-list')
        delete_ip_access_list.set('operation', 'delete')
            
    ip_direction_key = ET.SubElement(access_group, "ip-direction")
    ip_direction_key.text = kwargs.pop('ip_direction')
    if kwargs.pop('delete_ip_direction', False) is True:
        delete_ip_direction = config.find('.//*ip-direction')
        delete_ip_direction.set('operation', 'delete')
            
    traffic_type = ET.SubElement(access_group, "traffic-type")
    if kwargs.pop('delete_traffic_type', False) is True:
        delete_traffic_type = config.find('.//*traffic-type')
        delete_traffic_type.set('operation', 'delete')
        
    traffic_type.text = kwargs.pop('traffic_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ip_acl_interface_ip_access_group_traffic_type_act(Action):
    def run(self, name, delete_ip, ip_access_list, delete_ip_direction, delete_ip_acl_interface, delete_interface, delete_name, delete_traffic_type, ip_direction, delete_tengigabitethernet, traffic_type, delete_ip_access_list, delete_access_group, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ip_acl_interface_ip_access_group_traffic_type(delete_traffic_type=delete_traffic_type, traffic_type=traffic_type, name=name, delete_name=delete_name, delete_ip_acl_interface=delete_ip_acl_interface, delete_access_group=delete_access_group, delete_ip=delete_ip, ip_access_list=ip_access_list, delete_ip_access_list=delete_ip_access_list, delete_ip_direction=delete_ip_direction, host=host, delete_tengigabitethernet=delete_tengigabitethernet, delete_interface=delete_interface, username=username, ip_direction=ip_direction, password=password, callback=_callback, mgr=mgr)
        return 0
    