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


def interface_management_ip_gateway_gateway_address(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    management = ET.SubElement(interface, "management")
    if kwargs.pop('delete_management', False) is True:
        delete_management = config.find('.//*management')
        delete_management.set('operation', 'delete')
        
    name_key = ET.SubElement(management, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(management, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    gateway = ET.SubElement(ip, "gateway")
    if kwargs.pop('delete_gateway', False) is True:
        delete_gateway = config.find('.//*gateway')
        delete_gateway.set('operation', 'delete')
        
    gateway_address = ET.SubElement(gateway, "gateway-address")
    if kwargs.pop('delete_gateway_address', False) is True:
        delete_gateway_address = config.find('.//*gateway-address')
        delete_gateway_address.set('operation', 'delete')
        
    gateway_address.text = kwargs.pop('gateway_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_management_ip_gateway_gateway_address_act(Action):
    def run(self, delete_gateway_address, gateway_address, name, delete_ip, delete_interface, delete_name, delete_gateway, delete_management, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_management_ip_gateway_gateway_address(delete_management=delete_management, delete_gateway_address=delete_gateway_address, delete_name=delete_name, delete_ip=delete_ip, name=name, gateway_address=gateway_address, host=host, delete_gateway=delete_gateway, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    