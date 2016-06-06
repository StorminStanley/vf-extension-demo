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


def interface_port_channel_ipv6_interface_po_dhcp_conf_dhcp_relay_servers_relay_ip_addr(**kwargs):
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
        
    interface_po_dhcp_conf = ET.SubElement(ipv6, "interface-po-dhcp-conf", xmlns="urn:brocade.com:mgmt:brocade-dhcpv6")
    if kwargs.pop('delete_interface_po_dhcp_conf', False) is True:
        delete_interface_po_dhcp_conf = config.find('.//*interface-po-dhcp-conf')
        delete_interface_po_dhcp_conf.set('operation', 'delete')
        
    dhcp = ET.SubElement(interface_po_dhcp_conf, "dhcp")
    if kwargs.pop('delete_dhcp', False) is True:
        delete_dhcp = config.find('.//*dhcp')
        delete_dhcp.set('operation', 'delete')
        
    relay = ET.SubElement(dhcp, "relay")
    if kwargs.pop('delete_relay', False) is True:
        delete_relay = config.find('.//*relay')
        delete_relay.set('operation', 'delete')
        
    servers = ET.SubElement(relay, "servers")
    if kwargs.pop('delete_servers', False) is True:
        delete_servers = config.find('.//*servers')
        delete_servers.set('operation', 'delete')
        
    relay_ip_addr = ET.SubElement(servers, "relay-ip-addr")
    if kwargs.pop('delete_relay_ip_addr', False) is True:
        delete_relay_ip_addr = config.find('.//*relay-ip-addr')
        delete_relay_ip_addr.set('operation', 'delete')
        
    relay_ip_addr.text = kwargs.pop('relay_ip_addr')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ipv6_interface_po_dhcp_conf_dhcp_relay_servers_relay_ip_addr_act(Action):
    def run(self, relay_ip_addr, name, delete_port_channel, delete_interface_po_dhcp_conf, delete_servers, delete_dhcp, delete_relay, delete_interface, delete_name, delete_relay_ip_addr, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ipv6_interface_po_dhcp_conf_dhcp_relay_servers_relay_ip_addr(relay_ip_addr=relay_ip_addr, name=name, delete_name=delete_name, delete_relay=delete_relay, username=username, delete_dhcp=delete_dhcp, delete_port_channel=delete_port_channel, delete_interface_po_dhcp_conf=delete_interface_po_dhcp_conf, host=host, delete_interface=delete_interface, delete_servers=delete_servers, delete_relay_ip_addr=delete_relay_ip_addr, password=password, callback=_callback, mgr=mgr)
        return 0
    