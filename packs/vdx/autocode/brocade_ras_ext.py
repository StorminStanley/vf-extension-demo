#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ras_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_raslog_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        input = ET.SubElement(show_raslog, "input")
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
        
    def show_raslog_input_number_of_latest_events(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        input = ET.SubElement(show_raslog, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        number_of_latest_events = ET.SubElement(input, "number-of-latest-events")
        if kwargs.pop('delete_number_of_latest_events', False) is True:
            delete_number_of_latest_events = config.find('.//*number-of-latest-events')
            delete_number_of_latest_events.set('operation', 'delete')
            
        number_of_latest_events.text = kwargs.pop('number_of_latest_events')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(show_all_raslog, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        number_of_entries = ET.SubElement(show_all_raslog, "number-of-entries")
        if kwargs.pop('delete_number_of_entries', False) is True:
            delete_number_of_entries = config.find('.//*number-of-entries')
            delete_number_of_entries.set('operation', 'delete')
            
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        index = ET.SubElement(raslog_entries, "index")
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
            
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        message_id = ET.SubElement(raslog_entries, "message-id")
        if kwargs.pop('delete_message_id', False) is True:
            delete_message_id = config.find('.//*message-id')
            delete_message_id.set('operation', 'delete')
            
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        date_and_time_info = ET.SubElement(raslog_entries, "date-and-time-info")
        if kwargs.pop('delete_date_and_time_info', False) is True:
            delete_date_and_time_info = config.find('.//*date-and-time-info')
            delete_date_and_time_info.set('operation', 'delete')
            
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        severity = ET.SubElement(raslog_entries, "severity")
        if kwargs.pop('delete_severity', False) is True:
            delete_severity = config.find('.//*severity')
            delete_severity.set('operation', 'delete')
            
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_repeat_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        repeat_count = ET.SubElement(raslog_entries, "repeat-count")
        if kwargs.pop('delete_repeat_count', False) is True:
            delete_repeat_count = config.find('.//*repeat-count')
            delete_repeat_count.set('operation', 'delete')
            
        repeat_count.text = kwargs.pop('repeat_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        message = ET.SubElement(raslog_entries, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        message_flag = ET.SubElement(raslog_entries, "message-flag")
        if kwargs.pop('delete_message_flag', False) is True:
            delete_message_flag = config.find('.//*message-flag')
            delete_message_flag.set('operation', 'delete')
            
        message_flag.text = kwargs.pop('message_flag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_log_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        log_type = ET.SubElement(raslog_entries, "log-type")
        if kwargs.pop('delete_log_type', False) is True:
            delete_log_type = config.find('.//*log-type')
            delete_log_type.set('operation', 'delete')
            
        log_type.text = kwargs.pop('log_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_switch_or_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        if kwargs.pop('delete_show_all_raslog', False) is True:
            delete_show_all_raslog = config.find('.//*show-all-raslog')
            delete_show_all_raslog.set('operation', 'delete')
            
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        if kwargs.pop('delete_raslog_entries', False) is True:
            delete_raslog_entries = config.find('.//*raslog-entries')
            delete_raslog_entries.set('operation', 'delete')
            
        switch_or_chassis_name = ET.SubElement(raslog_entries, "switch-or-chassis-name")
        if kwargs.pop('delete_switch_or_chassis_name', False) is True:
            delete_switch_or_chassis_name = config.find('.//*switch-or-chassis-name')
            delete_switch_or_chassis_name.set('operation', 'delete')
            
        switch_or_chassis_name.text = kwargs.pop('switch_or_chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_cmd_status_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        if kwargs.pop('delete_show_raslog', False) is True:
            delete_show_raslog = config.find('.//*show-raslog')
            delete_show_raslog.set('operation', 'delete')
            
        output = ET.SubElement(show_raslog, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cmd_status_error_msg = ET.SubElement(output, "cmd-status-error-msg")
        if kwargs.pop('delete_cmd_status_error_msg', False) is True:
            delete_cmd_status_error_msg = config.find('.//*cmd-status-error-msg')
            delete_cmd_status_error_msg.set('operation', 'delete')
            
        cmd_status_error_msg.text = kwargs.pop('cmd_status_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        input = ET.SubElement(show_support_save_status, "input")
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
        
    def show_support_save_status_output_show_support_save_status_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        output = ET.SubElement(show_support_save_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(show_support_save_status, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        output = ET.SubElement(show_support_save_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        status = ET.SubElement(show_support_save_status, "status")
        if kwargs.pop('delete_status', False) is True:
            delete_status = config.find('.//*status')
            delete_status.set('operation', 'delete')
            
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        output = ET.SubElement(show_support_save_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        message = ET.SubElement(show_support_save_status, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_percentage_of_completion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        output = ET.SubElement(show_support_save_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        if kwargs.pop('delete_show_support_save_status', False) is True:
            delete_show_support_save_status = config.find('.//*show-support-save-status')
            delete_show_support_save_status.set('operation', 'delete')
            
        percentage_of_completion = ET.SubElement(show_support_save_status, "percentage-of-completion")
        if kwargs.pop('delete_percentage_of_completion', False) is True:
            delete_percentage_of_completion = config.find('.//*percentage-of-completion')
            delete_percentage_of_completion.set('operation', 'delete')
            
        percentage_of_completion.text = kwargs.pop('percentage_of_completion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        if kwargs.pop('delete_show_system_info', False) is True:
            delete_show_system_info = config.find('.//*show-system-info')
            delete_show_system_info.set('operation', 'delete')
            
        input = ET.SubElement(show_system_info, "input")
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
        
    def show_system_info_output_show_system_info_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        if kwargs.pop('delete_show_system_info', False) is True:
            delete_show_system_info = config.find('.//*show-system-info')
            delete_show_system_info.set('operation', 'delete')
            
        output = ET.SubElement(show_system_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_info = ET.SubElement(output, "show-system-info")
        if kwargs.pop('delete_show_system_info', False) is True:
            delete_show_system_info = config.find('.//*show-system-info')
            delete_show_system_info.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(show_system_info, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_output_show_system_info_stack_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        if kwargs.pop('delete_show_system_info', False) is True:
            delete_show_system_info = config.find('.//*show-system-info')
            delete_show_system_info.set('operation', 'delete')
            
        output = ET.SubElement(show_system_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_system_info = ET.SubElement(output, "show-system-info")
        if kwargs.pop('delete_show_system_info', False) is True:
            delete_show_system_info = config.find('.//*show-system-info')
            delete_show_system_info.set('operation', 'delete')
            
        stack_mac = ET.SubElement(show_system_info, "stack-mac")
        if kwargs.pop('delete_stack_mac', False) is True:
            delete_stack_mac = config.find('.//*stack-mac')
            delete_stack_mac.set('operation', 'delete')
            
        stack_mac.text = kwargs.pop('stack_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        