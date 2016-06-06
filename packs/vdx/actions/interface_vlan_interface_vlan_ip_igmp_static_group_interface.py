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


def interface_vlan_interface_vlan_ip_igmp_static_group_interface(**kwargs):
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
            
    ip = ET.SubElement(vlan, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    igmp = ET.SubElement(ip, "igmp", xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping")
    if kwargs.pop('delete_igmp', False) is True:
        delete_igmp = config.find('.//*igmp')
        delete_igmp.set('operation', 'delete')
        
    static_group = ET.SubElement(igmp, "static-group")
    if kwargs.pop('delete_static_group', False) is True:
        delete_static_group = config.find('.//*static-group')
        delete_static_group.set('operation', 'delete')
        
    mcast_address_key = ET.SubElement(static_group, "mcast-address")
    mcast_address_key.text = kwargs.pop('mcast_address')
    if kwargs.pop('delete_mcast_address', False) is True:
        delete_mcast_address = config.find('.//*mcast-address')
        delete_mcast_address.set('operation', 'delete')
            
    if_type_key = ET.SubElement(static_group, "if-type")
    if_type_key.text = kwargs.pop('if_type')
    if kwargs.pop('delete_if_type', False) is True:
        delete_if_type = config.find('.//*if-type')
        delete_if_type.set('operation', 'delete')
            
    value_key = ET.SubElement(static_group, "value")
    value_key.text = kwargs.pop('value')
    if kwargs.pop('delete_value', False) is True:
        delete_value = config.find('.//*value')
        delete_value.set('operation', 'delete')
            
    interface = ET.SubElement(static_group, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    interface.text = kwargs.pop('interface')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_ip_igmp_static_group_interface_act(Action):
    def run(self, delete_vlan, name, delete_ip, delete_mcast_address, delete_interface_vlan, mcast_address, value, delete_if_type, delete_igmp, delete_interface, delete_name, if_type, interface, delete_static_group, delete_value, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_ip_igmp_static_group_interface(mcast_address=mcast_address, name=name, delete_name=delete_name, delete_value=delete_value, username=username, delete_vlan=delete_vlan, if_type=if_type, delete_ip=delete_ip, delete_static_group=delete_static_group, delete_igmp=delete_igmp, delete_interface_vlan=delete_interface_vlan, host=host, interface=interface, value=value, delete_mcast_address=delete_mcast_address, delete_if_type=delete_if_type, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    