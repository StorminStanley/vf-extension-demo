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


def interface_tengigabitethernet_fabric_fabric_dport_fabric_dport_mode(**kwargs):
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
            
    fabric = ET.SubElement(tengigabitethernet, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
    if kwargs.pop('delete_fabric', False) is True:
        delete_fabric = config.find('.//*fabric')
        delete_fabric.set('operation', 'delete')
        
    fabric_dport = ET.SubElement(fabric, "fabric-dport")
    if kwargs.pop('delete_fabric_dport', False) is True:
        delete_fabric_dport = config.find('.//*fabric-dport')
        delete_fabric_dport.set('operation', 'delete')
        
    fabric_dport_mode = ET.SubElement(fabric_dport, "fabric-dport-mode")
    if kwargs.pop('delete_fabric_dport_mode', False) is True:
        delete_fabric_dport_mode = config.find('.//*fabric-dport-mode')
        delete_fabric_dport_mode.set('operation', 'delete')
        
    fabric_dport_mode.text = kwargs.pop('fabric_dport_mode')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_fabric_fabric_dport_fabric_dport_mode_act(Action):
    def run(self, name, fabric_dport_mode, delete_fabric, delete_fabric_dport_mode, delete_interface, delete_name, delete_fabric_dport, delete_tengigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_fabric_fabric_dport_fabric_dport_mode(name=name, delete_fabric=delete_fabric, username=username, password=password, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_fabric_dport=delete_fabric_dport, delete_name=delete_name, delete_interface=delete_interface, fabric_dport_mode=fabric_dport_mode, delete_fabric_dport_mode=delete_fabric_dport_mode, callback=_callback, mgr=mgr)
        return 0
    