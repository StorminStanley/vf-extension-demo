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


def interface_port_channel_ip_pbr_interface_ip_policy_route_map_route_map_name(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip_pbr_interface = ET.SubElement(port_channel, "ip-pbr-interface", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_ip_pbr_interface', False) is True:
        delete_ip_pbr_interface = config.find('.//*ip-pbr-interface')
        delete_ip_pbr_interface.set('operation', 'delete')
        
    ip = ET.SubElement(ip_pbr_interface, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    policy = ET.SubElement(ip, "policy")
    if kwargs.pop('delete_policy', False) is True:
        delete_policy = config.find('.//*policy')
        delete_policy.set('operation', 'delete')
        
    route_map = ET.SubElement(policy, "route-map")
    if kwargs.pop('delete_route_map', False) is True:
        delete_route_map = config.find('.//*route-map')
        delete_route_map.set('operation', 'delete')
        
    route_map_name = ET.SubElement(route_map, "route-map-name")
    if kwargs.pop('delete_route_map_name', False) is True:
        delete_route_map_name = config.find('.//*route-map-name')
        delete_route_map_name.set('operation', 'delete')
        
    route_map_name.text = kwargs.pop('route_map_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ip_pbr_interface_ip_policy_route_map_route_map_name_act(Action):
    def run(self, route_map_name, name, delete_ip, delete_route_map_name, delete_route_map, delete_policy, delete_port_channel, delete_interface, delete_name, delete_ip_pbr_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ip_pbr_interface_ip_policy_route_map_route_map_name(delete_port_channel=delete_port_channel, name=name, delete_name=delete_name, username=username, route_map_name=route_map_name, delete_ip=delete_ip, delete_route_map=delete_route_map, delete_policy=delete_policy, host=host, delete_ip_pbr_interface=delete_ip_pbr_interface, delete_interface=delete_interface, delete_route_map_name=delete_route_map_name, password=password, callback=_callback, mgr=mgr)
        return 0
    