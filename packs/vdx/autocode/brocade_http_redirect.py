#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_http_redirect(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def set_http_application_url_input_config_http_app_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        if kwargs.pop('delete_set_http_application_url', False) is True:
            delete_set_http_application_url = config.find('.//*set-http-application-url')
            delete_set_http_application_url.set('operation', 'delete')
            
        input = ET.SubElement(set_http_application_url, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        if kwargs.pop('delete_config_http_app_url', False) is True:
            delete_config_http_app_url = config.find('.//*config-http-app-url')
            delete_config_http_app_url.set('operation', 'delete')
            
        url = ET.SubElement(config_http_app_url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_input_config_http_app_url_op_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        if kwargs.pop('delete_set_http_application_url', False) is True:
            delete_set_http_application_url = config.find('.//*set-http-application-url')
            delete_set_http_application_url.set('operation', 'delete')
            
        input = ET.SubElement(set_http_application_url, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        if kwargs.pop('delete_config_http_app_url', False) is True:
            delete_config_http_app_url = config.find('.//*config-http-app-url')
            delete_config_http_app_url.set('operation', 'delete')
            
        op_type = ET.SubElement(config_http_app_url, "op-type")
        if kwargs.pop('delete_op_type', False) is True:
            delete_op_type = config.find('.//*op-type')
            delete_op_type.set('operation', 'delete')
            
        op_type.text = kwargs.pop('op_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        if kwargs.pop('delete_set_http_application_url', False) is True:
            delete_set_http_application_url = config.find('.//*set-http-application-url')
            delete_set_http_application_url.set('operation', 'delete')
            
        output = ET.SubElement(set_http_application_url, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status_code = ET.SubElement(output, "status-code")
        if kwargs.pop('delete_status_code', False) is True:
            delete_status_code = config.find('.//*status-code')
            delete_status_code.set('operation', 'delete')
            
        status_code.text = kwargs.pop('status_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        if kwargs.pop('delete_set_http_application_url', False) is True:
            delete_set_http_application_url = config.find('.//*set-http-application-url')
            delete_set_http_application_url.set('operation', 'delete')
            
        output = ET.SubElement(set_http_application_url, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status_string = ET.SubElement(output, "status-string")
        if kwargs.pop('delete_status_string', False) is True:
            delete_status_string = config.find('.//*status-string')
            delete_status_string.set('operation', 'delete')
            
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        