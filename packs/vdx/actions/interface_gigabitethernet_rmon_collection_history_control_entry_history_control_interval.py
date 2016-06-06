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


def interface_gigabitethernet_rmon_collection_history_control_entry_history_control_interval(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    gigabitethernet = ET.SubElement(interface, "gigabitethernet")
    if kwargs.pop('delete_gigabitethernet', False) is True:
        delete_gigabitethernet = config.find('.//*gigabitethernet')
        delete_gigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(gigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    rmon = ET.SubElement(gigabitethernet, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
    if kwargs.pop('delete_rmon', False) is True:
        delete_rmon = config.find('.//*rmon')
        delete_rmon.set('operation', 'delete')
        
    collection = ET.SubElement(rmon, "collection")
    if kwargs.pop('delete_collection', False) is True:
        delete_collection = config.find('.//*collection')
        delete_collection.set('operation', 'delete')
        
    history_control_entry = ET.SubElement(collection, "history-control-entry")
    if kwargs.pop('delete_history_control_entry', False) is True:
        delete_history_control_entry = config.find('.//*history-control-entry')
        delete_history_control_entry.set('operation', 'delete')
        
    history_control_index_key = ET.SubElement(history_control_entry, "history-control-index")
    history_control_index_key.text = kwargs.pop('history_control_index')
    if kwargs.pop('delete_history_control_index', False) is True:
        delete_history_control_index = config.find('.//*history-control-index')
        delete_history_control_index.set('operation', 'delete')
            
    history_control_interval = ET.SubElement(history_control_entry, "history-control-interval")
    if kwargs.pop('delete_history_control_interval', False) is True:
        delete_history_control_interval = config.find('.//*history-control-interval')
        delete_history_control_interval.set('operation', 'delete')
        
    history_control_interval.text = kwargs.pop('history_control_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_rmon_collection_history_control_entry_history_control_interval_act(Action):
    def run(self, delete_collection, delete_history_control_index, name, history_control_index, delete_rmon, delete_history_control_interval, delete_interface, delete_name, delete_history_control_entry, delete_gigabitethernet, history_control_interval, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_rmon_collection_history_control_entry_history_control_interval(delete_rmon=delete_rmon, name=name, history_control_index=history_control_index, delete_history_control_entry=delete_history_control_entry, delete_history_control_index=delete_history_control_index, delete_history_control_interval=delete_history_control_interval, delete_name=delete_name, history_control_interval=history_control_interval, host=host, delete_gigabitethernet=delete_gigabitethernet, delete_collection=delete_collection, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    