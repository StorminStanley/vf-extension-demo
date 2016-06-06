#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_clock(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def clock_sa_clock_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        clock_sa = ET.SubElement(config, "clock-sa", xmlns="urn:brocade.com:mgmt:brocade-clock")
        if kwargs.pop('delete_clock_sa', False) is True:
            delete_clock_sa = config.find('.//*clock-sa')
            delete_clock_sa.set('operation', 'delete')
            
        clock = ET.SubElement(clock_sa, "clock")
        if kwargs.pop('delete_clock', False) is True:
            delete_clock = config.find('.//*clock')
            delete_clock.set('operation', 'delete')
            
        timezone = ET.SubElement(clock, "timezone")
        if kwargs.pop('delete_timezone', False) is True:
            delete_timezone = config.find('.//*timezone')
            delete_timezone.set('operation', 'delete')
            
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        if kwargs.pop('delete_show_clock', False) is True:
            delete_show_clock = config.find('.//*show-clock')
            delete_show_clock.set('operation', 'delete')
            
        input = ET.SubElement(show_clock, "input")
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
        
    def show_clock_output_clock_time_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        if kwargs.pop('delete_show_clock', False) is True:
            delete_show_clock = config.find('.//*show-clock')
            delete_show_clock.set('operation', 'delete')
            
        output = ET.SubElement(show_clock, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        clock_time = ET.SubElement(output, "clock-time")
        if kwargs.pop('delete_clock_time', False) is True:
            delete_clock_time = config.find('.//*clock-time')
            delete_clock_time.set('operation', 'delete')
            
        rbridge_id_out = ET.SubElement(clock_time, "rbridge-id-out")
        if kwargs.pop('delete_rbridge_id_out', False) is True:
            delete_rbridge_id_out = config.find('.//*rbridge-id-out')
            delete_rbridge_id_out.set('operation', 'delete')
            
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_current_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        if kwargs.pop('delete_show_clock', False) is True:
            delete_show_clock = config.find('.//*show-clock')
            delete_show_clock.set('operation', 'delete')
            
        output = ET.SubElement(show_clock, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        clock_time = ET.SubElement(output, "clock-time")
        if kwargs.pop('delete_clock_time', False) is True:
            delete_clock_time = config.find('.//*clock-time')
            delete_clock_time.set('operation', 'delete')
            
        current_time = ET.SubElement(clock_time, "current-time")
        if kwargs.pop('delete_current_time', False) is True:
            delete_current_time = config.find('.//*current-time')
            delete_current_time.set('operation', 'delete')
            
        current_time.text = kwargs.pop('current_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        if kwargs.pop('delete_show_clock', False) is True:
            delete_show_clock = config.find('.//*show-clock')
            delete_show_clock.set('operation', 'delete')
            
        output = ET.SubElement(show_clock, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        clock_time = ET.SubElement(output, "clock-time")
        if kwargs.pop('delete_clock_time', False) is True:
            delete_clock_time = config.find('.//*clock-time')
            delete_clock_time.set('operation', 'delete')
            
        timezone = ET.SubElement(clock_time, "timezone")
        if kwargs.pop('delete_timezone', False) is True:
            delete_timezone = config.find('.//*timezone')
            delete_timezone.set('operation', 'delete')
            
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        