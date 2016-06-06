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


def rbridge_id_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    arp_entry = ET.SubElement(rbridge_id, "arp-entry", xmlns="urn:brocade.com:mgmt:brocade-arp")
    if kwargs.pop('delete_arp_entry', False) is True:
        delete_arp_entry = config.find('.//*arp-entry')
        delete_arp_entry.set('operation', 'delete')
        
    arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
    arp_ip_address_key.text = kwargs.pop('arp_ip_address')
    if kwargs.pop('delete_arp_ip_address', False) is True:
        delete_arp_ip_address = config.find('.//*arp-ip-address')
        delete_arp_ip_address.set('operation', 'delete')
            
    interfacetype = ET.SubElement(arp_entry, "interfacetype")
    if kwargs.pop('delete_interfacetype', False) is True:
        delete_interfacetype = config.find('.//*interfacetype')
        delete_interfacetype.set('operation', 'delete')
        
    GigabitEthernet = ET.SubElement(interfacetype, "GigabitEthernet")
    if kwargs.pop('delete_GigabitEthernet', False) is True:
        delete_GigabitEthernet = config.find('.//*GigabitEthernet')
        delete_GigabitEthernet.set('operation', 'delete')
        
    GigabitEthernet = ET.SubElement(GigabitEthernet, "GigabitEthernet")
    if kwargs.pop('delete_GigabitEthernet', False) is True:
        delete_GigabitEthernet = config.find('.//*GigabitEthernet')
        delete_GigabitEthernet.set('operation', 'delete')
        
    GigabitEthernet.text = kwargs.pop('GigabitEthernet')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet_act(Action):
    def run(self, rbridge_id, delete_interfacetype, GigabitEthernet, delete_arp_ip_address, arp_ip_address, delete_arp_entry, delete_rbridge_id, delete_GigabitEthernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet(delete_arp_entry=delete_arp_entry, username=username, rbridge_id=rbridge_id, delete_GigabitEthernet=delete_GigabitEthernet, delete_interfacetype=delete_interfacetype, arp_ip_address=arp_ip_address, host=host, delete_arp_ip_address=delete_arp_ip_address, GigabitEthernet=GigabitEthernet, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    