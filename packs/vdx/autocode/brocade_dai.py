#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_dai(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def arp_access_list_acl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name = ET.SubElement(access_list, "acl-name")
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
            
        acl_name.text = kwargs.pop('acl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_ip_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
                
        permit = ET.SubElement(access_list, "permit")
        if kwargs.pop('delete_permit', False) is True:
            delete_permit = config.find('.//*permit')
            delete_permit.set('operation', 'delete')
            
        permit_list = ET.SubElement(permit, "permit-list")
        if kwargs.pop('delete_permit_list', False) is True:
            delete_permit_list = config.find('.//*permit-list')
            delete_permit_list.set('operation', 'delete')
            
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
                
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
                
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        if kwargs.pop('delete_host_mac', False) is True:
            delete_host_mac = config.find('.//*host-mac')
            delete_host_mac.set('operation', 'delete')
                
        ip_type = ET.SubElement(permit_list, "ip-type")
        if kwargs.pop('delete_ip_type', False) is True:
            delete_ip_type = config.find('.//*ip-type')
            delete_ip_type.set('operation', 'delete')
            
        ip_type.text = kwargs.pop('ip_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
                
        permit = ET.SubElement(access_list, "permit")
        if kwargs.pop('delete_permit', False) is True:
            delete_permit = config.find('.//*permit')
            delete_permit.set('operation', 'delete')
            
        permit_list = ET.SubElement(permit, "permit-list")
        if kwargs.pop('delete_permit_list', False) is True:
            delete_permit_list = config.find('.//*permit-list')
            delete_permit_list.set('operation', 'delete')
            
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        if kwargs.pop('delete_ip_type', False) is True:
            delete_ip_type = config.find('.//*ip-type')
            delete_ip_type.set('operation', 'delete')
                
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
                
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        if kwargs.pop('delete_host_mac', False) is True:
            delete_host_mac = config.find('.//*host-mac')
            delete_host_mac.set('operation', 'delete')
                
        host_ip = ET.SubElement(permit_list, "host-ip")
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
            
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
                
        permit = ET.SubElement(access_list, "permit")
        if kwargs.pop('delete_permit', False) is True:
            delete_permit = config.find('.//*permit')
            delete_permit.set('operation', 'delete')
            
        permit_list = ET.SubElement(permit, "permit-list")
        if kwargs.pop('delete_permit_list', False) is True:
            delete_permit_list = config.find('.//*permit-list')
            delete_permit_list.set('operation', 'delete')
            
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        if kwargs.pop('delete_ip_type', False) is True:
            delete_ip_type = config.find('.//*ip-type')
            delete_ip_type.set('operation', 'delete')
                
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
                
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        if kwargs.pop('delete_host_mac', False) is True:
            delete_host_mac = config.find('.//*host-mac')
            delete_host_mac.set('operation', 'delete')
                
        mac_type = ET.SubElement(permit_list, "mac-type")
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
            
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
                
        permit = ET.SubElement(access_list, "permit")
        if kwargs.pop('delete_permit', False) is True:
            delete_permit = config.find('.//*permit')
            delete_permit.set('operation', 'delete')
            
        permit_list = ET.SubElement(permit, "permit-list")
        if kwargs.pop('delete_permit_list', False) is True:
            delete_permit_list = config.find('.//*permit-list')
            delete_permit_list.set('operation', 'delete')
            
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        if kwargs.pop('delete_ip_type', False) is True:
            delete_ip_type = config.find('.//*ip-type')
            delete_ip_type.set('operation', 'delete')
                
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
                
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
                
        host_mac = ET.SubElement(permit_list, "host-mac")
        if kwargs.pop('delete_host_mac', False) is True:
            delete_host_mac = config.find('.//*host-mac')
            delete_host_mac.set('operation', 'delete')
            
        host_mac.text = kwargs.pop('host_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        access_list = ET.SubElement(arp, "access-list")
        if kwargs.pop('delete_access_list', False) is True:
            delete_access_list = config.find('.//*access-list')
            delete_access_list.set('operation', 'delete')
            
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        if kwargs.pop('delete_acl_name', False) is True:
            delete_acl_name = config.find('.//*acl-name')
            delete_acl_name.set('operation', 'delete')
                
        permit = ET.SubElement(access_list, "permit")
        if kwargs.pop('delete_permit', False) is True:
            delete_permit = config.find('.//*permit')
            delete_permit.set('operation', 'delete')
            
        permit_list = ET.SubElement(permit, "permit-list")
        if kwargs.pop('delete_permit_list', False) is True:
            delete_permit_list = config.find('.//*permit-list')
            delete_permit_list.set('operation', 'delete')
            
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        if kwargs.pop('delete_ip_type', False) is True:
            delete_ip_type = config.find('.//*ip-type')
            delete_ip_type.set('operation', 'delete')
                
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
                
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        if kwargs.pop('delete_mac_type', False) is True:
            delete_mac_type = config.find('.//*mac-type')
            delete_mac_type.set('operation', 'delete')
                
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        if kwargs.pop('delete_host_mac', False) is True:
            delete_host_mac = config.find('.//*host-mac')
            delete_host_mac.set('operation', 'delete')
                
        log = ET.SubElement(permit_list, "log")
        if kwargs.pop('delete_log', False) is True:
            delete_log = config.find('.//*log')
            delete_log.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        