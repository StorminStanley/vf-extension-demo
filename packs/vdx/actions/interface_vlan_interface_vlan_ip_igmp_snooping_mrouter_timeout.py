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


def interface_vlan_interface_vlan_ip_igmp_snooping_mrouter_agtimeout(**kwargs):
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
        
    snooping = ET.SubElement(igmp, "snooping")
    if kwargs.pop('delete_snooping', False) is True:
        delete_snooping = config.find('.//*snooping')
        delete_snooping.set('operation', 'delete')
        
    mrouter_agtimeout = ET.SubElement(snooping, "mrouter-agtimeout")
    if kwargs.pop('delete_mrouter_agtimeout', False) is True:
        delete_mrouter_agtimeout = config.find('.//*mrouter-agtimeout')
        delete_mrouter_agtimeout.set('operation', 'delete')
        
    mrouter_agtimeout.text = kwargs.pop('mrouter_agtimeout')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_ip_igmp_snooping_mrouter_agtimeout_act(Action):
    def run(self, delete_vlan, name, delete_ip, delete_interface_vlan, delete_igmp, delete_interface, delete_name, mrouter_agtimeout, delete_mrouter_agtimeout, delete_snooping, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_ip_igmp_snooping_mrouter_agtimeout(name=name, delete_name=delete_name, delete_snooping=delete_snooping, delete_vlan=delete_vlan, delete_ip=delete_ip, delete_igmp=delete_igmp, delete_interface_vlan=delete_interface_vlan, host=host, delete_mrouter_agtimeout=delete_mrouter_agtimeout, mrouter_agtimeout=mrouter_agtimeout, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    