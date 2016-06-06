#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_policer(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def police_priority_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name = ET.SubElement(police_priority_map, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri0_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri0_conform = ET.SubElement(conform, "map-pri0-conform")
        if kwargs.pop('delete_map_pri0_conform', False) is True:
            delete_map_pri0_conform = config.find('.//*map-pri0-conform')
            delete_map_pri0_conform.set('operation', 'delete')
            
        map_pri0_conform.text = kwargs.pop('map_pri0_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri1_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri1_conform = ET.SubElement(conform, "map-pri1-conform")
        if kwargs.pop('delete_map_pri1_conform', False) is True:
            delete_map_pri1_conform = config.find('.//*map-pri1-conform')
            delete_map_pri1_conform.set('operation', 'delete')
            
        map_pri1_conform.text = kwargs.pop('map_pri1_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri2_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri2_conform = ET.SubElement(conform, "map-pri2-conform")
        if kwargs.pop('delete_map_pri2_conform', False) is True:
            delete_map_pri2_conform = config.find('.//*map-pri2-conform')
            delete_map_pri2_conform.set('operation', 'delete')
            
        map_pri2_conform.text = kwargs.pop('map_pri2_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri3_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri3_conform = ET.SubElement(conform, "map-pri3-conform")
        if kwargs.pop('delete_map_pri3_conform', False) is True:
            delete_map_pri3_conform = config.find('.//*map-pri3-conform')
            delete_map_pri3_conform.set('operation', 'delete')
            
        map_pri3_conform.text = kwargs.pop('map_pri3_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri4_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri4_conform = ET.SubElement(conform, "map-pri4-conform")
        if kwargs.pop('delete_map_pri4_conform', False) is True:
            delete_map_pri4_conform = config.find('.//*map-pri4-conform')
            delete_map_pri4_conform.set('operation', 'delete')
            
        map_pri4_conform.text = kwargs.pop('map_pri4_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri5_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri5_conform = ET.SubElement(conform, "map-pri5-conform")
        if kwargs.pop('delete_map_pri5_conform', False) is True:
            delete_map_pri5_conform = config.find('.//*map-pri5-conform')
            delete_map_pri5_conform.set('operation', 'delete')
            
        map_pri5_conform.text = kwargs.pop('map_pri5_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri6_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri6_conform = ET.SubElement(conform, "map-pri6-conform")
        if kwargs.pop('delete_map_pri6_conform', False) is True:
            delete_map_pri6_conform = config.find('.//*map-pri6-conform')
            delete_map_pri6_conform.set('operation', 'delete')
            
        map_pri6_conform.text = kwargs.pop('map_pri6_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri7_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        conform = ET.SubElement(police_priority_map, "conform")
        if kwargs.pop('delete_conform', False) is True:
            delete_conform = config.find('.//*conform')
            delete_conform.set('operation', 'delete')
            
        map_pri7_conform = ET.SubElement(conform, "map-pri7-conform")
        if kwargs.pop('delete_map_pri7_conform', False) is True:
            delete_map_pri7_conform = config.find('.//*map-pri7-conform')
            delete_map_pri7_conform.set('operation', 'delete')
            
        map_pri7_conform.text = kwargs.pop('map_pri7_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri0_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri0_exceed = ET.SubElement(exceed, "map-pri0-exceed")
        if kwargs.pop('delete_map_pri0_exceed', False) is True:
            delete_map_pri0_exceed = config.find('.//*map-pri0-exceed')
            delete_map_pri0_exceed.set('operation', 'delete')
            
        map_pri0_exceed.text = kwargs.pop('map_pri0_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri1_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri1_exceed = ET.SubElement(exceed, "map-pri1-exceed")
        if kwargs.pop('delete_map_pri1_exceed', False) is True:
            delete_map_pri1_exceed = config.find('.//*map-pri1-exceed')
            delete_map_pri1_exceed.set('operation', 'delete')
            
        map_pri1_exceed.text = kwargs.pop('map_pri1_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri2_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri2_exceed = ET.SubElement(exceed, "map-pri2-exceed")
        if kwargs.pop('delete_map_pri2_exceed', False) is True:
            delete_map_pri2_exceed = config.find('.//*map-pri2-exceed')
            delete_map_pri2_exceed.set('operation', 'delete')
            
        map_pri2_exceed.text = kwargs.pop('map_pri2_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri3_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri3_exceed = ET.SubElement(exceed, "map-pri3-exceed")
        if kwargs.pop('delete_map_pri3_exceed', False) is True:
            delete_map_pri3_exceed = config.find('.//*map-pri3-exceed')
            delete_map_pri3_exceed.set('operation', 'delete')
            
        map_pri3_exceed.text = kwargs.pop('map_pri3_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri4_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri4_exceed = ET.SubElement(exceed, "map-pri4-exceed")
        if kwargs.pop('delete_map_pri4_exceed', False) is True:
            delete_map_pri4_exceed = config.find('.//*map-pri4-exceed')
            delete_map_pri4_exceed.set('operation', 'delete')
            
        map_pri4_exceed.text = kwargs.pop('map_pri4_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri5_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri5_exceed = ET.SubElement(exceed, "map-pri5-exceed")
        if kwargs.pop('delete_map_pri5_exceed', False) is True:
            delete_map_pri5_exceed = config.find('.//*map-pri5-exceed')
            delete_map_pri5_exceed.set('operation', 'delete')
            
        map_pri5_exceed.text = kwargs.pop('map_pri5_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri6_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri6_exceed = ET.SubElement(exceed, "map-pri6-exceed")
        if kwargs.pop('delete_map_pri6_exceed', False) is True:
            delete_map_pri6_exceed = config.find('.//*map-pri6-exceed')
            delete_map_pri6_exceed.set('operation', 'delete')
            
        map_pri6_exceed.text = kwargs.pop('map_pri6_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri7_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_police_priority_map', False) is True:
            delete_police_priority_map = config.find('.//*police-priority-map')
            delete_police_priority_map.set('operation', 'delete')
            
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exceed = ET.SubElement(police_priority_map, "exceed")
        if kwargs.pop('delete_exceed', False) is True:
            delete_exceed = config.find('.//*exceed')
            delete_exceed.set('operation', 'delete')
            
        map_pri7_exceed = ET.SubElement(exceed, "map-pri7-exceed")
        if kwargs.pop('delete_map_pri7_exceed', False) is True:
            delete_map_pri7_exceed = config.find('.//*map-pri7-exceed')
            delete_map_pri7_exceed.set('operation', 'delete')
            
        map_pri7_exceed.text = kwargs.pop('map_pri7_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_class_map', False) is True:
            delete_class_map = config.find('.//*class-map')
            delete_class_map.set('operation', 'delete')
            
        name = ET.SubElement(class_map, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_match_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_class_map', False) is True:
            delete_class_map = config.find('.//*class-map')
            delete_class_map.set('operation', 'delete')
            
        name_key = ET.SubElement(class_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        match = ET.SubElement(class_map, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        access_group = ET.SubElement(match, "access-group")
        if kwargs.pop('delete_access_group', False) is True:
            delete_access_group = config.find('.//*access-group')
            delete_access_group.set('operation', 'delete')
            
        access_group_name = ET.SubElement(access_group, "access-group-name")
        if kwargs.pop('delete_access_group_name', False) is True:
            delete_access_group_name = config.find('.//*access-group-name')
            delete_access_group_name.set('operation', 'delete')
            
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_po_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name = ET.SubElement(policy_map, "po-name")
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
            
        po_name.text = kwargs.pop('po_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_cl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name = ET.SubElement(class, "cl-name")
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
            
        cl_name.text = kwargs.pop('cl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        cir = ET.SubElement(police, "cir")
        if kwargs.pop('delete_cir', False) is True:
            delete_cir = config.find('.//*cir')
            delete_cir.set('operation', 'delete')
            
        cir.text = kwargs.pop('cir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cbs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        cbs = ET.SubElement(police, "cbs")
        if kwargs.pop('delete_cbs', False) is True:
            delete_cbs = config.find('.//*cbs')
            delete_cbs.set('operation', 'delete')
            
        cbs.text = kwargs.pop('cbs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_eir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        eir = ET.SubElement(police, "eir")
        if kwargs.pop('delete_eir', False) is True:
            delete_eir = config.find('.//*eir')
            delete_eir.set('operation', 'delete')
            
        eir.text = kwargs.pop('eir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_ebs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        ebs = ET.SubElement(police, "ebs")
        if kwargs.pop('delete_ebs', False) is True:
            delete_ebs = config.find('.//*ebs')
            delete_ebs.set('operation', 'delete')
            
        ebs.text = kwargs.pop('ebs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_set_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        set_priority = ET.SubElement(police, "set-priority")
        if kwargs.pop('delete_set_priority', False) is True:
            delete_set_priority = config.find('.//*set-priority')
            delete_set_priority.set('operation', 'delete')
            
        set_priority.text = kwargs.pop('set_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        conform_set_dscp = ET.SubElement(police, "conform-set-dscp")
        if kwargs.pop('delete_conform_set_dscp', False) is True:
            delete_conform_set_dscp = config.find('.//*conform-set-dscp')
            delete_conform_set_dscp.set('operation', 'delete')
            
        conform_set_dscp.text = kwargs.pop('conform_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        conform_set_prec = ET.SubElement(police, "conform-set-prec")
        if kwargs.pop('delete_conform_set_prec', False) is True:
            delete_conform_set_prec = config.find('.//*conform-set-prec')
            delete_conform_set_prec.set('operation', 'delete')
            
        conform_set_prec.text = kwargs.pop('conform_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        conform_set_tc = ET.SubElement(police, "conform-set-tc")
        if kwargs.pop('delete_conform_set_tc', False) is True:
            delete_conform_set_tc = config.find('.//*conform-set-tc')
            delete_conform_set_tc.set('operation', 'delete')
            
        conform_set_tc.text = kwargs.pop('conform_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        exceed_set_dscp = ET.SubElement(police, "exceed-set-dscp")
        if kwargs.pop('delete_exceed_set_dscp', False) is True:
            delete_exceed_set_dscp = config.find('.//*exceed-set-dscp')
            delete_exceed_set_dscp.set('operation', 'delete')
            
        exceed_set_dscp.text = kwargs.pop('exceed_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        exceed_set_prec = ET.SubElement(police, "exceed-set-prec")
        if kwargs.pop('delete_exceed_set_prec', False) is True:
            delete_exceed_set_prec = config.find('.//*exceed-set-prec')
            delete_exceed_set_prec.set('operation', 'delete')
            
        exceed_set_prec.text = kwargs.pop('exceed_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        police = ET.SubElement(class, "police")
        if kwargs.pop('delete_police', False) is True:
            delete_police = config.find('.//*police')
            delete_police.set('operation', 'delete')
            
        exceed_set_tc = ET.SubElement(police, "exceed-set-tc")
        if kwargs.pop('delete_exceed_set_tc', False) is True:
            delete_exceed_set_tc = config.find('.//*exceed-set-tc')
            delete_exceed_set_tc.set('operation', 'delete')
            
        exceed_set_tc.text = kwargs.pop('exceed_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        set = ET.SubElement(class, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        if kwargs.pop('delete_set_cos_tc', False) is True:
            delete_set_cos_tc = config.find('.//*set_cos_tc')
            delete_set_cos_tc.set('operation', 'delete')
            
        cos = ET.SubElement(set_cos_tc, "cos")
        if kwargs.pop('delete_cos', False) is True:
            delete_cos = config.find('.//*cos')
            delete_cos.set('operation', 'delete')
            
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        set = ET.SubElement(class, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        if kwargs.pop('delete_set_cos_tc', False) is True:
            delete_set_cos_tc = config.find('.//*set_cos_tc')
            delete_set_cos_tc.set('operation', 'delete')
            
        traffic_class = ET.SubElement(set_cos_tc, "traffic-class")
        if kwargs.pop('delete_traffic_class', False) is True:
            delete_traffic_class = config.find('.//*traffic-class')
            delete_traffic_class.set('operation', 'delete')
            
        traffic_class.text = kwargs.pop('traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_dscp_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        set = ET.SubElement(class, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        set_dscp = ET.SubElement(set, "set_dscp")
        if kwargs.pop('delete_set_dscp', False) is True:
            delete_set_dscp = config.find('.//*set_dscp')
            delete_set_dscp.set('operation', 'delete')
            
        dscp = ET.SubElement(set_dscp, "dscp")
        if kwargs.pop('delete_dscp', False) is True:
            delete_dscp = config.find('.//*dscp')
            delete_dscp.set('operation', 'delete')
            
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_span_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        span = ET.SubElement(class, "span")
        if kwargs.pop('delete_span', False) is True:
            delete_span = config.find('.//*span')
            delete_span.set('operation', 'delete')
            
        session = ET.SubElement(span, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_mutation = ET.SubElement(map, "cos-mutation")
        if kwargs.pop('delete_cos_mutation', False) is True:
            delete_cos_mutation = config.find('.//*cos-mutation')
            delete_cos_mutation.set('operation', 'delete')
            
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        if kwargs.pop('delete_cos_traffic_class', False) is True:
            delete_cos_traffic_class = config.find('.//*cos-traffic-class')
            delete_cos_traffic_class.set('operation', 'delete')
            
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_cos = ET.SubElement(map, "dscp-cos")
        if kwargs.pop('delete_dscp_cos', False) is True:
            delete_dscp_cos = config.find('.//*dscp-cos')
            delete_dscp_cos.set('operation', 'delete')
            
        dscp_cos.text = kwargs.pop('dscp_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        if kwargs.pop('delete_dscp_traffic_class', False) is True:
            delete_dscp_traffic_class = config.find('.//*dscp-traffic-class')
            delete_dscp_traffic_class.set('operation', 'delete')
            
        dscp_traffic_class.text = kwargs.pop('dscp_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        if kwargs.pop('delete_dscp_mutation', False) is True:
            delete_dscp_mutation = config.find('.//*dscp-mutation')
            delete_dscp_mutation.set('operation', 'delete')
            
        dscp_mutation.text = kwargs.pop('dscp_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_sflow(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        map = ET.SubElement(class, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        sflow = ET.SubElement(map, "sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sflow.text = kwargs.pop('sflow')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_shape_shaping_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        shape = ET.SubElement(class, "shape")
        if kwargs.pop('delete_shape', False) is True:
            delete_shape = config.find('.//*shape')
            delete_shape.set('operation', 'delete')
            
        shaping_rate = ET.SubElement(shape, "shaping_rate")
        if kwargs.pop('delete_shaping_rate', False) is True:
            delete_shaping_rate = config.find('.//*shaping_rate')
            delete_shaping_rate.set('operation', 'delete')
            
        shaping_rate.text = kwargs.pop('shaping_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
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
        
    def policy_map_class_scheduler_strict_priority_TC1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC1 = ET.SubElement(strict_priority, "TC1")
        if kwargs.pop('delete_TC1', False) is True:
            delete_TC1 = config.find('.//*TC1')
            delete_TC1.set('operation', 'delete')
            
        TC1.text = kwargs.pop('TC1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC2 = ET.SubElement(strict_priority, "TC2")
        if kwargs.pop('delete_TC2', False) is True:
            delete_TC2 = config.find('.//*TC2')
            delete_TC2.set('operation', 'delete')
            
        TC2.text = kwargs.pop('TC2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC3 = ET.SubElement(strict_priority, "TC3")
        if kwargs.pop('delete_TC3', False) is True:
            delete_TC3 = config.find('.//*TC3')
            delete_TC3.set('operation', 'delete')
            
        TC3.text = kwargs.pop('TC3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC4 = ET.SubElement(strict_priority, "TC4")
        if kwargs.pop('delete_TC4', False) is True:
            delete_TC4 = config.find('.//*TC4')
            delete_TC4.set('operation', 'delete')
            
        TC4.text = kwargs.pop('TC4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC5 = ET.SubElement(strict_priority, "TC5")
        if kwargs.pop('delete_TC5', False) is True:
            delete_TC5 = config.find('.//*TC5')
            delete_TC5.set('operation', 'delete')
            
        TC5.text = kwargs.pop('TC5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC6 = ET.SubElement(strict_priority, "TC6")
        if kwargs.pop('delete_TC6', False) is True:
            delete_TC6 = config.find('.//*TC6')
            delete_TC6.set('operation', 'delete')
            
        TC6.text = kwargs.pop('TC6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        scheduler = ET.SubElement(class, "scheduler")
        if kwargs.pop('delete_scheduler', False) is True:
            delete_scheduler = config.find('.//*scheduler')
            delete_scheduler.set('operation', 'delete')
            
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        if kwargs.pop('delete_strict_priority', False) is True:
            delete_strict_priority = config.find('.//*strict-priority')
            delete_strict_priority.set('operation', 'delete')
            
        TC7 = ET.SubElement(strict_priority, "TC7")
        if kwargs.pop('delete_TC7', False) is True:
            delete_TC7 = config.find('.//*TC7')
            delete_TC7.set('operation', 'delete')
            
        TC7.text = kwargs.pop('TC7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_priority_mapping_table_imprt_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_policy_map', False) is True:
            delete_policy_map = config.find('.//*policy-map')
            delete_policy_map.set('operation', 'delete')
            
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        if kwargs.pop('delete_po_name', False) is True:
            delete_po_name = config.find('.//*po-name')
            delete_po_name.set('operation', 'delete')
                
        class = ET.SubElement(policy_map, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        cl_name_key = ET.SubElement(class, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        if kwargs.pop('delete_cl_name', False) is True:
            delete_cl_name = config.find('.//*cl-name')
            delete_cl_name.set('operation', 'delete')
                
        priority_mapping_table = ET.SubElement(class, "priority-mapping-table")
        if kwargs.pop('delete_priority_mapping_table', False) is True:
            delete_priority_mapping_table = config.find('.//*priority-mapping-table')
            delete_priority_mapping_table.set('operation', 'delete')
            
        imprt = ET.SubElement(priority_mapping_table, "import")
        if kwargs.pop('delete_imprt', False) is True:
            delete_imprt = config.find('.//*import')
            delete_imprt.set('operation', 'delete')
            
        cee = ET.SubElement(imprt, "cee")
        if kwargs.pop('delete_cee', False) is True:
            delete_cee = config.find('.//*cee')
            delete_cee.set('operation', 'delete')
            
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_system_qos', False) is True:
            delete_system_qos = config.find('.//*system-qos')
            delete_system_qos.set('operation', 'delete')
            
        qos = ET.SubElement(system_qos, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        service_policy = ET.SubElement(qos, "service-policy")
        if kwargs.pop('delete_service_policy', False) is True:
            delete_service_policy = config.find('.//*service-policy')
            delete_service_policy.set('operation', 'delete')
            
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        if kwargs.pop('delete_policy_map_name', False) is True:
            delete_policy_map_name = config.find('.//*policy-map-name')
            delete_policy_map_name.set('operation', 'delete')
                
        direction = ET.SubElement(service_policy, "direction")
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
            
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_policy_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_system_qos', False) is True:
            delete_system_qos = config.find('.//*system-qos')
            delete_system_qos.set('operation', 'delete')
            
        qos = ET.SubElement(system_qos, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        service_policy = ET.SubElement(qos, "service-policy")
        if kwargs.pop('delete_service_policy', False) is True:
            delete_service_policy = config.find('.//*service-policy')
            delete_service_policy.set('operation', 'delete')
            
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
                
        policy_map_name = ET.SubElement(service_policy, "policy-map-name")
        if kwargs.pop('delete_policy_map_name', False) is True:
            delete_policy_map_name = config.find('.//*policy-map-name')
            delete_policy_map_name.set('operation', 'delete')
            
        policy_map_name.text = kwargs.pop('policy_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_add_rb_add_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_system_qos', False) is True:
            delete_system_qos = config.find('.//*system-qos')
            delete_system_qos.set('operation', 'delete')
            
        qos = ET.SubElement(system_qos, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        service_policy = ET.SubElement(qos, "service-policy")
        if kwargs.pop('delete_service_policy', False) is True:
            delete_service_policy = config.find('.//*service-policy')
            delete_service_policy.set('operation', 'delete')
            
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
                
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        if kwargs.pop('delete_policy_map_name', False) is True:
            delete_policy_map_name = config.find('.//*policy-map-name')
            delete_policy_map_name.set('operation', 'delete')
                
        attach = ET.SubElement(service_policy, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        add = ET.SubElement(rbridge_id, "add")
        if kwargs.pop('delete_add', False) is True:
            delete_add = config.find('.//*add')
            delete_add.set('operation', 'delete')
            
        rb_add_range = ET.SubElement(add, "rb-add-range")
        if kwargs.pop('delete_rb_add_range', False) is True:
            delete_rb_add_range = config.find('.//*rb-add-range')
            delete_rb_add_range.set('operation', 'delete')
            
        rb_add_range.text = kwargs.pop('rb_add_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_remove_rb_remove_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        if kwargs.pop('delete_system_qos', False) is True:
            delete_system_qos = config.find('.//*system-qos')
            delete_system_qos.set('operation', 'delete')
            
        qos = ET.SubElement(system_qos, "qos")
        if kwargs.pop('delete_qos', False) is True:
            delete_qos = config.find('.//*qos')
            delete_qos.set('operation', 'delete')
            
        service_policy = ET.SubElement(qos, "service-policy")
        if kwargs.pop('delete_service_policy', False) is True:
            delete_service_policy = config.find('.//*service-policy')
            delete_service_policy.set('operation', 'delete')
            
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
                
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        if kwargs.pop('delete_policy_map_name', False) is True:
            delete_policy_map_name = config.find('.//*policy-map-name')
            delete_policy_map_name.set('operation', 'delete')
                
        attach = ET.SubElement(service_policy, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        remove = ET.SubElement(rbridge_id, "remove")
        if kwargs.pop('delete_remove', False) is True:
            delete_remove = config.find('.//*remove')
            delete_remove.set('operation', 'delete')
            
        rb_remove_range = ET.SubElement(remove, "rb-remove-range")
        if kwargs.pop('delete_rb_remove_range', False) is True:
            delete_rb_remove_range = config.find('.//*rb-remove-range')
            delete_rb_remove_range.set('operation', 'delete')
            
        rb_remove_range.text = kwargs.pop('rb_remove_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        