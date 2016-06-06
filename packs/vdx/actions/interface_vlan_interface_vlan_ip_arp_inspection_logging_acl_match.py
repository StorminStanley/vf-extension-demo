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


def interface_vlan_interface_vlan_ip_arp_inspection_logging_acl_match(**kwargs):
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
        
    arp = ET.SubElement(ip, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
    if kwargs.pop('delete_arp', False) is True:
        delete_arp = config.find('.//*arp')
        delete_arp.set('operation', 'delete')
        
    inspection = ET.SubElement(arp, "inspection")
    if kwargs.pop('delete_inspection', False) is True:
        delete_inspection = config.find('.//*inspection')
        delete_inspection.set('operation', 'delete')
        
    logging = ET.SubElement(inspection, "logging")
    if kwargs.pop('delete_logging', False) is True:
        delete_logging = config.find('.//*logging')
        delete_logging.set('operation', 'delete')
        
    acl_match = ET.SubElement(logging, "acl-match")
    if kwargs.pop('delete_acl_match', False) is True:
        delete_acl_match = config.find('.//*acl-match')
        delete_acl_match.set('operation', 'delete')
        
    acl_match.text = kwargs.pop('acl_match')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_ip_arp_inspection_logging_acl_match_act(Action):
    def run(self, delete_vlan, delete_logging, delete_inspection, name, delete_ip, acl_match, delete_interface_vlan, delete_interface, delete_name, delete_acl_match, delete_arp, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_ip_arp_inspection_logging_acl_match(delete_acl_match=delete_acl_match, delete_logging=delete_logging, delete_name=delete_name, delete_vlan=delete_vlan, delete_inspection=delete_inspection, delete_arp=delete_arp, delete_ip=delete_ip, name=name, acl_match=acl_match, delete_interface_vlan=delete_interface_vlan, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    