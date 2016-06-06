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


def interface_tengigabitethernet_switchport_trunk_native_vlan_xtagged_config_native_vlan_ctag_id_xtagged(**kwargs):
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
            
    switchport = ET.SubElement(tengigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    trunk = ET.SubElement(switchport, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    native_vlan_xtagged_config = ET.SubElement(trunk, "native-vlan-xtagged-config")
    if kwargs.pop('delete_native_vlan_xtagged_config', False) is True:
        delete_native_vlan_xtagged_config = config.find('.//*native-vlan-xtagged-config')
        delete_native_vlan_xtagged_config.set('operation', 'delete')
        
    native_vlan_ctag_id_xtagged = ET.SubElement(native_vlan_xtagged_config, "native-vlan-ctag-id-xtagged")
    if kwargs.pop('delete_native_vlan_ctag_id_xtagged', False) is True:
        delete_native_vlan_ctag_id_xtagged = config.find('.//*native-vlan-ctag-id-xtagged')
        delete_native_vlan_ctag_id_xtagged.set('operation', 'delete')
        
    native_vlan_ctag_id_xtagged.text = kwargs.pop('native_vlan_ctag_id_xtagged')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_trunk_native_vlan_xtagged_config_native_vlan_ctag_id_xtagged_act(Action):
    def run(self, delete_switchport, delete_native_vlan_xtagged_config, name, native_vlan_ctag_id_xtagged, delete_trunk, delete_native_vlan_ctag_id_xtagged, delete_interface, delete_name, delete_tengigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_trunk_native_vlan_xtagged_config_native_vlan_ctag_id_xtagged(name=name, delete_trunk=delete_trunk, delete_switchport=delete_switchport, username=username, delete_tengigabitethernet=delete_tengigabitethernet, delete_native_vlan_xtagged_config=delete_native_vlan_xtagged_config, delete_native_vlan_ctag_id_xtagged=delete_native_vlan_ctag_id_xtagged, host=host, delete_name=delete_name, delete_interface=delete_interface, native_vlan_ctag_id_xtagged=native_vlan_ctag_id_xtagged, password=password, callback=_callback, mgr=mgr)
        return 0
    