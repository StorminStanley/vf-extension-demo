#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_chassis(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_virtual_ip_holder_chassis_virtual_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        if kwargs.pop('delete_hide_virtual_ip_holder', False) is True:
            delete_hide_virtual_ip_holder = config.find('.//*hide-virtual-ip-holder')
            delete_hide_virtual_ip_holder.set('operation', 'delete')
            
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        if kwargs.pop('delete_chassis', False) is True:
            delete_chassis = config.find('.//*chassis')
            delete_chassis.set('operation', 'delete')
            
        virtual_ip = ET.SubElement(chassis, "virtual-ip")
        if kwargs.pop('delete_virtual_ip', False) is True:
            delete_virtual_ip = config.find('.//*virtual-ip')
            delete_virtual_ip.set('operation', 'delete')
            
        virtual_ip.text = kwargs.pop('virtual_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_virtual_ipv6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        if kwargs.pop('delete_hide_virtual_ip_holder', False) is True:
            delete_hide_virtual_ip_holder = config.find('.//*hide-virtual-ip-holder')
            delete_hide_virtual_ip_holder.set('operation', 'delete')
            
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        if kwargs.pop('delete_chassis', False) is True:
            delete_chassis = config.find('.//*chassis')
            delete_chassis.set('operation', 'delete')
            
        virtual_ipv6 = ET.SubElement(chassis, "virtual-ipv6")
        if kwargs.pop('delete_virtual_ipv6', False) is True:
            delete_virtual_ipv6 = config.find('.//*virtual-ipv6')
            delete_virtual_ipv6.set('operation', 'delete')
            
        virtual_ipv6.text = kwargs.pop('virtual_ipv6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_oper_address_virtual_oper_Vip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        if kwargs.pop('delete_hide_virtual_ip_holder', False) is True:
            delete_hide_virtual_ip_holder = config.find('.//*hide-virtual-ip-holder')
            delete_hide_virtual_ip_holder.set('operation', 'delete')
            
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        if kwargs.pop('delete_chassis', False) is True:
            delete_chassis = config.find('.//*chassis')
            delete_chassis.set('operation', 'delete')
            
        oper_address = ET.SubElement(chassis, "oper-address")
        if kwargs.pop('delete_oper_address', False) is True:
            delete_oper_address = config.find('.//*oper-address')
            delete_oper_address.set('operation', 'delete')
            
        virtual_oper_Vip_address = ET.SubElement(oper_address, "virtual-oper-Vip-address")
        if kwargs.pop('delete_virtual_oper_Vip_address', False) is True:
            delete_virtual_oper_Vip_address = config.find('.//*virtual-oper-Vip-address')
            delete_virtual_oper_Vip_address.set('operation', 'delete')
            
        virtual_oper_Vip_address.text = kwargs.pop('virtual_oper_Vip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        