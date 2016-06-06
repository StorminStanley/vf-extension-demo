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


def interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_hold_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(port_channel, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    hide_vrrpv3_holder = ET.SubElement(ipv6, "hide-vrrpv3-holder", xmlns="urn:brocade.com:mgmt:brocade-vrrpv3")
    if kwargs.pop('delete_hide_vrrpv3_holder', False) is True:
        delete_hide_vrrpv3_holder = config.find('.//*hide-vrrpv3-holder')
        delete_hide_vrrpv3_holder.set('operation', 'delete')
        
    vrrpv3 = ET.SubElement(hide_vrrpv3_holder, "vrrpv3")
    if kwargs.pop('delete_vrrpv3', False) is True:
        delete_vrrpv3 = config.find('.//*vrrpv3')
        delete_vrrpv3.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrpv3, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    hold_time = ET.SubElement(vrrpv3, "hold-time")
    if kwargs.pop('delete_hold_time', False) is True:
        delete_hold_time = config.find('.//*hold-time')
        delete_hold_time.set('operation', 'delete')
        
    hold_time.text = kwargs.pop('hold_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_hold_time_act(Action):
    def run(self, name, delete_vrid, delete_hold_time, vrid, delete_port_channel, delete_interface, delete_name, hold_time, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_hold_time(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_port_channel=delete_port_channel, host=host, vrid=vrid, hold_time=hold_time, delete_interface=delete_interface, username=username, delete_hold_time=delete_hold_time, password=password, callback=_callback, mgr=mgr)
        return 0
    