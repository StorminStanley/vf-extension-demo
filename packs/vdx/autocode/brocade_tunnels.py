#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_tunnels(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def nsx_controller_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name = ET.SubElement(nsx_controller, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        if kwargs.pop('delete_connection_addr', False) is True:
            delete_connection_addr = config.find('.//*connection-addr')
            delete_connection_addr.set('operation', 'delete')
            
        address = ET.SubElement(connection_addr, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        if kwargs.pop('delete_connection_addr', False) is True:
            delete_connection_addr = config.find('.//*connection-addr')
            delete_connection_addr.set('operation', 'delete')
            
        port = ET.SubElement(connection_addr, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_method(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        if kwargs.pop('delete_connection_addr', False) is True:
            delete_connection_addr = config.find('.//*connection-addr')
            delete_connection_addr.set('operation', 'delete')
            
        method = ET.SubElement(connection_addr, "method")
        if kwargs.pop('delete_method', False) is True:
            delete_method = config.find('.//*method')
            delete_method.set('operation', 'delete')
            
        method.text = kwargs.pop('method')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_reconnect_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        reconnect_interval = ET.SubElement(nsx_controller, "reconnect-interval")
        if kwargs.pop('delete_reconnect_interval', False) is True:
            delete_reconnect_interval = config.find('.//*reconnect-interval')
            delete_reconnect_interval.set('operation', 'delete')
            
        reconnect_interval.text = kwargs.pop('reconnect_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_nsx_controller', False) is True:
            delete_nsx_controller = config.find('.//*nsx-controller')
            delete_nsx_controller.set('operation', 'delete')
            
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        activate = ET.SubElement(nsx_controller, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name = ET.SubElement(overlay_gateway, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_gw_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        gw_type = ET.SubElement(overlay_gateway, "gw-type")
        if kwargs.pop('delete_gw_type', False) is True:
            delete_gw_type = config.find('.//*gw-type')
            delete_gw_type.set('operation', 'delete')
            
        gw_type.text = kwargs.pop('gw_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_ve_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        ip = ET.SubElement(overlay_gateway, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        interface = ET.SubElement(ip, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        ve = ET.SubElement(interface, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve_id = ET.SubElement(ve, "ve-id")
        if kwargs.pop('delete_ve_id', False) is True:
            delete_ve_id = config.find('.//*ve-id')
            delete_ve_id.set('operation', 'delete')
            
        ve_id.text = kwargs.pop('ve_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_vrrp_extended_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        ip = ET.SubElement(overlay_gateway, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        interface = ET.SubElement(ip, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        ve = ET.SubElement(interface, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        vrrp_extended_group = ET.SubElement(ve, "vrrp-extended-group")
        if kwargs.pop('delete_vrrp_extended_group', False) is True:
            delete_vrrp_extended_group = config.find('.//*vrrp-extended-group')
            delete_vrrp_extended_group.set('operation', 'delete')
            
        vrrp_extended_group.text = kwargs.pop('vrrp_extended_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_loopback_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        ip = ET.SubElement(overlay_gateway, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        interface = ET.SubElement(ip, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        loopback = ET.SubElement(interface, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        loopback_id = ET.SubElement(loopback, "loopback-id")
        if kwargs.pop('delete_loopback_id', False) is True:
            delete_loopback_id = config.find('.//*loopback-id')
            delete_loopback_id.set('operation', 'delete')
            
        loopback_id.text = kwargs.pop('loopback_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        attach = ET.SubElement(overlay_gateway, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rb_add = ET.SubElement(rbridge_id, "rb-add")
        if kwargs.pop('delete_rb_add', False) is True:
            delete_rb_add = config.find('.//*rb-add')
            delete_rb_add.set('operation', 'delete')
            
        rb_add.text = kwargs.pop('rb_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        attach = ET.SubElement(overlay_gateway, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rb_remove = ET.SubElement(rbridge_id, "rb-remove")
        if kwargs.pop('delete_rb_remove', False) is True:
            delete_rb_remove = config.find('.//*rb-remove')
            delete_rb_remove.set('operation', 'delete')
            
        rb_remove.text = kwargs.pop('rb_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        attach = ET.SubElement(overlay_gateway, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        vlan = ET.SubElement(attach, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        mac_key = ET.SubElement(vlan, "mac")
        mac_key.text = kwargs.pop('mac')
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
                
        vid = ET.SubElement(vlan, "vid")
        if kwargs.pop('delete_vid', False) is True:
            delete_vid = config.find('.//*vid')
            delete_vid.set('operation', 'delete')
            
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        attach = ET.SubElement(overlay_gateway, "attach")
        if kwargs.pop('delete_attach', False) is True:
            delete_attach = config.find('.//*attach')
            delete_attach.set('operation', 'delete')
            
        vlan = ET.SubElement(attach, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vid_key = ET.SubElement(vlan, "vid")
        vid_key.text = kwargs.pop('vid')
        if kwargs.pop('delete_vid', False) is True:
            delete_vid = config.find('.//*vid')
            delete_vid.set('operation', 'delete')
                
        mac = ET.SubElement(vlan, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        map = ET.SubElement(overlay_gateway, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        if kwargs.pop('delete_vlan_vni_mapping', False) is True:
            delete_vlan_vni_mapping = config.find('.//*vlan-vni-mapping')
            delete_vlan_vni_mapping.set('operation', 'delete')
            
        vid = ET.SubElement(vlan_vni_mapping, "vid")
        if kwargs.pop('delete_vid', False) is True:
            delete_vid = config.find('.//*vid')
            delete_vid.set('operation', 'delete')
            
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vni(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        map = ET.SubElement(overlay_gateway, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        if kwargs.pop('delete_vlan_vni_mapping', False) is True:
            delete_vlan_vni_mapping = config.find('.//*vlan-vni-mapping')
            delete_vlan_vni_mapping.set('operation', 'delete')
            
        vid_key = ET.SubElement(vlan_vni_mapping, "vid")
        vid_key.text = kwargs.pop('vid')
        if kwargs.pop('delete_vid', False) is True:
            delete_vid = config.find('.//*vid')
            delete_vid.set('operation', 'delete')
                
        vni = ET.SubElement(vlan_vni_mapping, "vni")
        if kwargs.pop('delete_vni', False) is True:
            delete_vni = config.find('.//*vni')
            delete_vni.set('operation', 'delete')
            
        vni.text = kwargs.pop('vni')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_auto(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        map = ET.SubElement(overlay_gateway, "map")
        if kwargs.pop('delete_map', False) is True:
            delete_map = config.find('.//*map')
            delete_map.set('operation', 'delete')
            
        vlan = ET.SubElement(map, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vni = ET.SubElement(vlan, "vni")
        if kwargs.pop('delete_vni', False) is True:
            delete_vni = config.find('.//*vni')
            delete_vni.set('operation', 'delete')
            
        auto = ET.SubElement(vni, "auto")
        if kwargs.pop('delete_auto', False) is True:
            delete_auto = config.find('.//*auto')
            delete_auto.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name = ET.SubElement(site, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_tunnel_dst_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        tunnel_dst = ET.SubElement(site, "tunnel-dst")
        if kwargs.pop('delete_tunnel_dst', False) is True:
            delete_tunnel_dst = config.find('.//*tunnel-dst')
            delete_tunnel_dst.set('operation', 'delete')
            
        address = ET.SubElement(tunnel_dst, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        extend = ET.SubElement(site, "extend")
        if kwargs.pop('delete_extend', False) is True:
            delete_extend = config.find('.//*extend')
            delete_extend.set('operation', 'delete')
            
        vlan = ET.SubElement(extend, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        add = ET.SubElement(vlan, "add")
        if kwargs.pop('delete_add', False) is True:
            delete_add = config.find('.//*add')
            delete_add.set('operation', 'delete')
            
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        extend = ET.SubElement(site, "extend")
        if kwargs.pop('delete_extend', False) is True:
            delete_extend = config.find('.//*extend')
            delete_extend.set('operation', 'delete')
            
        vlan = ET.SubElement(extend, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        remove = ET.SubElement(vlan, "remove")
        if kwargs.pop('delete_remove', False) is True:
            delete_remove = config.find('.//*remove')
            delete_remove.set('operation', 'delete')
            
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_mac_learning_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        mac_learning = ET.SubElement(site, "mac-learning")
        if kwargs.pop('delete_mac_learning', False) is True:
            delete_mac_learning = config.find('.//*mac-learning')
            delete_mac_learning.set('operation', 'delete')
            
        protocol = ET.SubElement(mac_learning, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd_enable = ET.SubElement(site, "bfd-enable")
        if kwargs.pop('delete_bfd_enable', False) is True:
            delete_bfd_enable = config.find('.//*bfd-enable')
            delete_bfd_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd = ET.SubElement(site, "bfd")
        if kwargs.pop('delete_bfd', False) is True:
            delete_bfd = config.find('.//*bfd')
            delete_bfd.set('operation', 'delete')
            
        params = ET.SubElement(bfd, "params")
        if kwargs.pop('delete_params', False) is True:
            delete_params = config.find('.//*params')
            delete_params.set('operation', 'delete')
            
        interval = ET.SubElement(params, "interval")
        if kwargs.pop('delete_interval', False) is True:
            delete_interval = config.find('.//*interval')
            delete_interval.set('operation', 'delete')
            
        min_tx = ET.SubElement(interval, "min-tx")
        if kwargs.pop('delete_min_tx', False) is True:
            delete_min_tx = config.find('.//*min-tx')
            delete_min_tx.set('operation', 'delete')
            
        min_tx.text = kwargs.pop('min_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd = ET.SubElement(site, "bfd")
        if kwargs.pop('delete_bfd', False) is True:
            delete_bfd = config.find('.//*bfd')
            delete_bfd.set('operation', 'delete')
            
        params = ET.SubElement(bfd, "params")
        if kwargs.pop('delete_params', False) is True:
            delete_params = config.find('.//*params')
            delete_params.set('operation', 'delete')
            
        interval = ET.SubElement(params, "interval")
        if kwargs.pop('delete_interval', False) is True:
            delete_interval = config.find('.//*interval')
            delete_interval.set('operation', 'delete')
            
        min_rx = ET.SubElement(interval, "min-rx")
        if kwargs.pop('delete_min_rx', False) is True:
            delete_min_rx = config.find('.//*min-rx')
            delete_min_rx.set('operation', 'delete')
            
        min_rx.text = kwargs.pop('min_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_multiplier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd = ET.SubElement(site, "bfd")
        if kwargs.pop('delete_bfd', False) is True:
            delete_bfd = config.find('.//*bfd')
            delete_bfd.set('operation', 'delete')
            
        params = ET.SubElement(bfd, "params")
        if kwargs.pop('delete_params', False) is True:
            delete_params = config.find('.//*params')
            delete_params.set('operation', 'delete')
            
        interval = ET.SubElement(params, "interval")
        if kwargs.pop('delete_interval', False) is True:
            delete_interval = config.find('.//*interval')
            delete_interval.set('operation', 'delete')
            
        multiplier = ET.SubElement(interval, "multiplier")
        if kwargs.pop('delete_multiplier', False) is True:
            delete_multiplier = config.find('.//*multiplier')
            delete_multiplier.set('operation', 'delete')
            
        multiplier.text = kwargs.pop('multiplier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_bfd_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        bfd = ET.SubElement(site, "bfd")
        if kwargs.pop('delete_bfd', False) is True:
            delete_bfd = config.find('.//*bfd')
            delete_bfd.set('operation', 'delete')
            
        params = ET.SubElement(bfd, "params")
        if kwargs.pop('delete_params', False) is True:
            delete_params = config.find('.//*params')
            delete_params.set('operation', 'delete')
            
        bfd_shutdown = ET.SubElement(params, "bfd-shutdown")
        if kwargs.pop('delete_bfd_shutdown', False) is True:
            delete_bfd_shutdown = config.find('.//*bfd-shutdown')
            delete_bfd_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        site = ET.SubElement(overlay_gateway, "site")
        if kwargs.pop('delete_site', False) is True:
            delete_site = config.find('.//*site')
            delete_site.set('operation', 'delete')
            
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        shutdown = ET.SubElement(site, "shutdown")
        if kwargs.pop('delete_shutdown', False) is True:
            delete_shutdown = config.find('.//*shutdown')
            delete_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_stats_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        enable = ET.SubElement(overlay_gateway, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            
        statistics = ET.SubElement(enable, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        stats_direction = ET.SubElement(statistics, "stats-direction")
        if kwargs.pop('delete_stats_direction', False) is True:
            delete_stats_direction = config.find('.//*stats-direction')
            delete_stats_direction.set('operation', 'delete')
            
        stats_direction.text = kwargs.pop('stats_direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        enable = ET.SubElement(overlay_gateway, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            
        statistics = ET.SubElement(enable, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        vlan_action = ET.SubElement(statistics, "vlan-action")
        if kwargs.pop('delete_vlan_action', False) is True:
            delete_vlan_action = config.find('.//*vlan-action')
            delete_vlan_action.set('operation', 'delete')
            
        vlan_action.text = kwargs.pop('vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_list(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        enable = ET.SubElement(overlay_gateway, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            
        statistics = ET.SubElement(enable, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        vlan_list = ET.SubElement(statistics, "vlan-list")
        if kwargs.pop('delete_vlan_list', False) is True:
            delete_vlan_list = config.find('.//*vlan-list')
            delete_vlan_list.set('operation', 'delete')
            
        vlan_list.text = kwargs.pop('vlan_list')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session = ET.SubElement(monitor, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
                
        direction = ET.SubElement(monitor, "direction")
        if kwargs.pop('delete_direction', False) is True:
            delete_direction = config.find('.//*direction')
            delete_direction.set('operation', 'delete')
            
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
                
        remote_endpoint = ET.SubElement(monitor, "remote-endpoint")
        if kwargs.pop('delete_remote_endpoint', False) is True:
            delete_remote_endpoint = config.find('.//*remote-endpoint')
            delete_remote_endpoint.set('operation', 'delete')
            
        remote_endpoint.text = kwargs.pop('remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
                
        vlan_leaf = ET.SubElement(monitor, "vlan-leaf")
        if kwargs.pop('delete_vlan_leaf', False) is True:
            delete_vlan_leaf = config.find('.//*vlan-leaf')
            delete_vlan_leaf.set('operation', 'delete')
            
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_add_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
                
        vlan_add_remove = ET.SubElement(monitor, "vlan-add-remove")
        if kwargs.pop('delete_vlan_add_remove', False) is True:
            delete_vlan_add_remove = config.find('.//*vlan-add-remove')
            delete_vlan_add_remove.set('operation', 'delete')
            
        vlan_add_remove.text = kwargs.pop('vlan_add_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        monitor = ET.SubElement(overlay_gateway, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
                
        vlan_range = ET.SubElement(monitor, "vlan-range")
        if kwargs.pop('delete_vlan_range', False) is True:
            delete_vlan_range = config.find('.//*vlan-range')
            delete_vlan_range.set('operation', 'delete')
            
        vlan_range.text = kwargs.pop('vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        sflow = ET.SubElement(overlay_gateway, "sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sflow_profile_name = ET.SubElement(sflow, "sflow-profile-name")
        if kwargs.pop('delete_sflow_profile_name', False) is True:
            delete_sflow_profile_name = config.find('.//*sflow-profile-name')
            delete_sflow_profile_name.set('operation', 'delete')
            
        sflow_profile_name.text = kwargs.pop('sflow_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        sflow = ET.SubElement(overlay_gateway, "sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        if kwargs.pop('delete_sflow_profile_name', False) is True:
            delete_sflow_profile_name = config.find('.//*sflow-profile-name')
            delete_sflow_profile_name.set('operation', 'delete')
                
        sflow_remote_endpoint = ET.SubElement(sflow, "sflow-remote-endpoint")
        if kwargs.pop('delete_sflow_remote_endpoint', False) is True:
            delete_sflow_remote_endpoint = config.find('.//*sflow-remote-endpoint')
            delete_sflow_remote_endpoint.set('operation', 'delete')
            
        sflow_remote_endpoint.text = kwargs.pop('sflow_remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        sflow = ET.SubElement(overlay_gateway, "sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        if kwargs.pop('delete_sflow_profile_name', False) is True:
            delete_sflow_profile_name = config.find('.//*sflow-profile-name')
            delete_sflow_profile_name.set('operation', 'delete')
                
        sflow_vlan_action = ET.SubElement(sflow, "sflow-vlan-action")
        if kwargs.pop('delete_sflow_vlan_action', False) is True:
            delete_sflow_vlan_action = config.find('.//*sflow-vlan-action')
            delete_sflow_vlan_action.set('operation', 'delete')
            
        sflow_vlan_action.text = kwargs.pop('sflow_vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        sflow = ET.SubElement(overlay_gateway, "sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        if kwargs.pop('delete_sflow_profile_name', False) is True:
            delete_sflow_profile_name = config.find('.//*sflow-profile-name')
            delete_sflow_profile_name.set('operation', 'delete')
                
        sflow_vlan_range = ET.SubElement(sflow, "sflow-vlan-range")
        if kwargs.pop('delete_sflow_vlan_range', False) is True:
            delete_sflow_vlan_range = config.find('.//*sflow-vlan-range')
            delete_sflow_vlan_range.set('operation', 'delete')
            
        sflow_vlan_range.text = kwargs.pop('sflow_vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        mac = ET.SubElement(access_lists, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        in_cg = ET.SubElement(mac, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        mac_acl_in_name = ET.SubElement(in_cg, "mac-acl-in-name")
        if kwargs.pop('delete_mac_acl_in_name', False) is True:
            delete_mac_acl_in_name = config.find('.//*mac-acl-in-name')
            delete_mac_acl_in_name.set('operation', 'delete')
            
        mac_acl_in_name.text = kwargs.pop('mac_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        mac = ET.SubElement(access_lists, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        in_cg = ET.SubElement(mac, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        mac_acl_in_dir = ET.SubElement(in_cg, "mac-acl-in-dir")
        if kwargs.pop('delete_mac_acl_in_dir', False) is True:
            delete_mac_acl_in_dir = config.find('.//*mac-acl-in-dir')
            delete_mac_acl_in_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        mac = ET.SubElement(access_lists, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        out = ET.SubElement(mac, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        mac_acl_out_name = ET.SubElement(out, "mac-acl-out-name")
        if kwargs.pop('delete_mac_acl_out_name', False) is True:
            delete_mac_acl_out_name = config.find('.//*mac-acl-out-name')
            delete_mac_acl_out_name.set('operation', 'delete')
            
        mac_acl_out_name.text = kwargs.pop('mac_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        mac = ET.SubElement(access_lists, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        out = ET.SubElement(mac, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        mac_acl_out_dir = ET.SubElement(out, "mac-acl-out-dir")
        if kwargs.pop('delete_mac_acl_out_dir', False) is True:
            delete_mac_acl_out_dir = config.find('.//*mac-acl-out-dir')
            delete_mac_acl_out_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv4 = ET.SubElement(access_lists, "ipv4")
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
            
        in_cg = ET.SubElement(ipv4, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        ipv4_acl_in_name = ET.SubElement(in_cg, "ipv4-acl-in-name")
        if kwargs.pop('delete_ipv4_acl_in_name', False) is True:
            delete_ipv4_acl_in_name = config.find('.//*ipv4-acl-in-name')
            delete_ipv4_acl_in_name.set('operation', 'delete')
            
        ipv4_acl_in_name.text = kwargs.pop('ipv4_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv4 = ET.SubElement(access_lists, "ipv4")
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
            
        in_cg = ET.SubElement(ipv4, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        ipv4_acl_in_dir = ET.SubElement(in_cg, "ipv4-acl-in-dir")
        if kwargs.pop('delete_ipv4_acl_in_dir', False) is True:
            delete_ipv4_acl_in_dir = config.find('.//*ipv4-acl-in-dir')
            delete_ipv4_acl_in_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv4 = ET.SubElement(access_lists, "ipv4")
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
            
        out = ET.SubElement(ipv4, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        ipv4_acl_out_name = ET.SubElement(out, "ipv4-acl-out-name")
        if kwargs.pop('delete_ipv4_acl_out_name', False) is True:
            delete_ipv4_acl_out_name = config.find('.//*ipv4-acl-out-name')
            delete_ipv4_acl_out_name.set('operation', 'delete')
            
        ipv4_acl_out_name.text = kwargs.pop('ipv4_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv4 = ET.SubElement(access_lists, "ipv4")
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
            
        out = ET.SubElement(ipv4, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        ipv4_acl_out_dir = ET.SubElement(out, "ipv4-acl-out-dir")
        if kwargs.pop('delete_ipv4_acl_out_dir', False) is True:
            delete_ipv4_acl_out_dir = config.find('.//*ipv4-acl-out-dir')
            delete_ipv4_acl_out_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv6 = ET.SubElement(access_lists, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        in_cg = ET.SubElement(ipv6, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        ipv6_acl_in_name = ET.SubElement(in_cg, "ipv6-acl-in-name")
        if kwargs.pop('delete_ipv6_acl_in_name', False) is True:
            delete_ipv6_acl_in_name = config.find('.//*ipv6-acl-in-name')
            delete_ipv6_acl_in_name.set('operation', 'delete')
            
        ipv6_acl_in_name.text = kwargs.pop('ipv6_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv6 = ET.SubElement(access_lists, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        in_cg = ET.SubElement(ipv6, "in")
        if kwargs.pop('delete_in_cg', False) is True:
            delete_in_cg = config.find('.//*in')
            delete_in_cg.set('operation', 'delete')
            
        ipv6_acl_in_dir = ET.SubElement(in_cg, "ipv6-acl-in-dir")
        if kwargs.pop('delete_ipv6_acl_in_dir', False) is True:
            delete_ipv6_acl_in_dir = config.find('.//*ipv6-acl-in-dir')
            delete_ipv6_acl_in_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv6 = ET.SubElement(access_lists, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        out = ET.SubElement(ipv6, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        ipv6_acl_out_name = ET.SubElement(out, "ipv6-acl-out-name")
        if kwargs.pop('delete_ipv6_acl_out_name', False) is True:
            delete_ipv6_acl_out_name = config.find('.//*ipv6-acl-out-name')
            delete_ipv6_acl_out_name.set('operation', 'delete')
            
        ipv6_acl_out_name.text = kwargs.pop('ipv6_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        if kwargs.pop('delete_access_lists', False) is True:
            delete_access_lists = config.find('.//*access-lists')
            delete_access_lists.set('operation', 'delete')
            
        ipv6 = ET.SubElement(access_lists, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        out = ET.SubElement(ipv6, "out")
        if kwargs.pop('delete_out', False) is True:
            delete_out = config.find('.//*out')
            delete_out.set('operation', 'delete')
            
        ipv6_acl_out_dir = ET.SubElement(out, "ipv6-acl-out-dir")
        if kwargs.pop('delete_ipv6_acl_out_dir', False) is True:
            delete_ipv6_acl_out_dir = config.find('.//*ipv6-acl-out-dir')
            delete_ipv6_acl_out_dir.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_overlay_gateway', False) is True:
            delete_overlay_gateway = config.find('.//*overlay-gateway')
            delete_overlay_gateway.set('operation', 'delete')
            
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        activate = ET.SubElement(overlay_gateway, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_ovsdb_server', False) is True:
            delete_ovsdb_server = config.find('.//*ovsdb-server')
            delete_ovsdb_server.set('operation', 'delete')
            
        name = ET.SubElement(ovsdb_server, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_ovsdb_server', False) is True:
            delete_ovsdb_server = config.find('.//*ovsdb-server')
            delete_ovsdb_server.set('operation', 'delete')
            
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        port = ET.SubElement(ovsdb_server, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        if kwargs.pop('delete_ovsdb_server', False) is True:
            delete_ovsdb_server = config.find('.//*ovsdb-server')
            delete_ovsdb_server.set('operation', 'delete')
            
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        activate = ET.SubElement(ovsdb_server, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        