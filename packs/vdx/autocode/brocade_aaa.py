#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_aaa(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def aaa_config_aaa_authentication_login_first(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_aaa_config', False) is True:
            delete_aaa_config = config.find('.//*aaa-config')
            delete_aaa_config.set('operation', 'delete')
            
        aaa = ET.SubElement(aaa_config, "aaa")
        if kwargs.pop('delete_aaa', False) is True:
            delete_aaa = config.find('.//*aaa')
            delete_aaa.set('operation', 'delete')
            
        authentication = ET.SubElement(aaa, "authentication")
        if kwargs.pop('delete_authentication', False) is True:
            delete_authentication = config.find('.//*authentication')
            delete_authentication.set('operation', 'delete')
            
        login = ET.SubElement(authentication, "login")
        if kwargs.pop('delete_login', False) is True:
            delete_login = config.find('.//*login')
            delete_login.set('operation', 'delete')
            
        first = ET.SubElement(login, "first")
        if kwargs.pop('delete_first', False) is True:
            delete_first = config.find('.//*first')
            delete_first.set('operation', 'delete')
            
        first.text = kwargs.pop('first')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_authentication_login_second(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_aaa_config', False) is True:
            delete_aaa_config = config.find('.//*aaa-config')
            delete_aaa_config.set('operation', 'delete')
            
        aaa = ET.SubElement(aaa_config, "aaa")
        if kwargs.pop('delete_aaa', False) is True:
            delete_aaa = config.find('.//*aaa')
            delete_aaa.set('operation', 'delete')
            
        authentication = ET.SubElement(aaa, "authentication")
        if kwargs.pop('delete_authentication', False) is True:
            delete_authentication = config.find('.//*authentication')
            delete_authentication.set('operation', 'delete')
            
        login = ET.SubElement(authentication, "login")
        if kwargs.pop('delete_login', False) is True:
            delete_login = config.find('.//*login')
            delete_login.set('operation', 'delete')
            
        second = ET.SubElement(login, "second")
        if kwargs.pop('delete_second', False) is True:
            delete_second = config.find('.//*second')
            delete_second.set('operation', 'delete')
            
        second.text = kwargs.pop('second')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_exec_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_aaa_config', False) is True:
            delete_aaa_config = config.find('.//*aaa-config')
            delete_aaa_config.set('operation', 'delete')
            
        aaa = ET.SubElement(aaa_config, "aaa")
        if kwargs.pop('delete_aaa', False) is True:
            delete_aaa = config.find('.//*aaa')
            delete_aaa.set('operation', 'delete')
            
        accounting = ET.SubElement(aaa, "accounting")
        if kwargs.pop('delete_accounting', False) is True:
            delete_accounting = config.find('.//*accounting')
            delete_accounting.set('operation', 'delete')
            
        exec = ET.SubElement(accounting, "exec")
        if kwargs.pop('delete_exec', False) is True:
            delete_exec = config.find('.//*exec')
            delete_exec.set('operation', 'delete')
            
        defaultacc = ET.SubElement(exec, "defaultacc")
        if kwargs.pop('delete_defaultacc', False) is True:
            delete_defaultacc = config.find('.//*defaultacc')
            delete_defaultacc.set('operation', 'delete')
            
        start_stop = ET.SubElement(defaultacc, "start-stop")
        if kwargs.pop('delete_start_stop', False) is True:
            delete_start_stop = config.find('.//*start-stop')
            delete_start_stop.set('operation', 'delete')
            
        server_type = ET.SubElement(start_stop, "server-type")
        if kwargs.pop('delete_server_type', False) is True:
            delete_server_type = config.find('.//*server-type')
            delete_server_type.set('operation', 'delete')
            
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_commands_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_aaa_config', False) is True:
            delete_aaa_config = config.find('.//*aaa-config')
            delete_aaa_config.set('operation', 'delete')
            
        aaa = ET.SubElement(aaa_config, "aaa")
        if kwargs.pop('delete_aaa', False) is True:
            delete_aaa = config.find('.//*aaa')
            delete_aaa.set('operation', 'delete')
            
        accounting = ET.SubElement(aaa, "accounting")
        if kwargs.pop('delete_accounting', False) is True:
            delete_accounting = config.find('.//*accounting')
            delete_accounting.set('operation', 'delete')
            
        commands = ET.SubElement(accounting, "commands")
        if kwargs.pop('delete_commands', False) is True:
            delete_commands = config.find('.//*commands')
            delete_commands.set('operation', 'delete')
            
        defaultacc = ET.SubElement(commands, "defaultacc")
        if kwargs.pop('delete_defaultacc', False) is True:
            delete_defaultacc = config.find('.//*defaultacc')
            delete_defaultacc.set('operation', 'delete')
            
        start_stop = ET.SubElement(defaultacc, "start-stop")
        if kwargs.pop('delete_start_stop', False) is True:
            delete_start_stop = config.find('.//*start-stop')
            delete_start_stop.set('operation', 'delete')
            
        server_type = ET.SubElement(start_stop, "server-type")
        if kwargs.pop('delete_server_type', False) is True:
            delete_server_type = config.find('.//*server-type')
            delete_server_type.set('operation', 'delete')
            
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name = ET.SubElement(username, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_user_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        user_password = ET.SubElement(username, "user-password")
        if kwargs.pop('delete_user_password', False) is True:
            delete_user_password = config.find('.//*user-password')
            delete_user_password.set('operation', 'delete')
            
        user_password.text = kwargs.pop('user_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        encryption_level = ET.SubElement(username, "encryption-level")
        if kwargs.pop('delete_encryption_level', False) is True:
            delete_encryption_level = config.find('.//*encryption-level')
            delete_encryption_level.set('operation', 'delete')
            
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        role = ET.SubElement(username, "role")
        if kwargs.pop('delete_role', False) is True:
            delete_role = config.find('.//*role')
            delete_role.set('operation', 'delete')
            
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        desc = ET.SubElement(username, "desc")
        if kwargs.pop('delete_desc', False) is True:
            delete_desc = config.find('.//*desc')
            delete_desc.set('operation', 'delete')
            
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        enable = ET.SubElement(username, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            
        enable.text = kwargs.pop('enable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_expire(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        expire = ET.SubElement(username, "expire")
        if kwargs.pop('delete_expire', False) is True:
            delete_expire = config.find('.//*expire')
            delete_expire.set('operation', 'delete')
            
        expire.text = kwargs.pop('expire')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def service_password_encryption(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        service = ET.SubElement(config, "service", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_service', False) is True:
            delete_service = config.find('.//*service')
            delete_service.set('operation', 'delete')
            
        password_encryption = ET.SubElement(service, "password-encryption")
        if kwargs.pop('delete_password_encryption', False) is True:
            delete_password_encryption = config.find('.//*password-encryption')
            delete_password_encryption.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_role', False) is True:
            delete_role = config.find('.//*role')
            delete_role.set('operation', 'delete')
            
        name = ET.SubElement(role, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name = ET.SubElement(name, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_role', False) is True:
            delete_role = config.find('.//*role')
            delete_role.set('operation', 'delete')
            
        name = ET.SubElement(role, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name_key = ET.SubElement(name, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        desc = ET.SubElement(name, "desc")
        if kwargs.pop('delete_desc', False) is True:
            delete_desc = config.find('.//*desc')
            delete_desc.set('operation', 'delete')
            
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        hostname = ET.SubElement(host, "hostname")
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
            
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf = ET.SubElement(host, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_auth_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        auth_port = ET.SubElement(host, "auth-port")
        if kwargs.pop('delete_auth_port', False) is True:
            delete_auth_port = config.find('.//*auth-port')
            delete_auth_port.set('operation', 'delete')
            
        auth_port.text = kwargs.pop('auth_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        protocol = ET.SubElement(host, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        key = ET.SubElement(host, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        encryption_level = ET.SubElement(host, "encryption-level")
        if kwargs.pop('delete_encryption_level', False) is True:
            delete_encryption_level = config.find('.//*encryption-level')
            delete_encryption_level.set('operation', 'delete')
            
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        retries = ET.SubElement(host, "retries")
        if kwargs.pop('delete_retries', False) is True:
            delete_retries = config.find('.//*retries')
            delete_retries.set('operation', 'delete')
            
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_radius_server', False) is True:
            delete_radius_server = config.find('.//*radius-server')
            delete_radius_server.set('operation', 'delete')
            
        host = ET.SubElement(radius_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        timeout = ET.SubElement(host, "timeout")
        if kwargs.pop('delete_timeout', False) is True:
            delete_timeout = config.find('.//*timeout')
            delete_timeout.set('operation', 'delete')
            
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        hostname = ET.SubElement(host, "hostname")
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
            
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf = ET.SubElement(host, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        port = ET.SubElement(host, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        protocol = ET.SubElement(host, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        key = ET.SubElement(host, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        encryption_level = ET.SubElement(host, "encryption-level")
        if kwargs.pop('delete_encryption_level', False) is True:
            delete_encryption_level = config.find('.//*encryption-level')
            delete_encryption_level.set('operation', 'delete')
            
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        retries = ET.SubElement(host, "retries")
        if kwargs.pop('delete_retries', False) is True:
            delete_retries = config.find('.//*retries')
            delete_retries.set('operation', 'delete')
            
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        host = ET.SubElement(tacacs_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        timeout = ET.SubElement(host, "timeout")
        if kwargs.pop('delete_timeout', False) is True:
            delete_timeout = config.find('.//*timeout')
            delete_timeout.set('operation', 'delete')
            
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_tacacs_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_tacacs_server', False) is True:
            delete_tacacs_server = config.find('.//*tacacs-server')
            delete_tacacs_server.set('operation', 'delete')
            
        tacacs_source_ip = ET.SubElement(tacacs_server, "tacacs-source-ip")
        if kwargs.pop('delete_tacacs_source_ip', False) is True:
            delete_tacacs_source_ip = config.find('.//*tacacs-source-ip')
            delete_tacacs_source_ip.set('operation', 'delete')
            
        tacacs_source_ip.text = kwargs.pop('tacacs_source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        hostname = ET.SubElement(host, "hostname")
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
            
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf = ET.SubElement(host, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        port = ET.SubElement(host, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        retries = ET.SubElement(host, "retries")
        if kwargs.pop('delete_retries', False) is True:
            delete_retries = config.find('.//*retries')
            delete_retries.set('operation', 'delete')
            
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        timeout = ET.SubElement(host, "timeout")
        if kwargs.pop('delete_timeout', False) is True:
            delete_timeout = config.find('.//*timeout')
            delete_timeout.set('operation', 'delete')
            
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_basedn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        host = ET.SubElement(ldap_server, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        if kwargs.pop('delete_hostname', False) is True:
            delete_hostname = config.find('.//*hostname')
            delete_hostname.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        basedn = ET.SubElement(host, "basedn")
        if kwargs.pop('delete_basedn', False) is True:
            delete_basedn = config.find('.//*basedn')
            delete_basedn.set('operation', 'delete')
            
        basedn.text = kwargs.pop('basedn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_ad_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        maprole = ET.SubElement(ldap_server, "maprole")
        if kwargs.pop('delete_maprole', False) is True:
            delete_maprole = config.find('.//*maprole')
            delete_maprole.set('operation', 'delete')
            
        group = ET.SubElement(maprole, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        ad_group = ET.SubElement(group, "ad-group")
        if kwargs.pop('delete_ad_group', False) is True:
            delete_ad_group = config.find('.//*ad-group')
            delete_ad_group.set('operation', 'delete')
            
        ad_group.text = kwargs.pop('ad_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_switch_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_ldap_server', False) is True:
            delete_ldap_server = config.find('.//*ldap-server')
            delete_ldap_server.set('operation', 'delete')
            
        maprole = ET.SubElement(ldap_server, "maprole")
        if kwargs.pop('delete_maprole', False) is True:
            delete_maprole = config.find('.//*maprole')
            delete_maprole.set('operation', 'delete')
            
        group = ET.SubElement(maprole, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        ad_group_key = ET.SubElement(group, "ad-group")
        ad_group_key.text = kwargs.pop('ad_group')
        if kwargs.pop('delete_ad_group', False) is True:
            delete_ad_group = config.find('.//*ad-group')
            delete_ad_group.set('operation', 'delete')
                
        switch_role = ET.SubElement(group, "switch-role")
        if kwargs.pop('delete_switch_role', False) is True:
            delete_switch_role = config.find('.//*switch-role')
            delete_switch_role.set('operation', 'delete')
            
        switch_role.text = kwargs.pop('switch_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_min_length(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        min_length = ET.SubElement(password_attributes, "min-length")
        if kwargs.pop('delete_min_length', False) is True:
            delete_min_length = config.find('.//*min-length')
            delete_min_length.set('operation', 'delete')
            
        min_length.text = kwargs.pop('min_length')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        max_retry = ET.SubElement(password_attributes, "max-retry")
        if kwargs.pop('delete_max_retry', False) is True:
            delete_max_retry = config.find('.//*max-retry')
            delete_max_retry.set('operation', 'delete')
            
        max_retry.text = kwargs.pop('max_retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_lockout_duration(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        max_lockout_duration = ET.SubElement(password_attributes, "max-lockout-duration")
        if kwargs.pop('delete_max_lockout_duration', False) is True:
            delete_max_lockout_duration = config.find('.//*max-lockout-duration')
            delete_max_lockout_duration.set('operation', 'delete')
            
        max_lockout_duration.text = kwargs.pop('max_lockout_duration')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        if kwargs.pop('delete_character_restriction', False) is True:
            delete_character_restriction = config.find('.//*character-restriction')
            delete_character_restriction.set('operation', 'delete')
            
        upper = ET.SubElement(character_restriction, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        if kwargs.pop('delete_character_restriction', False) is True:
            delete_character_restriction = config.find('.//*character-restriction')
            delete_character_restriction.set('operation', 'delete')
            
        lower = ET.SubElement(character_restriction, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_numeric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        if kwargs.pop('delete_character_restriction', False) is True:
            delete_character_restriction = config.find('.//*character-restriction')
            delete_character_restriction.set('operation', 'delete')
            
        numeric = ET.SubElement(character_restriction, "numeric")
        if kwargs.pop('delete_numeric', False) is True:
            delete_numeric = config.find('.//*numeric')
            delete_numeric.set('operation', 'delete')
            
        numeric.text = kwargs.pop('numeric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_special_char(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        if kwargs.pop('delete_character_restriction', False) is True:
            delete_character_restriction = config.find('.//*character-restriction')
            delete_character_restriction.set('operation', 'delete')
            
        special_char = ET.SubElement(character_restriction, "special-char")
        if kwargs.pop('delete_special_char', False) is True:
            delete_special_char = config.find('.//*special-char')
            delete_special_char.set('operation', 'delete')
            
        special_char.text = kwargs.pop('special_char')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_admin_lockout_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_password_attributes', False) is True:
            delete_password_attributes = config.find('.//*password-attributes')
            delete_password_attributes.set('operation', 'delete')
            
        admin_lockout_enable = ET.SubElement(password_attributes, "admin-lockout-enable")
        if kwargs.pop('delete_admin_lockout_enable', False) is True:
            delete_admin_lockout_enable = config.find('.//*admin-lockout-enable')
            delete_admin_lockout_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_login(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_banner', False) is True:
            delete_banner = config.find('.//*banner')
            delete_banner.set('operation', 'delete')
            
        login = ET.SubElement(banner, "login")
        if kwargs.pop('delete_login', False) is True:
            delete_login = config.find('.//*login')
            delete_login.set('operation', 'delete')
            
        login.text = kwargs.pop('login')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_motd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_banner', False) is True:
            delete_banner = config.find('.//*banner')
            delete_banner.set('operation', 'delete')
            
        motd = ET.SubElement(banner, "motd")
        if kwargs.pop('delete_motd', False) is True:
            delete_motd = config.find('.//*motd')
            delete_motd.set('operation', 'delete')
            
        motd.text = kwargs.pop('motd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_incoming(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_banner', False) is True:
            delete_banner = config.find('.//*banner')
            delete_banner.set('operation', 'delete')
            
        incoming = ET.SubElement(banner, "incoming")
        if kwargs.pop('delete_incoming', False) is True:
            delete_incoming = config.find('.//*incoming')
            delete_incoming.set('operation', 'delete')
            
        incoming.text = kwargs.pop('incoming')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index = ET.SubElement(rule, "index")
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
            
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        action = ET.SubElement(rule, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        operation = ET.SubElement(rule, "operation")
        if kwargs.pop('delete_operation', False) is True:
            delete_operation = config.find('.//*operation')
            delete_operation.set('operation', 'delete')
            
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        role = ET.SubElement(rule, "role")
        if kwargs.pop('delete_role', False) is True:
            delete_role = config.find('.//*role')
            delete_role.set('operation', 'delete')
            
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_container_cmds_enumList(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        container_cmds = ET.SubElement(cmdlist, "container-cmds")
        if kwargs.pop('delete_container_cmds', False) is True:
            delete_container_cmds = config.find('.//*container-cmds')
            delete_container_cmds.set('operation', 'delete')
            
        enumList = ET.SubElement(container_cmds, "enumList")
        if kwargs.pop('delete_enumList', False) is True:
            delete_enumList = config.find('.//*enumList')
            delete_enumList.set('operation', 'delete')
            
        enumList.text = kwargs.pop('enumList')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_d_interface_fcoe_leaf_interface_fcoe_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_d = ET.SubElement(cmdlist, "interface-d")
        if kwargs.pop('delete_interface_d', False) is True:
            delete_interface_d = config.find('.//*interface-d')
            delete_interface_d.set('operation', 'delete')
            
        interface_fcoe_leaf = ET.SubElement(interface_d, "interface-fcoe-leaf")
        if kwargs.pop('delete_interface_fcoe_leaf', False) is True:
            delete_interface_fcoe_leaf = config.find('.//*interface-fcoe-leaf')
            delete_interface_fcoe_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_fcoe_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        fcoe_leaf = ET.SubElement(interface, "fcoe-leaf")
        if kwargs.pop('delete_fcoe_leaf', False) is True:
            delete_fcoe_leaf = config.find('.//*fcoe-leaf')
            delete_fcoe_leaf.set('operation', 'delete')
            
        fcoe_leaf.text = kwargs.pop('fcoe_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_e_interface_te_leaf_interface_tengigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_e = ET.SubElement(cmdlist, "interface-e")
        if kwargs.pop('delete_interface_e', False) is True:
            delete_interface_e = config.find('.//*interface-e')
            delete_interface_e.set('operation', 'delete')
            
        interface_te_leaf = ET.SubElement(interface_e, "interface-te-leaf")
        if kwargs.pop('delete_interface_te_leaf', False) is True:
            delete_interface_te_leaf = config.find('.//*interface-te-leaf')
            delete_interface_te_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_te_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        tengigabitethernet_leaf = ET.SubElement(interface, "tengigabitethernet-leaf")
        if kwargs.pop('delete_tengigabitethernet_leaf', False) is True:
            delete_tengigabitethernet_leaf = config.find('.//*tengigabitethernet-leaf')
            delete_tengigabitethernet_leaf.set('operation', 'delete')
            
        tengigabitethernet_leaf.text = kwargs.pop('tengigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_h_interface_ge_leaf_interface_gigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_h = ET.SubElement(cmdlist, "interface-h")
        if kwargs.pop('delete_interface_h', False) is True:
            delete_interface_h = config.find('.//*interface-h')
            delete_interface_h.set('operation', 'delete')
            
        interface_ge_leaf = ET.SubElement(interface_h, "interface-ge-leaf")
        if kwargs.pop('delete_interface_ge_leaf', False) is True:
            delete_interface_ge_leaf = config.find('.//*interface-ge-leaf')
            delete_interface_ge_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_ge_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        gigabitethernet_leaf = ET.SubElement(interface, "gigabitethernet-leaf")
        if kwargs.pop('delete_gigabitethernet_leaf', False) is True:
            delete_gigabitethernet_leaf = config.find('.//*gigabitethernet-leaf')
            delete_gigabitethernet_leaf.set('operation', 'delete')
            
        gigabitethernet_leaf.text = kwargs.pop('gigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_j_interface_pc_leaf_interface_port_channel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_j = ET.SubElement(cmdlist, "interface-j")
        if kwargs.pop('delete_interface_j', False) is True:
            delete_interface_j = config.find('.//*interface-j')
            delete_interface_j.set('operation', 'delete')
            
        interface_pc_leaf = ET.SubElement(interface_j, "interface-pc-leaf")
        if kwargs.pop('delete_interface_pc_leaf', False) is True:
            delete_interface_pc_leaf = config.find('.//*interface-pc-leaf')
            delete_interface_pc_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_pc_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        port_channel_leaf = ET.SubElement(interface, "port-channel-leaf")
        if kwargs.pop('delete_port_channel_leaf', False) is True:
            delete_port_channel_leaf = config.find('.//*port-channel-leaf')
            delete_port_channel_leaf.set('operation', 'delete')
            
        port_channel_leaf.text = kwargs.pop('port_channel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_l_interface_vlan_leaf_interface_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_l = ET.SubElement(cmdlist, "interface-l")
        if kwargs.pop('delete_interface_l', False) is True:
            delete_interface_l = config.find('.//*interface-l')
            delete_interface_l.set('operation', 'delete')
            
        interface_vlan_leaf = ET.SubElement(interface_l, "interface-vlan-leaf")
        if kwargs.pop('delete_interface_vlan_leaf', False) is True:
            delete_interface_vlan_leaf = config.find('.//*interface-vlan-leaf')
            delete_interface_vlan_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_vlan_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        vlan_leaf = ET.SubElement(interface, "vlan-leaf")
        if kwargs.pop('delete_vlan_leaf', False) is True:
            delete_vlan_leaf = config.find('.//*vlan-leaf')
            delete_vlan_leaf.set('operation', 'delete')
            
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_m_interface_management_leaf_interface_management_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_m = ET.SubElement(cmdlist, "interface-m")
        if kwargs.pop('delete_interface_m', False) is True:
            delete_interface_m = config.find('.//*interface-m')
            delete_interface_m.set('operation', 'delete')
            
        interface_management_leaf = ET.SubElement(interface_m, "interface-management-leaf")
        if kwargs.pop('delete_interface_management_leaf', False) is True:
            delete_interface_management_leaf = config.find('.//*interface-management-leaf')
            delete_interface_management_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_management_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        management_leaf = ET.SubElement(interface, "management-leaf")
        if kwargs.pop('delete_management_leaf', False) is True:
            delete_management_leaf = config.find('.//*management-leaf')
            delete_management_leaf.set('operation', 'delete')
            
        management_leaf.text = kwargs.pop('management_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_o_interface_loopback_leaf_interface_loopback_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_o = ET.SubElement(cmdlist, "interface-o")
        if kwargs.pop('delete_interface_o', False) is True:
            delete_interface_o = config.find('.//*interface-o')
            delete_interface_o.set('operation', 'delete')
            
        interface_loopback_leaf = ET.SubElement(interface_o, "interface-loopback-leaf")
        if kwargs.pop('delete_interface_loopback_leaf', False) is True:
            delete_interface_loopback_leaf = config.find('.//*interface-loopback-leaf')
            delete_interface_loopback_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_loopback_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        loopback_leaf = ET.SubElement(interface, "loopback-leaf")
        if kwargs.pop('delete_loopback_leaf', False) is True:
            delete_loopback_leaf = config.find('.//*loopback-leaf')
            delete_loopback_leaf.set('operation', 'delete')
            
        loopback_leaf.text = kwargs.pop('loopback_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_q_interface_ve_leaf_interface_ve_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_q = ET.SubElement(cmdlist, "interface-q")
        if kwargs.pop('delete_interface_q', False) is True:
            delete_interface_q = config.find('.//*interface-q')
            delete_interface_q.set('operation', 'delete')
            
        interface_ve_leaf = ET.SubElement(interface_q, "interface-ve-leaf")
        if kwargs.pop('delete_interface_ve_leaf', False) is True:
            delete_interface_ve_leaf = config.find('.//*interface-ve-leaf')
            delete_interface_ve_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_ve_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        ve_leaf = ET.SubElement(interface, "ve-leaf")
        if kwargs.pop('delete_ve_leaf', False) is True:
            delete_ve_leaf = config.find('.//*ve-leaf')
            delete_ve_leaf.set('operation', 'delete')
            
        ve_leaf.text = kwargs.pop('ve_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_s_interface_fc_leaf_interface_fibrechannel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_s = ET.SubElement(cmdlist, "interface-s")
        if kwargs.pop('delete_interface_s', False) is True:
            delete_interface_s = config.find('.//*interface-s')
            delete_interface_s.set('operation', 'delete')
            
        interface_fc_leaf = ET.SubElement(interface_s, "interface-fc-leaf")
        if kwargs.pop('delete_interface_fc_leaf', False) is True:
            delete_interface_fc_leaf = config.find('.//*interface-fc-leaf')
            delete_interface_fc_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_fc_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        fibrechannel_leaf = ET.SubElement(interface, "fibrechannel-leaf")
        if kwargs.pop('delete_fibrechannel_leaf', False) is True:
            delete_fibrechannel_leaf = config.find('.//*fibrechannel-leaf')
            delete_fibrechannel_leaf.set('operation', 'delete')
            
        fibrechannel_leaf.text = kwargs.pop('fibrechannel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_u_interface_fe_leaf_interface_fortygigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_u = ET.SubElement(cmdlist, "interface-u")
        if kwargs.pop('delete_interface_u', False) is True:
            delete_interface_u = config.find('.//*interface-u')
            delete_interface_u.set('operation', 'delete')
            
        interface_fe_leaf = ET.SubElement(interface_u, "interface-fe-leaf")
        if kwargs.pop('delete_interface_fe_leaf', False) is True:
            delete_interface_fe_leaf = config.find('.//*interface-fe-leaf')
            delete_interface_fe_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_fe_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        fortygigabitethernet_leaf = ET.SubElement(interface, "fortygigabitethernet-leaf")
        if kwargs.pop('delete_fortygigabitethernet_leaf', False) is True:
            delete_fortygigabitethernet_leaf = config.find('.//*fortygigabitethernet-leaf')
            delete_fortygigabitethernet_leaf.set('operation', 'delete')
            
        fortygigabitethernet_leaf.text = kwargs.pop('fortygigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_w_interface_he_leaf_interface_hundredgigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        if kwargs.pop('delete_index', False) is True:
            delete_index = config.find('.//*index')
            delete_index.set('operation', 'delete')
                
        command = ET.SubElement(rule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        cmdlist = ET.SubElement(command, "cmdlist")
        if kwargs.pop('delete_cmdlist', False) is True:
            delete_cmdlist = config.find('.//*cmdlist')
            delete_cmdlist.set('operation', 'delete')
            
        interface_w = ET.SubElement(cmdlist, "interface-w")
        if kwargs.pop('delete_interface_w', False) is True:
            delete_interface_w = config.find('.//*interface-w')
            delete_interface_w.set('operation', 'delete')
            
        interface_he_leaf = ET.SubElement(interface_w, "interface-he-leaf")
        if kwargs.pop('delete_interface_he_leaf', False) is True:
            delete_interface_he_leaf = config.find('.//*interface-he-leaf')
            delete_interface_he_leaf.set('operation', 'delete')
            
        interface = ET.SubElement(interface_he_leaf, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        hundredgigabitethernet_leaf = ET.SubElement(interface, "hundredgigabitethernet-leaf")
        if kwargs.pop('delete_hundredgigabitethernet_leaf', False) is True:
            delete_hundredgigabitethernet_leaf = config.find('.//*hundredgigabitethernet-leaf')
            delete_hundredgigabitethernet_leaf.set('operation', 'delete')
            
        hundredgigabitethernet_leaf.text = kwargs.pop('hundredgigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_root_sa', False) is True:
            delete_root_sa = config.find('.//*root-sa')
            delete_root_sa.set('operation', 'delete')
            
        root = ET.SubElement(root_sa, "root")
        if kwargs.pop('delete_root', False) is True:
            delete_root = config.find('.//*root')
            delete_root.set('operation', 'delete')
            
        enable = ET.SubElement(root, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_root_sa', False) is True:
            delete_root_sa = config.find('.//*root-sa')
            delete_root_sa.set('operation', 'delete')
            
        root = ET.SubElement(root_sa, "root")
        if kwargs.pop('delete_root', False) is True:
            delete_root = config.find('.//*root')
            delete_root.set('operation', 'delete')
            
        access = ET.SubElement(root, "access")
        if kwargs.pop('delete_access', False) is True:
            delete_access = config.find('.//*access')
            delete_access.set('operation', 'delete')
            
        access.text = kwargs.pop('access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_alias_config', False) is True:
            delete_alias_config = config.find('.//*alias-config')
            delete_alias_config.set('operation', 'delete')
            
        alias = ET.SubElement(alias_config, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        name = ET.SubElement(alias, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_alias_config', False) is True:
            delete_alias_config = config.find('.//*alias-config')
            delete_alias_config.set('operation', 'delete')
            
        alias = ET.SubElement(alias_config, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        expansion = ET.SubElement(alias, "expansion")
        if kwargs.pop('delete_expansion', False) is True:
            delete_expansion = config.find('.//*expansion')
            delete_expansion.set('operation', 'delete')
            
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_alias_config', False) is True:
            delete_alias_config = config.find('.//*alias-config')
            delete_alias_config.set('operation', 'delete')
            
        user = ET.SubElement(alias_config, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        name = ET.SubElement(user, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_alias_config', False) is True:
            delete_alias_config = config.find('.//*alias-config')
            delete_alias_config.set('operation', 'delete')
            
        user = ET.SubElement(alias_config, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        alias = ET.SubElement(user, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        name = ET.SubElement(alias, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        if kwargs.pop('delete_alias_config', False) is True:
            delete_alias_config = config.find('.//*alias-config')
            delete_alias_config.set('operation', 'delete')
            
        user = ET.SubElement(alias_config, "user")
        if kwargs.pop('delete_user', False) is True:
            delete_user = config.find('.//*user')
            delete_user.set('operation', 'delete')
            
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        alias = ET.SubElement(user, "alias")
        if kwargs.pop('delete_alias', False) is True:
            delete_alias = config.find('.//*alias')
            delete_alias.set('operation', 'delete')
            
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        expansion = ET.SubElement(alias, "expansion")
        if kwargs.pop('delete_expansion', False) is True:
            delete_expansion = config.find('.//*expansion')
            delete_expansion.set('operation', 'delete')
            
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        