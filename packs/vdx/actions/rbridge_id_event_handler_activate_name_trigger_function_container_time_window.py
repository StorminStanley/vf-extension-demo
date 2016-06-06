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


def rbridge_id_event_handler_activate_name_trigger_function_container_time_window(**kwargs):
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
            
    event_handler = ET.SubElement(rbridge_id, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
    if kwargs.pop('delete_event_handler', False) is True:
        delete_event_handler = config.find('.//*event-handler')
        delete_event_handler.set('operation', 'delete')
        
    activate = ET.SubElement(event_handler, "activate")
    if kwargs.pop('delete_activate', False) is True:
        delete_activate = config.find('.//*activate')
        delete_activate.set('operation', 'delete')
        
    name = ET.SubElement(activate, "name")
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
        
    name_key = ET.SubElement(name, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    trigger_function_container = ET.SubElement(name, "trigger-function-container")
    if kwargs.pop('delete_trigger_function_container', False) is True:
        delete_trigger_function_container = config.find('.//*trigger-function-container')
        delete_trigger_function_container.set('operation', 'delete')
        
    time_window = ET.SubElement(trigger_function_container, "time-window")
    if kwargs.pop('delete_time_window', False) is True:
        delete_time_window = config.find('.//*time-window')
        delete_time_window.set('operation', 'delete')
        
    time_window.text = kwargs.pop('time_window')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_event_handler_activate_name_trigger_function_container_time_window_act(Action):
    def run(self, time_window, rbridge_id, delete_event_handler, delete_time_window, delete_activate, delete_trigger_function_container, delete_name, delete_rbridge_id, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_event_handler_activate_name_trigger_function_container_time_window(time_window=time_window, delete_activate=delete_activate, name=name, delete_name=delete_name, username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_trigger_function_container=delete_trigger_function_container, delete_event_handler=delete_event_handler, host=host, delete_time_window=delete_time_window, password=password, callback=_callback, mgr=mgr)
        return 0
    