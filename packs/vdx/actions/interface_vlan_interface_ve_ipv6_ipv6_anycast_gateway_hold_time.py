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


def interface_vlan_interface_ve_ipv6_ipv6_anycast_gateway_hold_time(**kwargs):
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
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    gve_name_key = ET.SubElement(ve, "gve-name")
    gve_name_key.text = kwargs.pop('gve_name')
    if kwargs.pop('delete_gve_name', False) is True:
        delete_gve_name = config.find('.//*gve-name')
        delete_gve_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(ve, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_anycast_gateway = ET.SubElement(ipv6, "ipv6-anycast-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
    if kwargs.pop('delete_ipv6_anycast_gateway', False) is True:
        delete_ipv6_anycast_gateway = config.find('.//*ipv6-anycast-gateway')
        delete_ipv6_anycast_gateway.set('operation', 'delete')
        
    ipv6_gw_id_key = ET.SubElement(ipv6_anycast_gateway, "ipv6-gw-id")
    ipv6_gw_id_key.text = kwargs.pop('ipv6_gw_id')
    if kwargs.pop('delete_ipv6_gw_id', False) is True:
        delete_ipv6_gw_id = config.find('.//*ipv6-gw-id')
        delete_ipv6_gw_id.set('operation', 'delete')
            
    hold_time = ET.SubElement(ipv6_anycast_gateway, "hold-time")
    if kwargs.pop('delete_hold_time', False) is True:
        delete_hold_time = config.find('.//*hold-time')
        delete_hold_time.set('operation', 'delete')
        
    hold_time.text = kwargs.pop('hold_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_ve_ipv6_ipv6_anycast_gateway_hold_time_act(Action):
    def run(self, gve_name, delete_hold_time, delete_interface_vlan, delete_ve, delete_interface, hold_time, delete_gve_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_ve_ipv6_ipv6_anycast_gateway_hold_time(delete_gve_name=delete_gve_name, gve_name=gve_name, delete_ve=delete_ve, host=host, hold_time=hold_time, delete_interface_vlan=delete_interface_vlan, delete_hold_time=delete_hold_time, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    