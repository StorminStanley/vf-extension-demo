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


def interface_gigabitethernet_switchport_private_vlan_trunk_allowed_vlan_pvlan_add(**kwargs):
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
            
    switchport = ET.SubElement(gigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    private_vlan = ET.SubElement(switchport, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    trunk = ET.SubElement(private_vlan, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    allowed = ET.SubElement(trunk, "allowed")
    if kwargs.pop('delete_allowed', False) is True:
        delete_allowed = config.find('.//*allowed')
        delete_allowed.set('operation', 'delete')
        
    vlan = ET.SubElement(allowed, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    pvlan_add = ET.SubElement(vlan, "pvlan_add")
    if kwargs.pop('delete_pvlan_add', False) is True:
        delete_pvlan_add = config.find('.//*pvlan_add')
        delete_pvlan_add.set('operation', 'delete')
        
    pvlan_add.text = kwargs.pop('pvlan_add')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_switchport_private_vlan_trunk_allowed_vlan_pvlan_add_act(Action):
    def run(self, delete_switchport, delete_vlan, delete_allowed, name, delete_trunk, delete_pvlan_add, delete_private_vlan, delete_interface, delete_name, pvlan_add, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_switchport_private_vlan_trunk_allowed_vlan_pvlan_add(name=name, delete_trunk=delete_trunk, delete_switchport=delete_switchport, username=username, delete_allowed=delete_allowed, delete_pvlan_add=delete_pvlan_add, delete_vlan=delete_vlan, host=host, delete_private_vlan=delete_private_vlan, delete_name=delete_name, delete_interface=delete_interface, delete_gigabitethernet=delete_gigabitethernet, pvlan_add=pvlan_add, password=password, callback=_callback, mgr=mgr)
        return 0
    