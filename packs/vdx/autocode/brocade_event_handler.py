#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_event_handler(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def event_handler_event_handler_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name = ET.SubElement(event_handler_list, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        description = ET.SubElement(event_handler_list, "description")
        if kwargs.pop('delete_description', False) is True:
            delete_description = config.find('.//*description')
            delete_description.set('operation', 'delete')
            
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        trigger = ET.SubElement(event_handler_list, "trigger")
        if kwargs.pop('delete_trigger', False) is True:
            delete_trigger = config.find('.//*trigger')
            delete_trigger.set('operation', 'delete')
            
        trigger_id = ET.SubElement(trigger, "trigger-id")
        if kwargs.pop('delete_trigger_id', False) is True:
            delete_trigger_id = config.find('.//*trigger-id')
            delete_trigger_id.set('operation', 'delete')
            
        trigger_id.text = kwargs.pop('trigger_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_vcs_vcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        trigger = ET.SubElement(event_handler_list, "trigger")
        if kwargs.pop('delete_trigger', False) is True:
            delete_trigger = config.find('.//*trigger')
            delete_trigger.set('operation', 'delete')
            
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        if kwargs.pop('delete_trigger_id', False) is True:
            delete_trigger_id = config.find('.//*trigger-id')
            delete_trigger_id.set('operation', 'delete')
                
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        if kwargs.pop('delete_trigger_choice', False) is True:
            delete_trigger_choice = config.find('.//*trigger-choice')
            delete_trigger_choice.set('operation', 'delete')
            
        vcs = ET.SubElement(trigger_choice, "vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        vcs = ET.SubElement(vcs, "vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        vcs.text = kwargs.pop('vcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_raslog_raslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        trigger = ET.SubElement(event_handler_list, "trigger")
        if kwargs.pop('delete_trigger', False) is True:
            delete_trigger = config.find('.//*trigger')
            delete_trigger.set('operation', 'delete')
            
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        if kwargs.pop('delete_trigger_id', False) is True:
            delete_trigger_id = config.find('.//*trigger-id')
            delete_trigger_id.set('operation', 'delete')
                
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        if kwargs.pop('delete_trigger_choice', False) is True:
            delete_trigger_choice = config.find('.//*trigger-choice')
            delete_trigger_choice.set('operation', 'delete')
            
        raslog = ET.SubElement(trigger_choice, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        raslog = ET.SubElement(raslog, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        raslog.text = kwargs.pop('raslog')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_action_action_choice_python_script_python_script(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        if kwargs.pop('delete_event_handler', False) is True:
            delete_event_handler = config.find('.//*event-handler')
            delete_event_handler.set('operation', 'delete')
            
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        if kwargs.pop('delete_event_handler_list', False) is True:
            delete_event_handler_list = config.find('.//*event-handler-list')
            delete_event_handler_list.set('operation', 'delete')
            
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action = ET.SubElement(event_handler_list, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action_choice = ET.SubElement(action, "action-choice")
        if kwargs.pop('delete_action_choice', False) is True:
            delete_action_choice = config.find('.//*action-choice')
            delete_action_choice.set('operation', 'delete')
            
        python_script = ET.SubElement(action_choice, "python-script")
        if kwargs.pop('delete_python_script', False) is True:
            delete_python_script = config.find('.//*python-script')
            delete_python_script.set('operation', 'delete')
            
        python_script = ET.SubElement(python_script, "python-script")
        if kwargs.pop('delete_python_script', False) is True:
            delete_python_script = config.find('.//*python-script')
            delete_python_script.set('operation', 'delete')
            
        python_script.text = kwargs.pop('python_script')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        