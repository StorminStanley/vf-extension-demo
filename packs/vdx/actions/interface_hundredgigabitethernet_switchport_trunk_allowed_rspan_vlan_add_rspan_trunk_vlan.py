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


def interface_hundredgigabitethernet_switchport_trunk_allowed_rspan_vlan_add_rspan_trunk_vlan(**kwargs):
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
        
    allowed = ET.SubElement(trunk, "allowed")
    if kwargs.pop('delete_allowed', False) is True:
        delete_allowed = config.find('.//*allowed')
        delete_allowed.set('operation', 'delete')
        
    rspan_vlan = ET.SubElement(allowed, "rspan-vlan")
    if kwargs.pop('delete_rspan_vlan', False) is True:
        delete_rspan_vlan = config.find('.//*rspan-vlan')
        delete_rspan_vlan.set('operation', 'delete')
        
    add_rspan_trunk_vlan = ET.SubElement(rspan_vlan, "add-rspan-trunk-vlan")
    if kwargs.pop('delete_add_rspan_trunk_vlan', False) is True:
        delete_add_rspan_trunk_vlan = config.find('.//*add-rspan-trunk-vlan')
        delete_add_rspan_trunk_vlan.set('operation', 'delete')
        
    add_rspan_trunk_vlan.text = kwargs.pop('add_rspan_trunk_vlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_switchport_trunk_allowed_rspan_vlan_add_rspan_trunk_vlan_act(Action):
    def run(self, delete_switchport, delete_allowed, delete_rspan_vlan, name, delete_trunk, delete_add_rspan_trunk_vlan, add_rspan_trunk_vlan, delete_interface, delete_name, delete_hundredgigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_switchport_trunk_allowed_rspan_vlan_add_rspan_trunk_vlan(delete_add_rspan_trunk_vlan=delete_add_rspan_trunk_vlan, name=name, delete_trunk=delete_trunk, add_rspan_trunk_vlan=add_rspan_trunk_vlan, delete_switchport=delete_switchport, delete_allowed=delete_allowed, delete_rspan_vlan=delete_rspan_vlan, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    