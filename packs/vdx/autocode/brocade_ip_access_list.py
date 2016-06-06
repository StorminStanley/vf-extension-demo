#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ip_access_list(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def ip_acl_ip_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
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
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
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
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        if kwargs.pop('delete_src_host_any_sip', False) is True:
            delete_src_host_any_sip = config.find('.//*src-host-any-sip')
            delete_src_host_any_sip.set('operation', 'delete')
            
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        if kwargs.pop('delete_src_host_ip', False) is True:
            delete_src_host_ip = config.find('.//*src-host-ip')
            delete_src_host_ip.set('operation', 'delete')
            
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_mask = ET.SubElement(seq, "src-mask")
        if kwargs.pop('delete_src_mask', False) is True:
            delete_src_mask = config.find('.//*src-mask')
            delete_src_mask.set('operation', 'delete')
            
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
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
        
    def ip_acl_ip_access_list_standard_hide_ip_acl_std_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_std = ET.SubElement(standard, "hide-ip-acl-std")
        if kwargs.pop('delete_hide_ip_acl_std', False) is True:
            delete_hide_ip_acl_std = config.find('.//*hide-ip-acl-std')
            delete_hide_ip_acl_std.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_std, "seq")
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
        
    def ip_acl_ip_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
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
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
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
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_protocol_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        protocol_type = ET.SubElement(seq, "protocol-type")
        if kwargs.pop('delete_protocol_type', False) is True:
            delete_protocol_type = config.find('.//*protocol-type')
            delete_protocol_type.set('operation', 'delete')
            
        protocol_type.text = kwargs.pop('protocol_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        if kwargs.pop('delete_src_host_any_sip', False) is True:
            delete_src_host_any_sip = config.find('.//*src-host-any-sip')
            delete_src_host_any_sip.set('operation', 'delete')
            
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        if kwargs.pop('delete_src_host_ip', False) is True:
            delete_src_host_ip = config.find('.//*src-host-ip')
            delete_src_host_ip.set('operation', 'delete')
            
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        src_mask = ET.SubElement(seq, "src-mask")
        if kwargs.pop('delete_src_mask', False) is True:
            delete_src_mask = config.find('.//*src-mask')
            delete_src_mask.set('operation', 'delete')
            
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport = ET.SubElement(seq, "sport")
        if kwargs.pop('delete_sport', False) is True:
            delete_sport = config.find('.//*sport')
            delete_sport.set('operation', 'delete')
            
        sport.text = kwargs.pop('sport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_eq_neq_tcp = ET.SubElement(seq, "sport-number-eq-neq-tcp")
        if kwargs.pop('delete_sport_number_eq_neq_tcp', False) is True:
            delete_sport_number_eq_neq_tcp = config.find('.//*sport-number-eq-neq-tcp')
            delete_sport_number_eq_neq_tcp.set('operation', 'delete')
            
        sport_number_eq_neq_tcp.text = kwargs.pop('sport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_lt_tcp = ET.SubElement(seq, "sport-number-lt-tcp")
        if kwargs.pop('delete_sport_number_lt_tcp', False) is True:
            delete_sport_number_lt_tcp = config.find('.//*sport-number-lt-tcp')
            delete_sport_number_lt_tcp.set('operation', 'delete')
            
        sport_number_lt_tcp.text = kwargs.pop('sport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_gt_tcp = ET.SubElement(seq, "sport-number-gt-tcp")
        if kwargs.pop('delete_sport_number_gt_tcp', False) is True:
            delete_sport_number_gt_tcp = config.find('.//*sport-number-gt-tcp')
            delete_sport_number_gt_tcp.set('operation', 'delete')
            
        sport_number_gt_tcp.text = kwargs.pop('sport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_eq_neq_udp = ET.SubElement(seq, "sport-number-eq-neq-udp")
        if kwargs.pop('delete_sport_number_eq_neq_udp', False) is True:
            delete_sport_number_eq_neq_udp = config.find('.//*sport-number-eq-neq-udp')
            delete_sport_number_eq_neq_udp.set('operation', 'delete')
            
        sport_number_eq_neq_udp.text = kwargs.pop('sport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_lt_udp = ET.SubElement(seq, "sport-number-lt-udp")
        if kwargs.pop('delete_sport_number_lt_udp', False) is True:
            delete_sport_number_lt_udp = config.find('.//*sport-number-lt-udp')
            delete_sport_number_lt_udp.set('operation', 'delete')
            
        sport_number_lt_udp.text = kwargs.pop('sport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_gt_udp = ET.SubElement(seq, "sport-number-gt-udp")
        if kwargs.pop('delete_sport_number_gt_udp', False) is True:
            delete_sport_number_gt_udp = config.find('.//*sport-number-gt-udp')
            delete_sport_number_gt_udp.set('operation', 'delete')
            
        sport_number_gt_udp.text = kwargs.pop('sport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_range_lower_tcp = ET.SubElement(seq, "sport-number-range-lower-tcp")
        if kwargs.pop('delete_sport_number_range_lower_tcp', False) is True:
            delete_sport_number_range_lower_tcp = config.find('.//*sport-number-range-lower-tcp')
            delete_sport_number_range_lower_tcp.set('operation', 'delete')
            
        sport_number_range_lower_tcp.text = kwargs.pop('sport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_range_lower_udp = ET.SubElement(seq, "sport-number-range-lower-udp")
        if kwargs.pop('delete_sport_number_range_lower_udp', False) is True:
            delete_sport_number_range_lower_udp = config.find('.//*sport-number-range-lower-udp')
            delete_sport_number_range_lower_udp.set('operation', 'delete')
            
        sport_number_range_lower_udp.text = kwargs.pop('sport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_range_higher_tcp = ET.SubElement(seq, "sport-number-range-higher-tcp")
        if kwargs.pop('delete_sport_number_range_higher_tcp', False) is True:
            delete_sport_number_range_higher_tcp = config.find('.//*sport-number-range-higher-tcp')
            delete_sport_number_range_higher_tcp.set('operation', 'delete')
            
        sport_number_range_higher_tcp.text = kwargs.pop('sport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sport_number_range_higher_udp = ET.SubElement(seq, "sport-number-range-higher-udp")
        if kwargs.pop('delete_sport_number_range_higher_udp', False) is True:
            delete_sport_number_range_higher_udp = config.find('.//*sport-number-range-higher-udp')
            delete_sport_number_range_higher_udp.set('operation', 'delete')
            
        sport_number_range_higher_udp.text = kwargs.pop('sport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dst_host_any_dip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dst_host_any_dip = ET.SubElement(seq, "dst-host-any-dip")
        if kwargs.pop('delete_dst_host_any_dip', False) is True:
            delete_dst_host_any_dip = config.find('.//*dst-host-any-dip')
            delete_dst_host_any_dip.set('operation', 'delete')
            
        dst_host_any_dip.text = kwargs.pop('dst_host_any_dip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dst_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dst_host_ip = ET.SubElement(seq, "dst-host-ip")
        if kwargs.pop('delete_dst_host_ip', False) is True:
            delete_dst_host_ip = config.find('.//*dst-host-ip')
            delete_dst_host_ip.set('operation', 'delete')
            
        dst_host_ip.text = kwargs.pop('dst_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dst_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dst_mask = ET.SubElement(seq, "dst-mask")
        if kwargs.pop('delete_dst_mask', False) is True:
            delete_dst_mask = config.find('.//*dst-mask')
            delete_dst_mask.set('operation', 'delete')
            
        dst_mask.text = kwargs.pop('dst_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport = ET.SubElement(seq, "dport")
        if kwargs.pop('delete_dport', False) is True:
            delete_dport = config.find('.//*dport')
            delete_dport.set('operation', 'delete')
            
        dport.text = kwargs.pop('dport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_eq_neq_tcp = ET.SubElement(seq, "dport-number-eq-neq-tcp")
        if kwargs.pop('delete_dport_number_eq_neq_tcp', False) is True:
            delete_dport_number_eq_neq_tcp = config.find('.//*dport-number-eq-neq-tcp')
            delete_dport_number_eq_neq_tcp.set('operation', 'delete')
            
        dport_number_eq_neq_tcp.text = kwargs.pop('dport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_lt_tcp = ET.SubElement(seq, "dport-number-lt-tcp")
        if kwargs.pop('delete_dport_number_lt_tcp', False) is True:
            delete_dport_number_lt_tcp = config.find('.//*dport-number-lt-tcp')
            delete_dport_number_lt_tcp.set('operation', 'delete')
            
        dport_number_lt_tcp.text = kwargs.pop('dport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_gt_tcp = ET.SubElement(seq, "dport-number-gt-tcp")
        if kwargs.pop('delete_dport_number_gt_tcp', False) is True:
            delete_dport_number_gt_tcp = config.find('.//*dport-number-gt-tcp')
            delete_dport_number_gt_tcp.set('operation', 'delete')
            
        dport_number_gt_tcp.text = kwargs.pop('dport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_eq_neq_udp = ET.SubElement(seq, "dport-number-eq-neq-udp")
        if kwargs.pop('delete_dport_number_eq_neq_udp', False) is True:
            delete_dport_number_eq_neq_udp = config.find('.//*dport-number-eq-neq-udp')
            delete_dport_number_eq_neq_udp.set('operation', 'delete')
            
        dport_number_eq_neq_udp.text = kwargs.pop('dport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_lt_udp = ET.SubElement(seq, "dport-number-lt-udp")
        if kwargs.pop('delete_dport_number_lt_udp', False) is True:
            delete_dport_number_lt_udp = config.find('.//*dport-number-lt-udp')
            delete_dport_number_lt_udp.set('operation', 'delete')
            
        dport_number_lt_udp.text = kwargs.pop('dport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_gt_udp = ET.SubElement(seq, "dport-number-gt-udp")
        if kwargs.pop('delete_dport_number_gt_udp', False) is True:
            delete_dport_number_gt_udp = config.find('.//*dport-number-gt-udp')
            delete_dport_number_gt_udp.set('operation', 'delete')
            
        dport_number_gt_udp.text = kwargs.pop('dport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_range_lower_tcp = ET.SubElement(seq, "dport-number-range-lower-tcp")
        if kwargs.pop('delete_dport_number_range_lower_tcp', False) is True:
            delete_dport_number_range_lower_tcp = config.find('.//*dport-number-range-lower-tcp')
            delete_dport_number_range_lower_tcp.set('operation', 'delete')
            
        dport_number_range_lower_tcp.text = kwargs.pop('dport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_range_lower_udp = ET.SubElement(seq, "dport-number-range-lower-udp")
        if kwargs.pop('delete_dport_number_range_lower_udp', False) is True:
            delete_dport_number_range_lower_udp = config.find('.//*dport-number-range-lower-udp')
            delete_dport_number_range_lower_udp.set('operation', 'delete')
            
        dport_number_range_lower_udp.text = kwargs.pop('dport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_range_higher_tcp = ET.SubElement(seq, "dport-number-range-higher-tcp")
        if kwargs.pop('delete_dport_number_range_higher_tcp', False) is True:
            delete_dport_number_range_higher_tcp = config.find('.//*dport-number-range-higher-tcp')
            delete_dport_number_range_higher_tcp.set('operation', 'delete')
            
        dport_number_range_higher_tcp.text = kwargs.pop('dport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dport_number_range_higher_udp = ET.SubElement(seq, "dport-number-range-higher-udp")
        if kwargs.pop('delete_dport_number_range_higher_udp', False) is True:
            delete_dport_number_range_higher_udp = config.find('.//*dport-number-range-higher-udp')
            delete_dport_number_range_higher_udp.set('operation', 'delete')
            
        dport_number_range_higher_udp.text = kwargs.pop('dport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        dscp = ET.SubElement(seq, "dscp")
        if kwargs.pop('delete_dscp', False) is True:
            delete_dscp = config.find('.//*dscp')
            delete_dscp.set('operation', 'delete')
            
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_urg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        urg = ET.SubElement(seq, "urg")
        if kwargs.pop('delete_urg', False) is True:
            delete_urg = config.find('.//*urg')
            delete_urg.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_ack(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        ack = ET.SubElement(seq, "ack")
        if kwargs.pop('delete_ack', False) is True:
            delete_ack = config.find('.//*ack')
            delete_ack.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_push(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        push = ET.SubElement(seq, "push")
        if kwargs.pop('delete_push', False) is True:
            delete_push = config.find('.//*push')
            delete_push.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_fin(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        fin = ET.SubElement(seq, "fin")
        if kwargs.pop('delete_fin', False) is True:
            delete_fin = config.find('.//*fin')
            delete_fin.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_rst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        rst = ET.SubElement(seq, "rst")
        if kwargs.pop('delete_rst', False) is True:
            delete_rst = config.find('.//*rst')
            delete_rst.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
        if kwargs.pop('delete_seq', False) is True:
            delete_seq = config.find('.//*seq')
            delete_seq.set('operation', 'delete')
            
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        if kwargs.pop('delete_seq_id', False) is True:
            delete_seq_id = config.find('.//*seq-id')
            delete_seq_id.set('operation', 'delete')
                
        sync = ET.SubElement(seq, "sync")
        if kwargs.pop('delete_sync', False) is True:
            delete_sync = config.find('.//*sync')
            delete_sync.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
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
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
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
        
    def ip_acl_ip_access_list_extended_hide_ip_acl_ext_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip_acl = ET.SubElement(config, "ip-acl", xmlns="urn:brocade.com:mgmt:brocade-ip-access-list")
        if kwargs.pop('delete_ip_acl', False) is True:
            delete_ip_acl = config.find('.//*ip-acl')
            delete_ip_acl.set('operation', 'delete')
            
        ip = ET.SubElement(ip_acl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        access_list = ET.SubElement(ip, "access-list")
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
                
        hide_ip_acl_ext = ET.SubElement(extended, "hide-ip-acl-ext")
        if kwargs.pop('delete_hide_ip_acl_ext', False) is True:
            delete_hide_ip_acl_ext = config.find('.//*hide-ip-acl-ext')
            delete_hide_ip_acl_ext.set('operation', 'delete')
            
        seq = ET.SubElement(hide_ip_acl_ext, "seq")
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
        