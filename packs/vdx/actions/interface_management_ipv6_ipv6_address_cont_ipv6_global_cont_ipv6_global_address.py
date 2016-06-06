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


def interface_management_ipv6_ipv6_address_cont_ipv6_global_cont_ipv6_global_address(**kwargs):
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
            
    ipv6 = ET.SubElement(management, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_address_cont = ET.SubElement(ipv6, "ipv6-address-cont")
    if kwargs.pop('delete_ipv6_address_cont', False) is True:
        delete_ipv6_address_cont = config.find('.//*ipv6-address-cont')
        delete_ipv6_address_cont.set('operation', 'delete')
        
    ipv6_global_cont = ET.SubElement(ipv6_address_cont, "ipv6-global-cont")
    if kwargs.pop('delete_ipv6_global_cont', False) is True:
        delete_ipv6_global_cont = config.find('.//*ipv6-global-cont')
        delete_ipv6_global_cont.set('operation', 'delete')
        
    ipv6_global_address = ET.SubElement(ipv6_global_cont, "ipv6-global-address")
    if kwargs.pop('delete_ipv6_global_address', False) is True:
        delete_ipv6_global_address = config.find('.//*ipv6-global-address')
        delete_ipv6_global_address.set('operation', 'delete')
        
    ipv6_global_address.text = kwargs.pop('ipv6_global_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_management_ipv6_ipv6_address_cont_ipv6_global_cont_ipv6_global_address_act(Action):
    def run(self, delete_management, delete_interface, delete_name, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_management_ipv6_ipv6_address_cont_ipv6_global_cont_ipv6_global_address(name=name, delete_name=delete_name, delete_management=delete_management, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    