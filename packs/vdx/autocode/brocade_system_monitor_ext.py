#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system_monitor_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_system_monitor_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        input = ET.SubElement(show_system_monitor, "input")
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
        
    def show_system_monitor_output_switch_status_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        rbridge_id_out = ET.SubElement(switch_status, "rbridge-id-out")
        if kwargs.pop('delete_rbridge_id_out', False) is True:
            delete_rbridge_id_out = config.find('.//*rbridge-id-out')
            delete_rbridge_id_out.set('operation', 'delete')
            
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        switch_name = ET.SubElement(switch_status, "switch-name")
        if kwargs.pop('delete_switch_name', False) is True:
            delete_switch_name = config.find('.//*switch-name')
            delete_switch_name.set('operation', 'delete')
            
        switch_name.text = kwargs.pop('switch_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        switch_ip = ET.SubElement(switch_status, "switch-ip")
        if kwargs.pop('delete_switch_ip', False) is True:
            delete_switch_ip = config.find('.//*switch-ip')
            delete_switch_ip.set('operation', 'delete')
            
        switch_ip.text = kwargs.pop('switch_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_report_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        report_time = ET.SubElement(switch_status, "report-time")
        if kwargs.pop('delete_report_time', False) is True:
            delete_report_time = config.find('.//*report-time')
            delete_report_time.set('operation', 'delete')
            
        report_time.text = kwargs.pop('report_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        switch_state = ET.SubElement(switch_status, "switch-state")
        if kwargs.pop('delete_switch_state', False) is True:
            delete_switch_state = config.find('.//*switch-state')
            delete_switch_state.set('operation', 'delete')
            
        switch_state.text = kwargs.pop('switch_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        switch_state_reason = ET.SubElement(switch_status, "switch-state-reason")
        if kwargs.pop('delete_switch_state_reason', False) is True:
            delete_switch_state_reason = config.find('.//*switch-state-reason')
            delete_switch_state_reason.set('operation', 'delete')
            
        switch_state_reason.text = kwargs.pop('switch_state_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        component_status = ET.SubElement(switch_status, "component-status")
        if kwargs.pop('delete_component_status', False) is True:
            delete_component_status = config.find('.//*component-status')
            delete_component_status.set('operation', 'delete')
            
        component_name = ET.SubElement(component_status, "component-name")
        if kwargs.pop('delete_component_name', False) is True:
            delete_component_name = config.find('.//*component-name')
            delete_component_name.set('operation', 'delete')
            
        component_name.text = kwargs.pop('component_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        component_status = ET.SubElement(switch_status, "component-status")
        if kwargs.pop('delete_component_status', False) is True:
            delete_component_status = config.find('.//*component-status')
            delete_component_status.set('operation', 'delete')
            
        component_state = ET.SubElement(component_status, "component-state")
        if kwargs.pop('delete_component_state', False) is True:
            delete_component_state = config.find('.//*component-state')
            delete_component_state.set('operation', 'delete')
            
        component_state.text = kwargs.pop('component_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_area(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        port_status = ET.SubElement(switch_status, "port-status")
        if kwargs.pop('delete_port_status', False) is True:
            delete_port_status = config.find('.//*port-status')
            delete_port_status.set('operation', 'delete')
            
        port_area = ET.SubElement(port_status, "port-area")
        if kwargs.pop('delete_port_area', False) is True:
            delete_port_area = config.find('.//*port-area')
            delete_port_area.set('operation', 'delete')
            
        port_area.text = kwargs.pop('port_area')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        port_status = ET.SubElement(switch_status, "port-status")
        if kwargs.pop('delete_port_status', False) is True:
            delete_port_status = config.find('.//*port-status')
            delete_port_status.set('operation', 'delete')
            
        port_name = ET.SubElement(port_status, "port-name")
        if kwargs.pop('delete_port_name', False) is True:
            delete_port_name = config.find('.//*port-name')
            delete_port_name.set('operation', 'delete')
            
        port_name.text = kwargs.pop('port_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        if kwargs.pop('delete_show_system_monitor', False) is True:
            delete_show_system_monitor = config.find('.//*show-system-monitor')
            delete_show_system_monitor.set('operation', 'delete')
            
        output = ET.SubElement(show_system_monitor, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switch_status = ET.SubElement(output, "switch-status")
        if kwargs.pop('delete_switch_status', False) is True:
            delete_switch_status = config.find('.//*switch-status')
            delete_switch_status.set('operation', 'delete')
            
        port_status = ET.SubElement(switch_status, "port-status")
        if kwargs.pop('delete_port_status', False) is True:
            delete_port_status = config.find('.//*port-status')
            delete_port_status.set('operation', 'delete')
            
        port_state = ET.SubElement(port_status, "port-state")
        if kwargs.pop('delete_port_state', False) is True:
            delete_port_state = config.find('.//*port-state')
            delete_port_state.set('operation', 'delete')
            
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        