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


def interface_gigabitethernet_ipv6_ipv6_config_address_ipv6_address_secondary(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    gigabitethernet = ET.SubElement(interface, "gigabitethernet")
    if kwargs.pop('delete_gigabitethernet', False) is True:
        delete_gigabitethernet = config.find('.//*gigabitethernet')
        delete_gigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(gigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(gigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_config = ET.SubElement(ipv6, "ipv6-config", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
    if kwargs.pop('delete_ipv6_config', False) is True:
        delete_ipv6_config = config.find('.//*ipv6-config')
        delete_ipv6_config.set('operation', 'delete')
        
    address = ET.SubElement(ipv6_config, "address")
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
        
    ipv6_address = ET.SubElement(address, "ipv6-address")
    if kwargs.pop('delete_ipv6_address', False) is True:
        delete_ipv6_address = config.find('.//*ipv6-address')
        delete_ipv6_address.set('operation', 'delete')
        
    address_key = ET.SubElement(ipv6_address, "address")
    address_key.text = kwargs.pop('address')
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
            
    secondary = ET.SubElement(ipv6_address, "secondary")
    if kwargs.pop('delete_secondary', False) is True:
        delete_secondary = config.find('.//*secondary')
        delete_secondary.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_ipv6_ipv6_config_address_ipv6_address_secondary_act(Action):
    def run(self, name, delete_secondary, delete_interface, delete_name, address, delete_address, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_ipv6_ipv6_config_address_ipv6_address_secondary(name=name, delete_name=delete_name, address=address, host=host, delete_secondary=delete_secondary, delete_gigabitethernet=delete_gigabitethernet, delete_address=delete_address, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    