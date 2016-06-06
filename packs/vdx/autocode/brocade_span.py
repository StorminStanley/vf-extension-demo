#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_span(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def monitor_session_session_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number = ET.SubElement(session, "session-number")
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
            
        session_number.text = kwargs.pop('session_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        description = ET.SubElement(session, "description")
        if kwargs.pop('delete_description', False) is True:
            delete_description = config.find('.//*description')
            delete_description.set('operation', 'delete')
            
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        source = ET.SubElement(span_command, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        src_tengigabitethernet = ET.SubElement(span_command, "src-tengigabitethernet")
        if kwargs.pop('delete_src_tengigabitethernet', False) is True:
            delete_src_tengigabitethernet = config.find('.//*src-tengigabitethernet')
            delete_src_tengigabitethernet.set('operation', 'delete')
            
        src_tengigabitethernet.text = kwargs.pop('src_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        src_tengigabitethernet_val = ET.SubElement(span_command, "src-tengigabitethernet-val")
        if kwargs.pop('delete_src_tengigabitethernet_val', False) is True:
            delete_src_tengigabitethernet_val = config.find('.//*src-tengigabitethernet-val')
            delete_src_tengigabitethernet_val.set('operation', 'delete')
            
        src_tengigabitethernet_val.text = kwargs.pop('src_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_destination(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        destination = ET.SubElement(span_command, "destination")
        if kwargs.pop('delete_destination', False) is True:
            delete_destination = config.find('.//*destination')
            delete_destination.set('operation', 'delete')
            
        destination.text = kwargs.pop('destination')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        dest_tengigabitethernet = ET.SubElement(span_command, "dest-tengigabitethernet")
        if kwargs.pop('delete_dest_tengigabitethernet', False) is True:
            delete_dest_tengigabitethernet = config.find('.//*dest-tengigabitethernet')
            delete_dest_tengigabitethernet.set('operation', 'delete')
            
        dest_tengigabitethernet.text = kwargs.pop('dest_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        dest_tengigabitethernet_val = ET.SubElement(span_command, "dest-tengigabitethernet-val")
        if kwargs.pop('delete_dest_tengigabitethernet_val', False) is True:
            delete_dest_tengigabitethernet_val = config.find('.//*dest-tengigabitethernet-val')
            delete_dest_tengigabitethernet_val.set('operation', 'delete')
            
        dest_tengigabitethernet_val.text = kwargs.pop('dest_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_vlan_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        dest_vlan_val = ET.SubElement(span_command, "dest-vlan-val")
        if kwargs.pop('delete_dest_vlan_val', False) is True:
            delete_dest_vlan_val = config.find('.//*dest-vlan-val')
            delete_dest_vlan_val.set('operation', 'delete')
            
        dest_vlan_val.text = kwargs.pop('dest_vlan_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        if kwargs.pop('delete_session_number', False) is True:
            delete_session_number = config.find('.//*session-number')
            delete_session_number.set('operation', 'delete')
                
        span_command = ET.SubElement(session, "span-command")
        if kwargs.pop('delete_span_command', False) is True:
            delete_span_command = config.find('.//*span-command')
            delete_span_command.set('operation', 'delete')
            
        direction = ET.SubElement(span_command, "direction")
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
            
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        