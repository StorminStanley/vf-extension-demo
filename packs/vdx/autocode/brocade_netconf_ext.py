#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_netconf_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_netconf_client_capabilities_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        input = ET.SubElement(get_netconf_client_capabilities, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        session_id = ET.SubElement(input, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id = ET.SubElement(session, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        user_name = ET.SubElement(session, "user-name")
        if kwargs.pop('delete_user_name', False) is True:
            delete_user_name = config.find('.//*user-name')
            delete_user_name.set('operation', 'delete')
            
        user_name.text = kwargs.pop('user_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        vendor = ET.SubElement(session, "vendor")
        if kwargs.pop('delete_vendor', False) is True:
            delete_vendor = config.find('.//*vendor')
            delete_vendor.set('operation', 'delete')
            
        vendor.text = kwargs.pop('vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_product(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        product = ET.SubElement(session, "product")
        if kwargs.pop('delete_product', False) is True:
            delete_product = config.find('.//*product')
            delete_product.set('operation', 'delete')
            
        product.text = kwargs.pop('product')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        version = ET.SubElement(session, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_identity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        identity = ET.SubElement(session, "identity")
        if kwargs.pop('delete_identity', False) is True:
            delete_identity = config.find('.//*identity')
            delete_identity.set('operation', 'delete')
            
        identity.text = kwargs.pop('identity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_af_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        af_type = ET.SubElement(session, "af-type")
        if kwargs.pop('delete_af_type', False) is True:
            delete_af_type = config.find('.//*af-type')
            delete_af_type.set('operation', 'delete')
            
        af_type.text = kwargs.pop('af_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip_v6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        host_ip_v6 = ET.SubElement(session, "host-ip-v6")
        if kwargs.pop('delete_host_ip_v6', False) is True:
            delete_host_ip_v6 = config.find('.//*host-ip-v6')
            delete_host_ip_v6.set('operation', 'delete')
            
        host_ip_v6.text = kwargs.pop('host_ip_v6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        host_ip = ET.SubElement(session, "host-ip")
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
            
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        if kwargs.pop('delete_get_netconf_client_capabilities', False) is True:
            delete_get_netconf_client_capabilities = config.find('.//*get-netconf-client-capabilities')
            delete_get_netconf_client_capabilities.set('operation', 'delete')
            
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session = ET.SubElement(output, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        time = ET.SubElement(session, "time")
        if kwargs.pop('delete_time', False) is True:
            delete_time = config.find('.//*time')
            delete_time.set('operation', 'delete')
            
        time.text = kwargs.pop('time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        