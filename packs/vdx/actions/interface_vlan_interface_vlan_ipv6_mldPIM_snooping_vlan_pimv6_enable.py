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


def interface_vlan_interface_vlan_ipv6_mldPIM_snooping_vlan_pimv6_enable(**kwargs):
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
            
    ipv6 = ET.SubElement(vlan, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    mldPIM = ET.SubElement(ipv6, "mldPIM", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
    if kwargs.pop('delete_mldPIM', False) is True:
        delete_mldPIM = config.find('.//*mldPIM')
        delete_mldPIM.set('operation', 'delete')
        
    snooping = ET.SubElement(mldPIM, "snooping")
    if kwargs.pop('delete_snooping', False) is True:
        delete_snooping = config.find('.//*snooping')
        delete_snooping.set('operation', 'delete')
        
    vlan_pimv6_enable = ET.SubElement(snooping, "vlan-pimv6-enable")
    if kwargs.pop('delete_vlan_pimv6_enable', False) is True:
        delete_vlan_pimv6_enable = config.find('.//*vlan-pimv6-enable')
        delete_vlan_pimv6_enable.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_ipv6_mldPIM_snooping_vlan_pimv6_enable_act(Action):
    def run(self, delete_vlan, name, delete_snooping, delete_mldPIM, delete_interface_vlan, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_ipv6_mldPIM_snooping_vlan_pimv6_enable(name=name, delete_name=delete_name, delete_vlan=delete_vlan, username=username, delete_snooping=delete_snooping, delete_interface_vlan=delete_interface_vlan, host=host, delete_interface=delete_interface, delete_mldPIM=delete_mldPIM, password=password, callback=_callback, mgr=mgr)
        return 0
    