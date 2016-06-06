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


def interface_port_channel_ip_ip_config_address_secondary(**kwargs):
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
            
    ip = ET.SubElement(port_channel, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    ip_config = ET.SubElement(ip, "ip-config", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip_config', False) is True:
        delete_ip_config = config.find('.//*ip-config')
        delete_ip_config.set('operation', 'delete')
        
    address = ET.SubElement(ip_config, "address")
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
        
    address_key = ET.SubElement(address, "address")
    address_key.text = kwargs.pop('address')
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
            
    secondary = ET.SubElement(address, "secondary")
    if kwargs.pop('delete_secondary', False) is True:
        delete_secondary = config.find('.//*secondary')
        delete_secondary.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ip_ip_config_address_secondary_act(Action):
    def run(self, delete_ip_config, name, delete_ip, delete_secondary, delete_port_channel, delete_interface, delete_name, address, delete_address, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ip_ip_config_address_secondary(name=name, delete_secondary=delete_secondary, address=address, delete_ip_config=delete_ip_config, delete_ip=delete_ip, delete_port_channel=delete_port_channel, delete_address=delete_address, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    