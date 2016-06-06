#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_snmp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def snmp_server_context_context_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        context = ET.SubElement(snmp_server, "context")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context_name = ET.SubElement(context, "context-name")
        if kwargs.pop('delete_context_name', False) is True:
            delete_context_name = config.find('.//*context-name')
            delete_context_name.set('operation', 'delete')
            
        context_name.text = kwargs.pop('context_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_context_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        context = ET.SubElement(snmp_server, "context")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context_name_key = ET.SubElement(context, "context-name")
        context_name_key.text = kwargs.pop('context_name')
        if kwargs.pop('delete_context_name', False) is True:
            delete_context_name = config.find('.//*context-name')
            delete_context_name.set('operation', 'delete')
                
        vrf_name = ET.SubElement(context, "vrf-name")
        if kwargs.pop('delete_vrf_name', False) is True:
            delete_vrf_name = config.find('.//*vrf-name')
            delete_vrf_name.set('operation', 'delete')
            
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        community = ET.SubElement(snmp_server, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community = ET.SubElement(community, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        community = ET.SubElement(snmp_server, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        groupname = ET.SubElement(community, "groupname")
        if kwargs.pop('delete_groupname', False) is True:
            delete_groupname = config.find('.//*groupname')
            delete_groupname.set('operation', 'delete')
            
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        community = ET.SubElement(snmp_server, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        ipv4_acl = ET.SubElement(community, "ipv4-acl")
        if kwargs.pop('delete_ipv4_acl', False) is True:
            delete_ipv4_acl = config.find('.//*ipv4-acl')
            delete_ipv4_acl.set('operation', 'delete')
            
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        community = ET.SubElement(snmp_server, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        ipv6_acl = ET.SubElement(community, "ipv6-acl")
        if kwargs.pop('delete_ipv6_acl', False) is True:
            delete_ipv6_acl = config.find('.//*ipv6-acl')
            delete_ipv6_acl.set('operation', 'delete')
            
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username = ET.SubElement(user, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        groupname = ET.SubElement(user, "groupname")
        if kwargs.pop('delete_groupname', False) is True:
            delete_groupname = config.find('.//*groupname')
            delete_groupname.set('operation', 'delete')
            
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        auth = ET.SubElement(user, "auth")
        if kwargs.pop('delete_auth', False) is True:
            delete_auth = config.find('.//*auth')
            delete_auth.set('operation', 'delete')
            
        auth.text = kwargs.pop('auth')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        auth_password = ET.SubElement(user, "auth-password")
        if kwargs.pop('delete_auth_password', False) is True:
            delete_auth_password = config.find('.//*auth-password')
            delete_auth_password.set('operation', 'delete')
            
        auth_password.text = kwargs.pop('auth_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        priv = ET.SubElement(user, "priv")
        if kwargs.pop('delete_priv', False) is True:
            delete_priv = config.find('.//*priv')
            delete_priv.set('operation', 'delete')
            
        priv.text = kwargs.pop('priv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        priv_password = ET.SubElement(user, "priv-password")
        if kwargs.pop('delete_priv_password', False) is True:
            delete_priv_password = config.find('.//*priv-password')
            delete_priv_password.set('operation', 'delete')
            
        priv_password.text = kwargs.pop('priv_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_encrypted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        encrypted = ET.SubElement(user, "encrypted")
        if kwargs.pop('delete_encrypted', False) is True:
            delete_encrypted = config.find('.//*encrypted')
            delete_encrypted.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        ipv4_acl = ET.SubElement(user, "ipv4-acl")
        if kwargs.pop('delete_ipv4_acl', False) is True:
            delete_ipv4_acl = config.find('.//*ipv4-acl')
            delete_ipv4_acl.set('operation', 'delete')
            
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        user = ET.SubElement(snmp_server, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        ipv6_acl = ET.SubElement(user, "ipv6-acl")
        if kwargs.pop('delete_ipv6_acl', False) is True:
            delete_ipv6_acl = config.find('.//*ipv6-acl')
            delete_ipv6_acl.set('operation', 'delete')
            
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        hostip = ET.SubElement(v3host, "hostip")
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
            
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username = ET.SubElement(v3host, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        udp_port = ET.SubElement(v3host, "udp-port")
        if kwargs.pop('delete_udp_port', False) is True:
            delete_udp_port = config.find('.//*udp-port')
            delete_udp_port.set('operation', 'delete')
            
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_notifytype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        notifytype = ET.SubElement(v3host, "notifytype")
        if kwargs.pop('delete_notifytype', False) is True:
            delete_notifytype = config.find('.//*notifytype')
            delete_notifytype.set('operation', 'delete')
            
        notifytype.text = kwargs.pop('notifytype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_engineid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        engineid = ET.SubElement(v3host, "engineid")
        if kwargs.pop('delete_engineid', False) is True:
            delete_engineid = config.find('.//*engineid')
            delete_engineid.set('operation', 'delete')
            
        engineid.text = kwargs.pop('engineid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        severity_level = ET.SubElement(v3host, "severity-level")
        if kwargs.pop('delete_severity_level', False) is True:
            delete_severity_level = config.find('.//*severity-level')
            delete_severity_level.set('operation', 'delete')
            
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        use_vrf = ET.SubElement(v3host, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        source_interface = ET.SubElement(v3host, "source-interface")
        if kwargs.pop('delete_source_interface', False) is True:
            delete_source_interface = config.find('.//*source-interface')
            delete_source_interface.set('operation', 'delete')
            
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        if kwargs.pop('delete_source_interface_type', False) is True:
            delete_source_interface_type = config.find('.//*source-interface-type')
            delete_source_interface_type.set('operation', 'delete')
            
        loopback = ET.SubElement(source_interface_type, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        loopback = ET.SubElement(loopback, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        v3host = ET.SubElement(snmp_server, "v3host")
        if kwargs.pop('delete_v3host', False) is True:
            delete_v3host = config.find('.//*v3host')
            delete_v3host.set('operation', 'delete')
            
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
                
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        source_interface = ET.SubElement(v3host, "source-interface")
        if kwargs.pop('delete_source_interface', False) is True:
            delete_source_interface = config.find('.//*source-interface')
            delete_source_interface.set('operation', 'delete')
            
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        if kwargs.pop('delete_source_interface_type', False) is True:
            delete_source_interface_type = config.find('.//*source-interface-type')
            delete_source_interface_type.set('operation', 'delete')
            
        ve = ET.SubElement(source_interface_type, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve = ET.SubElement(ve, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        ip = ET.SubElement(host, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        version = ET.SubElement(host, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community = ET.SubElement(host, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        udp_port = ET.SubElement(host, "udp-port")
        if kwargs.pop('delete_udp_port', False) is True:
            delete_udp_port = config.find('.//*udp-port')
            delete_udp_port.set('operation', 'delete')
            
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        severity_level = ET.SubElement(host, "severity-level")
        if kwargs.pop('delete_severity_level', False) is True:
            delete_severity_level = config.find('.//*severity-level')
            delete_severity_level.set('operation', 'delete')
            
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        use_vrf = ET.SubElement(host, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        source_interface = ET.SubElement(host, "source-interface")
        if kwargs.pop('delete_source_interface', False) is True:
            delete_source_interface = config.find('.//*source-interface')
            delete_source_interface.set('operation', 'delete')
            
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        if kwargs.pop('delete_source_interface_type', False) is True:
            delete_source_interface_type = config.find('.//*source-interface-type')
            delete_source_interface_type.set('operation', 'delete')
            
        loopback = ET.SubElement(source_interface_type, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        loopback = ET.SubElement(loopback, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        host = ET.SubElement(snmp_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
                
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        source_interface = ET.SubElement(host, "source-interface")
        if kwargs.pop('delete_source_interface', False) is True:
            delete_source_interface = config.find('.//*source-interface')
            delete_source_interface.set('operation', 'delete')
            
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        if kwargs.pop('delete_source_interface_type', False) is True:
            delete_source_interface_type = config.find('.//*source-interface-type')
            delete_source_interface_type.set('operation', 'delete')
            
        ve = ET.SubElement(source_interface_type, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve = ET.SubElement(ve, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_contact(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        if kwargs.pop('delete_agtconfig', False) is True:
            delete_agtconfig = config.find('.//*agtconfig')
            delete_agtconfig.set('operation', 'delete')
            
        contact = ET.SubElement(agtconfig, "contact")
        if kwargs.pop('delete_contact', False) is True:
            delete_contact = config.find('.//*contact')
            delete_contact.set('operation', 'delete')
            
        contact.text = kwargs.pop('contact')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_location(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        if kwargs.pop('delete_agtconfig', False) is True:
            delete_agtconfig = config.find('.//*agtconfig')
            delete_agtconfig.set('operation', 'delete')
            
        location = ET.SubElement(agtconfig, "location")
        if kwargs.pop('delete_location', False) is True:
            delete_location = config.find('.//*location')
            delete_location.set('operation', 'delete')
            
        location.text = kwargs.pop('location')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_sys_descr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        if kwargs.pop('delete_agtconfig', False) is True:
            delete_agtconfig = config.find('.//*agtconfig')
            delete_agtconfig.set('operation', 'delete')
            
        sys_descr = ET.SubElement(agtconfig, "sys-descr")
        if kwargs.pop('delete_sys_descr', False) is True:
            delete_sys_descr = config.find('.//*sys-descr')
            delete_sys_descr.set('operation', 'delete')
            
        sys_descr.text = kwargs.pop('sys_descr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_enable_trap_trap_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        enable = ET.SubElement(snmp_server, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            
        trap = ET.SubElement(enable, "trap")
        if kwargs.pop('delete_trap', False) is True:
            delete_trap = config.find('.//*trap')
            delete_trap.set('operation', 'delete')
            
        trap_flag = ET.SubElement(trap, "trap-flag")
        if kwargs.pop('delete_trap_flag', False) is True:
            delete_trap_flag = config.find('.//*trap-flag')
            delete_trap_flag.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_engineID_drop_engineID_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        engineID_drop = ET.SubElement(snmp_server, "engineID-drop")
        if kwargs.pop('delete_engineID_drop', False) is True:
            delete_engineID_drop = config.find('.//*engineID-drop')
            delete_engineID_drop.set('operation', 'delete')
            
        engineID = ET.SubElement(engineID_drop, "engineID")
        if kwargs.pop('delete_engineID', False) is True:
            delete_engineID = config.find('.//*engineID')
            delete_engineID.set('operation', 'delete')
            
        local = ET.SubElement(engineID, "local")
        if kwargs.pop('delete_local', False) is True:
            delete_local = config.find('.//*local')
            delete_local.set('operation', 'delete')
            
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_viewname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        view = ET.SubElement(snmp_server, "view")
        if kwargs.pop('delete_view', False) is True:
            delete_view = config.find('.//*view')
            delete_view.set('operation', 'delete')
            
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        if kwargs.pop('delete_mibtree', False) is True:
            delete_mibtree = config.find('.//*mibtree')
            delete_mibtree.set('operation', 'delete')
                
        viewname = ET.SubElement(view, "viewname")
        if kwargs.pop('delete_viewname', False) is True:
            delete_viewname = config.find('.//*viewname')
            delete_viewname.set('operation', 'delete')
            
        viewname.text = kwargs.pop('viewname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        view = ET.SubElement(snmp_server, "view")
        if kwargs.pop('delete_view', False) is True:
            delete_view = config.find('.//*view')
            delete_view.set('operation', 'delete')
            
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        if kwargs.pop('delete_viewname', False) is True:
            delete_viewname = config.find('.//*viewname')
            delete_viewname.set('operation', 'delete')
                
        mibtree = ET.SubElement(view, "mibtree")
        if kwargs.pop('delete_mibtree', False) is True:
            delete_mibtree = config.find('.//*mibtree')
            delete_mibtree.set('operation', 'delete')
            
        mibtree.text = kwargs.pop('mibtree')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        view = ET.SubElement(snmp_server, "view")
        if kwargs.pop('delete_view', False) is True:
            delete_view = config.find('.//*view')
            delete_view.set('operation', 'delete')
            
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        if kwargs.pop('delete_viewname', False) is True:
            delete_viewname = config.find('.//*viewname')
            delete_viewname.set('operation', 'delete')
                
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        if kwargs.pop('delete_mibtree', False) is True:
            delete_mibtree = config.find('.//*mibtree')
            delete_mibtree.set('operation', 'delete')
                
        mibtree_access = ET.SubElement(view, "mibtree-access")
        if kwargs.pop('delete_mibtree_access', False) is True:
            delete_mibtree_access = config.find('.//*mibtree-access')
            delete_mibtree_access.set('operation', 'delete')
            
        mibtree_access.text = kwargs.pop('mibtree_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
                
        group_name = ET.SubElement(group, "group-name")
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
            
        group_name.text = kwargs.pop('group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
                
        group_version = ET.SubElement(group, "group-version")
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
            
        group_version.text = kwargs.pop('group_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_auth_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
                
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
                
        group_auth_mode = ET.SubElement(group, "group-auth-mode")
        if kwargs.pop('delete_group_auth_mode', False) is True:
            delete_group_auth_mode = config.find('.//*group-auth-mode')
            delete_group_auth_mode.set('operation', 'delete')
            
        group_auth_mode.text = kwargs.pop('group_auth_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_read(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
                
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
                
        read = ET.SubElement(group, "read")
        if kwargs.pop('delete_read', False) is True:
            delete_read = config.find('.//*read')
            delete_read.set('operation', 'delete')
            
        read.text = kwargs.pop('read')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_write(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
                
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
                
        write = ET.SubElement(group, "write")
        if kwargs.pop('delete_write', False) is True:
            delete_write = config.find('.//*write')
            delete_write.set('operation', 'delete')
            
        write.text = kwargs.pop('write')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_notify(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        group = ET.SubElement(snmp_server, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        if kwargs.pop('delete_group_name', False) is True:
            delete_group_name = config.find('.//*group-name')
            delete_group_name.set('operation', 'delete')
                
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        if kwargs.pop('delete_group_version', False) is True:
            delete_group_version = config.find('.//*group-version')
            delete_group_version.set('operation', 'delete')
                
        notify = ET.SubElement(group, "notify")
        if kwargs.pop('delete_notify', False) is True:
            delete_notify = config.find('.//*notify')
            delete_notify.set('operation', 'delete')
            
        notify.text = kwargs.pop('notify')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        mib = ET.SubElement(snmp_server, "mib")
        if kwargs.pop('delete_mib', False) is True:
            delete_mib = config.find('.//*mib')
            delete_mib.set('operation', 'delete')
            
        community_map = ET.SubElement(mib, "community-map")
        if kwargs.pop('delete_community_map', False) is True:
            delete_community_map = config.find('.//*community-map')
            delete_community_map.set('operation', 'delete')
            
        community = ET.SubElement(community_map, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        if kwargs.pop('delete_snmp_server', False) is True:
            delete_snmp_server = config.find('.//*snmp-server')
            delete_snmp_server.set('operation', 'delete')
            
        mib = ET.SubElement(snmp_server, "mib")
        if kwargs.pop('delete_mib', False) is True:
            delete_mib = config.find('.//*mib')
            delete_mib.set('operation', 'delete')
            
        community_map = ET.SubElement(mib, "community-map")
        if kwargs.pop('delete_community_map', False) is True:
            delete_community_map = config.find('.//*community-map')
            delete_community_map.set('operation', 'delete')
            
        community_key = ET.SubElement(community_map, "community")
        community_key.text = kwargs.pop('community')
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
                
        context = ET.SubElement(community_map, "context")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        