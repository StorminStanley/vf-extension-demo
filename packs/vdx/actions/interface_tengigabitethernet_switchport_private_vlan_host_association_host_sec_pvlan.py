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


def interface_tengigabitethernet_switchport_private_vlan_host_association_host_sec_pvlan(**kwargs):
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
        
    private_vlan = ET.SubElement(switchport, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    host_association = ET.SubElement(private_vlan, "host-association")
    if kwargs.pop('delete_host_association', False) is True:
        delete_host_association = config.find('.//*host-association')
        delete_host_association.set('operation', 'delete')
        
    host_sec_pvlan = ET.SubElement(host_association, "host-sec-pvlan")
    if kwargs.pop('delete_host_sec_pvlan', False) is True:
        delete_host_sec_pvlan = config.find('.//*host-sec-pvlan')
        delete_host_sec_pvlan.set('operation', 'delete')
        
    host_sec_pvlan.text = kwargs.pop('host_sec_pvlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_switchport_private_vlan_host_association_host_sec_pvlan_act(Action):
    def run(self, delete_switchport, delete_host_sec_pvlan, name, host_sec_pvlan, delete_private_vlan, delete_interface, delete_name, delete_tengigabitethernet, delete_host_association, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_switchport_private_vlan_host_association_host_sec_pvlan(name=name, host_sec_pvlan=host_sec_pvlan, delete_switchport=delete_switchport, username=username, delete_private_vlan=delete_private_vlan, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_host_sec_pvlan=delete_host_sec_pvlan, delete_name=delete_name, delete_interface=delete_interface, delete_host_association=delete_host_association, password=password, callback=_callback, mgr=mgr)
        return 0
    