#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mac_access_list(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mac_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name = ET.SubElement(standard, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id = ET.SubElement(seq, "seq-id")
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
            
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        action = ET.SubElement(seq, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        source = ET.SubElement(seq, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        srchost = ET.SubElement(seq, "srchost")
        if kwargs.pop('delete_srchost', False) is True:
            delete_srchost = config.find('.//*srchost')
            delete_srchost.set('operation', 'delete')
            
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        if kwargs.pop('delete_src_mac_addr_mask', False) is True:
            delete_src_mac_addr_mask = config.find('.//*src-mac-addr-mask')
            delete_src_mac_addr_mask.set('operation', 'delete')
            
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        count = ET.SubElement(seq, "count")
        if kwargs.pop('delete_count', False) is True:
            delete_count = config.find('.//*count')
            delete_count.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        standard = ET.SubElement(access_list, "standard")
        if kwargs.pop('delete_standard', False) is True:
            delete_standard = config.find('.//*standard')
            delete_standard.set('operation', 'delete')
            
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        if kwargs.pop('delete_hide_mac_acl_std', False) is True:
            delete_hide_mac_acl_std = config.find('.//*hide-mac-acl-std')
            delete_hide_mac_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        log = ET.SubElement(seq, "log")
        if kwargs.pop('delete_log', False) is True:
            delete_log = config.find('.//*log')
            delete_log.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name = ET.SubElement(extended, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id = ET.SubElement(seq, "seq-id")
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
            
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        action = ET.SubElement(seq, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        source = ET.SubElement(seq, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        srchost = ET.SubElement(seq, "srchost")
        if kwargs.pop('delete_srchost', False) is True:
            delete_srchost = config.find('.//*srchost')
            delete_srchost.set('operation', 'delete')
            
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        if kwargs.pop('delete_src_mac_addr_mask', False) is True:
            delete_src_mac_addr_mask = config.find('.//*src-mac-addr-mask')
            delete_src_mac_addr_mask.set('operation', 'delete')
            
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dst = ET.SubElement(seq, "dst")
        if kwargs.pop('delete_dst', False) is True:
            delete_dst = config.find('.//*dst')
            delete_dst.set('operation', 'delete')
            
        dst.text = kwargs.pop('dst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dsthost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dsthost = ET.SubElement(seq, "dsthost")
        if kwargs.pop('delete_dsthost', False) is True:
            delete_dsthost = config.find('.//*dsthost')
            delete_dsthost.set('operation', 'delete')
            
        dsthost.text = kwargs.pop('dsthost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dst_mac_addr_mask = ET.SubElement(seq, "dst-mac-addr-mask")
        if kwargs.pop('delete_dst_mac_addr_mask', False) is True:
            delete_dst_mac_addr_mask = config.find('.//*dst-mac-addr-mask')
            delete_dst_mac_addr_mask.set('operation', 'delete')
            
        dst_mac_addr_mask.text = kwargs.pop('dst_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_ethertype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        ethertype = ET.SubElement(seq, "ethertype")
        if kwargs.pop('delete_ethertype', False) is True:
            delete_ethertype = config.find('.//*ethertype')
            delete_ethertype.set('operation', 'delete')
            
        ethertype.text = kwargs.pop('ethertype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        vlan = ET.SubElement(seq, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        count = ET.SubElement(seq, "count")
        if kwargs.pop('delete_count', False) is True:
            delete_count = config.find('.//*count')
            delete_count.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        access_list = ET.SubElement(mac, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        extended = ET.SubElement(access_list, "extended")
        if kwargs.pop('delete_extended', False) is True:
            delete_extended = config.find('.//*extended')
            delete_extended.set('operation', 'delete')
            
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        if kwargs.pop('delete_hide_mac_acl_ext', False) is True:
            delete_hide_mac_acl_ext = config.find('.//*hide-mac-acl-ext')
            delete_hide_mac_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        log = ET.SubElement(seq, "log")
        if kwargs.pop('delete_log', False) is True:
            delete_log = config.find('.//*log')
            delete_log.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        interface_type = ET.SubElement(input, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        interface_name = ET.SubElement(input, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        direction = ET.SubElement(input, "direction")
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
            
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_ingress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ingress_policy = ET.SubElement(interface, "ingress-policy")
        if kwargs.pop('delete_ingress_policy', False) is True:
            delete_ingress_policy = config.find('.//*ingress-policy')
            delete_ingress_policy.set('operation', 'delete')
            
        policy_name = ET.SubElement(ingress_policy, "policy-name")
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy-name')
            delete_policy_name.set('operation', 'delete')
            
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_egress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        if kwargs.pop('delete_get_mac_acl_for_intf', False) is True:
            delete_get_mac_acl_for_intf = config.find('.//*get-mac-acl-for-intf')
            delete_get_mac_acl_for_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        egress_policy = ET.SubElement(interface, "egress-policy")
        if kwargs.pop('delete_egress_policy', False) is True:
            delete_egress_policy = config.find('.//*egress-policy')
            delete_egress_policy.set('operation', 'delete')
            
        policy_name = ET.SubElement(egress_policy, "policy-name")
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy-name')
            delete_policy_name.set('operation', 'delete')
            
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        