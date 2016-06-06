#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_license(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def dpod_port_id_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        if kwargs.pop('delete_dpod', False) is True:
            delete_dpod = config.find('.//*dpod')
            delete_dpod.set('operation', 'delete')
            
        port_id = ET.SubElement(dpod, "port-id")
        if kwargs.pop('delete_port_id', False) is True:
            delete_port_id = config.find('.//*port-id')
            delete_port_id.set('operation', 'delete')
            
        port_id = ET.SubElement(port_id, "port-id")
        if kwargs.pop('delete_port_id', False) is True:
            delete_port_id = config.find('.//*port-id')
            delete_port_id.set('operation', 'delete')
            
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dpod_port_id_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        if kwargs.pop('delete_dpod', False) is True:
            delete_dpod = config.find('.//*dpod')
            delete_dpod.set('operation', 'delete')
            
        port_id = ET.SubElement(dpod, "port-id")
        if kwargs.pop('delete_port_id', False) is True:
            delete_port_id = config.find('.//*port-id')
            delete_port_id.set('operation', 'delete')
            
        port_id_key = ET.SubElement(port_id, "port-id")
        port_id_key.text = kwargs.pop('port_id')
        if kwargs.pop('delete_port_id', False) is True:
            delete_port_id = config.find('.//*port-id')
            delete_port_id.set('operation', 'delete')
                
        operation = ET.SubElement(port_id, "operation")
        if kwargs.pop('delete_operation', False) is True:
            delete_operation = config.find('.//*operation')
            delete_operation.set('operation', 'delete')
            
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        