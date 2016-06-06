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


def interface_fortygigabitethernet_switchport_trunk_default_vlan_config_default_transparent_vlan(**kwargs):
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
            
    switchport = ET.SubElement(fortygigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    trunk = ET.SubElement(switchport, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    default_vlan_config = ET.SubElement(trunk, "default-vlan-config")
    if kwargs.pop('delete_default_vlan_config', False) is True:
        delete_default_vlan_config = config.find('.//*default-vlan-config')
        delete_default_vlan_config.set('operation', 'delete')
        
    default_transparent_vlan = ET.SubElement(default_vlan_config, "default-transparent-vlan")
    if kwargs.pop('delete_default_transparent_vlan', False) is True:
        delete_default_transparent_vlan = config.find('.//*default-transparent-vlan')
        delete_default_transparent_vlan.set('operation', 'delete')
        
    default_transparent_vlan.text = kwargs.pop('default_transparent_vlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_switchport_trunk_default_vlan_config_default_transparent_vlan_act(Action):
    def run(self, delete_switchport, name, delete_trunk, delete_fortygigabitethernet, delete_default_vlan_config, delete_interface, delete_name, delete_default_transparent_vlan, default_transparent_vlan, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_switchport_trunk_default_vlan_config_default_transparent_vlan(default_transparent_vlan=default_transparent_vlan, name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_switchport=delete_switchport, username=username, delete_name=delete_name, delete_default_vlan_config=delete_default_vlan_config, host=host, delete_trunk=delete_trunk, delete_interface=delete_interface, delete_default_transparent_vlan=delete_default_transparent_vlan, password=password, callback=_callback, mgr=mgr)
        return 0
    