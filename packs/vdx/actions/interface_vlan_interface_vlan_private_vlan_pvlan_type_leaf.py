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


def interface_vlan_interface_vlan_private_vlan_pvlan_type_leaf(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface_vlan = ET.SubElement(config, "interface-vlan", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface_vlan', False) is True:
        delete_interface_vlan = config.find('.//*interface-vlan')
        delete_interface_vlan.set('operation', 'delete')
        
    interface = ET.SubElement(interface_vlan, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    vlan = ET.SubElement(interface, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    name_key = ET.SubElement(vlan, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    private_vlan = ET.SubElement(vlan, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    pvlan_type_leaf = ET.SubElement(private_vlan, "pvlan-type-leaf")
    if kwargs.pop('delete_pvlan_type_leaf', False) is True:
        delete_pvlan_type_leaf = config.find('.//*pvlan-type-leaf')
        delete_pvlan_type_leaf.set('operation', 'delete')
        
    pvlan_type_leaf.text = kwargs.pop('pvlan_type_leaf')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_private_vlan_pvlan_type_leaf_act(Action):
    def run(self, delete_vlan, name, delete_interface_vlan, delete_private_vlan, delete_interface, delete_name, delete_pvlan_type_leaf, pvlan_type_leaf, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_private_vlan_pvlan_type_leaf(name=name, delete_name=delete_name, delete_vlan=delete_vlan, pvlan_type_leaf=pvlan_type_leaf, delete_interface_vlan=delete_interface_vlan, delete_private_vlan=delete_private_vlan, host=host, delete_interface=delete_interface, username=username, delete_pvlan_type_leaf=delete_pvlan_type_leaf, password=password, callback=_callback, mgr=mgr)
        return 0
    