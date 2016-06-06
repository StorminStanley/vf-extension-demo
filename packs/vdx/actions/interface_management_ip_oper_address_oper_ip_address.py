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


def interface_management_ip_oper_address_oper_ip_address(**kwargs):
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
        
    oper_address = ET.SubElement(ip, "oper-address")
    if kwargs.pop('delete_oper_address', False) is True:
        delete_oper_address = config.find('.//*oper-address')
        delete_oper_address.set('operation', 'delete')
        
    oper_ip_address = ET.SubElement(oper_address, "oper-ip-address")
    if kwargs.pop('delete_oper_ip_address', False) is True:
        delete_oper_ip_address = config.find('.//*oper-ip-address')
        delete_oper_ip_address.set('operation', 'delete')
        
    oper_ip_address.text = kwargs.pop('oper_ip_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_management_ip_oper_address_oper_ip_address_act(Action):
    def run(self, name, delete_ip, oper_ip_address, delete_oper_address, delete_interface, delete_name, delete_oper_ip_address, delete_management, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_management_ip_oper_address_oper_ip_address(delete_management=delete_management, name=name, delete_name=delete_name, oper_ip_address=oper_ip_address, delete_oper_ip_address=delete_oper_ip_address, delete_ip=delete_ip, delete_oper_address=delete_oper_address, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    