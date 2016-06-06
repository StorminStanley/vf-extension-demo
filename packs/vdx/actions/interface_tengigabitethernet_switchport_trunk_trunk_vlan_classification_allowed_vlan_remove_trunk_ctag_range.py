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


def interface_tengigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_range(**kwargs):
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
        
    trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
    if kwargs.pop('delete_trunk_vlan_classification', False) is True:
        delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
        delete_trunk_vlan_classification.set('operation', 'delete')
        
    allowed = ET.SubElement(trunk_vlan_classification, "allowed")
    if kwargs.pop('delete_allowed', False) is True:
        delete_allowed = config.find('.//*allowed')
        delete_allowed.set('operation', 'delete')
        
    vlan = ET.SubElement(allowed, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    remove = ET.SubElement(vlan, "remove")
    if kwargs.pop('delete_remove', False) is True:
        delete_remove = config.find('.//*remove')
        delete_remove.set('operation', 'delete')
        
    trunk_vlan_id_key = ET.SubElement(remove, "trunk-vlan-id")
    trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
    if kwargs.pop('delete_trunk_vlan_id', False) is True:
        delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
        delete_trunk_vlan_id.set('operation', 'delete')
            
    trunk_ctag_range = ET.SubElement(remove, "trunk-ctag-range")
    if kwargs.pop('delete_trunk_ctag_range', False) is True:
        delete_trunk_ctag_range = config.find('.//*trunk-ctag-range')
        delete_trunk_ctag_range.set('operation', 'delete')
        
    trunk_ctag_range.text = kwargs.pop('trunk_ctag_range')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_range_act(Action):
    def run(self, delete_switchport, delete_vlan, delete_allowed, name, delete_trunk_vlan_classification, delete_trunk, trunk_vlan_id, delete_trunk_ctag_range, delete_interface, delete_name, delete_remove, delete_tengigabitethernet, trunk_ctag_range, delete_trunk_vlan_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_range(trunk_ctag_range=trunk_ctag_range, name=name, delete_trunk=delete_trunk, delete_trunk_vlan_id=delete_trunk_vlan_id, username=username, delete_switchport=delete_switchport, delete_remove=delete_remove, delete_trunk_vlan_classification=delete_trunk_vlan_classification, delete_allowed=delete_allowed, trunk_vlan_id=trunk_vlan_id, delete_vlan=delete_vlan, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_name=delete_name, delete_interface=delete_interface, delete_trunk_ctag_range=delete_trunk_ctag_range, password=password, callback=_callback, mgr=mgr)
        return 0
    