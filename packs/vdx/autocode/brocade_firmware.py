#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_firmware(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def firmware_autoupgrade_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade = ET.SubElement(firmware, "autoupgrade")
        if kwargs.pop('delete_autoupgrade', False) is True:
            delete_autoupgrade = config.find('.//*autoupgrade')
            delete_autoupgrade.set('operation', 'delete')
            
        enable = ET.SubElement(autoupgrade, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        if kwargs.pop('delete_autoupgrade_params', False) is True:
            delete_autoupgrade_params = config.find('.//*autoupgrade-params')
            delete_autoupgrade_params.set('operation', 'delete')
            
        path = ET.SubElement(autoupgrade_params, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        if kwargs.pop('delete_autoupgrade_params', False) is True:
            delete_autoupgrade_params = config.find('.//*autoupgrade-params')
            delete_autoupgrade_params.set('operation', 'delete')
            
        protocol = ET.SubElement(autoupgrade_params, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_ipaddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        if kwargs.pop('delete_autoupgrade_params', False) is True:
            delete_autoupgrade_params = config.find('.//*autoupgrade-params')
            delete_autoupgrade_params.set('operation', 'delete')
            
        ipaddress = ET.SubElement(autoupgrade_params, "ipaddress")
        if kwargs.pop('delete_ipaddress', False) is True:
            delete_ipaddress = config.find('.//*ipaddress')
            delete_ipaddress.set('operation', 'delete')
            
        ipaddress.text = kwargs.pop('ipaddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        if kwargs.pop('delete_autoupgrade_params', False) is True:
            delete_autoupgrade_params = config.find('.//*autoupgrade-params')
            delete_autoupgrade_params.set('operation', 'delete')
            
        username = ET.SubElement(autoupgrade_params, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_pass(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        if kwargs.pop('delete_firmware', False) is True:
            delete_firmware = config.find('.//*firmware')
            delete_firmware.set('operation', 'delete')
            
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        if kwargs.pop('delete_autoupgrade_params', False) is True:
            delete_autoupgrade_params = config.find('.//*autoupgrade-params')
            delete_autoupgrade_params.set('operation', 'delete')
            
        pass = ET.SubElement(autoupgrade_params, "pass")
        if kwargs.pop('delete_pass', False) is True:
            delete_pass = config.find('.//*pass')
            delete_pass.set('operation', 'delete')
            
        pass.text = kwargs.pop('pass')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_input_fwdl_tid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        input = ET.SubElement(fwdl_status, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fwdl_tid = ET.SubElement(input, "fwdl-tid")
        if kwargs.pop('delete_fwdl_tid', False) is True:
            delete_fwdl_tid = config.find('.//*fwdl-tid')
            delete_fwdl_tid.set('operation', 'delete')
            
        fwdl_tid.text = kwargs.pop('fwdl_tid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        number_of_entries = ET.SubElement(output, "number-of-entries")
        if kwargs.pop('delete_number_of_entries', False) is True:
            delete_number_of_entries = config.find('.//*number-of-entries')
            delete_number_of_entries.set('operation', 'delete')
            
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_state = ET.SubElement(output, "fwdl-state")
        if kwargs.pop('delete_fwdl_state', False) is True:
            delete_fwdl_state = config.find('.//*fwdl-state')
            delete_fwdl_state.set('operation', 'delete')
            
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        index = ET.SubElement(fwdl_entries, "index")
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
            
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        message_id = ET.SubElement(fwdl_entries, "message-id")
        if kwargs.pop('delete_message_id', False) is True:
            delete_message_id = config.find('.//*message-id')
            delete_message_id.set('operation', 'delete')
            
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        if kwargs.pop('delete_date_and_time_info', False) is True:
            delete_date_and_time_info = config.find('.//*date-and-time-info')
            delete_date_and_time_info.set('operation', 'delete')
            
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        message = ET.SubElement(fwdl_entries, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        if kwargs.pop('delete_blade_slot', False) is True:
            delete_blade_slot = config.find('.//*blade-slot')
            delete_blade_slot.set('operation', 'delete')
            
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        if kwargs.pop('delete_blade_swbd', False) is True:
            delete_blade_swbd = config.find('.//*blade-swbd')
            delete_blade_swbd.set('operation', 'delete')
            
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        if kwargs.pop('delete_blade_name', False) is True:
            delete_blade_name = config.find('.//*blade-name')
            delete_blade_name.set('operation', 'delete')
            
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        if kwargs.pop('delete_blade_state', False) is True:
            delete_blade_state = config.find('.//*blade-state')
            delete_blade_state.set('operation', 'delete')
            
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        if kwargs.pop('delete_blade_app', False) is True:
            delete_blade_app = config.find('.//*blade-app')
            delete_blade_app.set('operation', 'delete')
            
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        if kwargs.pop('delete_activate_status', False) is True:
            delete_activate_status = config.find('.//*activate-status')
            delete_activate_status.set('operation', 'delete')
            
        input = ET.SubElement(activate_status, "input")
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
        
    def activate_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        if kwargs.pop('delete_activate_status', False) is True:
            delete_activate_status = config.find('.//*activate-status')
            delete_activate_status.set('operation', 'delete')
            
        output = ET.SubElement(activate_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        overall_status = ET.SubElement(output, "overall-status")
        if kwargs.pop('delete_overall_status', False) is True:
            delete_overall_status = config.find('.//*overall-status')
            delete_overall_status.set('operation', 'delete')
            
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_overall_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        if kwargs.pop('delete_activate_status', False) is True:
            delete_activate_status = config.find('.//*activate-status')
            delete_activate_status.set('operation', 'delete')
            
        output = ET.SubElement(activate_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        overall_error_msg = ET.SubElement(output, "overall-error-msg")
        if kwargs.pop('delete_overall_error_msg', False) is True:
            delete_overall_error_msg = config.find('.//*overall-error-msg')
            delete_overall_error_msg.set('operation', 'delete')
            
        overall_error_msg.text = kwargs.pop('overall_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        if kwargs.pop('delete_activate_status', False) is True:
            delete_activate_status = config.find('.//*activate-status')
            delete_activate_status.set('operation', 'delete')
            
        output = ET.SubElement(activate_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        activate_entries = ET.SubElement(output, "activate-entries")
        if kwargs.pop('delete_activate_entries', False) is True:
            delete_activate_entries = config.find('.//*activate-entries')
            delete_activate_entries.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(activate_entries, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        if kwargs.pop('delete_activate_status', False) is True:
            delete_activate_status = config.find('.//*activate-status')
            delete_activate_status.set('operation', 'delete')
            
        output = ET.SubElement(activate_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        activate_entries = ET.SubElement(output, "activate-entries")
        if kwargs.pop('delete_activate_entries', False) is True:
            delete_activate_entries = config.find('.//*activate-entries')
            delete_activate_entries.set('operation', 'delete')
            
        status = ET.SubElement(activate_entries, "status")
        if kwargs.pop('delete_status', False) is True:
            delete_status = config.find('.//*status')
            delete_status.set('operation', 'delete')
            
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_scp_protocol_scp_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        scp_protocol = ET.SubElement(protocol_type, "scp-protocol")
        if kwargs.pop('delete_scp_protocol', False) is True:
            delete_scp_protocol = config.find('.//*scp-protocol')
            delete_scp_protocol.set('operation', 'delete')
            
        scp = ET.SubElement(scp_protocol, "scp")
        if kwargs.pop('delete_scp', False) is True:
            delete_scp = config.find('.//*scp')
            delete_scp.set('operation', 'delete')
            
        user = ET.SubElement(scp, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_scp_protocol_scp_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        scp_protocol = ET.SubElement(protocol_type, "scp-protocol")
        if kwargs.pop('delete_scp_protocol', False) is True:
            delete_scp_protocol = config.find('.//*scp-protocol')
            delete_scp_protocol.set('operation', 'delete')
            
        scp = ET.SubElement(scp_protocol, "scp")
        if kwargs.pop('delete_scp', False) is True:
            delete_scp = config.find('.//*scp')
            delete_scp.set('operation', 'delete')
            
        password = ET.SubElement(scp, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_scp_protocol_scp_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        scp_protocol = ET.SubElement(protocol_type, "scp-protocol")
        if kwargs.pop('delete_scp_protocol', False) is True:
            delete_scp_protocol = config.find('.//*scp-protocol')
            delete_scp_protocol.set('operation', 'delete')
            
        scp = ET.SubElement(scp_protocol, "scp")
        if kwargs.pop('delete_scp', False) is True:
            delete_scp = config.find('.//*scp')
            delete_scp.set('operation', 'delete')
            
        host = ET.SubElement(scp, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_scp_protocol_scp_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        scp_protocol = ET.SubElement(protocol_type, "scp-protocol")
        if kwargs.pop('delete_scp_protocol', False) is True:
            delete_scp_protocol = config.find('.//*scp-protocol')
            delete_scp_protocol.set('operation', 'delete')
            
        scp = ET.SubElement(scp_protocol, "scp")
        if kwargs.pop('delete_scp', False) is True:
            delete_scp = config.find('.//*scp')
            delete_scp.set('operation', 'delete')
            
        directory = ET.SubElement(scp, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_scp_protocol_scp_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        scp_protocol = ET.SubElement(protocol_type, "scp-protocol")
        if kwargs.pop('delete_scp_protocol', False) is True:
            delete_scp_protocol = config.find('.//*scp-protocol')
            delete_scp_protocol.set('operation', 'delete')
            
        scp = ET.SubElement(scp_protocol, "scp")
        if kwargs.pop('delete_scp', False) is True:
            delete_scp = config.find('.//*scp')
            delete_scp.set('operation', 'delete')
            
        file = ET.SubElement(scp, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_ftp_protocol_ftp_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        ftp_protocol = ET.SubElement(protocol_type, "ftp-protocol")
        if kwargs.pop('delete_ftp_protocol', False) is True:
            delete_ftp_protocol = config.find('.//*ftp-protocol')
            delete_ftp_protocol.set('operation', 'delete')
            
        ftp = ET.SubElement(ftp_protocol, "ftp")
        if kwargs.pop('delete_ftp', False) is True:
            delete_ftp = config.find('.//*ftp')
            delete_ftp.set('operation', 'delete')
            
        user = ET.SubElement(ftp, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_ftp_protocol_ftp_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        ftp_protocol = ET.SubElement(protocol_type, "ftp-protocol")
        if kwargs.pop('delete_ftp_protocol', False) is True:
            delete_ftp_protocol = config.find('.//*ftp-protocol')
            delete_ftp_protocol.set('operation', 'delete')
            
        ftp = ET.SubElement(ftp_protocol, "ftp")
        if kwargs.pop('delete_ftp', False) is True:
            delete_ftp = config.find('.//*ftp')
            delete_ftp.set('operation', 'delete')
            
        password = ET.SubElement(ftp, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_ftp_protocol_ftp_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        ftp_protocol = ET.SubElement(protocol_type, "ftp-protocol")
        if kwargs.pop('delete_ftp_protocol', False) is True:
            delete_ftp_protocol = config.find('.//*ftp-protocol')
            delete_ftp_protocol.set('operation', 'delete')
            
        ftp = ET.SubElement(ftp_protocol, "ftp")
        if kwargs.pop('delete_ftp', False) is True:
            delete_ftp = config.find('.//*ftp')
            delete_ftp.set('operation', 'delete')
            
        host = ET.SubElement(ftp, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_ftp_protocol_ftp_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        ftp_protocol = ET.SubElement(protocol_type, "ftp-protocol")
        if kwargs.pop('delete_ftp_protocol', False) is True:
            delete_ftp_protocol = config.find('.//*ftp-protocol')
            delete_ftp_protocol.set('operation', 'delete')
            
        ftp = ET.SubElement(ftp_protocol, "ftp")
        if kwargs.pop('delete_ftp', False) is True:
            delete_ftp = config.find('.//*ftp')
            delete_ftp.set('operation', 'delete')
            
        directory = ET.SubElement(ftp, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_ftp_protocol_ftp_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        ftp_protocol = ET.SubElement(protocol_type, "ftp-protocol")
        if kwargs.pop('delete_ftp_protocol', False) is True:
            delete_ftp_protocol = config.find('.//*ftp-protocol')
            delete_ftp_protocol.set('operation', 'delete')
            
        ftp = ET.SubElement(ftp_protocol, "ftp")
        if kwargs.pop('delete_ftp', False) is True:
            delete_ftp = config.find('.//*ftp')
            delete_ftp.set('operation', 'delete')
            
        file = ET.SubElement(ftp, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        user = ET.SubElement(sftp, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        password = ET.SubElement(sftp, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        host = ET.SubElement(sftp, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        directory = ET.SubElement(sftp, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        file = ET.SubElement(sftp, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        port = ET.SubElement(sftp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_sftp_protocol_sftp_host_key_check(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        sftp_protocol = ET.SubElement(protocol_type, "sftp-protocol")
        if kwargs.pop('delete_sftp_protocol', False) is True:
            delete_sftp_protocol = config.find('.//*sftp-protocol')
            delete_sftp_protocol.set('operation', 'delete')
            
        sftp = ET.SubElement(sftp_protocol, "sftp")
        if kwargs.pop('delete_sftp', False) is True:
            delete_sftp = config.find('.//*sftp')
            delete_sftp.set('operation', 'delete')
            
        host_key_check = ET.SubElement(sftp, "host-key-check")
        if kwargs.pop('delete_host_key_check', False) is True:
            delete_host_key_check = config.find('.//*host-key-check')
            delete_host_key_check.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_protocol_type_usb_protocol_usb_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol_type = ET.SubElement(input, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        usb_protocol = ET.SubElement(protocol_type, "usb-protocol")
        if kwargs.pop('delete_usb_protocol', False) is True:
            delete_usb_protocol = config.find('.//*usb-protocol')
            delete_usb_protocol.set('operation', 'delete')
            
        usb = ET.SubElement(usb_protocol, "usb")
        if kwargs.pop('delete_usb', False) is True:
            delete_usb = config.find('.//*usb')
            delete_usb.set('operation', 'delete')
            
        directory = ET.SubElement(usb, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
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
        
    def firmware_download_input_reboot_options_auto_activate_auto_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        reboot_options = ET.SubElement(input, "reboot-options")
        if kwargs.pop('delete_reboot_options', False) is True:
            delete_reboot_options = config.find('.//*reboot-options')
            delete_reboot_options.set('operation', 'delete')
            
        auto_activate = ET.SubElement(reboot_options, "auto-activate")
        if kwargs.pop('delete_auto_activate', False) is True:
            delete_auto_activate = config.find('.//*auto-activate')
            delete_auto_activate.set('operation', 'delete')
            
        auto_activate = ET.SubElement(auto_activate, "auto-activate")
        if kwargs.pop('delete_auto_activate', False) is True:
            delete_auto_activate = config.find('.//*auto-activate')
            delete_auto_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_input_reboot_options_coldboot_coldboot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        input = ET.SubElement(firmware_download, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        reboot_options = ET.SubElement(input, "reboot-options")
        if kwargs.pop('delete_reboot_options', False) is True:
            delete_reboot_options = config.find('.//*reboot-options')
            delete_reboot_options.set('operation', 'delete')
            
        coldboot = ET.SubElement(reboot_options, "coldboot")
        if kwargs.pop('delete_coldboot', False) is True:
            delete_coldboot = config.find('.//*coldboot')
            delete_coldboot.set('operation', 'delete')
            
        coldboot = ET.SubElement(coldboot, "coldboot")
        if kwargs.pop('delete_coldboot', False) is True:
            delete_coldboot = config.find('.//*coldboot')
            delete_coldboot.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_output_fwdl_cmd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        output = ET.SubElement(firmware_download, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_cmd_status = ET.SubElement(output, "fwdl-cmd-status")
        if kwargs.pop('delete_fwdl_cmd_status', False) is True:
            delete_fwdl_cmd_status = config.find('.//*fwdl-cmd-status')
            delete_fwdl_cmd_status.set('operation', 'delete')
            
        fwdl_cmd_status.text = kwargs.pop('fwdl_cmd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_output_fwdl_cmd_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        output = ET.SubElement(firmware_download, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_cmd_msg = ET.SubElement(output, "fwdl-cmd-msg")
        if kwargs.pop('delete_fwdl_cmd_msg', False) is True:
            delete_fwdl_cmd_msg = config.find('.//*fwdl-cmd-msg')
            delete_fwdl_cmd_msg.set('operation', 'delete')
            
        fwdl_cmd_msg.text = kwargs.pop('fwdl_cmd_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_output_cluster_output_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        output = ET.SubElement(firmware_download, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(cluster_output, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_output_cluster_output_fwdl_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        output = ET.SubElement(firmware_download, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        fwdl_status = ET.SubElement(cluster_output, "fwdl-status")
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        fwdl_status.text = kwargs.pop('fwdl_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_download_output_cluster_output_fwdl_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware_download = ET.Element("firmware_download")
        config = firmware_download
        if kwargs.pop('delete_firmware_download', False) is True:
            delete_firmware_download = config.find('.//*firmware-download')
            delete_firmware_download.set('operation', 'delete')
            
        output = ET.SubElement(firmware_download, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        fwdl_msg = ET.SubElement(cluster_output, "fwdl-msg")
        if kwargs.pop('delete_fwdl_msg', False) is True:
            delete_fwdl_msg = config.find('.//*fwdl-msg')
            delete_fwdl_msg.set('operation', 'delete')
            
        fwdl_msg.text = kwargs.pop('fwdl_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        user = ET.SubElement(input, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        password = ET.SubElement(input, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        host = ET.SubElement(input, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        directory = ET.SubElement(input, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        file = ET.SubElement(input, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
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
        
    def logical_chassis_fwdl_sanity_input_cluster_options_auto_activate_auto_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        cluster_options = ET.SubElement(input, "cluster-options")
        if kwargs.pop('delete_cluster_options', False) is True:
            delete_cluster_options = config.find('.//*cluster-options')
            delete_cluster_options.set('operation', 'delete')
            
        auto_activate = ET.SubElement(cluster_options, "auto-activate")
        if kwargs.pop('delete_auto_activate', False) is True:
            delete_auto_activate = config.find('.//*auto-activate')
            delete_auto_activate.set('operation', 'delete')
            
        auto_activate = ET.SubElement(auto_activate, "auto-activate")
        if kwargs.pop('delete_auto_activate', False) is True:
            delete_auto_activate = config.find('.//*auto-activate')
            delete_auto_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_cluster_options_coldboot_coldboot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        cluster_options = ET.SubElement(input, "cluster-options")
        if kwargs.pop('delete_cluster_options', False) is True:
            delete_cluster_options = config.find('.//*cluster-options')
            delete_cluster_options.set('operation', 'delete')
            
        coldboot = ET.SubElement(cluster_options, "coldboot")
        if kwargs.pop('delete_coldboot', False) is True:
            delete_coldboot = config.find('.//*coldboot')
            delete_coldboot.set('operation', 'delete')
            
        coldboot = ET.SubElement(coldboot, "coldboot")
        if kwargs.pop('delete_coldboot', False) is True:
            delete_coldboot = config.find('.//*coldboot')
            delete_coldboot.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocol = ET.SubElement(input, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_cmd_status = ET.SubElement(output, "fwdl-cmd-status")
        if kwargs.pop('delete_fwdl_cmd_status', False) is True:
            delete_fwdl_cmd_status = config.find('.//*fwdl-cmd-status')
            delete_fwdl_cmd_status.set('operation', 'delete')
            
        fwdl_cmd_status.text = kwargs.pop('fwdl_cmd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fwdl_cmd_msg = ET.SubElement(output, "fwdl-cmd-msg")
        if kwargs.pop('delete_fwdl_cmd_msg', False) is True:
            delete_fwdl_cmd_msg = config.find('.//*fwdl-cmd-msg')
            delete_fwdl_cmd_msg.set('operation', 'delete')
            
        fwdl_cmd_msg.text = kwargs.pop('fwdl_cmd_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(cluster_output, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        fwdl_status = ET.SubElement(cluster_output, "fwdl-status")
        if kwargs.pop('delete_fwdl_status', False) is True:
            delete_fwdl_status = config.find('.//*fwdl-status')
            delete_fwdl_status.set('operation', 'delete')
            
        fwdl_status.text = kwargs.pop('fwdl_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        if kwargs.pop('delete_logical_chassis_fwdl_sanity', False) is True:
            delete_logical_chassis_fwdl_sanity = config.find('.//*logical-chassis-fwdl-sanity')
            delete_logical_chassis_fwdl_sanity.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_output = ET.SubElement(output, "cluster-output")
        if kwargs.pop('delete_cluster_output', False) is True:
            delete_cluster_output = config.find('.//*cluster-output')
            delete_cluster_output.set('operation', 'delete')
            
        fwdl_msg = ET.SubElement(cluster_output, "fwdl-msg")
        if kwargs.pop('delete_fwdl_msg', False) is True:
            delete_fwdl_msg = config.find('.//*fwdl-msg')
            delete_fwdl_msg.set('operation', 'delete')
            
        fwdl_msg.text = kwargs.pop('fwdl_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        input = ET.SubElement(logical_chassis_fwdl_status, "input")
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
        
    def logical_chassis_fwdl_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        overall_status = ET.SubElement(output, "overall-status")
        if kwargs.pop('delete_overall_status', False) is True:
            delete_overall_status = config.find('.//*overall-status')
            delete_overall_status.set('operation', 'delete')
            
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(cluster_fwdl_entries, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_state = ET.SubElement(cluster_fwdl_entries, "fwdl-state")
        if kwargs.pop('delete_fwdl_state', False) is True:
            delete_fwdl_state = config.find('.//*fwdl-state')
            delete_fwdl_state.set('operation', 'delete')
            
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        index = ET.SubElement(fwdl_entries, "index")
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
            
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        message_id = ET.SubElement(fwdl_entries, "message-id")
        if kwargs.pop('delete_message_id', False) is True:
            delete_message_id = config.find('.//*message-id')
            delete_message_id.set('operation', 'delete')
            
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        if kwargs.pop('delete_date_and_time_info', False) is True:
            delete_date_and_time_info = config.find('.//*date-and-time-info')
            delete_date_and_time_info.set('operation', 'delete')
            
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        message = ET.SubElement(fwdl_entries, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        if kwargs.pop('delete_blade_slot', False) is True:
            delete_blade_slot = config.find('.//*blade-slot')
            delete_blade_slot.set('operation', 'delete')
            
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        if kwargs.pop('delete_blade_swbd', False) is True:
            delete_blade_swbd = config.find('.//*blade-swbd')
            delete_blade_swbd.set('operation', 'delete')
            
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        if kwargs.pop('delete_blade_name', False) is True:
            delete_blade_name = config.find('.//*blade-name')
            delete_blade_name.set('operation', 'delete')
            
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        if kwargs.pop('delete_blade_state', False) is True:
            delete_blade_state = config.find('.//*blade-state')
            delete_blade_state.set('operation', 'delete')
            
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        if kwargs.pop('delete_logical_chassis_fwdl_status', False) is True:
            delete_logical_chassis_fwdl_status = config.find('.//*logical-chassis-fwdl-status')
            delete_logical_chassis_fwdl_status.set('operation', 'delete')
            
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        if kwargs.pop('delete_cluster_fwdl_entries', False) is True:
            delete_cluster_fwdl_entries = config.find('.//*cluster-fwdl-entries')
            delete_cluster_fwdl_entries.set('operation', 'delete')
            
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        if kwargs.pop('delete_fwdl_entries', False) is True:
            delete_fwdl_entries = config.find('.//*fwdl-entries')
            delete_fwdl_entries.set('operation', 'delete')
            
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        if kwargs.pop('delete_blade_app', False) is True:
            delete_blade_app = config.find('.//*blade-app')
            delete_blade_app.set('operation', 'delete')
            
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_last_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        if kwargs.pop('delete_dad_status', False) is True:
            delete_dad_status = config.find('.//*dad-status')
            delete_dad_status.set('operation', 'delete')
            
        output = ET.SubElement(dad_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        dad_last_state = ET.SubElement(output, "dad-last-state")
        if kwargs.pop('delete_dad_last_state', False) is True:
            delete_dad_last_state = config.find('.//*dad-last-state')
            delete_dad_last_state.set('operation', 'delete')
            
        dad_last_state.text = kwargs.pop('dad_last_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        if kwargs.pop('delete_dad_status', False) is True:
            delete_dad_status = config.find('.//*dad-status')
            delete_dad_status.set('operation', 'delete')
            
        output = ET.SubElement(dad_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        if kwargs.pop('delete_dad_status_entries', False) is True:
            delete_dad_status_entries = config.find('.//*dad-status-entries')
            delete_dad_status_entries.set('operation', 'delete')
            
        index = ET.SubElement(dad_status_entries, "index")
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
            
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        if kwargs.pop('delete_dad_status', False) is True:
            delete_dad_status = config.find('.//*dad-status')
            delete_dad_status.set('operation', 'delete')
            
        output = ET.SubElement(dad_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        if kwargs.pop('delete_dad_status_entries', False) is True:
            delete_dad_status_entries = config.find('.//*dad-status-entries')
            delete_dad_status_entries.set('operation', 'delete')
            
        date_and_time_info = ET.SubElement(dad_status_entries, "date-and-time-info")
        if kwargs.pop('delete_date_and_time_info', False) is True:
            delete_date_and_time_info = config.find('.//*date-and-time-info')
            delete_date_and_time_info.set('operation', 'delete')
            
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        if kwargs.pop('delete_dad_status', False) is True:
            delete_dad_status = config.find('.//*dad-status')
            delete_dad_status.set('operation', 'delete')
            
        output = ET.SubElement(dad_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        if kwargs.pop('delete_dad_status_entries', False) is True:
            delete_dad_status_entries = config.find('.//*dad-status-entries')
            delete_dad_status_entries.set('operation', 'delete')
            
        message = ET.SubElement(dad_status_entries, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        