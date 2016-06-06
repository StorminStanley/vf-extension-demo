#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_zone(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def zoning_defined_configuration_cfg_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        cfg = ET.SubElement(defined_configuration, "cfg")
        if kwargs.pop('delete_cfg', False) is True:
            delete_cfg = config.find('.//*cfg')
            delete_cfg.set('operation', 'delete')
            
        cfg_name = ET.SubElement(cfg, "cfg-name")
        if kwargs.pop('delete_cfg_name', False) is True:
            delete_cfg_name = config.find('.//*cfg-name')
            delete_cfg_name.set('operation', 'delete')
            
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_cfg_member_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        cfg = ET.SubElement(defined_configuration, "cfg")
        if kwargs.pop('delete_cfg', False) is True:
            delete_cfg = config.find('.//*cfg')
            delete_cfg.set('operation', 'delete')
            
        cfg_name_key = ET.SubElement(cfg, "cfg-name")
        cfg_name_key.text = kwargs.pop('cfg_name')
        if kwargs.pop('delete_cfg_name', False) is True:
            delete_cfg_name = config.find('.//*cfg-name')
            delete_cfg_name.set('operation', 'delete')
                
        member_zone = ET.SubElement(cfg, "member-zone")
        if kwargs.pop('delete_member_zone', False) is True:
            delete_member_zone = config.find('.//*member-zone')
            delete_member_zone.set('operation', 'delete')
            
        zone_name = ET.SubElement(member_zone, "zone-name")
        if kwargs.pop('delete_zone_name', False) is True:
            delete_zone_name = config.find('.//*zone-name')
            delete_zone_name.set('operation', 'delete')
            
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        zone = ET.SubElement(defined_configuration, "zone")
        if kwargs.pop('delete_zone', False) is True:
            delete_zone = config.find('.//*zone')
            delete_zone.set('operation', 'delete')
            
        zone_name = ET.SubElement(zone, "zone-name")
        if kwargs.pop('delete_zone_name', False) is True:
            delete_zone_name = config.find('.//*zone-name')
            delete_zone_name.set('operation', 'delete')
            
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        zone = ET.SubElement(defined_configuration, "zone")
        if kwargs.pop('delete_zone', False) is True:
            delete_zone = config.find('.//*zone')
            delete_zone.set('operation', 'delete')
            
        zone_name_key = ET.SubElement(zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        if kwargs.pop('delete_zone_name', False) is True:
            delete_zone_name = config.find('.//*zone-name')
            delete_zone_name.set('operation', 'delete')
                
        member_entry = ET.SubElement(zone, "member-entry")
        if kwargs.pop('delete_member_entry', False) is True:
            delete_member_entry = config.find('.//*member-entry')
            delete_member_entry.set('operation', 'delete')
            
        entry_name = ET.SubElement(member_entry, "entry-name")
        if kwargs.pop('delete_entry_name', False) is True:
            delete_entry_name = config.find('.//*entry-name')
            delete_entry_name.set('operation', 'delete')
            
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        alias = ET.SubElement(defined_configuration, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        alias_name = ET.SubElement(alias, "alias-name")
        if kwargs.pop('delete_alias_name', False) is True:
            delete_alias_name = config.find('.//*alias-name')
            delete_alias_name.set('operation', 'delete')
            
        alias_name.text = kwargs.pop('alias_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_member_entry_alias_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        if kwargs.pop('delete_defined_configuration', False) is True:
            delete_defined_configuration = config.find('.//*defined-configuration')
            delete_defined_configuration.set('operation', 'delete')
            
        alias = ET.SubElement(defined_configuration, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        alias_name_key = ET.SubElement(alias, "alias-name")
        alias_name_key.text = kwargs.pop('alias_name')
        if kwargs.pop('delete_alias_name', False) is True:
            delete_alias_name = config.find('.//*alias-name')
            delete_alias_name.set('operation', 'delete')
                
        member_entry = ET.SubElement(alias, "member-entry")
        if kwargs.pop('delete_member_entry', False) is True:
            delete_member_entry = config.find('.//*member-entry')
            delete_member_entry.set('operation', 'delete')
            
        alias_entry_name = ET.SubElement(member_entry, "alias-entry-name")
        if kwargs.pop('delete_alias_entry_name', False) is True:
            delete_alias_entry_name = config.find('.//*alias-entry-name')
            delete_alias_entry_name.set('operation', 'delete')
            
        alias_entry_name.text = kwargs.pop('alias_entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        if kwargs.pop('delete_cfg_name', False) is True:
            delete_cfg_name = config.find('.//*cfg-name')
            delete_cfg_name.set('operation', 'delete')
            
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_default_zone_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        default_zone_access = ET.SubElement(enabled_configuration, "default-zone-access")
        if kwargs.pop('delete_default_zone_access', False) is True:
            delete_default_zone_access = config.find('.//*default-zone-access')
            delete_default_zone_access.set('operation', 'delete')
            
        default_zone_access.text = kwargs.pop('default_zone_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        if kwargs.pop('delete_zoning', False) is True:
            delete_zoning = config.find('.//*zoning')
            delete_zoning.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        cfg_action = ET.SubElement(enabled_configuration, "cfg-action")
        if kwargs.pop('delete_cfg_action', False) is True:
            delete_cfg_action = config.find('.//*cfg-action')
            delete_cfg_action.set('operation', 'delete')
            
        cfg_action.text = kwargs.pop('cfg_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_request_zone_name_pattern(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
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
            
        zone_name_pattern = ET.SubElement(get_request, "zone-name-pattern")
        if kwargs.pop('delete_zone_name_pattern', False) is True:
            delete_zone_name_pattern = config.find('.//*zone-name-pattern')
            delete_zone_name_pattern.set('operation', 'delete')
            
        zone_name_pattern.text = kwargs.pop('zone_name_pattern')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_next_request_last_rcvd_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
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
            
        last_rcvd_zone_name = ET.SubElement(get_next_request, "last-rcvd-zone-name")
        if kwargs.pop('delete_last_rcvd_zone_name', False) is True:
            delete_last_rcvd_zone_name = config.find('.//*last-rcvd-zone-name')
            delete_last_rcvd_zone_name.set('operation', 'delete')
            
        last_rcvd_zone_name.text = kwargs.pop('last_rcvd_zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        if kwargs.pop('delete_cfg_name', False) is True:
            delete_cfg_name = config.find('.//*cfg-name')
            delete_cfg_name.set('operation', 'delete')
            
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        if kwargs.pop('delete_enabled_zone', False) is True:
            delete_enabled_zone = config.find('.//*enabled-zone')
            delete_enabled_zone.set('operation', 'delete')
            
        zone_name = ET.SubElement(enabled_zone, "zone-name")
        if kwargs.pop('delete_zone_name', False) is True:
            delete_zone_name = config.find('.//*zone-name')
            delete_zone_name.set('operation', 'delete')
            
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        if kwargs.pop('delete_enabled_zone', False) is True:
            delete_enabled_zone = config.find('.//*enabled-zone')
            delete_enabled_zone.set('operation', 'delete')
            
        zone_name_key = ET.SubElement(enabled_zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        if kwargs.pop('delete_zone_name', False) is True:
            delete_zone_name = config.find('.//*zone-name')
            delete_zone_name.set('operation', 'delete')
                
        member_entry = ET.SubElement(enabled_zone, "member-entry")
        if kwargs.pop('delete_member_entry', False) is True:
            delete_member_entry = config.find('.//*member-entry')
            delete_member_entry.set('operation', 'delete')
            
        entry_name = ET.SubElement(member_entry, "entry-name")
        if kwargs.pop('delete_entry_name', False) is True:
            delete_entry_name = config.find('.//*entry-name')
            delete_entry_name.set('operation', 'delete')
            
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        if kwargs.pop('delete_show_zoning_enabled_configuration', False) is True:
            delete_show_zoning_enabled_configuration = config.find('.//*show-zoning-enabled-configuration')
            delete_show_zoning_enabled_configuration.set('operation', 'delete')
            
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        if kwargs.pop('delete_enabled_configuration', False) is True:
            delete_enabled_configuration = config.find('.//*enabled-configuration')
            delete_enabled_configuration.set('operation', 'delete')
            
        has_more = ET.SubElement(enabled_configuration, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        