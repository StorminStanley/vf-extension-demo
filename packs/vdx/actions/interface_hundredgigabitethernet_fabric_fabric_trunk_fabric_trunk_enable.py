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


def interface_hundredgigabitethernet_fabric_fabric_trunk_fabric_trunk_enable(**kwargs):
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
            
    fabric = ET.SubElement(hundredgigabitethernet, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
    if kwargs.pop('delete_fabric', False) is True:
        delete_fabric = config.find('.//*fabric')
        delete_fabric.set('operation', 'delete')
        
    fabric_trunk = ET.SubElement(fabric, "fabric-trunk")
    if kwargs.pop('delete_fabric_trunk', False) is True:
        delete_fabric_trunk = config.find('.//*fabric-trunk')
        delete_fabric_trunk.set('operation', 'delete')
        
    fabric_trunk_enable = ET.SubElement(fabric_trunk, "fabric-trunk-enable")
    if kwargs.pop('delete_fabric_trunk_enable', False) is True:
        delete_fabric_trunk_enable = config.find('.//*fabric-trunk-enable')
        delete_fabric_trunk_enable.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_fabric_fabric_trunk_fabric_trunk_enable_act(Action):
    def run(self, name, delete_fabric, delete_interface, delete_name, delete_fabric_trunk, delete_hundredgigabitethernet, delete_fabric_trunk_enable, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_fabric_fabric_trunk_fabric_trunk_enable(name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_fabric_trunk_enable=delete_fabric_trunk_enable, delete_fabric_trunk=delete_fabric_trunk, host=host, delete_fabric=delete_fabric, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    