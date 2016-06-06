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


def interface_port_channel_vrrp_virtual_ip_virtual_ipaddr(**kwargs):
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
            
    vrrp = ET.SubElement(port_channel, "vrrp", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_vrrp', False) is True:
        delete_vrrp = config.find('.//*vrrp')
        delete_vrrp.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrp, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    version_key = ET.SubElement(vrrp, "version")
    version_key.text = kwargs.pop('version')
    if kwargs.pop('delete_version', False) is True:
        delete_version = config.find('.//*version')
        delete_version.set('operation', 'delete')
            
    virtual_ip = ET.SubElement(vrrp, "virtual-ip")
    if kwargs.pop('delete_virtual_ip', False) is True:
        delete_virtual_ip = config.find('.//*virtual-ip')
        delete_virtual_ip.set('operation', 'delete')
        
    virtual_ipaddr = ET.SubElement(virtual_ip, "virtual-ipaddr")
    if kwargs.pop('delete_virtual_ipaddr', False) is True:
        delete_virtual_ipaddr = config.find('.//*virtual-ipaddr')
        delete_virtual_ipaddr.set('operation', 'delete')
        
    virtual_ipaddr.text = kwargs.pop('virtual_ipaddr')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_vrrp_virtual_ip_virtual_ipaddr_act(Action):
    def run(self, virtual_ipaddr, name, delete_vrid, vrid, delete_version, delete_port_channel, version, delete_interface, delete_name, delete_vrrp, delete_virtual_ip, delete_virtual_ipaddr, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_vrrp_virtual_ip_virtual_ipaddr(delete_vrid=delete_vrid, version=version, name=name, delete_version=delete_version, delete_virtual_ip=delete_virtual_ip, virtual_ipaddr=virtual_ipaddr, delete_vrrp=delete_vrrp, delete_port_channel=delete_port_channel, delete_virtual_ipaddr=delete_virtual_ipaddr, host=host, vrid=vrid, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    