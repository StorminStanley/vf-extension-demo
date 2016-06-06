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


def interface_port_channel_ipv6_access_group_ipv6_access_list(**kwargs):
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
            
    ipv6 = ET.SubElement(port_channel, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    access_group = ET.SubElement(ipv6, "access-group", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
    if kwargs.pop('delete_access_group', False) is True:
        delete_access_group = config.find('.//*access-group')
        delete_access_group.set('operation', 'delete')
        
    ip_direction_key = ET.SubElement(access_group, "ip-direction")
    ip_direction_key.text = kwargs.pop('ip_direction')
    if kwargs.pop('delete_ip_direction', False) is True:
        delete_ip_direction = config.find('.//*ip-direction')
        delete_ip_direction.set('operation', 'delete')
            
    ipv6_access_list = ET.SubElement(access_group, "ipv6-access-list")
    if kwargs.pop('delete_ipv6_access_list', False) is True:
        delete_ipv6_access_list = config.find('.//*ipv6-access-list')
        delete_ipv6_access_list.set('operation', 'delete')
        
    ipv6_access_list.text = kwargs.pop('ipv6_access_list')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ipv6_access_group_ipv6_access_list_act(Action):
    def run(self, name, delete_ip_direction, delete_port_channel, delete_access_group, delete_name, ip_direction, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ipv6_access_group_ipv6_access_list(name=name, delete_name=delete_name, delete_access_group=delete_access_group, delete_port_channel=delete_port_channel, delete_ip_direction=delete_ip_direction, host=host, ip_direction=ip_direction, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    