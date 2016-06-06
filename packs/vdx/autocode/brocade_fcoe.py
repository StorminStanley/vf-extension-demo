#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fcoe(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcoe_fsb_fcoe_fsb_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_fsb = ET.SubElement(config, "fcoe-fsb", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe_fsb', False) is True:
            delete_fcoe_fsb = config.find('.//*fcoe-fsb')
            delete_fcoe_fsb.set('operation', 'delete')
            
        fcoe_fsb_enable = ET.SubElement(fcoe_fsb, "fcoe-fsb-enable")
        if kwargs.pop('delete_fcoe_fsb_enable', False) is True:
            delete_fcoe_fsb_enable = config.find('.//*fcoe-fsb-enable')
            delete_fcoe_fsb_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
            
        fcoe_fabric_map_name.text = kwargs.pop('fcoe_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fabric_map_vlan = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-vlan")
        if kwargs.pop('delete_fcoe_fabric_map_vlan', False) is True:
            delete_fcoe_fabric_map_vlan = config.find('.//*fcoe-fabric-map-vlan')
            delete_fcoe_fabric_map_vlan.set('operation', 'delete')
            
        fcoe_fabric_map_vlan.text = kwargs.pop('fcoe_fabric_map_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fabric_mode = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-mode")
        if kwargs.pop('delete_fcoe_fabric_mode', False) is True:
            delete_fcoe_fabric_mode = config.find('.//*fcoe-fabric-mode')
            delete_fcoe_fabric_mode.set('operation', 'delete')
            
        fcoe_fabric_mode.text = kwargs.pop('fcoe_fabric_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fabric_map_priority = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-priority")
        if kwargs.pop('delete_fcoe_fabric_map_priority', False) is True:
            delete_fcoe_fabric_map_priority = config.find('.//*fcoe-fabric-map-priority')
            delete_fcoe_fabric_map_priority.set('operation', 'delete')
            
        fcoe_fabric_map_priority.text = kwargs.pop('fcoe_fabric_map_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_virtual_fabric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fabric_map_virtual_fabric = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-virtual-fabric")
        if kwargs.pop('delete_fcoe_fabric_map_virtual_fabric', False) is True:
            delete_fcoe_fabric_map_virtual_fabric = config.find('.//*fcoe-fabric-map-virtual-fabric')
            delete_fcoe_fabric_map_virtual_fabric.set('operation', 'delete')
            
        fcoe_fabric_map_virtual_fabric.text = kwargs.pop('fcoe_fabric_map_virtual_fabric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_fcmap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fabric_map_fcmap = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-fcmap")
        if kwargs.pop('delete_fcoe_fabric_map_fcmap', False) is True:
            delete_fcoe_fabric_map_fcmap = config.find('.//*fcoe-fabric-map-fcmap')
            delete_fcoe_fabric_map_fcmap.set('operation', 'delete')
            
        fcoe_fabric_map_fcmap.text = kwargs.pop('fcoe_fabric_map_fcmap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_advertisement_fcoe_fip_advertisement_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fip_advertisement = ET.SubElement(fcoe_fabric_map, "fcoe-fip-advertisement")
        if kwargs.pop('delete_fcoe_fip_advertisement', False) is True:
            delete_fcoe_fip_advertisement = config.find('.//*fcoe-fip-advertisement')
            delete_fcoe_fip_advertisement.set('operation', 'delete')
            
        fcoe_fip_advertisement_interval = ET.SubElement(fcoe_fip_advertisement, "fcoe-fip-advertisement-interval")
        if kwargs.pop('delete_fcoe_fip_advertisement_interval', False) is True:
            delete_fcoe_fip_advertisement_interval = config.find('.//*fcoe-fip-advertisement-interval')
            delete_fcoe_fip_advertisement_interval.set('operation', 'delete')
            
        fcoe_fip_advertisement_interval.text = kwargs.pop('fcoe_fip_advertisement_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_keep_alive_fcoe_fip_keep_alive_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fip_keep_alive = ET.SubElement(fcoe_fabric_map, "fcoe-fip-keep-alive")
        if kwargs.pop('delete_fcoe_fip_keep_alive', False) is True:
            delete_fcoe_fip_keep_alive = config.find('.//*fcoe-fip-keep-alive')
            delete_fcoe_fip_keep_alive.set('operation', 'delete')
            
        fcoe_fip_keep_alive_timeout = ET.SubElement(fcoe_fip_keep_alive, "fcoe-fip-keep-alive-timeout")
        if kwargs.pop('delete_fcoe_fip_keep_alive_timeout', False) is True:
            delete_fcoe_fip_keep_alive_timeout = config.find('.//*fcoe-fip-keep-alive-timeout')
            delete_fcoe_fip_keep_alive_timeout.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        if kwargs.pop('delete_fcoe_fcf_map', False) is True:
            delete_fcoe_fcf_map = config.find('.//*fcoe-fcf-map')
            delete_fcoe_fcf_map.set('operation', 'delete')
            
        fcf_map_name = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        if kwargs.pop('delete_fcf_map_name', False) is True:
            delete_fcf_map_name = config.find('.//*fcf-map-name')
            delete_fcf_map_name.set('operation', 'delete')
            
        fcf_map_name.text = kwargs.pop('fcf_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fcf_rbid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        if kwargs.pop('delete_fcoe_fcf_map', False) is True:
            delete_fcoe_fcf_map = config.find('.//*fcoe-fcf-map')
            delete_fcoe_fcf_map.set('operation', 'delete')
            
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        if kwargs.pop('delete_fcf_map_name', False) is True:
            delete_fcf_map_name = config.find('.//*fcf-map-name')
            delete_fcf_map_name.set('operation', 'delete')
                
        fcf_map_fcf_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fcf-rbid")
        if kwargs.pop('delete_fcf_map_fcf_rbid', False) is True:
            delete_fcf_map_fcf_rbid = config.find('.//*fcf-map-fcf-rbid')
            delete_fcf_map_fcf_rbid.set('operation', 'delete')
            
        fcf_map_fcf_rbid.text = kwargs.pop('fcf_map_fcf_rbid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        if kwargs.pop('delete_fcoe_fcf_map', False) is True:
            delete_fcoe_fcf_map = config.find('.//*fcoe-fcf-map')
            delete_fcoe_fcf_map.set('operation', 'delete')
            
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        if kwargs.pop('delete_fcf_map_name', False) is True:
            delete_fcf_map_name = config.find('.//*fcf-map-name')
            delete_fcf_map_name.set('operation', 'delete')
                
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        if kwargs.pop('delete_fcf_map_fif_rbid', False) is True:
            delete_fcf_map_fif_rbid = config.find('.//*fcf-map-fif-rbid')
            delete_fcf_map_fif_rbid.set('operation', 'delete')
            
        fcf_map_fif_rbid_add = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-add")
        if kwargs.pop('delete_fcf_map_fif_rbid_add', False) is True:
            delete_fcf_map_fif_rbid_add = config.find('.//*fcf-map-fif-rbid-add')
            delete_fcf_map_fif_rbid_add.set('operation', 'delete')
            
        fcf_map_fif_rbid_add.text = kwargs.pop('fcf_map_fif_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        if kwargs.pop('delete_fcoe_fcf_map', False) is True:
            delete_fcoe_fcf_map = config.find('.//*fcoe-fcf-map')
            delete_fcoe_fcf_map.set('operation', 'delete')
            
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        if kwargs.pop('delete_fcf_map_name', False) is True:
            delete_fcf_map_name = config.find('.//*fcf-map-name')
            delete_fcf_map_name.set('operation', 'delete')
                
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        if kwargs.pop('delete_fcf_map_fif_rbid', False) is True:
            delete_fcf_map_fif_rbid = config.find('.//*fcf-map-fif-rbid')
            delete_fcf_map_fif_rbid.set('operation', 'delete')
            
        fcf_map_fif_rbid_remove = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-remove")
        if kwargs.pop('delete_fcf_map_fif_rbid_remove', False) is True:
            delete_fcf_map_fif_rbid_remove = config.find('.//*fcf-map-fif-rbid-remove')
            delete_fcf_map_fif_rbid_remove.set('operation', 'delete')
            
        fcf_map_fif_rbid_remove.text = kwargs.pop('fcf_map_fif_rbid_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        if kwargs.pop('delete_fcoe_fcport_group_config', False) is True:
            delete_fcoe_fcport_group_config = config.find('.//*fcoe-fcport-group-config')
            delete_fcoe_fcport_group_config.set('operation', 'delete')
            
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        if kwargs.pop('delete_fcport_group_rbid', False) is True:
            delete_fcport_group_rbid = config.find('.//*fcport-group-rbid')
            delete_fcport_group_rbid.set('operation', 'delete')
            
        fcport_group_rbid_add = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-add")
        if kwargs.pop('delete_fcport_group_rbid_add', False) is True:
            delete_fcport_group_rbid_add = config.find('.//*fcport-group-rbid-add')
            delete_fcport_group_rbid_add.set('operation', 'delete')
            
        fcport_group_rbid_add.text = kwargs.pop('fcport_group_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        if kwargs.pop('delete_fcoe_fabric_map', False) is True:
            delete_fcoe_fabric_map = config.find('.//*fcoe-fabric-map')
            delete_fcoe_fabric_map.set('operation', 'delete')
            
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        if kwargs.pop('delete_fcoe_fabric_map_name', False) is True:
            delete_fcoe_fabric_map_name = config.find('.//*fcoe-fabric-map-name')
            delete_fcoe_fabric_map_name.set('operation', 'delete')
                
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        if kwargs.pop('delete_fcoe_fcport_group_config', False) is True:
            delete_fcoe_fcport_group_config = config.find('.//*fcoe-fcport-group-config')
            delete_fcoe_fcport_group_config.set('operation', 'delete')
            
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        if kwargs.pop('delete_fcport_group_rbid', False) is True:
            delete_fcport_group_rbid = config.find('.//*fcport-group-rbid')
            delete_fcport_group_rbid.set('operation', 'delete')
            
        fcport_group_rbid_remove = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-remove")
        if kwargs.pop('delete_fcport_group_rbid_remove', False) is True:
            delete_fcport_group_rbid_remove = config.find('.//*fcport-group-rbid-remove')
            delete_fcport_group_rbid_remove.set('operation', 'delete')
            
        fcport_group_rbid_remove.text = kwargs.pop('fcport_group_rbid_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        if kwargs.pop('delete_fcoe_map', False) is True:
            delete_fcoe_map = config.find('.//*fcoe-map')
            delete_fcoe_map.set('operation', 'delete')
            
        fcoe_map_name = ET.SubElement(fcoe_map, "fcoe-map-name")
        if kwargs.pop('delete_fcoe_map_name', False) is True:
            delete_fcoe_map_name = config.find('.//*fcoe-map-name')
            delete_fcoe_map_name.set('operation', 'delete')
            
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_cee_map_fcoe_map_cee_map_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        if kwargs.pop('delete_fcoe', False) is True:
            delete_fcoe = config.find('.//*fcoe')
            delete_fcoe.set('operation', 'delete')
            
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        if kwargs.pop('delete_fcoe_map', False) is True:
            delete_fcoe_map = config.find('.//*fcoe-map')
            delete_fcoe_map.set('operation', 'delete')
            
        fcoe_map_name_key = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name_key.text = kwargs.pop('fcoe_map_name')
        if kwargs.pop('delete_fcoe_map_name', False) is True:
            delete_fcoe_map_name = config.find('.//*fcoe-map-name')
            delete_fcoe_map_name.set('operation', 'delete')
                
        fcoe_map_cee_map = ET.SubElement(fcoe_map, "fcoe-map-cee-map")
        if kwargs.pop('delete_fcoe_map_cee_map', False) is True:
            delete_fcoe_map_cee_map = config.find('.//*fcoe-map-cee-map')
            delete_fcoe_map_cee_map.set('operation', 'delete')
            
        fcoe_map_cee_map_leaf = ET.SubElement(fcoe_map_cee_map, "fcoe-map-cee-map-leaf")
        if kwargs.pop('delete_fcoe_map_cee_map_leaf', False) is True:
            delete_fcoe_map_cee_map_leaf = config.find('.//*fcoe-map-cee-map-leaf')
            delete_fcoe_map_cee_map_leaf.set('operation', 'delete')
            
        fcoe_map_cee_map_leaf.text = kwargs.pop('fcoe_map_cee_map_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        