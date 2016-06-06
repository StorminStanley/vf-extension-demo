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


def interface_hundredgigabitethernet_rmon_collection_ether_stats_entry_ether_stats_owner(**kwargs):
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
            
    rmon = ET.SubElement(hundredgigabitethernet, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
    if kwargs.pop('delete_rmon', False) is True:
        delete_rmon = config.find('.//*rmon')
        delete_rmon.set('operation', 'delete')
        
    collection = ET.SubElement(rmon, "collection")
    if kwargs.pop('delete_collection', False) is True:
        delete_collection = config.find('.//*collection')
        delete_collection.set('operation', 'delete')
        
    ether_stats_entry = ET.SubElement(collection, "ether-stats-entry")
    if kwargs.pop('delete_ether_stats_entry', False) is True:
        delete_ether_stats_entry = config.find('.//*ether-stats-entry')
        delete_ether_stats_entry.set('operation', 'delete')
        
    ether_stats_index_key = ET.SubElement(ether_stats_entry, "ether-stats-index")
    ether_stats_index_key.text = kwargs.pop('ether_stats_index')
    if kwargs.pop('delete_ether_stats_index', False) is True:
        delete_ether_stats_index = config.find('.//*ether-stats-index')
        delete_ether_stats_index.set('operation', 'delete')
            
    ether_stats_owner = ET.SubElement(ether_stats_entry, "ether-stats-owner")
    if kwargs.pop('delete_ether_stats_owner', False) is True:
        delete_ether_stats_owner = config.find('.//*ether-stats-owner')
        delete_ether_stats_owner.set('operation', 'delete')
        
    ether_stats_owner.text = kwargs.pop('ether_stats_owner')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_rmon_collection_ether_stats_entry_ether_stats_owner_act(Action):
    def run(self, delete_collection, name, ether_stats_owner, delete_ether_stats_index, delete_rmon, delete_ether_stats_entry, ether_stats_index, delete_interface, delete_name, delete_hundredgigabitethernet, delete_ether_stats_owner, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_rmon_collection_ether_stats_entry_ether_stats_owner(ether_stats_owner=ether_stats_owner, delete_rmon=delete_rmon, name=name, delete_collection=delete_collection, delete_hundredgigabitethernet=delete_hundredgigabitethernet, username=username, delete_ether_stats_entry=delete_ether_stats_entry, ether_stats_index=ether_stats_index, host=host, delete_name=delete_name, delete_ether_stats_index=delete_ether_stats_index, delete_ether_stats_owner=delete_ether_stats_owner, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    