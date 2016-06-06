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


def interface_hundredgigabitethernet_mac_learning_mac_learn_disable_vlan_mac_learning_vlan_add(**kwargs):
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
            
    mac_learning = ET.SubElement(hundredgigabitethernet, "mac-learning")
    if kwargs.pop('delete_mac_learning', False) is True:
        delete_mac_learning = config.find('.//*mac-learning')
        delete_mac_learning.set('operation', 'delete')
        
    mac_learn_disable = ET.SubElement(mac_learning, "mac-learn-disable")
    if kwargs.pop('delete_mac_learn_disable', False) is True:
        delete_mac_learn_disable = config.find('.//*mac-learn-disable')
        delete_mac_learn_disable.set('operation', 'delete')
        
    vlan = ET.SubElement(mac_learn_disable, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    mac_learning_vlan_add = ET.SubElement(vlan, "mac-learning-vlan-add")
    if kwargs.pop('delete_mac_learning_vlan_add', False) is True:
        delete_mac_learning_vlan_add = config.find('.//*mac-learning-vlan-add')
        delete_mac_learning_vlan_add.set('operation', 'delete')
        
    mac_learning_vlan_add.text = kwargs.pop('mac_learning_vlan_add')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_mac_learning_mac_learn_disable_vlan_mac_learning_vlan_add_act(Action):
    def run(self, delete_vlan, name, delete_mac_learning_vlan_add, delete_mac_learn_disable, delete_mac_learning, delete_interface, delete_name, delete_hundredgigabitethernet, mac_learning_vlan_add, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_mac_learning_mac_learn_disable_vlan_mac_learning_vlan_add(delete_mac_learning=delete_mac_learning, name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_vlan=delete_vlan, delete_mac_learn_disable=delete_mac_learn_disable, mac_learning_vlan_add=mac_learning_vlan_add, delete_mac_learning_vlan_add=delete_mac_learning_vlan_add, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    