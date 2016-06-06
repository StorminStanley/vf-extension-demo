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


def interface_tengigabitethernet_ipv6_interface_ospfv3_conf_link_interval_properties_hello_interval(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    tengigabitethernet = ET.SubElement(interface, "tengigabitethernet")
    if kwargs.pop('delete_tengigabitethernet', False) is True:
        delete_tengigabitethernet = config.find('.//*tengigabitethernet')
        delete_tengigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(tengigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(tengigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    interface_ospfv3_conf = ET.SubElement(ipv6, "interface-ospfv3-conf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_interface_ospfv3_conf', False) is True:
        delete_interface_ospfv3_conf = config.find('.//*interface-ospfv3-conf')
        delete_interface_ospfv3_conf.set('operation', 'delete')
        
    link_interval_properties = ET.SubElement(interface_ospfv3_conf, "link-interval-properties")
    if kwargs.pop('delete_link_interval_properties', False) is True:
        delete_link_interval_properties = config.find('.//*link-interval-properties')
        delete_link_interval_properties.set('operation', 'delete')
        
    hello_interval = ET.SubElement(link_interval_properties, "hello-interval")
    if kwargs.pop('delete_hello_interval', False) is True:
        delete_hello_interval = config.find('.//*hello-interval')
        delete_hello_interval.set('operation', 'delete')
        
    hello_interval.text = kwargs.pop('hello_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ipv6_interface_ospfv3_conf_link_interval_properties_hello_interval_act(Action):
    def run(self, name, delete_interface, delete_name, delete_link_interval_properties, delete_hello_interval, delete_tengigabitethernet, hello_interval, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ipv6_interface_ospfv3_conf_link_interval_properties_hello_interval(name=name, delete_name=delete_name, hello_interval=hello_interval, delete_link_interval_properties=delete_link_interval_properties, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_hello_interval=delete_hello_interval, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    