#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_qos(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def qos_map_dscp_mutation_dscp_mutation_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        if kwargs.pop('delete_dscp_mutation', False) is True:
            delete_dscp_mutation = config.find('.//*dscp-mutation')
            delete_dscp_mutation.set('operation', 'delete')
            
        dscp_mutation_map_name = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        if kwargs.pop('delete_dscp_mutation_map_name', False) is True:
            delete_dscp_mutation_map_name = config.find('.//*dscp-mutation-map-name')
            delete_dscp_mutation_map_name.set('operation', 'delete')
            
        dscp_mutation_map_name.text = kwargs.pop('dscp_mutation_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        if kwargs.pop('delete_dscp_mutation', False) is True:
            delete_dscp_mutation = config.find('.//*dscp-mutation')
            delete_dscp_mutation.set('operation', 'delete')
            
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        if kwargs.pop('delete_dscp_mutation_map_name', False) is True:
            delete_dscp_mutation_map_name = config.find('.//*dscp-mutation-map-name')
            delete_dscp_mutation_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_mutation, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
            
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        if kwargs.pop('delete_dscp_mutation', False) is True:
            delete_dscp_mutation = config.find('.//*dscp-mutation')
            delete_dscp_mutation.set('operation', 'delete')
            
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        if kwargs.pop('delete_dscp_mutation_map_name', False) is True:
            delete_dscp_mutation_map_name = config.find('.//*dscp-mutation-map-name')
            delete_dscp_mutation_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_mutation, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
                
        to = ET.SubElement(mark, "to")
        if kwargs.pop('delete_to', False) is True:
            delete_to = config.find('.//*to')
            delete_to.set('operation', 'delete')
            
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_dscp_traffic_class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        if kwargs.pop('delete_dscp_traffic_class', False) is True:
            delete_dscp_traffic_class = config.find('.//*dscp-traffic-class')
            delete_dscp_traffic_class.set('operation', 'delete')
            
        dscp_traffic_class_map_name = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        if kwargs.pop('delete_dscp_traffic_class_map_name', False) is True:
            delete_dscp_traffic_class_map_name = config.find('.//*dscp-traffic-class-map-name')
            delete_dscp_traffic_class_map_name.set('operation', 'delete')
            
        dscp_traffic_class_map_name.text = kwargs.pop('dscp_traffic_class_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        if kwargs.pop('delete_dscp_traffic_class', False) is True:
            delete_dscp_traffic_class = config.find('.//*dscp-traffic-class')
            delete_dscp_traffic_class.set('operation', 'delete')
            
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        if kwargs.pop('delete_dscp_traffic_class_map_name', False) is True:
            delete_dscp_traffic_class_map_name = config.find('.//*dscp-traffic-class-map-name')
            delete_dscp_traffic_class_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_traffic_class, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
            
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        if kwargs.pop('delete_dscp_traffic_class', False) is True:
            delete_dscp_traffic_class = config.find('.//*dscp-traffic-class')
            delete_dscp_traffic_class.set('operation', 'delete')
            
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        if kwargs.pop('delete_dscp_traffic_class_map_name', False) is True:
            delete_dscp_traffic_class_map_name = config.find('.//*dscp-traffic-class-map-name')
            delete_dscp_traffic_class_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_traffic_class, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
                
        to = ET.SubElement(mark, "to")
        if kwargs.pop('delete_to', False) is True:
            delete_to = config.find('.//*to')
            delete_to.set('operation', 'delete')
            
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_dscp_cos_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_cos = ET.SubElement(map, "dscp-cos")
        if kwargs.pop('delete_dscp_cos', False) is True:
            delete_dscp_cos = config.find('.//*dscp-cos')
            delete_dscp_cos.set('operation', 'delete')
            
        dscp_cos_map_name = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        if kwargs.pop('delete_dscp_cos_map_name', False) is True:
            delete_dscp_cos_map_name = config.find('.//*dscp-cos-map-name')
            delete_dscp_cos_map_name.set('operation', 'delete')
            
        dscp_cos_map_name.text = kwargs.pop('dscp_cos_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_cos = ET.SubElement(map, "dscp-cos")
        if kwargs.pop('delete_dscp_cos', False) is True:
            delete_dscp_cos = config.find('.//*dscp-cos')
            delete_dscp_cos.set('operation', 'delete')
            
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        if kwargs.pop('delete_dscp_cos_map_name', False) is True:
            delete_dscp_cos_map_name = config.find('.//*dscp-cos-map-name')
            delete_dscp_cos_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_cos, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
            
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_cos = ET.SubElement(map, "dscp-cos")
        if kwargs.pop('delete_dscp_cos', False) is True:
            delete_dscp_cos = config.find('.//*dscp-cos')
            delete_dscp_cos.set('operation', 'delete')
            
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        if kwargs.pop('delete_dscp_cos_map_name', False) is True:
            delete_dscp_cos_map_name = config.find('.//*dscp-cos-map-name')
            delete_dscp_cos_map_name.set('operation', 'delete')
                
        mark = ET.SubElement(dscp_cos, "mark")
        if kwargs.pop('delete_mark', False) is True:
            delete_mark = config.find('.//*mark')
            delete_mark.set('operation', 'delete')
            
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        if kwargs.pop('delete_dscp_in_values', False) is True:
            delete_dscp_in_values = config.find('.//*dscp-in-values')
            delete_dscp_in_values.set('operation', 'delete')
                
        to = ET.SubElement(mark, "to")
        if kwargs.pop('delete_to', False) is True:
            delete_to = config.find('.//*to')
            delete_to.set('operation', 'delete')
            
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name = ET.SubElement(cos_mutation, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos0 = ET.SubElement(cos_mutation, "cos0")
        if kwargs.pop('delete_cos0', False) is True:
            delete_cos0 = config.find('.//*cos0')
            delete_cos0.set('operation', 'delete')
            
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos1 = ET.SubElement(cos_mutation, "cos1")
        if kwargs.pop('delete_cos1', False) is True:
            delete_cos1 = config.find('.//*cos1')
            delete_cos1.set('operation', 'delete')
            
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos2 = ET.SubElement(cos_mutation, "cos2")
        if kwargs.pop('delete_cos2', False) is True:
            delete_cos2 = config.find('.//*cos2')
            delete_cos2.set('operation', 'delete')
            
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos3 = ET.SubElement(cos_mutation, "cos3")
        if kwargs.pop('delete_cos3', False) is True:
            delete_cos3 = config.find('.//*cos3')
            delete_cos3.set('operation', 'delete')
            
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos4 = ET.SubElement(cos_mutation, "cos4")
        if kwargs.pop('delete_cos4', False) is True:
            delete_cos4 = config.find('.//*cos4')
            delete_cos4.set('operation', 'delete')
            
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos5 = ET.SubElement(cos_mutation, "cos5")
        if kwargs.pop('delete_cos5', False) is True:
            delete_cos5 = config.find('.//*cos5')
            delete_cos5.set('operation', 'delete')
            
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos6 = ET.SubElement(cos_mutation, "cos6")
        if kwargs.pop('delete_cos6', False) is True:
            delete_cos6 = config.find('.//*cos6')
            delete_cos6.set('operation', 'delete')
            
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos7 = ET.SubElement(cos_mutation, "cos7")
        if kwargs.pop('delete_cos7', False) is True:
            delete_cos7 = config.find('.//*cos7')
            delete_cos7.set('operation', 'delete')
            
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name = ET.SubElement(cos_traffic_class, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos0 = ET.SubElement(cos_traffic_class, "cos0")
        if kwargs.pop('delete_cos0', False) is True:
            delete_cos0 = config.find('.//*cos0')
            delete_cos0.set('operation', 'delete')
            
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos1 = ET.SubElement(cos_traffic_class, "cos1")
        if kwargs.pop('delete_cos1', False) is True:
            delete_cos1 = config.find('.//*cos1')
            delete_cos1.set('operation', 'delete')
            
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos2 = ET.SubElement(cos_traffic_class, "cos2")
        if kwargs.pop('delete_cos2', False) is True:
            delete_cos2 = config.find('.//*cos2')
            delete_cos2.set('operation', 'delete')
            
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos3 = ET.SubElement(cos_traffic_class, "cos3")
        if kwargs.pop('delete_cos3', False) is True:
            delete_cos3 = config.find('.//*cos3')
            delete_cos3.set('operation', 'delete')
            
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos4 = ET.SubElement(cos_traffic_class, "cos4")
        if kwargs.pop('delete_cos4', False) is True:
            delete_cos4 = config.find('.//*cos4')
            delete_cos4.set('operation', 'delete')
            
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos5 = ET.SubElement(cos_traffic_class, "cos5")
        if kwargs.pop('delete_cos5', False) is True:
            delete_cos5 = config.find('.//*cos5')
            delete_cos5.set('operation', 'delete')
            
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos6 = ET.SubElement(cos_traffic_class, "cos6")
        if kwargs.pop('delete_cos6', False) is True:
            delete_cos6 = config.find('.//*cos6')
            delete_cos6.set('operation', 'delete')
            
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        map = ET.SubElement(qos, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cos7 = ET.SubElement(cos_traffic_class, "cos7")
        if kwargs.pop('delete_cos7', False) is True:
            delete_cos7 = config.find('.//*cos7')
            delete_cos7.set('operation', 'delete')
            
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_profile_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        red_profile = ET.SubElement(qos, "red-profile")
        if kwargs.pop('delete_red_profile', False) is True:
            delete_red_profile = config.find('.//*red-profile')
            delete_red_profile.set('operation', 'delete')
            
        profile_id = ET.SubElement(red_profile, "profile-id")
        if kwargs.pop('delete_profile_id', False) is True:
            delete_profile_id = config.find('.//*profile-id')
            delete_profile_id.set('operation', 'delete')
            
        profile_id.text = kwargs.pop('profile_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_min_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        red_profile = ET.SubElement(qos, "red-profile")
        if kwargs.pop('delete_red_profile', False) is True:
            delete_red_profile = config.find('.//*red-profile')
            delete_red_profile.set('operation', 'delete')
            
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        if kwargs.pop('delete_profile_id', False) is True:
            delete_profile_id = config.find('.//*profile-id')
            delete_profile_id.set('operation', 'delete')
                
        min_threshold = ET.SubElement(red_profile, "min-threshold")
        if kwargs.pop('delete_min_threshold', False) is True:
            delete_min_threshold = config.find('.//*min-threshold')
            delete_min_threshold.set('operation', 'delete')
            
        min_threshold.text = kwargs.pop('min_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_max_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        red_profile = ET.SubElement(qos, "red-profile")
        if kwargs.pop('delete_red_profile', False) is True:
            delete_red_profile = config.find('.//*red-profile')
            delete_red_profile.set('operation', 'delete')
            
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        if kwargs.pop('delete_profile_id', False) is True:
            delete_profile_id = config.find('.//*profile-id')
            delete_profile_id.set('operation', 'delete')
                
        max_threshold = ET.SubElement(red_profile, "max-threshold")
        if kwargs.pop('delete_max_threshold', False) is True:
            delete_max_threshold = config.find('.//*max-threshold')
            delete_max_threshold.set('operation', 'delete')
            
        max_threshold.text = kwargs.pop('max_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_drop_probability(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        red_profile = ET.SubElement(qos, "red-profile")
        if kwargs.pop('delete_red_profile', False) is True:
            delete_red_profile = config.find('.//*red-profile')
            delete_red_profile.set('operation', 'delete')
            
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        if kwargs.pop('delete_profile_id', False) is True:
            delete_profile_id = config.find('.//*profile-id')
            delete_profile_id.set('operation', 'delete')
                
        drop_probability = ET.SubElement(red_profile, "drop-probability")
        if kwargs.pop('delete_drop_probability', False) is True:
            delete_drop_probability = config.find('.//*drop-probability')
            delete_drop_probability.set('operation', 'delete')
            
        drop_probability.text = kwargs.pop('drop_probability')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class0 = ET.SubElement(dwrr, "dwrr-traffic-class0")
        if kwargs.pop('delete_dwrr_traffic_class0', False) is True:
            delete_dwrr_traffic_class0 = config.find('.//*dwrr-traffic-class0')
            delete_dwrr_traffic_class0.set('operation', 'delete')
            
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class1 = ET.SubElement(dwrr, "dwrr-traffic-class1")
        if kwargs.pop('delete_dwrr_traffic_class1', False) is True:
            delete_dwrr_traffic_class1 = config.find('.//*dwrr-traffic-class1')
            delete_dwrr_traffic_class1.set('operation', 'delete')
            
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class2 = ET.SubElement(dwrr, "dwrr-traffic-class2")
        if kwargs.pop('delete_dwrr_traffic_class2', False) is True:
            delete_dwrr_traffic_class2 = config.find('.//*dwrr-traffic-class2')
            delete_dwrr_traffic_class2.set('operation', 'delete')
            
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class3 = ET.SubElement(dwrr, "dwrr-traffic-class3")
        if kwargs.pop('delete_dwrr_traffic_class3', False) is True:
            delete_dwrr_traffic_class3 = config.find('.//*dwrr-traffic-class3')
            delete_dwrr_traffic_class3.set('operation', 'delete')
            
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class4 = ET.SubElement(dwrr, "dwrr-traffic-class4")
        if kwargs.pop('delete_dwrr_traffic_class4', False) is True:
            delete_dwrr_traffic_class4 = config.find('.//*dwrr-traffic-class4')
            delete_dwrr_traffic_class4.set('operation', 'delete')
            
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class5 = ET.SubElement(dwrr, "dwrr-traffic-class5")
        if kwargs.pop('delete_dwrr_traffic_class5', False) is True:
            delete_dwrr_traffic_class5 = config.find('.//*dwrr-traffic-class5')
            delete_dwrr_traffic_class5.set('operation', 'delete')
            
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class6 = ET.SubElement(dwrr, "dwrr-traffic-class6")
        if kwargs.pop('delete_dwrr_traffic_class6', False) is True:
            delete_dwrr_traffic_class6 = config.find('.//*dwrr-traffic-class6')
            delete_dwrr_traffic_class6.set('operation', 'delete')
            
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        scheduler = ET.SubElement(multicast, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        dwrr = ET.SubElement(scheduler, "dwrr")
        if kwargs.pop('delete_dwrr', False) is True:
            delete_dwrr = config.find('.//*dwrr')
            delete_dwrr.set('operation', 'delete')
            
        dwrr_traffic_class7 = ET.SubElement(dwrr, "dwrr-traffic-class7")
        if kwargs.pop('delete_dwrr_traffic_class7', False) is True:
            delete_dwrr_traffic_class7 = config.find('.//*dwrr-traffic-class7')
            delete_dwrr_traffic_class7.set('operation', 'delete')
            
        dwrr_traffic_class7.text = kwargs.pop('dwrr_traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        priority_number = ET.SubElement(strict_priority, "priority-number")
        if kwargs.pop('delete_priority_number', False) is True:
            delete_priority_number = config.find('.//*priority-number')
            delete_priority_number.set('operation', 'delete')
            
        priority_number.text = kwargs.pop('priority_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        scheduler_type = ET.SubElement(strict_priority, "scheduler-type")
        if kwargs.pop('delete_scheduler_type', False) is True:
            delete_scheduler_type = config.find('.//*scheduler-type')
            delete_scheduler_type.set('operation', 'delete')
            
        scheduler_type.text = kwargs.pop('scheduler_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class0 = ET.SubElement(strict_priority, "dwrr-traffic-class0")
        if kwargs.pop('delete_dwrr_traffic_class0', False) is True:
            delete_dwrr_traffic_class0 = config.find('.//*dwrr-traffic-class0')
            delete_dwrr_traffic_class0.set('operation', 'delete')
            
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class1 = ET.SubElement(strict_priority, "dwrr-traffic-class1")
        if kwargs.pop('delete_dwrr_traffic_class1', False) is True:
            delete_dwrr_traffic_class1 = config.find('.//*dwrr-traffic-class1')
            delete_dwrr_traffic_class1.set('operation', 'delete')
            
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class2 = ET.SubElement(strict_priority, "dwrr-traffic-class2")
        if kwargs.pop('delete_dwrr_traffic_class2', False) is True:
            delete_dwrr_traffic_class2 = config.find('.//*dwrr-traffic-class2')
            delete_dwrr_traffic_class2.set('operation', 'delete')
            
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class3 = ET.SubElement(strict_priority, "dwrr-traffic-class3")
        if kwargs.pop('delete_dwrr_traffic_class3', False) is True:
            delete_dwrr_traffic_class3 = config.find('.//*dwrr-traffic-class3')
            delete_dwrr_traffic_class3.set('operation', 'delete')
            
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class4 = ET.SubElement(strict_priority, "dwrr-traffic-class4")
        if kwargs.pop('delete_dwrr_traffic_class4', False) is True:
            delete_dwrr_traffic_class4 = config.find('.//*dwrr-traffic-class4')
            delete_dwrr_traffic_class4.set('operation', 'delete')
            
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class5 = ET.SubElement(strict_priority, "dwrr-traffic-class5")
        if kwargs.pop('delete_dwrr_traffic_class5', False) is True:
            delete_dwrr_traffic_class5 = config.find('.//*dwrr-traffic-class5')
            delete_dwrr_traffic_class5.set('operation', 'delete')
            
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class6 = ET.SubElement(strict_priority, "dwrr-traffic-class6")
        if kwargs.pop('delete_dwrr_traffic_class6', False) is True:
            delete_dwrr_traffic_class6 = config.find('.//*dwrr-traffic-class6')
            delete_dwrr_traffic_class6.set('operation', 'delete')
            
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        queue = ET.SubElement(qos, "queue")
        if kwargs.pop('delete_queue', False) is True:
            delete_queue = config.find('.//*queue')
            delete_queue.set('operation', 'delete')
            
        scheduler = ET.SubElement(queue, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        dwrr_traffic_class_last = ET.SubElement(strict_priority, "dwrr-traffic-class-last")
        if kwargs.pop('delete_dwrr_traffic_class_last', False) is True:
            delete_dwrr_traffic_class_last = config.find('.//*dwrr-traffic-class-last')
            delete_dwrr_traffic_class_last.set('operation', 'delete')
            
        dwrr_traffic_class_last.text = kwargs.pop('dwrr_traffic_class_last')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class0 = ET.SubElement(threshold, "traffic-class0")
        if kwargs.pop('delete_traffic_class0', False) is True:
            delete_traffic_class0 = config.find('.//*traffic-class0')
            delete_traffic_class0.set('operation', 'delete')
            
        traffic_class0.text = kwargs.pop('traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class1 = ET.SubElement(threshold, "traffic-class1")
        if kwargs.pop('delete_traffic_class1', False) is True:
            delete_traffic_class1 = config.find('.//*traffic-class1')
            delete_traffic_class1.set('operation', 'delete')
            
        traffic_class1.text = kwargs.pop('traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class2 = ET.SubElement(threshold, "traffic-class2")
        if kwargs.pop('delete_traffic_class2', False) is True:
            delete_traffic_class2 = config.find('.//*traffic-class2')
            delete_traffic_class2.set('operation', 'delete')
            
        traffic_class2.text = kwargs.pop('traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class3 = ET.SubElement(threshold, "traffic-class3")
        if kwargs.pop('delete_traffic_class3', False) is True:
            delete_traffic_class3 = config.find('.//*traffic-class3')
            delete_traffic_class3.set('operation', 'delete')
            
        traffic_class3.text = kwargs.pop('traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class4 = ET.SubElement(threshold, "traffic-class4")
        if kwargs.pop('delete_traffic_class4', False) is True:
            delete_traffic_class4 = config.find('.//*traffic-class4')
            delete_traffic_class4.set('operation', 'delete')
            
        traffic_class4.text = kwargs.pop('traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class5 = ET.SubElement(threshold, "traffic-class5")
        if kwargs.pop('delete_traffic_class5', False) is True:
            delete_traffic_class5 = config.find('.//*traffic-class5')
            delete_traffic_class5.set('operation', 'delete')
            
        traffic_class5.text = kwargs.pop('traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class6 = ET.SubElement(threshold, "traffic-class6")
        if kwargs.pop('delete_traffic_class6', False) is True:
            delete_traffic_class6 = config.find('.//*traffic-class6')
            delete_traffic_class6.set('operation', 'delete')
            
        traffic_class6.text = kwargs.pop('traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        threshold = ET.SubElement(multicast, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        traffic_class7 = ET.SubElement(threshold, "traffic-class7")
        if kwargs.pop('delete_traffic_class7', False) is True:
            delete_traffic_class7 = config.find('.//*traffic-class7')
            delete_traffic_class7.set('operation', 'delete')
            
        traffic_class7.text = kwargs.pop('traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        rate_limit = ET.SubElement(multicast, "rate-limit")
        if kwargs.pop('delete_rate_limit', False) is True:
            delete_rate_limit = config.find('.//*rate-limit')
            delete_rate_limit.set('operation', 'delete')
            
        limit = ET.SubElement(rate_limit, "limit")
        if kwargs.pop('delete_limit', False) is True:
            delete_limit = config.find('.//*limit')
            delete_limit.set('operation', 'delete')
            
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_burst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        if kwargs.pop('delete_rcv_queue', False) is True:
            delete_rcv_queue = config.find('.//*rcv-queue')
            delete_rcv_queue.set('operation', 'delete')
            
        multicast = ET.SubElement(rcv_queue, "multicast")
        if kwargs.pop('delete_multicast', False) is True:
            delete_multicast = config.find('.//*multicast')
            delete_multicast.set('operation', 'delete')
            
        rate_limit = ET.SubElement(multicast, "rate-limit")
        if kwargs.pop('delete_rate_limit', False) is True:
            delete_rate_limit = config.find('.//*rate-limit')
            delete_rate_limit.set('operation', 'delete')
            
        burst = ET.SubElement(rate_limit, "burst")
        if kwargs.pop('delete_burst', False) is True:
            delete_burst = config.find('.//*burst')
            delete_burst.set('operation', 'delete')
            
        burst.text = kwargs.pop('burst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_nas', False) is True:
            delete_nas = config.find('.//*nas')
            delete_nas.set('operation', 'delete')
            
        auto_qos = ET.SubElement(nas, "auto-qos")
        if kwargs.pop('delete_auto_qos', False) is True:
            delete_auto_qos = config.find('.//*auto-qos')
            delete_auto_qos.set('operation', 'delete')
            
        set = ET.SubElement(auto_qos, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        cos = ET.SubElement(set, "cos")
        if kwargs.pop('delete_cos', False) is True:
            delete_cos = config.find('.//*cos')
            delete_cos.set('operation', 'delete')
            
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_nas', False) is True:
            delete_nas = config.find('.//*nas')
            delete_nas.set('operation', 'delete')
            
        auto_qos = ET.SubElement(nas, "auto-qos")
        if kwargs.pop('delete_auto_qos', False) is True:
            delete_auto_qos = config.find('.//*auto-qos')
            delete_auto_qos.set('operation', 'delete')
            
        set = ET.SubElement(auto_qos, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        dscp = ET.SubElement(set, "dscp")
        if kwargs.pop('delete_dscp', False) is True:
            delete_dscp = config.find('.//*dscp')
            delete_dscp.set('operation', 'delete')
            
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_nas', False) is True:
            delete_nas = config.find('.//*nas')
            delete_nas.set('operation', 'delete')
            
        server_ip = ET.SubElement(nas, "server-ip")
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
            
        server_ip = ET.SubElement(server_ip, "server-ip")
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
            
        server_ip.text = kwargs.pop('server_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vrf_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_nas', False) is True:
            delete_nas = config.find('.//*nas')
            delete_nas.set('operation', 'delete')
            
        server_ip = ET.SubElement(nas, "server-ip")
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
            
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
                
        vrf = ET.SubElement(server_ip, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        vrf_name = ET.SubElement(vrf, "vrf-name")
        if kwargs.pop('delete_vrf_name', False) is True:
            delete_vrf_name = config.find('.//*vrf-name')
            delete_vrf_name.set('operation', 'delete')
            
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vlan_vlan_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        if kwargs.pop('delete_nas', False) is True:
            delete_nas = config.find('.//*nas')
            delete_nas.set('operation', 'delete')
            
        server_ip = ET.SubElement(nas, "server-ip")
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
            
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        if kwargs.pop('delete_server_ip', False) is True:
            delete_server_ip = config.find('.//*server-ip')
            delete_server_ip.set('operation', 'delete')
                
        vlan = ET.SubElement(server_ip, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_number = ET.SubElement(vlan, "vlan-number")
        if kwargs.pop('delete_vlan_number', False) is True:
            delete_vlan_number = config.find('.//*vlan-number')
            delete_vlan_number.set('operation', 'delete')
            
        vlan_number.text = kwargs.pop('vlan_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        