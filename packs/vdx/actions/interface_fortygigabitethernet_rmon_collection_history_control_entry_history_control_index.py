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


def interface_fortygigabitethernet_rmon_collection_history_control_entry_history_control_index(**kwargs):
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
            
    rmon = ET.SubElement(fortygigabitethernet, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
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
        
    history_control_index = ET.SubElement(history_control_entry, "history-control-index")
    if kwargs.pop('delete_history_control_index', False) is True:
        delete_history_control_index = config.find('.//*history-control-index')
        delete_history_control_index.set('operation', 'delete')
        
    history_control_index.text = kwargs.pop('history_control_index')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_rmon_collection_history_control_entry_history_control_index_act(Action):
    def run(self, delete_collection, delete_rmon, name, history_control_index, delete_fortygigabitethernet, delete_history_control_index, delete_interface, delete_name, delete_history_control_entry, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_rmon_collection_history_control_entry_history_control_index(delete_rmon=delete_rmon, name=name, history_control_index=history_control_index, delete_history_control_entry=delete_history_control_entry, delete_history_control_index=delete_history_control_index, delete_name=delete_name, host=host, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_collection=delete_collection, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    