#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mac_address_table(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mac_address_table_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
                
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
                
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address = ET.SubElement(static, "mac-address")
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
            
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_forward(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
                
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        forward = ET.SubElement(static, "forward")
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
            
        forward.text = kwargs.pop('forward')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
                
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        interface_type = ET.SubElement(static, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
                
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
                
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        interface_name = ET.SubElement(static, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
                
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        vlan = ET.SubElement(static, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        static = ET.SubElement(mac_address_table, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        if kwargs.pop('delete_forward', False) is True:
            delete_forward = config.find('.//*forward')
            delete_forward.set('operation', 'delete')
                
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
                
        vlanid = ET.SubElement(static, "vlanid")
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
            
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_learning_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        learning_mode = ET.SubElement(mac_address_table, "learning-mode")
        if kwargs.pop('delete_learning_mode', False) is True:
            delete_learning_mode = config.find('.//*learning-mode')
            delete_learning_mode.set('operation', 'delete')
            
        learning_mode.text = kwargs.pop('learning_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_conversational_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        if kwargs.pop('delete_aging_time', False) is True:
            delete_aging_time = config.find('.//*aging-time')
            delete_aging_time.set('operation', 'delete')
            
        conversational_time_out = ET.SubElement(aging_time, "conversational-time-out")
        if kwargs.pop('delete_conversational_time_out', False) is True:
            delete_conversational_time_out = config.find('.//*conversational-time-out')
            delete_conversational_time_out.set('operation', 'delete')
            
        conversational_time_out.text = kwargs.pop('conversational_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_legacy_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        if kwargs.pop('delete_aging_time', False) is True:
            delete_aging_time = config.find('.//*aging-time')
            delete_aging_time.set('operation', 'delete')
            
        legacy_time_out = ET.SubElement(aging_time, "legacy-time-out")
        if kwargs.pop('delete_legacy_time_out', False) is True:
            delete_legacy_time_out = config.find('.//*legacy-time-out')
            delete_legacy_time_out.set('operation', 'delete')
            
        legacy_time_out.text = kwargs.pop('legacy_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_detect_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        if kwargs.pop('delete_mac_move', False) is True:
            delete_mac_move = config.find('.//*mac-move')
            delete_mac_move.set('operation', 'delete')
            
        mac_move_detect_enable = ET.SubElement(mac_move, "mac-move-detect-enable")
        if kwargs.pop('delete_mac_move_detect_enable', False) is True:
            delete_mac_move_detect_enable = config.find('.//*mac-move-detect-enable')
            delete_mac_move_detect_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        if kwargs.pop('delete_mac_move', False) is True:
            delete_mac_move = config.find('.//*mac-move')
            delete_mac_move.set('operation', 'delete')
            
        mac_move_limit = ET.SubElement(mac_move, "mac-move-limit")
        if kwargs.pop('delete_mac_move_limit', False) is True:
            delete_mac_move_limit = config.find('.//*mac-move-limit')
            delete_mac_move_limit.set('operation', 'delete')
            
        mac_move_limit.text = kwargs.pop('mac_move_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        if kwargs.pop('delete_consistency_check', False) is True:
            delete_consistency_check = config.find('.//*consistency-check')
            delete_consistency_check.set('operation', 'delete')
            
        mac_consistency_check_suppress = ET.SubElement(consistency_check, "mac-consistency-check-suppress")
        if kwargs.pop('delete_mac_consistency_check_suppress', False) is True:
            delete_mac_consistency_check_suppress = config.find('.//*mac-consistency-check-suppress')
            delete_mac_consistency_check_suppress.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        if kwargs.pop('delete_consistency_check', False) is True:
            delete_consistency_check = config.find('.//*consistency-check')
            delete_consistency_check.set('operation', 'delete')
            
        mac_consistency_check_interval = ET.SubElement(consistency_check, "mac-consistency-check-interval")
        if kwargs.pop('delete_mac_consistency_check_interval', False) is True:
            delete_mac_consistency_check_interval = config.find('.//*mac-consistency-check-interval')
            delete_mac_consistency_check_interval.set('operation', 'delete')
            
        mac_consistency_check_interval.text = kwargs.pop('mac_consistency_check_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_group', False) is True:
            delete_mac_group = config.find('.//*mac-group')
            delete_mac_group.set('operation', 'delete')
            
        mac_group_id = ET.SubElement(mac_group, "mac-group-id")
        if kwargs.pop('delete_mac_group_id', False) is True:
            delete_mac_group_id = config.find('.//*mac-group-id')
            delete_mac_group_id.set('operation', 'delete')
            
        mac_group_id.text = kwargs.pop('mac_group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_entry_entry_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        if kwargs.pop('delete_mac_group', False) is True:
            delete_mac_group = config.find('.//*mac-group')
            delete_mac_group.set('operation', 'delete')
            
        mac_group_id_key = ET.SubElement(mac_group, "mac-group-id")
        mac_group_id_key.text = kwargs.pop('mac_group_id')
        if kwargs.pop('delete_mac_group_id', False) is True:
            delete_mac_group_id = config.find('.//*mac-group-id')
            delete_mac_group_id.set('operation', 'delete')
                
        mac_group_entry = ET.SubElement(mac_group, "mac-group-entry")
        if kwargs.pop('delete_mac_group_entry', False) is True:
            delete_mac_group_entry = config.find('.//*mac-group-entry')
            delete_mac_group_entry.set('operation', 'delete')
            
        entry_address = ET.SubElement(mac_group_entry, "entry-address")
        if kwargs.pop('delete_entry_address', False) is True:
            delete_entry_address = config.find('.//*entry-address')
            delete_entry_address.set('operation', 'delete')
            
        entry_address.text = kwargs.pop('entry_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_request_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_address_table, "input")
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
            
        mac_address = ET.SubElement(get_request, "mac-address")
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
            
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_address_table, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_next_request = ET.SubElement(request_type, "get-next-request")
        if kwargs.pop('delete_get_next_request', False) is True:
            delete_get_next_request = config.find('.//*get-next-request')
            delete_get_next_request.set('operation', 'delete')
            
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        if kwargs.pop('delete_last_mac_address_details', False) is True:
            delete_last_mac_address_details = config.find('.//*last-mac-address-details')
            delete_last_mac_address_details.set('operation', 'delete')
            
        last_mac_address = ET.SubElement(last_mac_address_details, "last-mac-address")
        if kwargs.pop('delete_last_mac_address', False) is True:
            delete_last_mac_address = config.find('.//*last-mac-address')
            delete_last_mac_address.set('operation', 'delete')
            
        last_mac_address.text = kwargs.pop('last_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_address_table, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_next_request = ET.SubElement(request_type, "get-next-request")
        if kwargs.pop('delete_get_next_request', False) is True:
            delete_get_next_request = config.find('.//*get-next-request')
            delete_get_next_request.set('operation', 'delete')
            
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        if kwargs.pop('delete_last_mac_address_details', False) is True:
            delete_last_mac_address_details = config.find('.//*last-mac-address-details')
            delete_last_mac_address_details.set('operation', 'delete')
            
        last_vlan_id = ET.SubElement(last_mac_address_details, "last-vlan-id")
        if kwargs.pop('delete_last_vlan_id', False) is True:
            delete_last_vlan_id = config.find('.//*last-vlan-id')
            delete_last_vlan_id.set('operation', 'delete')
            
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_address_table, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_next_request = ET.SubElement(request_type, "get-next-request")
        if kwargs.pop('delete_get_next_request', False) is True:
            delete_get_next_request = config.find('.//*get-next-request')
            delete_get_next_request.set('operation', 'delete')
            
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        if kwargs.pop('delete_last_mac_address_details', False) is True:
            delete_last_mac_address_details = config.find('.//*last-mac-address-details')
            delete_last_mac_address_details.set('operation', 'delete')
            
        last_mac_type = ET.SubElement(last_mac_address_details, "last-mac-type")
        if kwargs.pop('delete_last_mac_type', False) is True:
            delete_last_mac_type = config.find('.//*last-mac-type')
            delete_last_mac_type.set('operation', 'delete')
            
        last_mac_type.text = kwargs.pop('last_mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        vlanid = ET.SubElement(mac_address_table, "vlanid")
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
            
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address = ET.SubElement(mac_address_table, "mac-address")
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
            
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        mac_type = ET.SubElement(mac_address_table, "mac-type")
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
            
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        mac_state = ET.SubElement(mac_address_table, "mac-state")
        if kwargs.pop('delete_mac_state', False) is True:
            delete_mac_state = config.find('.//*mac-state')
            delete_mac_state.set('operation', 'delete')
            
        mac_state.text = kwargs.pop('mac_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        if kwargs.pop('delete_forwarding_interface', False) is True:
            delete_forwarding_interface = config.find('.//*forwarding-interface')
            delete_forwarding_interface.set('operation', 'delete')
            
        interface_type = ET.SubElement(forwarding_interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        mac_address_table = ET.SubElement(output, "mac-address-table")
        if kwargs.pop('delete_mac_address_table', False) is True:
            delete_mac_address_table = config.find('.//*mac-address-table')
            delete_mac_address_table.set('operation', 'delete')
            
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        if kwargs.pop('delete_vlanid', False) is True:
            delete_vlanid = config.find('.//*vlanid')
            delete_vlanid.set('operation', 'delete')
                
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
                
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        if kwargs.pop('delete_forwarding_interface', False) is True:
            delete_forwarding_interface = config.find('.//*forwarding-interface')
            delete_forwarding_interface.set('operation', 'delete')
            
        interface_name = ET.SubElement(forwarding_interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        if kwargs.pop('delete_get_mac_address_table', False) is True:
            delete_get_mac_address_table = config.find('.//*get-mac-address-table')
            delete_get_mac_address_table.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_address_table, "output")
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
        