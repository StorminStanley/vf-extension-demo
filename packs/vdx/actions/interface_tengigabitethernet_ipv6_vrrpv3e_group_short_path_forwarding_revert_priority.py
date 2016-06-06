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


def interface_tengigabitethernet_ipv6_vrrpv3e_group_short_path_forwarding_revert_priority(**kwargs):
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
            
    ipv6 = ET.SubElement(tengigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    vrrpv3e_group = ET.SubElement(ipv6, "vrrpv3e-group", xmlns="urn:brocade.com:mgmt:brocade-vrrpv3")
    if kwargs.pop('delete_vrrpv3e_group', False) is True:
        delete_vrrpv3e_group = config.find('.//*vrrpv3e-group')
        delete_vrrpv3e_group.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrpv3e_group, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    short_path_forwarding = ET.SubElement(vrrpv3e_group, "short-path-forwarding")
    if kwargs.pop('delete_short_path_forwarding', False) is True:
        delete_short_path_forwarding = config.find('.//*short-path-forwarding')
        delete_short_path_forwarding.set('operation', 'delete')
        
    revert_priority = ET.SubElement(short_path_forwarding, "revert-priority")
    if kwargs.pop('delete_revert_priority', False) is True:
        delete_revert_priority = config.find('.//*revert-priority')
        delete_revert_priority.set('operation', 'delete')
        
    revert_priority.text = kwargs.pop('revert_priority')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ipv6_vrrpv3e_group_short_path_forwarding_revert_priority_act(Action):
    def run(self, name, revert_priority, delete_vrid, vrid, delete_short_path_forwarding, delete_interface, delete_name, delete_tengigabitethernet, delete_revert_priority, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ipv6_vrrpv3e_group_short_path_forwarding_revert_priority(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_short_path_forwarding=delete_short_path_forwarding, delete_tengigabitethernet=delete_tengigabitethernet, vrid=vrid, revert_priority=revert_priority, host=host, delete_interface=delete_interface, username=username, delete_revert_priority=delete_revert_priority, password=password, callback=_callback, mgr=mgr)
        return 0
    