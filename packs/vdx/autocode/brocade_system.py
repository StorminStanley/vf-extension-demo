#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_system_uptime_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        input = ET.SubElement(get_system_uptime, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(input, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        if kwargs.pop('delete_show_system_uptime', False) is True:
            delete_show_system_uptime = config.find('.//*show-system-uptime')
            delete_show_system_uptime.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(show_system_uptime, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_days(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        if kwargs.pop('delete_show_system_uptime', False) is True:
            delete_show_system_uptime = config.find('.//*show-system-uptime')
            delete_show_system_uptime.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        days = ET.SubElement(show_system_uptime, "days")
        if kwargs.pop('delete_days', False) is True:
            delete_days = config.find('.//*days')
            delete_days.set('operation', 'delete')
            
        days.text = kwargs.pop('days')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_hours(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        if kwargs.pop('delete_show_system_uptime', False) is True:
            delete_show_system_uptime = config.find('.//*show-system-uptime')
            delete_show_system_uptime.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        hours = ET.SubElement(show_system_uptime, "hours")
        if kwargs.pop('delete_hours', False) is True:
            delete_hours = config.find('.//*hours')
            delete_hours.set('operation', 'delete')
            
        hours.text = kwargs.pop('hours')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_minutes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        if kwargs.pop('delete_show_system_uptime', False) is True:
            delete_show_system_uptime = config.find('.//*show-system-uptime')
            delete_show_system_uptime.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        minutes = ET.SubElement(show_system_uptime, "minutes")
        if kwargs.pop('delete_minutes', False) is True:
            delete_minutes = config.find('.//*minutes')
            delete_minutes.set('operation', 'delete')
            
        minutes.text = kwargs.pop('minutes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_seconds(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        if kwargs.pop('delete_show_system_uptime', False) is True:
            delete_show_system_uptime = config.find('.//*show-system-uptime')
            delete_show_system_uptime.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        seconds = ET.SubElement(show_system_uptime, "seconds")
        if kwargs.pop('delete_seconds', False) is True:
            delete_seconds = config.find('.//*seconds')
            delete_seconds.set('operation', 'delete')
            
        seconds.text = kwargs.pop('seconds')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_cmd_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        if kwargs.pop('delete_get_system_uptime', False) is True:
            delete_get_system_uptime = config.find('.//*get-system-uptime')
            delete_get_system_uptime.set('operation', 'delete')
            
        output = ET.SubElement(get_system_uptime, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cmd_error = ET.SubElement(output, "cmd-error")
        if kwargs.pop('delete_cmd_error', False) is True:
            delete_cmd_error = config.find('.//*cmd-error')
            delete_cmd_error.set('operation', 'delete')
            
        cmd_error.text = kwargs.pop('cmd_error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        