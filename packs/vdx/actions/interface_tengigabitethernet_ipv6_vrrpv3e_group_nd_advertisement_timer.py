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


def interface_tengigabitethernet_ipv6_vrrpv3e_group_nd_advertisement_timer(**kwargs):
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
            
    nd_advertisement_timer = ET.SubElement(vrrpv3e_group, "nd-advertisement-timer")
    if kwargs.pop('delete_nd_advertisement_timer', False) is True:
        delete_nd_advertisement_timer = config.find('.//*nd-advertisement-timer')
        delete_nd_advertisement_timer.set('operation', 'delete')
        
    nd_advertisement_timer.text = kwargs.pop('nd_advertisement_timer')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ipv6_vrrpv3e_group_nd_advertisement_timer_act(Action):
    def run(self, delete_nd_advertisement_timer, name, delete_vrid, vrid, delete_interface, delete_name, delete_tengigabitethernet, nd_advertisement_timer, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ipv6_vrrpv3e_group_nd_advertisement_timer(delete_vrid=delete_vrid, name=name, delete_name=delete_name, nd_advertisement_timer=nd_advertisement_timer, username=username, delete_tengigabitethernet=delete_tengigabitethernet, vrid=vrid, host=host, delete_interface=delete_interface, delete_nd_advertisement_timer=delete_nd_advertisement_timer, password=password, callback=_callback, mgr=mgr)
        return 0
    