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


def interface_fortygigabitethernet_switchport_private_vlan_association_trunk_trunk_pri_pvlan(**kwargs):
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
        
    private_vlan = ET.SubElement(switchport, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    association = ET.SubElement(private_vlan, "association")
    if kwargs.pop('delete_association', False) is True:
        delete_association = config.find('.//*association')
        delete_association.set('operation', 'delete')
        
    trunk = ET.SubElement(association, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    trunk_sec_pvlan_key = ET.SubElement(trunk, "trunk-sec-pvlan")
    trunk_sec_pvlan_key.text = kwargs.pop('trunk_sec_pvlan')
    if kwargs.pop('delete_trunk_sec_pvlan', False) is True:
        delete_trunk_sec_pvlan = config.find('.//*trunk-sec-pvlan')
        delete_trunk_sec_pvlan.set('operation', 'delete')
            
    trunk_pri_pvlan = ET.SubElement(trunk, "trunk-pri-pvlan")
    if kwargs.pop('delete_trunk_pri_pvlan', False) is True:
        delete_trunk_pri_pvlan = config.find('.//*trunk-pri-pvlan')
        delete_trunk_pri_pvlan.set('operation', 'delete')
        
    trunk_pri_pvlan.text = kwargs.pop('trunk_pri_pvlan')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_switchport_private_vlan_association_trunk_trunk_pri_pvlan_act(Action):
    def run(self, delete_switchport, delete_association, delete_trunk_sec_pvlan, name, delete_trunk, delete_fortygigabitethernet, delete_trunk_pri_pvlan, trunk_sec_pvlan, delete_private_vlan, delete_interface, delete_name, trunk_pri_pvlan, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_switchport_private_vlan_association_trunk_trunk_pri_pvlan(name=name, delete_trunk=delete_trunk, delete_association=delete_association, trunk_pri_pvlan=trunk_pri_pvlan, delete_switchport=delete_switchport, delete_name=delete_name, delete_trunk_pri_pvlan=delete_trunk_pri_pvlan, host=host, delete_fortygigabitethernet=delete_fortygigabitethernet, trunk_sec_pvlan=trunk_sec_pvlan, delete_trunk_sec_pvlan=delete_trunk_sec_pvlan, delete_interface=delete_interface, username=username, password=password, delete_private_vlan=delete_private_vlan, callback=_callback, mgr=mgr)
        return 0
    