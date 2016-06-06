#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_openflow(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def openflow_controller_controller_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        openflow_controller = ET.SubElement(config, "openflow-controller", xmlns="urn:brocade.com:mgmt:brocade-openflow")
        if kwargs.pop('delete_openflow_controller', False) is True:
            delete_openflow_controller = config.find('.//*openflow-controller')
            delete_openflow_controller.set('operation', 'delete')
            
        controller_name = ET.SubElement(openflow_controller, "controller-name")
        if kwargs.pop('delete_controller_name', False) is True:
            delete_controller_name = config.find('.//*controller-name')
            delete_controller_name.set('operation', 'delete')
            
        controller_name.text = kwargs.pop('controller_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def openflow_controller_connection_address_controller_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        openflow_controller = ET.SubElement(config, "openflow-controller", xmlns="urn:brocade.com:mgmt:brocade-openflow")
        if kwargs.pop('delete_openflow_controller', False) is True:
            delete_openflow_controller = config.find('.//*openflow-controller')
            delete_openflow_controller.set('operation', 'delete')
            
        controller_name_key = ET.SubElement(openflow_controller, "controller-name")
        controller_name_key.text = kwargs.pop('controller_name')
        if kwargs.pop('delete_controller_name', False) is True:
            delete_controller_name = config.find('.//*controller-name')
            delete_controller_name.set('operation', 'delete')
                
        connection_address = ET.SubElement(openflow_controller, "connection-address")
        if kwargs.pop('delete_connection_address', False) is True:
            delete_connection_address = config.find('.//*connection-address')
            delete_connection_address.set('operation', 'delete')
            
        controller_address = ET.SubElement(connection_address, "controller-address")
        if kwargs.pop('delete_controller_address', False) is True:
            delete_controller_address = config.find('.//*controller-address')
            delete_controller_address.set('operation', 'delete')
            
        controller_address.text = kwargs.pop('controller_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def openflow_controller_connection_address_connection_method(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        openflow_controller = ET.SubElement(config, "openflow-controller", xmlns="urn:brocade.com:mgmt:brocade-openflow")
        if kwargs.pop('delete_openflow_controller', False) is True:
            delete_openflow_controller = config.find('.//*openflow-controller')
            delete_openflow_controller.set('operation', 'delete')
            
        controller_name_key = ET.SubElement(openflow_controller, "controller-name")
        controller_name_key.text = kwargs.pop('controller_name')
        if kwargs.pop('delete_controller_name', False) is True:
            delete_controller_name = config.find('.//*controller-name')
            delete_controller_name.set('operation', 'delete')
                
        connection_address = ET.SubElement(openflow_controller, "connection-address")
        if kwargs.pop('delete_connection_address', False) is True:
            delete_connection_address = config.find('.//*connection-address')
            delete_connection_address.set('operation', 'delete')
            
        connection_method = ET.SubElement(connection_address, "connection-method")
        if kwargs.pop('delete_connection_method', False) is True:
            delete_connection_method = config.find('.//*connection-method')
            delete_connection_method.set('operation', 'delete')
            
        connection_method.text = kwargs.pop('connection_method')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def openflow_controller_connection_address_connection_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        openflow_controller = ET.SubElement(config, "openflow-controller", xmlns="urn:brocade.com:mgmt:brocade-openflow")
        if kwargs.pop('delete_openflow_controller', False) is True:
            delete_openflow_controller = config.find('.//*openflow-controller')
            delete_openflow_controller.set('operation', 'delete')
            
        controller_name_key = ET.SubElement(openflow_controller, "controller-name")
        controller_name_key.text = kwargs.pop('controller_name')
        if kwargs.pop('delete_controller_name', False) is True:
            delete_controller_name = config.find('.//*controller-name')
            delete_controller_name.set('operation', 'delete')
                
        connection_address = ET.SubElement(openflow_controller, "connection-address")
        if kwargs.pop('delete_connection_address', False) is True:
            delete_connection_address = config.find('.//*connection-address')
            delete_connection_address.set('operation', 'delete')
            
        connection_port = ET.SubElement(connection_address, "connection-port")
        if kwargs.pop('delete_connection_port', False) is True:
            delete_connection_port = config.find('.//*connection-port')
            delete_connection_port.set('operation', 'delete')
            
        connection_port.text = kwargs.pop('connection_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def openflow_controller_connection_address_active_controller_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        openflow_controller = ET.SubElement(config, "openflow-controller", xmlns="urn:brocade.com:mgmt:brocade-openflow")
        if kwargs.pop('delete_openflow_controller', False) is True:
            delete_openflow_controller = config.find('.//*openflow-controller')
            delete_openflow_controller.set('operation', 'delete')
            
        controller_name_key = ET.SubElement(openflow_controller, "controller-name")
        controller_name_key.text = kwargs.pop('controller_name')
        if kwargs.pop('delete_controller_name', False) is True:
            delete_controller_name = config.find('.//*controller-name')
            delete_controller_name.set('operation', 'delete')
                
        connection_address = ET.SubElement(openflow_controller, "connection-address")
        if kwargs.pop('delete_connection_address', False) is True:
            delete_connection_address = config.find('.//*connection-address')
            delete_connection_address.set('operation', 'delete')
            
        active_controller_vrf = ET.SubElement(connection_address, "active-controller-vrf")
        if kwargs.pop('delete_active_controller_vrf', False) is True:
            delete_active_controller_vrf = config.find('.//*active-controller-vrf')
            delete_active_controller_vrf.set('operation', 'delete')
            
        active_controller_vrf.text = kwargs.pop('active_controller_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        