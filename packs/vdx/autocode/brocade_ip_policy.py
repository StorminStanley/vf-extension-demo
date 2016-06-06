#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ip_policy(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_routemap_holder_route_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        name = ET.SubElement(route_map, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_action_rm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        action_rm = ET.SubElement(route_map, "action-rm")
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
            
        action_rm.text = kwargs.pop('action_rm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance = ET.SubElement(route_map, "instance")
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
            
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        vrf = ET.SubElement(match, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ipv6 = ET.SubElement(match, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        address = ET.SubElement(ipv6, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        ipv6_prefix_list_rmm = ET.SubElement(address, "ipv6-prefix-list-rmm")
        if kwargs.pop('delete_ipv6_prefix_list_rmm', False) is True:
            delete_ipv6_prefix_list_rmm = config.find('.//*ipv6-prefix-list-rmm')
            delete_ipv6_prefix_list_rmm.set('operation', 'delete')
            
        ipv6_prefix_list_rmm.text = kwargs.pop('ipv6_prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ipv6 = ET.SubElement(match, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        address = ET.SubElement(ipv6, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        ipv6_acl_rmm = ET.SubElement(address, "ipv6-acl-rmm")
        if kwargs.pop('delete_ipv6_acl_rmm', False) is True:
            delete_ipv6_acl_rmm = config.find('.//*ipv6-acl-rmm')
            delete_ipv6_acl_rmm.set('operation', 'delete')
            
        ipv6_acl_rmm.text = kwargs.pop('ipv6_acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_next_hop_ipv6_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ipv6 = ET.SubElement(match, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        next_hop = ET.SubElement(ipv6, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        ipv6_prefix_list_rmm_n = ET.SubElement(next_hop, "ipv6-prefix-list-rmm-n")
        if kwargs.pop('delete_ipv6_prefix_list_rmm_n', False) is True:
            delete_ipv6_prefix_list_rmm_n = config.find('.//*ipv6-prefix-list-rmm-n')
            delete_ipv6_prefix_list_rmm_n.set('operation', 'delete')
            
        ipv6_prefix_list_rmm_n.text = kwargs.pop('ipv6_prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_route_source_ipv6_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ipv6 = ET.SubElement(match, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        route_source = ET.SubElement(ipv6, "route-source")
        if kwargs.pop('delete_route_source', False) is True:
            delete_route_source = config.find('.//*route-source')
            delete_route_source.set('operation', 'delete')
            
        ipv6_prefix_list_rmrs = ET.SubElement(route_source, "ipv6-prefix-list-rmrs")
        if kwargs.pop('delete_ipv6_prefix_list_rmrs', False) is True:
            delete_ipv6_prefix_list_rmrs = config.find('.//*ipv6-prefix-list-rmrs')
            delete_ipv6_prefix_list_rmrs.set('operation', 'delete')
            
        ipv6_prefix_list_rmrs.text = kwargs.pop('ipv6_prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ip = ET.SubElement(match, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        address = ET.SubElement(ip, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        prefix_list_rmm = ET.SubElement(address, "prefix-list-rmm")
        if kwargs.pop('delete_prefix_list_rmm', False) is True:
            delete_prefix_list_rmm = config.find('.//*prefix-list-rmm')
            delete_prefix_list_rmm.set('operation', 'delete')
            
        prefix_list_rmm.text = kwargs.pop('prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ip = ET.SubElement(match, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        address = ET.SubElement(ip, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        acl_rmm = ET.SubElement(address, "acl-rmm")
        if kwargs.pop('delete_acl_rmm', False) is True:
            delete_acl_rmm = config.find('.//*acl-rmm')
            delete_acl_rmm.set('operation', 'delete')
            
        acl_rmm.text = kwargs.pop('acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_next_hop_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ip = ET.SubElement(match, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        next_hop = ET.SubElement(ip, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        prefix_list_rmm_n = ET.SubElement(next_hop, "prefix-list-rmm-n")
        if kwargs.pop('delete_prefix_list_rmm_n', False) is True:
            delete_prefix_list_rmm_n = config.find('.//*prefix-list-rmm-n')
            delete_prefix_list_rmm_n.set('operation', 'delete')
            
        prefix_list_rmm_n.text = kwargs.pop('prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_route_source_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        ip = ET.SubElement(match, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        route_source = ET.SubElement(ip, "route-source")
        if kwargs.pop('delete_route_source', False) is True:
            delete_route_source = config.find('.//*route-source')
            delete_route_source.set('operation', 'delete')
            
        prefix_list_rmrs = ET.SubElement(route_source, "prefix-list-rmrs")
        if kwargs.pop('delete_prefix_list_rmrs', False) is True:
            delete_prefix_list_rmrs = config.find('.//*prefix-list-rmrs')
            delete_prefix_list_rmrs.set('operation', 'delete')
            
        prefix_list_rmrs.text = kwargs.pop('prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_extcommunity_extcommunity_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        extcommunity = ET.SubElement(match, "extcommunity")
        if kwargs.pop('delete_extcommunity', False) is True:
            delete_extcommunity = config.find('.//*extcommunity')
            delete_extcommunity.set('operation', 'delete')
            
        extcommunity_num = ET.SubElement(extcommunity, "extcommunity-num")
        if kwargs.pop('delete_extcommunity_num', False) is True:
            delete_extcommunity_num = config.find('.//*extcommunity-num')
            delete_extcommunity_num.set('operation', 'delete')
            
        extcommunity_num.text = kwargs.pop('extcommunity_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_metric_metric_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        metric = ET.SubElement(match, "metric")
        if kwargs.pop('delete_metric', False) is True:
            delete_metric = config.find('.//*metric')
            delete_metric.set('operation', 'delete')
            
        metric_rmm = ET.SubElement(metric, "metric-rmm")
        if kwargs.pop('delete_metric_rmm', False) is True:
            delete_metric_rmm = config.find('.//*metric-rmm')
            delete_metric_rmm.set('operation', 'delete')
            
        metric_rmm.text = kwargs.pop('metric_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_route_type_route_type_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        route_type = ET.SubElement(match, "route-type")
        if kwargs.pop('delete_route_type', False) is True:
            delete_route_type = config.find('.//*route-type')
            delete_route_type.set('operation', 'delete')
            
        route_type_rmm = ET.SubElement(route_type, "route-type-rmm")
        if kwargs.pop('delete_route_type_rmm', False) is True:
            delete_route_type_rmm = config.find('.//*route-type-rmm')
            delete_route_type_rmm.set('operation', 'delete')
            
        route_type_rmm.text = kwargs.pop('route_type_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_as_path_as_path_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        as_path = ET.SubElement(match, "as-path")
        if kwargs.pop('delete_as_path', False) is True:
            delete_as_path = config.find('.//*as-path')
            delete_as_path.set('operation', 'delete')
            
        as_path_access_list_name = ET.SubElement(as_path, "as-path-access-list-name")
        if kwargs.pop('delete_as_path_access_list_name', False) is True:
            delete_as_path_access_list_name = config.find('.//*as-path-access-list-name')
            delete_as_path_access_list_name.set('operation', 'delete')
            
        as_path_access_list_name.text = kwargs.pop('as_path_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_community_community_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        community = ET.SubElement(match, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        community_access_list_name = ET.SubElement(community, "community-access-list-name")
        if kwargs.pop('delete_community_access_list_name', False) is True:
            delete_community_access_list_name = config.find('.//*community-access-list-name')
            delete_community_access_list_name.set('operation', 'delete')
            
        community_access_list_name.text = kwargs.pop('community_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_next_hop_next_hop_filter_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        next_hop = ET.SubElement(match, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop_filter_val = ET.SubElement(next_hop, "next-hop-filter-val")
        if kwargs.pop('delete_next_hop_filter_val', False) is True:
            delete_next_hop_filter_val = config.find('.//*next-hop-filter-val')
            delete_next_hop_filter_val.set('operation', 'delete')
            
        next_hop_filter_val.text = kwargs.pop('next_hop_filter_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_protocol_static_container_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        protocol = ET.SubElement(match, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol_static_container = ET.SubElement(protocol, "protocol-static-container")
        if kwargs.pop('delete_protocol_static_container', False) is True:
            delete_protocol_static_container = config.find('.//*protocol-static-container')
            delete_protocol_static_container.set('operation', 'delete')
            
        static = ET.SubElement(protocol_static_container, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_protocol_bgp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        protocol = ET.SubElement(match, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        if kwargs.pop('delete_bgp_protocol_container', False) is True:
            delete_bgp_protocol_container = config.find('.//*bgp-protocol-container')
            delete_bgp_protocol_container.set('operation', 'delete')
            
        protocol_bgp = ET.SubElement(bgp_protocol_container, "protocol-bgp")
        if kwargs.pop('delete_protocol_bgp', False) is True:
            delete_protocol_bgp = config.find('.//*protocol-bgp')
            delete_protocol_bgp.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_bgp_route_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        match = ET.SubElement(content, "match")
        if kwargs.pop('delete_match', False) is True:
            delete_match = config.find('.//*match')
            delete_match.set('operation', 'delete')
            
        protocol = ET.SubElement(match, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        if kwargs.pop('delete_bgp_protocol_container', False) is True:
            delete_bgp_protocol_container = config.find('.//*bgp-protocol-container')
            delete_bgp_protocol_container.set('operation', 'delete')
            
        bgp_route_type = ET.SubElement(bgp_protocol_container, "bgp-route-type")
        if kwargs.pop('delete_bgp_route_type', False) is True:
            delete_bgp_route_type = config.find('.//*bgp-route-type')
            delete_bgp_route_type.set('operation', 'delete')
            
        bgp_route_type.text = kwargs.pop('bgp_route_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_dscp_dscp_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        dscp = ET.SubElement(ip, "dscp")
        if kwargs.pop('delete_dscp', False) is True:
            delete_dscp = config.find('.//*dscp')
            delete_dscp.set('operation', 'delete')
            
        dscp_rms = ET.SubElement(dscp, "dscp-rms")
        if kwargs.pop('delete_dscp_rms', False) is True:
            delete_dscp_rms = config.find('.//*dscp-rms')
            delete_dscp_rms.set('operation', 'delete')
            
        dscp_rms.text = kwargs.pop('dscp_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_interface_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        interface = ET.SubElement(ip, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        null0 = ET.SubElement(interface, "null0")
        if kwargs.pop('delete_null0', False) is True:
            delete_null0 = config.find('.//*null0')
            delete_null0.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_hop_peer_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        next_hop = ET.SubElement(ip, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        peer_address = ET.SubElement(next_hop, "peer-address")
        if kwargs.pop('delete_peer_address', False) is True:
            delete_peer_address = config.find('.//*peer-address')
            delete_peer_address.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        globl = ET.SubElement(ip, "global")
        if kwargs.pop('delete_globl', False) is True:
            delete_globl = config.find('.//*global')
            delete_globl.set('operation', 'delete')
            
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        if kwargs.pop('delete_next_global_hop', False) is True:
            delete_next_global_hop = config.find('.//*next-global-hop')
            delete_next_global_hop.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        next_ip = ET.SubElement(ip, "next-ip")
        if kwargs.pop('delete_next_ip', False) is True:
            delete_next_ip = config.find('.//*next-ip')
            delete_next_ip.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_ip, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_hop, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        next_vrf = ET.SubElement(ip, "next-vrf")
        if kwargs.pop('delete_next_vrf', False) is True:
            delete_next_vrf = config.find('.//*next-vrf')
            delete_next_vrf.set('operation', 'delete')
            
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        if kwargs.pop('delete_next_vrf_list', False) is True:
            delete_next_vrf_list = config.find('.//*next-vrf-list')
            delete_next_vrf_list.set('operation', 'delete')
            
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
                
        vrf = ET.SubElement(next_vrf_list, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ip = ET.SubElement(set, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        next_vrf = ET.SubElement(ip, "next-vrf")
        if kwargs.pop('delete_next_vrf', False) is True:
            delete_next_vrf = config.find('.//*next-vrf')
            delete_next_vrf.set('operation', 'delete')
            
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        if kwargs.pop('delete_next_vrf_list', False) is True:
            delete_next_vrf_list = config.find('.//*next-vrf-list')
            delete_next_vrf_list.set('operation', 'delete')
            
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
                
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_interface_ipv6_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ipv6 = ET.SubElement(set, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        interface = ET.SubElement(ipv6, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        ipv6_null0 = ET.SubElement(interface, "ipv6-null0")
        if kwargs.pop('delete_ipv6_null0', False) is True:
            delete_ipv6_null0 = config.find('.//*ipv6-null0')
            delete_ipv6_null0.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ipv6 = ET.SubElement(set, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        globl = ET.SubElement(ipv6, "global")
        if kwargs.pop('delete_globl', False) is True:
            delete_globl = config.find('.//*global')
            delete_globl.set('operation', 'delete')
            
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        if kwargs.pop('delete_next_global_hop', False) is True:
            delete_next_global_hop = config.find('.//*next-global-hop')
            delete_next_global_hop.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ipv6 = ET.SubElement(set, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        next_ip = ET.SubElement(ipv6, "next-ip")
        if kwargs.pop('delete_next_ip', False) is True:
            delete_next_ip = config.find('.//*next-ip')
            delete_next_ip.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_ip, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop = ET.SubElement(next_hop, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ipv6 = ET.SubElement(set, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        if kwargs.pop('delete_next_vrf', False) is True:
            delete_next_vrf = config.find('.//*next-vrf')
            delete_next_vrf.set('operation', 'delete')
            
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        if kwargs.pop('delete_next_vrf_list', False) is True:
            delete_next_vrf_list = config.find('.//*next-vrf-list')
            delete_next_vrf_list.set('operation', 'delete')
            
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
                
        vrf = ET.SubElement(next_vrf_list, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        ipv6 = ET.SubElement(set, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        if kwargs.pop('delete_next_vrf', False) is True:
            delete_next_vrf = config.find('.//*next-vrf')
            delete_next_vrf.set('operation', 'delete')
            
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        if kwargs.pop('delete_next_vrf_list', False) is True:
            delete_next_vrf_list = config.find('.//*next-vrf-list')
            delete_next_vrf_list.set('operation', 'delete')
            
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
                
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        if kwargs.pop('delete_next_hop', False) is True:
            delete_next_hop = config.find('.//*next-hop')
            delete_next_hop.set('operation', 'delete')
            
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_rt_ASN_NN_rt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        extcommunity = ET.SubElement(set, "extcommunity")
        if kwargs.pop('delete_extcommunity', False) is True:
            delete_extcommunity = config.find('.//*extcommunity')
            delete_extcommunity.set('operation', 'delete')
            
        rt = ET.SubElement(extcommunity, "rt")
        if kwargs.pop('delete_rt', False) is True:
            delete_rt = config.find('.//*rt')
            delete_rt.set('operation', 'delete')
            
        ASN_NN_rt = ET.SubElement(rt, "ASN-NN-rt")
        if kwargs.pop('delete_ASN_NN_rt', False) is True:
            delete_ASN_NN_rt = config.find('.//*ASN-NN-rt')
            delete_ASN_NN_rt.set('operation', 'delete')
            
        ASN_NN_rt.text = kwargs.pop('ASN_NN_rt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_soo_ASN_NN_soo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        extcommunity = ET.SubElement(set, "extcommunity")
        if kwargs.pop('delete_extcommunity', False) is True:
            delete_extcommunity = config.find('.//*extcommunity')
            delete_extcommunity.set('operation', 'delete')
            
        soo = ET.SubElement(extcommunity, "soo")
        if kwargs.pop('delete_soo', False) is True:
            delete_soo = config.find('.//*soo')
            delete_soo.set('operation', 'delete')
            
        ASN_NN_soo = ET.SubElement(soo, "ASN-NN-soo")
        if kwargs.pop('delete_ASN_NN_soo', False) is True:
            delete_ASN_NN_soo = config.find('.//*ASN-NN-soo')
            delete_ASN_NN_soo.set('operation', 'delete')
            
        ASN_NN_soo.text = kwargs.pop('ASN_NN_soo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_community_set_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        community = ET.SubElement(set, "community")
        if kwargs.pop('delete_community', False) is True:
            delete_community = config.find('.//*community')
            delete_community.set('operation', 'delete')
            
        set_community_expr = ET.SubElement(community, "set-community-expr")
        if kwargs.pop('delete_set_community_expr', False) is True:
            delete_set_community_expr = config.find('.//*set-community-expr')
            delete_set_community_expr.set('operation', 'delete')
            
        set_community_expr.text = kwargs.pop('set_community_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_delta_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric = ET.SubElement(set, "metric")
        if kwargs.pop('delete_metric', False) is True:
            delete_metric = config.find('.//*metric')
            delete_metric.set('operation', 'delete')
            
        delta_rms = ET.SubElement(metric, "delta-rms")
        if kwargs.pop('delete_delta_rms', False) is True:
            delete_delta_rms = config.find('.//*delta-rms')
            delete_delta_rms.set('operation', 'delete')
            
        delta_rms.text = kwargs.pop('delta_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_metric_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric = ET.SubElement(set, "metric")
        if kwargs.pop('delete_metric', False) is True:
            delete_metric = config.find('.//*metric')
            delete_metric.set('operation', 'delete')
            
        metric_rms = ET.SubElement(metric, "metric-rms")
        if kwargs.pop('delete_metric_rms', False) is True:
            delete_metric_rms = config.find('.//*metric-rms')
            delete_metric_rms.set('operation', 'delete')
            
        metric_rms.text = kwargs.pop('metric_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_distance_dist_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        distance = ET.SubElement(set, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        dist_rms = ET.SubElement(distance, "dist-rms")
        if kwargs.pop('delete_dist_rms', False) is True:
            delete_dist_rms = config.find('.//*dist-rms')
            delete_dist_rms.set('operation', 'delete')
            
        dist_rms.text = kwargs.pop('dist_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_route_type_route_type_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        route_type = ET.SubElement(set, "route-type")
        if kwargs.pop('delete_route_type', False) is True:
            delete_route_type = config.find('.//*route-type')
            delete_route_type.set('operation', 'delete')
            
        route_type_rms = ET.SubElement(route_type, "route-type-rms")
        if kwargs.pop('delete_route_type_rms', False) is True:
            delete_route_type_rms = config.find('.//*route-type-rms')
            delete_route_type_rms.set('operation', 'delete')
            
        route_type_rms.text = kwargs.pop('route_type_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_tag_tag_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        tag = ET.SubElement(set, "tag")
        if kwargs.pop('delete_tag', False) is True:
            delete_tag = config.find('.//*tag')
            delete_tag.set('operation', 'delete')
            
        tag_rms = ET.SubElement(tag, "tag-rms")
        if kwargs.pop('delete_tag_rms', False) is True:
            delete_tag_rms = config.find('.//*tag-rms')
            delete_tag_rms.set('operation', 'delete')
            
        tag_rms.text = kwargs.pop('tag_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_weight_weight_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        weight = ET.SubElement(set, "weight")
        if kwargs.pop('delete_weight', False) is True:
            delete_weight = config.find('.//*weight')
            delete_weight.set('operation', 'delete')
            
        weight_value = ET.SubElement(weight, "weight-value")
        if kwargs.pop('delete_weight_value', False) is True:
            delete_weight_value = config.find('.//*weight-value')
            delete_weight_value.set('operation', 'delete')
            
        weight_value.text = kwargs.pop('weight_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_aspath_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        as_path = ET.SubElement(set, "as-path")
        if kwargs.pop('delete_as_path', False) is True:
            delete_as_path = config.find('.//*as-path')
            delete_as_path.set('operation', 'delete')
            
        aspath_tag = ET.SubElement(as_path, "aspath-tag")
        if kwargs.pop('delete_aspath_tag', False) is True:
            delete_aspath_tag = config.find('.//*aspath-tag')
            delete_aspath_tag.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_prepend(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        as_path = ET.SubElement(set, "as-path")
        if kwargs.pop('delete_as_path', False) is True:
            delete_as_path = config.find('.//*as-path')
            delete_as_path.set('operation', 'delete')
            
        prepend = ET.SubElement(as_path, "prepend")
        if kwargs.pop('delete_prepend', False) is True:
            delete_prepend = config.find('.//*prepend')
            delete_prepend.set('operation', 'delete')
            
        prepend.text = kwargs.pop('prepend')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_automatic_tag_tag_empty(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        automatic_tag = ET.SubElement(set, "automatic-tag")
        if kwargs.pop('delete_automatic_tag', False) is True:
            delete_automatic_tag = config.find('.//*automatic-tag')
            delete_automatic_tag.set('operation', 'delete')
            
        tag_empty = ET.SubElement(automatic_tag, "tag-empty")
        if kwargs.pop('delete_tag_empty', False) is True:
            delete_tag_empty = config.find('.//*tag-empty')
            delete_tag_empty.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_comm_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        comm_list = ET.SubElement(set, "comm-list")
        if kwargs.pop('delete_comm_list', False) is True:
            delete_comm_list = config.find('.//*comm-list')
            delete_comm_list.set('operation', 'delete')
            
        comm_list_name = ET.SubElement(comm_list, "comm-list-name")
        if kwargs.pop('delete_comm_list_name', False) is True:
            delete_comm_list_name = config.find('.//*comm-list-name')
            delete_comm_list_name.set('operation', 'delete')
            
        comm_list_name.text = kwargs.pop('comm_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_match_comm_delete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        comm_list = ET.SubElement(set, "comm-list")
        if kwargs.pop('delete_comm_list', False) is True:
            delete_comm_list = config.find('.//*comm-list')
            delete_comm_list.set('operation', 'delete')
            
        match_comm_delete = ET.SubElement(comm_list, "match-comm-delete")
        if kwargs.pop('delete_match_comm_delete', False) is True:
            delete_match_comm_delete = config.find('.//*match-comm-delete')
            delete_match_comm_delete.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_half_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        dampening = ET.SubElement(set, "dampening")
        if kwargs.pop('delete_dampening', False) is True:
            delete_dampening = config.find('.//*dampening')
            delete_dampening.set('operation', 'delete')
            
        half_life = ET.SubElement(dampening, "half-life")
        if kwargs.pop('delete_half_life', False) is True:
            delete_half_life = config.find('.//*half-life')
            delete_half_life.set('operation', 'delete')
            
        half_life.text = kwargs.pop('half_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_reuse(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        dampening = ET.SubElement(set, "dampening")
        if kwargs.pop('delete_dampening', False) is True:
            delete_dampening = config.find('.//*dampening')
            delete_dampening.set('operation', 'delete')
            
        reuse = ET.SubElement(dampening, "reuse")
        if kwargs.pop('delete_reuse', False) is True:
            delete_reuse = config.find('.//*reuse')
            delete_reuse.set('operation', 'delete')
            
        reuse.text = kwargs.pop('reuse')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        dampening = ET.SubElement(set, "dampening")
        if kwargs.pop('delete_dampening', False) is True:
            delete_dampening = config.find('.//*dampening')
            delete_dampening.set('operation', 'delete')
            
        suppress = ET.SubElement(dampening, "suppress")
        if kwargs.pop('delete_suppress', False) is True:
            delete_suppress = config.find('.//*suppress')
            delete_suppress.set('operation', 'delete')
            
        suppress.text = kwargs.pop('suppress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_max_suppress_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        dampening = ET.SubElement(set, "dampening")
        if kwargs.pop('delete_dampening', False) is True:
            delete_dampening = config.find('.//*dampening')
            delete_dampening.set('operation', 'delete')
            
        max_suppress_time = ET.SubElement(dampening, "max-suppress-time")
        if kwargs.pop('delete_max_suppress_time', False) is True:
            delete_max_suppress_time = config.find('.//*max-suppress-time')
            delete_max_suppress_time.set('operation', 'delete')
            
        max_suppress_time.text = kwargs.pop('max_suppress_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_local_preference_local_preference_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        local_preference = ET.SubElement(set, "local-preference")
        if kwargs.pop('delete_local_preference', False) is True:
            delete_local_preference = config.find('.//*local-preference')
            delete_local_preference.set('operation', 'delete')
            
        local_preference_value = ET.SubElement(local_preference, "local-preference-value")
        if kwargs.pop('delete_local_preference_value', False) is True:
            delete_local_preference_value = config.find('.//*local-preference-value')
            delete_local_preference_value.set('operation', 'delete')
            
        local_preference_value.text = kwargs.pop('local_preference_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_igp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        origin = ET.SubElement(set, "origin")
        if kwargs.pop('delete_origin', False) is True:
            delete_origin = config.find('.//*origin')
            delete_origin.set('operation', 'delete')
            
        origin_igp = ET.SubElement(origin, "origin-igp")
        if kwargs.pop('delete_origin_igp', False) is True:
            delete_origin_igp = config.find('.//*origin-igp')
            delete_origin_igp.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_incomplete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        origin = ET.SubElement(set, "origin")
        if kwargs.pop('delete_origin', False) is True:
            delete_origin = config.find('.//*origin')
            delete_origin.set('operation', 'delete')
            
        origin_incomplete = ET.SubElement(origin, "origin-incomplete")
        if kwargs.pop('delete_origin_incomplete', False) is True:
            delete_origin_incomplete = config.find('.//*origin-incomplete')
            delete_origin_incomplete.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_external(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric_type = ET.SubElement(set, "metric-type")
        if kwargs.pop('delete_metric_type', False) is True:
            delete_metric_type = config.find('.//*metric-type')
            delete_metric_type.set('operation', 'delete')
            
        external = ET.SubElement(metric_type, "external")
        if kwargs.pop('delete_external', False) is True:
            delete_external = config.find('.//*external')
            delete_external.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_internal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric_type = ET.SubElement(set, "metric-type")
        if kwargs.pop('delete_metric_type', False) is True:
            delete_metric_type = config.find('.//*metric-type')
            delete_metric_type.set('operation', 'delete')
            
        internal = ET.SubElement(metric_type, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric_type = ET.SubElement(set, "metric-type")
        if kwargs.pop('delete_metric_type', False) is True:
            delete_metric_type = config.find('.//*metric-type')
            delete_metric_type.set('operation', 'delete')
            
        type_1 = ET.SubElement(metric_type, "type-1")
        if kwargs.pop('delete_type_1', False) is True:
            delete_type_1 = config.find('.//*type-1')
            delete_type_1.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        set = ET.SubElement(content, "set")
        if kwargs.pop('delete_set', False) is True:
            delete_set = config.find('.//*set')
            delete_set.set('operation', 'delete')
            
        metric_type = ET.SubElement(set, "metric-type")
        if kwargs.pop('delete_metric_type', False) is True:
            delete_metric_type = config.find('.//*metric-type')
            delete_metric_type.set('operation', 'delete')
            
        type_2 = ET.SubElement(metric_type, "type-2")
        if kwargs.pop('delete_type_2', False) is True:
            delete_type_2 = config.find('.//*type-2')
            delete_type_2.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_cont(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        continue_holder = ET.SubElement(content, "continue-holder")
        if kwargs.pop('delete_continue_holder', False) is True:
            delete_continue_holder = config.find('.//*continue-holder')
            delete_continue_holder.set('operation', 'delete')
            
        cont = ET.SubElement(continue_holder, "continue")
        if kwargs.pop('delete_cont', False) is True:
            delete_cont = config.find('.//*continue')
            delete_cont.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_continue_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_routemap_holder', False) is True:
            delete_hide_routemap_holder = config.find('.//*hide-routemap-holder')
            delete_hide_routemap_holder.set('operation', 'delete')
            
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        if kwargs.pop('delete_route_map', False) is True:
            delete_route_map = config.find('.//*route-map')
            delete_route_map.set('operation', 'delete')
            
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        if kwargs.pop('delete_action_rm', False) is True:
            delete_action_rm = config.find('.//*action-rm')
            delete_action_rm.set('operation', 'delete')
                
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        if kwargs.pop('delete_instance', False) is True:
            delete_instance = config.find('.//*instance')
            delete_instance.set('operation', 'delete')
                
        content = ET.SubElement(route_map, "content")
        if kwargs.pop('delete_content', False) is True:
            delete_content = config.find('.//*content')
            delete_content.set('operation', 'delete')
            
        continue_holder = ET.SubElement(content, "continue-holder")
        if kwargs.pop('delete_continue_holder', False) is True:
            delete_continue_holder = config.find('.//*continue-holder')
            delete_continue_holder.set('operation', 'delete')
            
        continue_val = ET.SubElement(continue_holder, "continue-val")
        if kwargs.pop('delete_continue_val', False) is True:
            delete_continue_val = config.find('.//*continue-val')
            delete_continue_val.set('operation', 'delete')
            
        continue_val.text = kwargs.pop('continue_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_filter_change_update_delay_holder_filter_change_update_delay_filter_delay_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_filter_change_update_delay_holder = ET.SubElement(config, "hide-filter-change-update-delay-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        if kwargs.pop('delete_hide_filter_change_update_delay_holder', False) is True:
            delete_hide_filter_change_update_delay_holder = config.find('.//*hide-filter-change-update-delay-holder')
            delete_hide_filter_change_update_delay_holder.set('operation', 'delete')
            
        filter_change_update_delay = ET.SubElement(hide_filter_change_update_delay_holder, "filter-change-update-delay")
        if kwargs.pop('delete_filter_change_update_delay', False) is True:
            delete_filter_change_update_delay = config.find('.//*filter-change-update-delay')
            delete_filter_change_update_delay.set('operation', 'delete')
            
        filter_delay_value = ET.SubElement(filter_change_update_delay, "filter-delay-value")
        if kwargs.pop('delete_filter_delay_value', False) is True:
            delete_filter_delay_value = config.find('.//*filter-delay-value')
            delete_filter_delay_value.set('operation', 'delete')
            
        filter_delay_value.text = kwargs.pop('filter_delay_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        