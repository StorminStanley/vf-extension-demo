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


def interface_hundredgigabitethernet_spanning_tree_hello_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    spanning_tree = ET.SubElement(hundredgigabitethernet, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    hello_time = ET.SubElement(spanning_tree, "hello-time")
    if kwargs.pop('delete_hello_time', False) is True:
        delete_hello_time = config.find('.//*hello-time')
        delete_hello_time.set('operation', 'delete')
        
    hello_time.text = kwargs.pop('hello_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_spanning_tree_hello_time_act(Action):
    def run(self, delete_hello_time, name, hello_time, delete_interface, delete_name, delete_hundredgigabitethernet, delete_spanning_tree, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_spanning_tree_hello_time(name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_spanning_tree=delete_spanning_tree, delete_hello_time=delete_hello_time, host=host, hello_time=hello_time, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    