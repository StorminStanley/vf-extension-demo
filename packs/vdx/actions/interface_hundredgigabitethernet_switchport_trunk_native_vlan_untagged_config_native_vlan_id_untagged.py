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


def interface_hundredgigabitethernet_switchport_trunk_native_vlan_untagged_config_native_vlan_id_untagged(**kwargs):
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
            
    switchport = ET.SubElement(hundredgigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    trunk = ET.SubElement(switchport, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    native_vlan_untagged_config = ET.SubElement(trunk, "native-vlan-untagged-config")
    if kwargs.pop('delete_native_vlan_untagged_config', False) is True:
        delete_native_vlan_untagged_config = config.find('.//*native-vlan-untagged-config')
        delete_native_vlan_untagged_config.set('operation', 'delete')
        
    native_vlan_id_untagged = ET.SubElement(native_vlan_untagged_config, "native-vlan-id-untagged")
    if kwargs.pop('delete_native_vlan_id_untagged', False) is True:
        delete_native_vlan_id_untagged = config.find('.//*native-vlan-id-untagged')
        delete_native_vlan_id_untagged.set('operation', 'delete')
        
    native_vlan_id_untagged.text = kwargs.pop('native_vlan_id_untagged')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_switchport_trunk_native_vlan_untagged_config_native_vlan_id_untagged_act(Action):
    def run(self, delete_switchport, name, delete_trunk, delete_native_vlan_id_untagged, delete_interface, delete_name, delete_hundredgigabitethernet, delete_native_vlan_untagged_config, native_vlan_id_untagged, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_switchport_trunk_native_vlan_untagged_config_native_vlan_id_untagged(name=name, delete_name=delete_name, delete_switchport=delete_switchport, delete_native_vlan_id_untagged=delete_native_vlan_id_untagged, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_native_vlan_untagged_config=delete_native_vlan_untagged_config, host=host, delete_trunk=delete_trunk, delete_interface=delete_interface, native_vlan_id_untagged=native_vlan_id_untagged, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    