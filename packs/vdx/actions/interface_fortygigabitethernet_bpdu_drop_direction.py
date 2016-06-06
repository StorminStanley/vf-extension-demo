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


def interface_fortygigabitethernet_bpdu_drop_direction(**kwargs):
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
            
    bpdu_drop = ET.SubElement(fortygigabitethernet, "bpdu-drop", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_bpdu_drop', False) is True:
        delete_bpdu_drop = config.find('.//*bpdu-drop')
        delete_bpdu_drop.set('operation', 'delete')
        
    direction = ET.SubElement(bpdu_drop, "direction")
    if kwargs.pop('delete_direction', False) is True:
        delete_direction = config.find('.//*direction')
        delete_direction.set('operation', 'delete')
        
    direction.text = kwargs.pop('direction')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_bpdu_drop_direction_act(Action):
    def run(self, direction, name, delete_fortygigabitethernet, delete_bpdu_drop, delete_name, delete_interface, delete_direction, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_bpdu_drop_direction(name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, password=password, direction=direction, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_bpdu_drop=delete_bpdu_drop, delete_direction=delete_direction, callback=_callback, mgr=mgr)
        return 0
    