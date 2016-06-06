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


def interface_fortygigabitethernet_storm_control_ingress_rate_bps(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    storm_control = ET.SubElement(fortygigabitethernet, "storm-control", xmlns="urn:brocade.com:mgmt:brocade-bum-storm-control")
    if kwargs.pop('delete_storm_control', False) is True:
        delete_storm_control = config.find('.//*storm-control')
        delete_storm_control.set('operation', 'delete')
        
    ingress = ET.SubElement(storm_control, "ingress")
    if kwargs.pop('delete_ingress', False) is True:
        delete_ingress = config.find('.//*ingress')
        delete_ingress.set('operation', 'delete')
        
    protocol_type_key = ET.SubElement(ingress, "protocol-type")
    protocol_type_key.text = kwargs.pop('protocol_type')
    if kwargs.pop('delete_protocol_type', False) is True:
        delete_protocol_type = config.find('.//*protocol-type')
        delete_protocol_type.set('operation', 'delete')
            
    rate_bps = ET.SubElement(ingress, "rate-bps")
    if kwargs.pop('delete_rate_bps', False) is True:
        delete_rate_bps = config.find('.//*rate-bps')
        delete_rate_bps.set('operation', 'delete')
        
    rate_bps.text = kwargs.pop('rate_bps')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_storm_control_ingress_rate_bps_act(Action):
    def run(self, delete_protocol_type, delete_storm_control, rate_bps, delete_ingress, delete_fortygigabitethernet, delete_rate_bps, delete_interface, delete_name, protocol_type, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_storm_control_ingress_rate_bps(name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_storm_control=delete_storm_control, delete_rate_bps=delete_rate_bps, delete_ingress=delete_ingress, protocol_type=protocol_type, host=host, delete_protocol_type=delete_protocol_type, rate_bps=rate_bps, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    