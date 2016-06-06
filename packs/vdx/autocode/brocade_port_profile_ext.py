#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_port_profile_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_port_profile_for_intf_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_for_intf, "input")
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
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_request = ET.SubElement(request_type, "get-request")
        if kwargs.pop('delete_get_request', False) is True:
            delete_get_request = config.find('.//*get-request')
            delete_get_request.set('operation', 'delete')
            
        interface_type = ET.SubElement(get_request, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_request = ET.SubElement(request_type, "get-request")
        if kwargs.pop('delete_get_request', False) is True:
            delete_get_request = config.find('.//*get-request')
            delete_get_request.set('operation', 'delete')
            
        interface_name = ET.SubElement(get_request, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        if kwargs.pop('delete_last_received_interface_info', False) is True:
            delete_last_received_interface_info = config.find('.//*last-received-interface-info')
            delete_last_received_interface_info.set('operation', 'delete')
            
        interface_type = ET.SubElement(last_received_interface_info, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        if kwargs.pop('delete_last_received_interface_info', False) is True:
            delete_last_received_interface_info = config.find('.//*last-received-interface-info')
            delete_last_received_interface_info.set('operation', 'delete')
            
        interface_name = ET.SubElement(last_received_interface_info, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        port_profile = ET.SubElement(interface, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name = ET.SubElement(port_profile, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        if kwargs.pop('delete_get_port_profile_for_intf', False) is True:
            delete_get_port_profile_for_intf = config.find('.//*get-port-profile-for-intf')
            delete_get_port_profile_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_status, "input")
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
        
    def get_port_profile_status_input_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_status, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        port_profile_name = ET.SubElement(input, "port-profile-name")
        if kwargs.pop('delete_port_profile_name', False) is True:
            delete_port_profile_name = config.find('.//*port-profile-name')
            delete_port_profile_name.set('operation', 'delete')
            
        port_profile_name.text = kwargs.pop('port_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_port_profile_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_status, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        port_profile_status = ET.SubElement(input, "port-profile-status")
        if kwargs.pop('delete_port_profile_status', False) is True:
            delete_port_profile_status = config.find('.//*port-profile-status')
            delete_port_profile_status.set('operation', 'delete')
            
        port_profile_status.text = kwargs.pop('port_profile_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_status, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        if kwargs.pop('delete_last_received_port_profile_info', False) is True:
            delete_last_received_port_profile_info = config.find('.//*last-received-port-profile-info')
            delete_last_received_port_profile_info.set('operation', 'delete')
            
        profile_name = ET.SubElement(last_received_port_profile_info, "profile-name")
        if kwargs.pop('delete_profile_name', False) is True:
            delete_profile_name = config.find('.//*profile-name')
            delete_profile_name.set('operation', 'delete')
            
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        input = ET.SubElement(get_port_profile_status, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        if kwargs.pop('delete_last_received_port_profile_info', False) is True:
            delete_last_received_port_profile_info = config.find('.//*last-received-port-profile-info')
            delete_last_received_port_profile_info.set('operation', 'delete')
            
        profile_mac = ET.SubElement(last_received_port_profile_info, "profile-mac")
        if kwargs.pop('delete_profile_mac', False) is True:
            delete_profile_mac = config.find('.//*profile-mac')
            delete_profile_mac.set('operation', 'delete')
            
        profile_mac.text = kwargs.pop('profile_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name = ET.SubElement(port_profile, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_ppid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        ppid = ET.SubElement(port_profile, "ppid")
        if kwargs.pop('delete_ppid', False) is True:
            delete_ppid = config.find('.//*ppid')
            delete_ppid.set('operation', 'delete')
            
        ppid.text = kwargs.pop('ppid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_is_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        is_active = ET.SubElement(port_profile, "is-active")
        if kwargs.pop('delete_is_active', False) is True:
            delete_is_active = config.find('.//*is-active')
            delete_is_active.set('operation', 'delete')
            
        is_active.text = kwargs.pop('is_active')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mac_association = ET.SubElement(port_profile, "mac-association")
        if kwargs.pop('delete_mac_association', False) is True:
            delete_mac_association = config.find('.//*mac-association')
            delete_mac_association.set('operation', 'delete')
            
        mac = ET.SubElement(mac_association, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mac_association = ET.SubElement(port_profile, "mac-association")
        if kwargs.pop('delete_mac_association', False) is True:
            delete_mac_association = config.find('.//*mac-association')
            delete_mac_association.set('operation', 'delete')
            
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
                
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        if kwargs.pop('delete_applied_interface', False) is True:
            delete_applied_interface = config.find('.//*applied-interface')
            delete_applied_interface.set('operation', 'delete')
            
        interface_type = ET.SubElement(applied_interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mac_association = ET.SubElement(port_profile, "mac-association")
        if kwargs.pop('delete_mac_association', False) is True:
            delete_mac_association = config.find('.//*mac-association')
            delete_mac_association.set('operation', 'delete')
            
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
                
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        if kwargs.pop('delete_applied_interface', False) is True:
            delete_applied_interface = config.find('.//*applied-interface')
            delete_applied_interface.set('operation', 'delete')
            
        interface_name = ET.SubElement(applied_interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        if kwargs.pop('delete_get_port_profile_status', False) is True:
            delete_get_port_profile_status = config.find('.//*get-port-profile-status')
            delete_get_port_profile_status.set('operation', 'delete')
            
        output = ET.SubElement(get_port_profile_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        port_profile = ET.SubElement(output, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        has_more = ET.SubElement(port_profile, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        