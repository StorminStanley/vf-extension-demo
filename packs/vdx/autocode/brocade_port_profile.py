#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_port_profile(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
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
        
    def port_profile_allow_nonprofiledmacs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        allow = ET.SubElement(port_profile, "allow")
        if kwargs.pop('delete_allow', False) is True:
            delete_allow = config.find('.//*allow')
            delete_allow.set('operation', 'delete')
            
        nonprofiledmacs = ET.SubElement(allow, "nonprofiledmacs")
        if kwargs.pop('delete_nonprofiledmacs', False) is True:
            delete_nonprofiledmacs = config.find('.//*nonprofiledmacs')
            delete_nonprofiledmacs.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_basic_basic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport_basic = ET.SubElement(vlan_profile, "switchport-basic")
        if kwargs.pop('delete_switchport_basic', False) is True:
            delete_switchport_basic = config.find('.//*switchport-basic')
            delete_switchport_basic.set('operation', 'delete')
            
        basic = ET.SubElement(switchport_basic, "basic")
        if kwargs.pop('delete_basic', False) is True:
            delete_basic = config.find('.//*basic')
            delete_basic.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_mode_vlan_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        mode = ET.SubElement(switchport, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        vlan_mode = ET.SubElement(mode, "vlan-mode")
        if kwargs.pop('delete_vlan_mode', False) is True:
            delete_vlan_mode = config.find('.//*vlan-mode')
            delete_vlan_mode.set('operation', 'delete')
            
        vlan_mode.text = kwargs.pop('vlan_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        access = ET.SubElement(switchport, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        vlan = ET.SubElement(access, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        name = ET.SubElement(vlan, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        if kwargs.pop('delete_access_mac_vlan_classification', False) is True:
            delete_access_mac_vlan_classification = config.find('.//*access-mac-vlan-classification')
            delete_access_mac_vlan_classification.set('operation', 'delete')
            
        access = ET.SubElement(access_mac_vlan_classification, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        vlan = ET.SubElement(access, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        access_mac_address_key = ET.SubElement(vlan, "access-mac-address")
        access_mac_address_key.text = kwargs.pop('access_mac_address')
        if kwargs.pop('delete_access_mac_address', False) is True:
            delete_access_mac_address = config.find('.//*access-mac-address')
            delete_access_mac_address.set('operation', 'delete')
                
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        if kwargs.pop('delete_access_vlan_id', False) is True:
            delete_access_vlan_id = config.find('.//*access-vlan-id')
            delete_access_vlan_id.set('operation', 'delete')
            
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        if kwargs.pop('delete_access_mac_vlan_classification', False) is True:
            delete_access_mac_vlan_classification = config.find('.//*access-mac-vlan-classification')
            delete_access_mac_vlan_classification.set('operation', 'delete')
            
        access = ET.SubElement(access_mac_vlan_classification, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        vlan = ET.SubElement(access, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        if kwargs.pop('delete_access_vlan_id', False) is True:
            delete_access_vlan_id = config.find('.//*access-vlan-id')
            delete_access_vlan_id.set('operation', 'delete')
                
        access_mac_address = ET.SubElement(vlan, "access-mac-address")
        if kwargs.pop('delete_access_mac_address', False) is True:
            delete_access_mac_address = config.find('.//*access-mac-address')
            delete_access_mac_address.set('operation', 'delete')
            
        access_mac_address.text = kwargs.pop('access_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        if kwargs.pop('delete_access_mac_group_vlan_classification', False) is True:
            delete_access_mac_group_vlan_classification = config.find('.//*access-mac-group-vlan-classification')
            delete_access_mac_group_vlan_classification.set('operation', 'delete')
            
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        vlan = ET.SubElement(access, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        access_mac_group_key = ET.SubElement(vlan, "access-mac-group")
        access_mac_group_key.text = kwargs.pop('access_mac_group')
        if kwargs.pop('delete_access_mac_group', False) is True:
            delete_access_mac_group = config.find('.//*access-mac-group')
            delete_access_mac_group.set('operation', 'delete')
                
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        if kwargs.pop('delete_access_vlan_id', False) is True:
            delete_access_vlan_id = config.find('.//*access-vlan-id')
            delete_access_vlan_id.set('operation', 'delete')
            
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_mac_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        if kwargs.pop('delete_access_mac_group_vlan_classification', False) is True:
            delete_access_mac_group_vlan_classification = config.find('.//*access-mac-group-vlan-classification')
            delete_access_mac_group_vlan_classification.set('operation', 'delete')
            
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        vlan = ET.SubElement(access, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        if kwargs.pop('delete_access_vlan_id', False) is True:
            delete_access_vlan_id = config.find('.//*access-vlan-id')
            delete_access_vlan_id.set('operation', 'delete')
                
        access_mac_group = ET.SubElement(vlan, "access-mac-group")
        if kwargs.pop('delete_access_mac_group', False) is True:
            delete_access_mac_group = config.find('.//*access-mac-group')
            delete_access_mac_group.set('operation', 'delete')
            
        access_mac_group.text = kwargs.pop('access_mac_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        all = ET.SubElement(vlan, "all")
        if kwargs.pop('delete_all', False) is True:
            delete_all = config.find('.//*all')
            delete_all.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_none(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        none = ET.SubElement(vlan, "none")
        if kwargs.pop('delete_none', False) is True:
            delete_none = config.find('.//*none')
            delete_none.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        add = ET.SubElement(vlan, "add")
        if kwargs.pop('delete_add', False) is True:
            delete_add = config.find('.//*add')
            delete_add.set('operation', 'delete')
            
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_excpt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        excpt = ET.SubElement(vlan, "except")
        if kwargs.pop('delete_excpt', False) is True:
            delete_excpt = config.find('.//*except')
            delete_excpt.set('operation', 'delete')
            
        excpt.text = kwargs.pop('excpt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        remove = ET.SubElement(vlan, "remove")
        if kwargs.pop('delete_remove', False) is True:
            delete_remove = config.find('.//*remove')
            delete_remove.set('operation', 'delete')
            
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        if kwargs.pop('delete_trunk_vlan_classification', False) is True:
            delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
            delete_trunk_vlan_classification.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        add = ET.SubElement(vlan, "add")
        if kwargs.pop('delete_add', False) is True:
            delete_add = config.find('.//*add')
            delete_add.set('operation', 'delete')
            
        trunk_ctag_id_key = ET.SubElement(add, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        if kwargs.pop('delete_trunk_ctag_id', False) is True:
            delete_trunk_ctag_id = config.find('.//*trunk-ctag-id')
            delete_trunk_ctag_id.set('operation', 'delete')
                
        trunk_vlan_id = ET.SubElement(add, "trunk-vlan-id")
        if kwargs.pop('delete_trunk_vlan_id', False) is True:
            delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
            delete_trunk_vlan_id.set('operation', 'delete')
            
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        if kwargs.pop('delete_trunk_vlan_classification', False) is True:
            delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
            delete_trunk_vlan_classification.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        add = ET.SubElement(vlan, "add")
        if kwargs.pop('delete_add', False) is True:
            delete_add = config.find('.//*add')
            delete_add.set('operation', 'delete')
            
        trunk_vlan_id_key = ET.SubElement(add, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        if kwargs.pop('delete_trunk_vlan_id', False) is True:
            delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
            delete_trunk_vlan_id.set('operation', 'delete')
                
        trunk_ctag_id = ET.SubElement(add, "trunk-ctag-id")
        if kwargs.pop('delete_trunk_ctag_id', False) is True:
            delete_trunk_ctag_id = config.find('.//*trunk-ctag-id')
            delete_trunk_ctag_id.set('operation', 'delete')
            
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        if kwargs.pop('delete_trunk_vlan_classification', False) is True:
            delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
            delete_trunk_vlan_classification.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        remove = ET.SubElement(vlan, "remove")
        if kwargs.pop('delete_remove', False) is True:
            delete_remove = config.find('.//*remove')
            delete_remove.set('operation', 'delete')
            
        trunk_ctag_id_key = ET.SubElement(remove, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        if kwargs.pop('delete_trunk_ctag_id', False) is True:
            delete_trunk_ctag_id = config.find('.//*trunk-ctag-id')
            delete_trunk_ctag_id.set('operation', 'delete')
                
        trunk_vlan_id = ET.SubElement(remove, "trunk-vlan-id")
        if kwargs.pop('delete_trunk_vlan_id', False) is True:
            delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
            delete_trunk_vlan_id.set('operation', 'delete')
            
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        if kwargs.pop('delete_trunk_vlan_classification', False) is True:
            delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
            delete_trunk_vlan_classification.set('operation', 'delete')
            
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        if kwargs.pop('delete_allowed', False) is True:
            delete_allowed = config.find('.//*allowed')
            delete_allowed.set('operation', 'delete')
            
        vlan = ET.SubElement(allowed, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        remove = ET.SubElement(vlan, "remove")
        if kwargs.pop('delete_remove', False) is True:
            delete_remove = config.find('.//*remove')
            delete_remove.set('operation', 'delete')
            
        trunk_vlan_id_key = ET.SubElement(remove, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        if kwargs.pop('delete_trunk_vlan_id', False) is True:
            delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
            delete_trunk_vlan_id.set('operation', 'delete')
                
        trunk_ctag_id = ET.SubElement(remove, "trunk-ctag-id")
        if kwargs.pop('delete_trunk_ctag_id', False) is True:
            delete_trunk_ctag_id = config.find('.//*trunk-ctag-id')
            delete_trunk_ctag_id.set('operation', 'delete')
            
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        if kwargs.pop('delete_native_vlan_classification', False) is True:
            delete_native_vlan_classification = config.find('.//*native-vlan-classification')
            delete_native_vlan_classification.set('operation', 'delete')
            
        native_vlan_id = ET.SubElement(native_vlan_classification, "native-vlan-id")
        if kwargs.pop('delete_native_vlan_id', False) is True:
            delete_native_vlan_id = config.find('.//*native-vlan-id')
            delete_native_vlan_id.set('operation', 'delete')
            
        native_vlan_id.text = kwargs.pop('native_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        if kwargs.pop('delete_native_vlan_classification', False) is True:
            delete_native_vlan_classification = config.find('.//*native-vlan-classification')
            delete_native_vlan_classification.set('operation', 'delete')
            
        native_vlan_ctag_id = ET.SubElement(native_vlan_classification, "native-vlan-ctag-id")
        if kwargs.pop('delete_native_vlan_ctag_id', False) is True:
            delete_native_vlan_ctag_id = config.find('.//*native-vlan-ctag-id')
            delete_native_vlan_ctag_id.set('operation', 'delete')
            
        native_vlan_ctag_id.text = kwargs.pop('native_vlan_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        if kwargs.pop('delete_vlan_profile', False) is True:
            delete_vlan_profile = config.find('.//*vlan-profile')
            delete_vlan_profile.set('operation', 'delete')
            
        switchport = ET.SubElement(vlan_profile, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        trunk = ET.SubElement(switchport, "trunk")
        if kwargs.pop('delete_trunk', False) is True:
            delete_trunk = config.find('.//*trunk')
            delete_trunk.set('operation', 'delete')
            
        native_vlan = ET.SubElement(trunk, "native-vlan")
        if kwargs.pop('delete_native_vlan', False) is True:
            delete_native_vlan = config.find('.//*native-vlan')
            delete_native_vlan.set('operation', 'delete')
            
        native_vlan.text = kwargs.pop('native_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_fcoe_profile_fcoeport_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        fcoe_profile = ET.SubElement(port_profile, "fcoe-profile")
        if kwargs.pop('delete_fcoe_profile', False) is True:
            delete_fcoe_profile = config.find('.//*fcoe-profile')
            delete_fcoe_profile.set('operation', 'delete')
            
        fcoeport = ET.SubElement(fcoe_profile, "fcoeport")
        if kwargs.pop('delete_fcoeport', False) is True:
            delete_fcoeport = config.find('.//*fcoeport')
            delete_fcoeport.set('operation', 'delete')
            
        fcoe_map_name = ET.SubElement(fcoeport, "fcoe-map-name")
        if kwargs.pop('delete_fcoe_map_name', False) is True:
            delete_fcoe_map_name = config.find('.//*fcoe-map-name')
            delete_fcoe_map_name.set('operation', 'delete')
            
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        cee = ET.SubElement(qos_profile, "cee")
        if kwargs.pop('delete_cee', False) is True:
            delete_cee = config.find('.//*cee')
            delete_cee.set('operation', 'delete')
            
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        cos = ET.SubElement(qos, "cos")
        if kwargs.pop('delete_cos', False) is True:
            delete_cos = config.find('.//*cos')
            delete_cos.set('operation', 'delete')
            
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_trust_trust_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        trust = ET.SubElement(qos, "trust")
        if kwargs.pop('delete_trust', False) is True:
            delete_trust = config.find('.//*trust')
            delete_trust.set('operation', 'delete')
            
        trust_cos = ET.SubElement(trust, "trust-cos")
        if kwargs.pop('delete_trust_cos', False) is True:
            delete_trust_cos = config.find('.//*trust-cos')
            delete_trust_cos.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(qos, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(qos, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        if kwargs.pop('delete_flowcontrol', False) is True:
            delete_flowcontrol = config.find('.//*flowcontrol')
            delete_flowcontrol.set('operation', 'delete')
            
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        if kwargs.pop('delete_flowcontrolglobal', False) is True:
            delete_flowcontrolglobal = config.find('.//*flowcontrolglobal')
            delete_flowcontrolglobal.set('operation', 'delete')
            
        tx = ET.SubElement(flowcontrolglobal, "tx")
        if kwargs.pop('delete_tx', False) is True:
            delete_tx = config.find('.//*tx')
            delete_tx.set('operation', 'delete')
            
        tx.text = kwargs.pop('tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        if kwargs.pop('delete_flowcontrol', False) is True:
            delete_flowcontrol = config.find('.//*flowcontrol')
            delete_flowcontrol.set('operation', 'delete')
            
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        if kwargs.pop('delete_flowcontrolglobal', False) is True:
            delete_flowcontrolglobal = config.find('.//*flowcontrolglobal')
            delete_flowcontrolglobal.set('operation', 'delete')
            
        rx = ET.SubElement(flowcontrolglobal, "rx")
        if kwargs.pop('delete_rx', False) is True:
            delete_rx = config.find('.//*rx')
            delete_rx.set('operation', 'delete')
            
        rx.text = kwargs.pop('rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        if kwargs.pop('delete_flowcontrol', False) is True:
            delete_flowcontrol = config.find('.//*flowcontrol')
            delete_flowcontrol.set('operation', 'delete')
            
        pfc = ET.SubElement(flowcontrol, "pfc")
        if kwargs.pop('delete_pfc', False) is True:
            delete_pfc = config.find('.//*pfc')
            delete_pfc.set('operation', 'delete')
            
        pfc_cos = ET.SubElement(pfc, "pfc-cos")
        if kwargs.pop('delete_pfc_cos', False) is True:
            delete_pfc_cos = config.find('.//*pfc-cos')
            delete_pfc_cos.set('operation', 'delete')
            
        pfc_cos.text = kwargs.pop('pfc_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        if kwargs.pop('delete_flowcontrol', False) is True:
            delete_flowcontrol = config.find('.//*flowcontrol')
            delete_flowcontrol.set('operation', 'delete')
            
        pfc = ET.SubElement(flowcontrol, "pfc")
        if kwargs.pop('delete_pfc', False) is True:
            delete_pfc = config.find('.//*pfc')
            delete_pfc.set('operation', 'delete')
            
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        if kwargs.pop('delete_pfc_cos', False) is True:
            delete_pfc_cos = config.find('.//*pfc-cos')
            delete_pfc_cos.set('operation', 'delete')
                
        pfc_tx = ET.SubElement(pfc, "pfc-tx")
        if kwargs.pop('delete_pfc_tx', False) is True:
            delete_pfc_tx = config.find('.//*pfc-tx')
            delete_pfc_tx.set('operation', 'delete')
            
        pfc_tx.text = kwargs.pop('pfc_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        if kwargs.pop('delete_qos_profile', False) is True:
            delete_qos_profile = config.find('.//*qos-profile')
            delete_qos_profile.set('operation', 'delete')
            
        qos = ET.SubElement(qos_profile, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        if kwargs.pop('delete_flowcontrol', False) is True:
            delete_flowcontrol = config.find('.//*flowcontrol')
            delete_flowcontrol.set('operation', 'delete')
            
        pfc = ET.SubElement(flowcontrol, "pfc")
        if kwargs.pop('delete_pfc', False) is True:
            delete_pfc = config.find('.//*pfc')
            delete_pfc.set('operation', 'delete')
            
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        if kwargs.pop('delete_pfc_cos', False) is True:
            delete_pfc_cos = config.find('.//*pfc-cos')
            delete_pfc_cos.set('operation', 'delete')
                
        pfc_rx = ET.SubElement(pfc, "pfc-rx")
        if kwargs.pop('delete_pfc_rx', False) is True:
            delete_pfc_rx = config.find('.//*pfc-rx')
            delete_pfc_rx.set('operation', 'delete')
            
        pfc_rx.text = kwargs.pop('pfc_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        mac = ET.SubElement(security_profile, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_group = ET.SubElement(mac, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        access_group_name = ET.SubElement(access_group, "access-group-name")
        if kwargs.pop('delete_access_group_name', False) is True:
            delete_access_group_name = config.find('.//*access-group-name')
            delete_access_group_name.set('operation', 'delete')
            
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_in_cg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        mac = ET.SubElement(security_profile, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_group = ET.SubElement(mac, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        in_cg = ET.SubElement(access_group, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        ip = ET.SubElement(security_profile, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_group = ET.SubElement(ip, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        ipv4_access_group_name = ET.SubElement(access_group, "ipv4-access-group-name")
        if kwargs.pop('delete_ipv4_access_group_name', False) is True:
            delete_ipv4_access_group_name = config.find('.//*ipv4-access-group-name')
            delete_ipv4_access_group_name.set('operation', 'delete')
            
        ipv4_access_group_name.text = kwargs.pop('ipv4_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        ip = ET.SubElement(security_profile, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_group = ET.SubElement(ip, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        ipv4_in = ET.SubElement(access_group, "ipv4-in")
        if kwargs.pop('delete_ipv4_in', False) is True:
            delete_ipv4_in = config.find('.//*ipv4-in')
            delete_ipv4_in.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        ipv6 = ET.SubElement(security_profile, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        access_group = ET.SubElement(ipv6, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        ipv6_access_group_name = ET.SubElement(access_group, "ipv6-access-group-name")
        if kwargs.pop('delete_ipv6_access_group_name', False) is True:
            delete_ipv6_access_group_name = config.find('.//*ipv6-access-group-name')
            delete_ipv6_access_group_name.set('operation', 'delete')
            
        ipv6_access_group_name.text = kwargs.pop('ipv6_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        security_profile = ET.SubElement(port_profile, "security-profile")
        if kwargs.pop('delete_security_profile', False) is True:
            delete_security_profile = config.find('.//*security-profile')
            delete_security_profile.set('operation', 'delete')
            
        ipv6 = ET.SubElement(security_profile, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        access_group = ET.SubElement(ipv6, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        ipv6_in = ET.SubElement(access_group, "ipv6-in")
        if kwargs.pop('delete_ipv6_in', False) is True:
            delete_ipv6_in = config.find('.//*ipv6-in')
            delete_ipv6_in.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_restrict_flooding_container_restrict_flooding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        restrict_flooding_container = ET.SubElement(port_profile, "restrict-flooding-container")
        if kwargs.pop('delete_restrict_flooding_container', False) is True:
            delete_restrict_flooding_container = config.find('.//*restrict-flooding-container')
            delete_restrict_flooding_container.set('operation', 'delete')
            
        restrict_flooding = ET.SubElement(restrict_flooding_container, "restrict-flooding")
        if kwargs.pop('delete_restrict_flooding', False) is True:
            delete_restrict_flooding = config.find('.//*restrict-flooding')
            delete_restrict_flooding.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile_global', False) is True:
            delete_port_profile_global = config.find('.//*port-profile-global')
            delete_port_profile_global.set('operation', 'delete')
            
        port_profile = ET.SubElement(port_profile_global, "port-profile")
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
        
    def port_profile_global_port_profile_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile_global', False) is True:
            delete_port_profile_global = config.find('.//*port-profile-global')
            delete_port_profile_global.set('operation', 'delete')
            
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        activate = ET.SubElement(port_profile, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile_global', False) is True:
            delete_port_profile_global = config.find('.//*port-profile-global')
            delete_port_profile_global.set('operation', 'delete')
            
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        if kwargs.pop('delete_port_profile', False) is True:
            delete_port_profile = config.find('.//*port-profile')
            delete_port_profile.set('operation', 'delete')
            
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        static = ET.SubElement(port_profile, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        mac_address = ET.SubElement(static, "mac-address")
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
            
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_port_profile_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile_domain', False) is True:
            delete_port_profile_domain = config.find('.//*port-profile-domain')
            delete_port_profile_domain.set('operation', 'delete')
            
        port_profile_domain_name = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        if kwargs.pop('delete_port_profile_domain_name', False) is True:
            delete_port_profile_domain_name = config.find('.//*port-profile-domain-name')
            delete_port_profile_domain_name.set('operation', 'delete')
            
        port_profile_domain_name.text = kwargs.pop('port_profile_domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        if kwargs.pop('delete_port_profile_domain', False) is True:
            delete_port_profile_domain = config.find('.//*port-profile-domain')
            delete_port_profile_domain.set('operation', 'delete')
            
        port_profile_domain_name_key = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        port_profile_domain_name_key.text = kwargs.pop('port_profile_domain_name')
        if kwargs.pop('delete_port_profile_domain_name', False) is True:
            delete_port_profile_domain_name = config.find('.//*port-profile-domain-name')
            delete_port_profile_domain_name.set('operation', 'delete')
                
        profile = ET.SubElement(port_profile_domain, "profile")
        if kwargs.pop('delete_profile', False) is True:
            delete_profile = config.find('.//*profile')
            delete_profile.set('operation', 'delete')
            
        profile_name = ET.SubElement(profile, "profile-name")
        if kwargs.pop('delete_profile_name', False) is True:
            delete_profile_name = config.find('.//*profile-name')
            delete_profile_name.set('operation', 'delete')
            
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        