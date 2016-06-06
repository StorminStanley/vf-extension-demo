#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_hardware(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hardware_connector_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        connector = ET.SubElement(hardware, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        name = ET.SubElement(connector, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_sfp_breakout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        connector = ET.SubElement(hardware, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        name_key = ET.SubElement(connector, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        sfp = ET.SubElement(connector, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        breakout = ET.SubElement(sfp, "breakout")
        if kwargs.pop('delete_breakout', False) is True:
            delete_breakout = config.find('.//*breakout')
            delete_breakout.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        port_group = ET.SubElement(hardware, "port-group")
        if kwargs.pop('delete_port_group', False) is True:
            delete_port_group = config.find('.//*port-group')
            delete_port_group.set('operation', 'delete')
            
        name = ET.SubElement(port_group, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        port_group = ET.SubElement(hardware, "port-group")
        if kwargs.pop('delete_port_group', False) is True:
            delete_port_group = config.find('.//*port-group')
            delete_port_group.set('operation', 'delete')
            
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mode = ET.SubElement(port_group, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        performance = ET.SubElement(mode, "performance")
        if kwargs.pop('delete_performance', False) is True:
            delete_performance = config.find('.//*performance')
            delete_performance.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_portgroup_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        port_group = ET.SubElement(hardware, "port-group")
        if kwargs.pop('delete_port_group', False) is True:
            delete_port_group = config.find('.//*port-group')
            delete_port_group.set('operation', 'delete')
            
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mode = ET.SubElement(port_group, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        portgroup_speed = ET.SubElement(mode, "portgroup-speed")
        if kwargs.pop('delete_portgroup_speed', False) is True:
            delete_portgroup_speed = config.find('.//*portgroup-speed')
            delete_portgroup_speed.set('operation', 'delete')
            
        portgroup_speed.text = kwargs.pop('portgroup_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_support_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        port_group = ET.SubElement(hardware, "port-group")
        if kwargs.pop('delete_port_group', False) is True:
            delete_port_group = config.find('.//*port-group')
            delete_port_group.set('operation', 'delete')
            
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mode = ET.SubElement(port_group, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        support_performance = ET.SubElement(mode, "support_performance")
        if kwargs.pop('delete_support_performance', False) is True:
            delete_support_performance = config.find('.//*support_performance')
            delete_support_performance.set('operation', 'delete')
            
        support_performance.text = kwargs.pop('support_performance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_support_multispeed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        port_group = ET.SubElement(hardware, "port-group")
        if kwargs.pop('delete_port_group', False) is True:
            delete_port_group = config.find('.//*port-group')
            delete_port_group.set('operation', 'delete')
            
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mode = ET.SubElement(port_group, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        support_multispeed = ET.SubElement(mode, "support_multispeed")
        if kwargs.pop('delete_support_multispeed', False) is True:
            delete_support_multispeed = config.find('.//*support_multispeed')
            delete_support_multispeed.set('operation', 'delete')
            
        support_multispeed.text = kwargs.pop('support_multispeed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        connector_group = ET.SubElement(hardware, "connector-group")
        if kwargs.pop('delete_connector_group', False) is True:
            delete_connector_group = config.find('.//*connector-group')
            delete_connector_group.set('operation', 'delete')
            
        id = ET.SubElement(connector_group, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        connector_group = ET.SubElement(hardware, "connector-group")
        if kwargs.pop('delete_connector_group', False) is True:
            delete_connector_group = config.find('.//*connector-group')
            delete_connector_group.set('operation', 'delete')
            
        id_key = ET.SubElement(connector_group, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        speed = ET.SubElement(connector_group, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        flexport = ET.SubElement(hardware, "flexport")
        if kwargs.pop('delete_flexport', False) is True:
            delete_flexport = config.find('.//*flexport')
            delete_flexport.set('operation', 'delete')
            
        id = ET.SubElement(flexport, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        flexport = ET.SubElement(hardware, "flexport")
        if kwargs.pop('delete_flexport', False) is True:
            delete_flexport = config.find('.//*flexport')
            delete_flexport.set('operation', 'delete')
            
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        flexport_type = ET.SubElement(flexport, "flexport_type")
        if kwargs.pop('delete_flexport_type', False) is True:
            delete_flexport_type = config.find('.//*flexport_type')
            delete_flexport_type.set('operation', 'delete')
            
        type = ET.SubElement(flexport_type, "type")
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
            
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        flexport = ET.SubElement(hardware, "flexport")
        if kwargs.pop('delete_flexport', False) is True:
            delete_flexport = config.find('.//*flexport')
            delete_flexport.set('operation', 'delete')
            
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        flexport_type = ET.SubElement(flexport, "flexport_type")
        if kwargs.pop('delete_flexport_type', False) is True:
            delete_flexport_type = config.find('.//*flexport_type')
            delete_flexport_type.set('operation', 'delete')
            
        instance = ET.SubElement(flexport_type, "instance")
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
            
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_skip_deconfig(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        flexport = ET.SubElement(hardware, "flexport")
        if kwargs.pop('delete_flexport', False) is True:
            delete_flexport = config.find('.//*flexport')
            delete_flexport.set('operation', 'delete')
            
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        flexport_type = ET.SubElement(flexport, "flexport_type")
        if kwargs.pop('delete_flexport_type', False) is True:
            delete_flexport_type = config.find('.//*flexport_type')
            delete_flexport_type.set('operation', 'delete')
            
        skip_deconfig = ET.SubElement(flexport_type, "skip_deconfig")
        if kwargs.pop('delete_skip_deconfig', False) is True:
            delete_skip_deconfig = config.find('.//*skip_deconfig')
            delete_skip_deconfig.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name = ET.SubElement(kap_custom_profile, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        lacp_hello_interval = ET.SubElement(lacp, "lacp_hello_interval")
        if kwargs.pop('delete_lacp_hello_interval', False) is True:
            delete_lacp_hello_interval = config.find('.//*lacp_hello_interval')
            delete_lacp_hello_interval.set('operation', 'delete')
            
        lacp_hello_interval.text = kwargs.pop('lacp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        lacp_num_entry = ET.SubElement(lacp, "lacp_num_entry")
        if kwargs.pop('delete_lacp_num_entry', False) is True:
            delete_lacp_num_entry = config.find('.//*lacp_num_entry')
            delete_lacp_num_entry.set('operation', 'delete')
            
        lacp_num_entry.text = kwargs.pop('lacp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        if kwargs.pop('delete_xstp', False) is True:
            delete_xstp = config.find('.//*xstp')
            delete_xstp.set('operation', 'delete')
            
        xstp_hello_interval = ET.SubElement(xstp, "xstp_hello_interval")
        if kwargs.pop('delete_xstp_hello_interval', False) is True:
            delete_xstp_hello_interval = config.find('.//*xstp_hello_interval')
            delete_xstp_hello_interval.set('operation', 'delete')
            
        xstp_hello_interval.text = kwargs.pop('xstp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        if kwargs.pop('delete_xstp', False) is True:
            delete_xstp = config.find('.//*xstp')
            delete_xstp.set('operation', 'delete')
            
        xstp_num_entry = ET.SubElement(xstp, "xstp_num_entry")
        if kwargs.pop('delete_xstp_num_entry', False) is True:
            delete_xstp_num_entry = config.find('.//*xstp_num_entry')
            delete_xstp_num_entry.set('operation', 'delete')
            
        xstp_num_entry.text = kwargs.pop('xstp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        if kwargs.pop('delete_rpvst', False) is True:
            delete_rpvst = config.find('.//*rpvst')
            delete_rpvst.set('operation', 'delete')
            
        rpvst_hello_interval = ET.SubElement(rpvst, "rpvst_hello_interval")
        if kwargs.pop('delete_rpvst_hello_interval', False) is True:
            delete_rpvst_hello_interval = config.find('.//*rpvst_hello_interval')
            delete_rpvst_hello_interval.set('operation', 'delete')
            
        rpvst_hello_interval.text = kwargs.pop('rpvst_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        if kwargs.pop('delete_rpvst', False) is True:
            delete_rpvst = config.find('.//*rpvst')
            delete_rpvst.set('operation', 'delete')
            
        rpvst_num_entry = ET.SubElement(rpvst, "rpvst_num_entry")
        if kwargs.pop('delete_rpvst_num_entry', False) is True:
            delete_rpvst_num_entry = config.find('.//*rpvst_num_entry')
            delete_rpvst_num_entry.set('operation', 'delete')
            
        rpvst_num_entry.text = kwargs.pop('rpvst_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        udld = ET.SubElement(kap_custom_profile, "udld")
        if kwargs.pop('delete_udld', False) is True:
            delete_udld = config.find('.//*udld')
            delete_udld.set('operation', 'delete')
            
        udld_hello_interval = ET.SubElement(udld, "udld_hello_interval")
        if kwargs.pop('delete_udld_hello_interval', False) is True:
            delete_udld_hello_interval = config.find('.//*udld_hello_interval')
            delete_udld_hello_interval.set('operation', 'delete')
            
        udld_hello_interval.text = kwargs.pop('udld_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        udld = ET.SubElement(kap_custom_profile, "udld")
        if kwargs.pop('delete_udld', False) is True:
            delete_udld = config.find('.//*udld')
            delete_udld.set('operation', 'delete')
            
        udld_num_entry = ET.SubElement(udld, "udld_num_entry")
        if kwargs.pop('delete_udld_num_entry', False) is True:
            delete_udld_num_entry = config.find('.//*udld_num_entry')
            delete_udld_num_entry.set('operation', 'delete')
            
        udld_num_entry.text = kwargs.pop('udld_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        if kwargs.pop('delete_bfd_vxlan', False) is True:
            delete_bfd_vxlan = config.find('.//*bfd-vxlan')
            delete_bfd_vxlan.set('operation', 'delete')
            
        bfd_vxlan_hello_interval = ET.SubElement(bfd_vxlan, "bfd_vxlan_hello_interval")
        if kwargs.pop('delete_bfd_vxlan_hello_interval', False) is True:
            delete_bfd_vxlan_hello_interval = config.find('.//*bfd_vxlan_hello_interval')
            delete_bfd_vxlan_hello_interval.set('operation', 'delete')
            
        bfd_vxlan_hello_interval.text = kwargs.pop('bfd_vxlan_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        if kwargs.pop('delete_bfd_vxlan', False) is True:
            delete_bfd_vxlan = config.find('.//*bfd-vxlan')
            delete_bfd_vxlan.set('operation', 'delete')
            
        bfd_vxlan_num_entry = ET.SubElement(bfd_vxlan, "bfd_vxlan_num_entry")
        if kwargs.pop('delete_bfd_vxlan_num_entry', False) is True:
            delete_bfd_vxlan_num_entry = config.find('.//*bfd_vxlan_num_entry')
            delete_bfd_vxlan_num_entry.set('operation', 'delete')
            
        bfd_vxlan_num_entry.text = kwargs.pop('bfd_vxlan_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        if kwargs.pop('delete_bfd_l3', False) is True:
            delete_bfd_l3 = config.find('.//*bfd-l3')
            delete_bfd_l3.set('operation', 'delete')
            
        bfd_l3_hello_interval = ET.SubElement(bfd_l3, "bfd_l3_hello_interval")
        if kwargs.pop('delete_bfd_l3_hello_interval', False) is True:
            delete_bfd_l3_hello_interval = config.find('.//*bfd_l3_hello_interval')
            delete_bfd_l3_hello_interval.set('operation', 'delete')
            
        bfd_l3_hello_interval.text = kwargs.pop('bfd_l3_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        if kwargs.pop('delete_bfd_l3', False) is True:
            delete_bfd_l3 = config.find('.//*bfd-l3')
            delete_bfd_l3.set('operation', 'delete')
            
        bfd_l3_num_entry = ET.SubElement(bfd_l3, "bfd_l3_num_entry")
        if kwargs.pop('delete_bfd_l3_num_entry', False) is True:
            delete_bfd_l3_num_entry = config.find('.//*bfd_l3_num_entry')
            delete_bfd_l3_num_entry.set('operation', 'delete')
            
        bfd_l3_num_entry.text = kwargs.pop('bfd_l3_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_hello_interval = ET.SubElement(fcoe, "fcoe_hello_interval")
        if kwargs.pop('delete_fcoe_hello_interval', False) is True:
            delete_fcoe_hello_interval = config.find('.//*fcoe_hello_interval')
            delete_fcoe_hello_interval.set('operation', 'delete')
            
        fcoe_hello_interval.text = kwargs.pop('fcoe_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        if kwargs.pop('delete_hardware', False) is True:
            delete_hardware = config.find('.//*hardware')
            delete_hardware.set('operation', 'delete')
            
        custom_profile = ET.SubElement(hardware, "custom-profile")
        if kwargs.pop('delete_custom_profile', False) is True:
            delete_custom_profile = config.find('.//*custom-profile')
            delete_custom_profile.set('operation', 'delete')
            
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        if kwargs.pop('delete_kap_custom_profile', False) is True:
            delete_kap_custom_profile = config.find('.//*kap-custom-profile')
            delete_kap_custom_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_num_entry = ET.SubElement(fcoe, "fcoe_num_entry")
        if kwargs.pop('delete_fcoe_num_entry', False) is True:
            delete_fcoe_num_entry = config.find('.//*fcoe_num_entry')
            delete_fcoe_num_entry.set('operation', 'delete')
            
        fcoe_num_entry.text = kwargs.pop('fcoe_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_flexports_output_flexport_list_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_flexports = ET.Element("get_flexports")
        config = get_flexports
        if kwargs.pop('delete_get_flexports', False) is True:
            delete_get_flexports = config.find('.//*get-flexports')
            delete_get_flexports.set('operation', 'delete')
            
        output = ET.SubElement(get_flexports, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        flexport_list = ET.SubElement(output, "flexport-list")
        if kwargs.pop('delete_flexport_list', False) is True:
            delete_flexport_list = config.find('.//*flexport-list')
            delete_flexport_list.set('operation', 'delete')
            
        port_id = ET.SubElement(flexport_list, "port-id")
        if kwargs.pop('delete_port_id', False) is True:
            delete_port_id = config.find('.//*port-id')
            delete_port_id.set('operation', 'delete')
            
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        