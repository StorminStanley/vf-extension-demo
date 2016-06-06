#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ntp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_ntp_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        if kwargs.pop('delete_show_ntp', False) is True:
            delete_show_ntp = config.find('.//*show-ntp')
            delete_show_ntp.set('operation', 'delete')
            
        input = ET.SubElement(show_ntp, "input")
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
        
    def show_ntp_output_node_active_server_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        if kwargs.pop('delete_show_ntp', False) is True:
            delete_show_ntp = config.find('.//*show-ntp')
            delete_show_ntp.set('operation', 'delete')
            
        output = ET.SubElement(show_ntp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        node_active_server = ET.SubElement(output, "node-active-server")
        if kwargs.pop('delete_node_active_server', False) is True:
            delete_node_active_server = config.find('.//*node-active-server')
            delete_node_active_server.set('operation', 'delete')
            
        rbridge_id_out = ET.SubElement(node_active_server, "rbridge-id-out")
        if kwargs.pop('delete_rbridge_id_out', False) is True:
            delete_rbridge_id_out = config.find('.//*rbridge-id-out')
            delete_rbridge_id_out.set('operation', 'delete')
            
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_ipv4_6_active_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        if kwargs.pop('delete_show_ntp', False) is True:
            delete_show_ntp = config.find('.//*show-ntp')
            delete_show_ntp.set('operation', 'delete')
            
        output = ET.SubElement(show_ntp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        node_active_server = ET.SubElement(output, "node-active-server")
        if kwargs.pop('delete_node_active_server', False) is True:
            delete_node_active_server = config.find('.//*node-active-server')
            delete_node_active_server.set('operation', 'delete')
            
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        if kwargs.pop('delete_ip4_6_or_local', False) is True:
            delete_ip4_6_or_local = config.find('.//*ip4-6-or-local')
            delete_ip4_6_or_local.set('operation', 'delete')
            
        ipv4_6 = ET.SubElement(ip4_6_or_local, "ipv4-6")
        if kwargs.pop('delete_ipv4_6', False) is True:
            delete_ipv4_6 = config.find('.//*ipv4-6')
            delete_ipv4_6.set('operation', 'delete')
            
        active_server = ET.SubElement(ipv4_6, "active-server")
        if kwargs.pop('delete_active_server', False) is True:
            delete_active_server = config.find('.//*active-server')
            delete_active_server.set('operation', 'delete')
            
        active_server.text = kwargs.pop('active_server')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_local_LOCL(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        if kwargs.pop('delete_show_ntp', False) is True:
            delete_show_ntp = config.find('.//*show-ntp')
            delete_show_ntp.set('operation', 'delete')
            
        output = ET.SubElement(show_ntp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        node_active_server = ET.SubElement(output, "node-active-server")
        if kwargs.pop('delete_node_active_server', False) is True:
            delete_node_active_server = config.find('.//*node-active-server')
            delete_node_active_server.set('operation', 'delete')
            
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        if kwargs.pop('delete_ip4_6_or_local', False) is True:
            delete_ip4_6_or_local = config.find('.//*ip4-6-or-local')
            delete_ip4_6_or_local.set('operation', 'delete')
            
        local = ET.SubElement(ip4_6_or_local, "local")
        if kwargs.pop('delete_local', False) is True:
            delete_local = config.find('.//*local')
            delete_local.set('operation', 'delete')
            
        LOCL = ET.SubElement(local, "LOCL")
        if kwargs.pop('delete_LOCL', False) is True:
            delete_LOCL = config.find('.//*LOCL')
            delete_LOCL.set('operation', 'delete')
            
        LOCL.text = kwargs.pop('LOCL')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        server = ET.SubElement(ntp, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        use_vrf_key = ET.SubElement(server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        ip = ET.SubElement(server, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        server = ET.SubElement(ntp, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        ip_key = ET.SubElement(server, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        key = ET.SubElement(server, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        server = ET.SubElement(ntp, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        ip_key = ET.SubElement(server, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        use_vrf = ET.SubElement(server, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_keyid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        authentication_key = ET.SubElement(ntp, "authentication-key")
        if kwargs.pop('delete_authentication_key', False) is True:
            delete_authentication_key = config.find('.//*authentication-key')
            delete_authentication_key.set('operation', 'delete')
            
        keyid = ET.SubElement(authentication_key, "keyid")
        if kwargs.pop('delete_keyid', False) is True:
            delete_keyid = config.find('.//*keyid')
            delete_keyid.set('operation', 'delete')
            
        keyid.text = kwargs.pop('keyid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_encryption_type_md5_type_md5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        authentication_key = ET.SubElement(ntp, "authentication-key")
        if kwargs.pop('delete_authentication_key', False) is True:
            delete_authentication_key = config.find('.//*authentication-key')
            delete_authentication_key.set('operation', 'delete')
            
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        if kwargs.pop('delete_keyid', False) is True:
            delete_keyid = config.find('.//*keyid')
            delete_keyid.set('operation', 'delete')
                
        encryption_type = ET.SubElement(authentication_key, "encryption-type")
        if kwargs.pop('delete_encryption_type', False) is True:
            delete_encryption_type = config.find('.//*encryption-type')
            delete_encryption_type.set('operation', 'delete')
            
        md5_type = ET.SubElement(encryption_type, "md5-type")
        if kwargs.pop('delete_md5_type', False) is True:
            delete_md5_type = config.find('.//*md5-type')
            delete_md5_type.set('operation', 'delete')
            
        md5 = ET.SubElement(md5_type, "md5")
        if kwargs.pop('delete_md5', False) is True:
            delete_md5 = config.find('.//*md5')
            delete_md5.set('operation', 'delete')
            
        md5.text = kwargs.pop('md5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_encryption_type_sha1_type_sha1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        authentication_key = ET.SubElement(ntp, "authentication-key")
        if kwargs.pop('delete_authentication_key', False) is True:
            delete_authentication_key = config.find('.//*authentication-key')
            delete_authentication_key.set('operation', 'delete')
            
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        if kwargs.pop('delete_keyid', False) is True:
            delete_keyid = config.find('.//*keyid')
            delete_keyid.set('operation', 'delete')
                
        encryption_type = ET.SubElement(authentication_key, "encryption-type")
        if kwargs.pop('delete_encryption_type', False) is True:
            delete_encryption_type = config.find('.//*encryption-type')
            delete_encryption_type.set('operation', 'delete')
            
        sha1_type = ET.SubElement(encryption_type, "sha1-type")
        if kwargs.pop('delete_sha1_type', False) is True:
            delete_sha1_type = config.find('.//*sha1-type')
            delete_sha1_type.set('operation', 'delete')
            
        sha1 = ET.SubElement(sha1_type, "sha1")
        if kwargs.pop('delete_sha1', False) is True:
            delete_sha1 = config.find('.//*sha1')
            delete_sha1.set('operation', 'delete')
            
        sha1.text = kwargs.pop('sha1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        authentication_key = ET.SubElement(ntp, "authentication-key")
        if kwargs.pop('delete_authentication_key', False) is True:
            delete_authentication_key = config.find('.//*authentication-key')
            delete_authentication_key.set('operation', 'delete')
            
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        if kwargs.pop('delete_keyid', False) is True:
            delete_keyid = config.find('.//*keyid')
            delete_keyid.set('operation', 'delete')
                
        encryption_level = ET.SubElement(authentication_key, "encryption-level")
        if kwargs.pop('delete_encryption_level', False) is True:
            delete_encryption_level = config.find('.//*encryption-level')
            delete_encryption_level.set('operation', 'delete')
            
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        if kwargs.pop('delete_ntp', False) is True:
            delete_ntp = config.find('.//*ntp')
            delete_ntp.set('operation', 'delete')
            
        source_ip = ET.SubElement(ntp, "source-ip")
        if kwargs.pop('delete_source_ip', False) is True:
            delete_source_ip = config.find('.//*source-ip')
            delete_source_ip.set('operation', 'delete')
            
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        