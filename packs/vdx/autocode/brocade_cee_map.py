#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_cee_map(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def cee_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name = ET.SubElement(cee_map, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_precedence(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        precedence = ET.SubElement(cee_map, "precedence")
        if kwargs.pop('delete_precedence', False) is True:
            delete_precedence = config.find('.//*precedence')
            delete_precedence.set('operation', 'delete')
            
        precedence.text = kwargs.pop('precedence')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_PGID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        if kwargs.pop('delete_priority_group_table', False) is True:
            delete_priority_group_table = config.find('.//*priority-group-table')
            delete_priority_group_table.set('operation', 'delete')
            
        PGID = ET.SubElement(priority_group_table, "PGID")
        if kwargs.pop('delete_PGID', False) is True:
            delete_PGID = config.find('.//*PGID')
            delete_PGID.set('operation', 'delete')
            
        PGID.text = kwargs.pop('PGID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_weight(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        if kwargs.pop('delete_priority_group_table', False) is True:
            delete_priority_group_table = config.find('.//*priority-group-table')
            delete_priority_group_table.set('operation', 'delete')
            
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        if kwargs.pop('delete_PGID', False) is True:
            delete_PGID = config.find('.//*PGID')
            delete_PGID.set('operation', 'delete')
                
        weight = ET.SubElement(priority_group_table, "weight")
        if kwargs.pop('delete_weight', False) is True:
            delete_weight = config.find('.//*weight')
            delete_weight.set('operation', 'delete')
            
        weight.text = kwargs.pop('weight')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_pfc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        if kwargs.pop('delete_priority_group_table', False) is True:
            delete_priority_group_table = config.find('.//*priority-group-table')
            delete_priority_group_table.set('operation', 'delete')
            
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        if kwargs.pop('delete_PGID', False) is True:
            delete_PGID = config.find('.//*PGID')
            delete_PGID.set('operation', 'delete')
                
        pfc = ET.SubElement(priority_group_table, "pfc")
        if kwargs.pop('delete_pfc', False) is True:
            delete_pfc = config.find('.//*pfc')
            delete_pfc.set('operation', 'delete')
            
        pfc.text = kwargs.pop('pfc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos0_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos0_pgid = ET.SubElement(priority_table, "map-cos0-pgid")
        if kwargs.pop('delete_map_cos0_pgid', False) is True:
            delete_map_cos0_pgid = config.find('.//*map-cos0-pgid')
            delete_map_cos0_pgid.set('operation', 'delete')
            
        map_cos0_pgid.text = kwargs.pop('map_cos0_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos1_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos1_pgid = ET.SubElement(priority_table, "map-cos1-pgid")
        if kwargs.pop('delete_map_cos1_pgid', False) is True:
            delete_map_cos1_pgid = config.find('.//*map-cos1-pgid')
            delete_map_cos1_pgid.set('operation', 'delete')
            
        map_cos1_pgid.text = kwargs.pop('map_cos1_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos2_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos2_pgid = ET.SubElement(priority_table, "map-cos2-pgid")
        if kwargs.pop('delete_map_cos2_pgid', False) is True:
            delete_map_cos2_pgid = config.find('.//*map-cos2-pgid')
            delete_map_cos2_pgid.set('operation', 'delete')
            
        map_cos2_pgid.text = kwargs.pop('map_cos2_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos3_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos3_pgid = ET.SubElement(priority_table, "map-cos3-pgid")
        if kwargs.pop('delete_map_cos3_pgid', False) is True:
            delete_map_cos3_pgid = config.find('.//*map-cos3-pgid')
            delete_map_cos3_pgid.set('operation', 'delete')
            
        map_cos3_pgid.text = kwargs.pop('map_cos3_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos4_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos4_pgid = ET.SubElement(priority_table, "map-cos4-pgid")
        if kwargs.pop('delete_map_cos4_pgid', False) is True:
            delete_map_cos4_pgid = config.find('.//*map-cos4-pgid')
            delete_map_cos4_pgid.set('operation', 'delete')
            
        map_cos4_pgid.text = kwargs.pop('map_cos4_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos5_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos5_pgid = ET.SubElement(priority_table, "map-cos5-pgid")
        if kwargs.pop('delete_map_cos5_pgid', False) is True:
            delete_map_cos5_pgid = config.find('.//*map-cos5-pgid')
            delete_map_cos5_pgid.set('operation', 'delete')
            
        map_cos5_pgid.text = kwargs.pop('map_cos5_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos6_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos6_pgid = ET.SubElement(priority_table, "map-cos6-pgid")
        if kwargs.pop('delete_map_cos6_pgid', False) is True:
            delete_map_cos6_pgid = config.find('.//*map-cos6-pgid')
            delete_map_cos6_pgid.set('operation', 'delete')
            
        map_cos6_pgid.text = kwargs.pop('map_cos6_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos7_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        priority_table = ET.SubElement(cee_map, "priority-table")
        if kwargs.pop('delete_priority_table', False) is True:
            delete_priority_table = config.find('.//*priority-table')
            delete_priority_table.set('operation', 'delete')
            
        map_cos7_pgid = ET.SubElement(priority_table, "map-cos7-pgid")
        if kwargs.pop('delete_map_cos7_pgid', False) is True:
            delete_map_cos7_pgid = config.find('.//*map-cos7-pgid')
            delete_map_cos7_pgid.set('operation', 'delete')
            
        map_cos7_pgid.text = kwargs.pop('map_cos7_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_fabric_priority_fabric_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        remap = ET.SubElement(cee_map, "remap")
        if kwargs.pop('delete_remap', False) is True:
            delete_remap = config.find('.//*remap')
            delete_remap.set('operation', 'delete')
            
        fabric_priority = ET.SubElement(remap, "fabric-priority")
        if kwargs.pop('delete_fabric_priority', False) is True:
            delete_fabric_priority = config.find('.//*fabric-priority')
            delete_fabric_priority.set('operation', 'delete')
            
        fabric_remapped_priority = ET.SubElement(fabric_priority, "fabric-remapped-priority")
        if kwargs.pop('delete_fabric_remapped_priority', False) is True:
            delete_fabric_remapped_priority = config.find('.//*fabric-remapped-priority')
            delete_fabric_remapped_priority.set('operation', 'delete')
            
        fabric_remapped_priority.text = kwargs.pop('fabric_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_lossless_priority_lossless_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        if kwargs.pop('delete_cee_map', False) is True:
            delete_cee_map = config.find('.//*cee-map')
            delete_cee_map.set('operation', 'delete')
            
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        remap = ET.SubElement(cee_map, "remap")
        if kwargs.pop('delete_remap', False) is True:
            delete_remap = config.find('.//*remap')
            delete_remap.set('operation', 'delete')
            
        lossless_priority = ET.SubElement(remap, "lossless-priority")
        if kwargs.pop('delete_lossless_priority', False) is True:
            delete_lossless_priority = config.find('.//*lossless-priority')
            delete_lossless_priority.set('operation', 'delete')
            
        lossless_remapped_priority = ET.SubElement(lossless_priority, "lossless-remapped-priority")
        if kwargs.pop('delete_lossless_remapped_priority', False) is True:
            delete_lossless_remapped_priority = config.find('.//*lossless-remapped-priority')
            delete_lossless_remapped_priority.set('operation', 'delete')
            
        lossless_remapped_priority.text = kwargs.pop('lossless_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        