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


def interface_tengigabitethernet_vrrp_arp_unicast_request_receive(**kwargs):
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
            
    vrrp = ET.SubElement(tengigabitethernet, "vrrp", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_vrrp', False) is True:
        delete_vrrp = config.find('.//*vrrp')
        delete_vrrp.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrp, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    version_key = ET.SubElement(vrrp, "version")
    version_key.text = kwargs.pop('version')
    if kwargs.pop('delete_version', False) is True:
        delete_version = config.find('.//*version')
        delete_version.set('operation', 'delete')
            
    arp = ET.SubElement(vrrp, "arp")
    if kwargs.pop('delete_arp', False) is True:
        delete_arp = config.find('.//*arp')
        delete_arp.set('operation', 'delete')
        
    unicast_request = ET.SubElement(arp, "unicast-request")
    if kwargs.pop('delete_unicast_request', False) is True:
        delete_unicast_request = config.find('.//*unicast-request')
        delete_unicast_request.set('operation', 'delete')
        
    receive = ET.SubElement(unicast_request, "receive")
    if kwargs.pop('delete_receive', False) is True:
        delete_receive = config.find('.//*receive')
        delete_receive.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_vrrp_arp_unicast_request_receive_act(Action):
    def run(self, delete_unicast_request, name, delete_vrid, delete_receive, vrid, delete_version, version, delete_interface, delete_name, delete_vrrp, delete_tengigabitethernet, delete_arp, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_vrrp_arp_unicast_request_receive(delete_vrid=delete_vrid, delete_vrrp=delete_vrrp, name=name, delete_version=delete_version, delete_arp=delete_arp, delete_receive=delete_receive, password=password, version=version, delete_tengigabitethernet=delete_tengigabitethernet, host=host, vrid=vrid, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_unicast_request=delete_unicast_request, callback=_callback, mgr=mgr)
        return 0
    