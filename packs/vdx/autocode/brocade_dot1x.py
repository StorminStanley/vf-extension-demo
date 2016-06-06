#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_dot1x(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def dot1x_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        if kwargs.pop('delete_dot1x', False) is True:
            delete_dot1x = config.find('.//*dot1x')
            delete_dot1x.set('operation', 'delete')
            
        enable = ET.SubElement(dot1x, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dot1x_test_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        if kwargs.pop('delete_dot1x', False) is True:
            delete_dot1x = config.find('.//*dot1x')
            delete_dot1x.set('operation', 'delete')
            
        test = ET.SubElement(dot1x, "test")
        if kwargs.pop('delete_test', False) is True:
            delete_test = config.find('.//*test')
            delete_test.set('operation', 'delete')
            
        timeout = ET.SubElement(test, "timeout")
        if kwargs.pop('delete_timeout', False) is True:
            delete_timeout = config.find('.//*timeout')
            delete_timeout.set('operation', 'delete')
            
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        