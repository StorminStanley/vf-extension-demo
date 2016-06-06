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


def interface_hundredgigabitethernet_switchport_access_rspan_access_rspan_access_vlan(**kwargs):
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
        
    access = ET.SubElement(switchport, "access")
    if kwargs.pop('delete_access', False) is True:
        delete_access = config.find('.//*access')
        delete_access.set('operation', 'delete')
        
    rspan_access = ET.SubElement(access, "rspan-access")
    if kwargs.pop('delete_rspan_access', False) is True:
        delete_rspan_access = config.find('.//*rspan-access')
        delete_rspan_access.set('operation', 'delete')
        
    rspan_access_vlan = ET.SubElement(rspan_access, "rspan-access-vlan")
    if kwargs.pop('delete_rspan_access_vlan', False) is True:
        delete_rspan_access_vlan = config.find('.//*rspan-access-vlan')
        delete_rspan_access_vlan.set('operation', 'delete')
        
    rspan_access_vlan.text = kwargs.pop('rspan_access_vlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_switchport_access_rspan_access_rspan_access_vlan_act(Action):
    def run(self, delete_switchport, name, rspan_access_vlan, delete_access, delete_interface, delete_name, delete_rspan_access_vlan, delete_hundredgigabitethernet, delete_rspan_access, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_switchport_access_rspan_access_rspan_access_vlan(name=name, delete_name=delete_name, delete_switchport=delete_switchport, delete_access=delete_access, delete_hundredgigabitethernet=delete_hundredgigabitethernet, rspan_access_vlan=rspan_access_vlan, delete_rspan_access_vlan=delete_rspan_access_vlan, delete_rspan_access=delete_rspan_access, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    