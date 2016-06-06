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


def interface_fortygigabitethernet_channel_group_port_int(**kwargs):
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
            
    channel_group = ET.SubElement(fortygigabitethernet, "channel-group")
    if kwargs.pop('delete_channel_group', False) is True:
        delete_channel_group = config.find('.//*channel-group')
        delete_channel_group.set('operation', 'delete')
        
    port_int = ET.SubElement(channel_group, "port-int")
    if kwargs.pop('delete_port_int', False) is True:
        delete_port_int = config.find('.//*port-int')
        delete_port_int.set('operation', 'delete')
        
    port_int.text = kwargs.pop('port_int')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_channel_group_port_int_act(Action):
    def run(self, name, delete_fortygigabitethernet, port_int, delete_channel_group, delete_name, delete_port_int, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_channel_group_port_int(name=name, delete_name=delete_name, delete_channel_group=delete_channel_group, delete_port_int=delete_port_int, host=host, password=password, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_interface=delete_interface, username=username, port_int=port_int, callback=_callback, mgr=mgr)
        return 0
    