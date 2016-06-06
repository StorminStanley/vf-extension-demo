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


def interface_gigabitethernet_storm_control_ingress_protocol_type(**kwargs):
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
            
    storm_control = ET.SubElement(gigabitethernet, "storm-control", xmlns="urn:brocade.com:mgmt:brocade-bum-storm-control")
    if kwargs.pop('delete_storm_control', False) is True:
        delete_storm_control = config.find('.//*storm-control')
        delete_storm_control.set('operation', 'delete')
        
    ingress = ET.SubElement(storm_control, "ingress")
    if kwargs.pop('delete_ingress', False) is True:
        delete_ingress = config.find('.//*ingress')
        delete_ingress.set('operation', 'delete')
        
    protocol_type = ET.SubElement(ingress, "protocol-type")
    if kwargs.pop('delete_protocol_type', False) is True:
        delete_protocol_type = config.find('.//*protocol-type')
        delete_protocol_type.set('operation', 'delete')
        
    protocol_type.text = kwargs.pop('protocol_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_storm_control_ingress_protocol_type_act(Action):
    def run(self, protocol_type, delete_storm_control, delete_ingress, delete_protocol_type, delete_interface, delete_name, delete_gigabitethernet, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_storm_control_ingress_protocol_type(name=name, delete_name=delete_name, delete_storm_control=delete_storm_control, delete_ingress=delete_ingress, protocol_type=protocol_type, delete_protocol_type=delete_protocol_type, delete_gigabitethernet=delete_gigabitethernet, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    