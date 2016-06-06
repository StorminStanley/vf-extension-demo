#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_arp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_arp_holder_system_max_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        system_max = ET.SubElement(hide_arp_holder, "system-max")
        if kwargs.pop('delete_system_max', False) is True:
            delete_system_max = config.find('.//*system-max')
            delete_system_max.set('operation', 'delete')
            
        arp = ET.SubElement(system_max, "arp")
        if kwargs.pop('delete_arp', False) is True:
            delete_arp = config.find('.//*arp')
            delete_arp.set('operation', 'delete')
            
        arp.text = kwargs.pop('arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_arp_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address = ET.SubElement(arp_entry, "arp-ip-address")
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
            
        arp_ip_address.text = kwargs.pop('arp_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_mac_address_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        mac_address_value = ET.SubElement(arp_entry, "mac-address-value")
        if kwargs.pop('delete_mac_address_value', False) is True:
            delete_mac_address_value = config.find('.//*mac-address-value')
            delete_mac_address_value.set('operation', 'delete')
            
        mac_address_value.text = kwargs.pop('mac_address_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacename = ET.SubElement(arp_entry, "interfacename")
        if kwargs.pop('delete_interfacename', False) is True:
            delete_interfacename = config.find('.//*interfacename')
            delete_interfacename.set('operation', 'delete')
            
        interfacename.text = kwargs.pop('interfacename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_Port_channel_Port_channel(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        Port_channel = ET.SubElement(interfacetype, "Port-channel")
        if kwargs.pop('delete_Port_channel', False) is True:
            delete_Port_channel = config.find('.//*Port-channel')
            delete_Port_channel.set('operation', 'delete')
            
        Port_channel = ET.SubElement(Port_channel, "Port-channel")
        if kwargs.pop('delete_Port_channel', False) is True:
            delete_Port_channel = config.find('.//*Port-channel')
            delete_Port_channel.set('operation', 'delete')
            
        Port_channel.text = kwargs.pop('Port_channel')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        GigabitEthernet = ET.SubElement(interfacetype, "GigabitEthernet")
        if kwargs.pop('delete_GigabitEthernet', False) is True:
            delete_GigabitEthernet = config.find('.//*GigabitEthernet')
            delete_GigabitEthernet.set('operation', 'delete')
            
        GigabitEthernet = ET.SubElement(GigabitEthernet, "GigabitEthernet")
        if kwargs.pop('delete_GigabitEthernet', False) is True:
            delete_GigabitEthernet = config.find('.//*GigabitEthernet')
            delete_GigabitEthernet.set('operation', 'delete')
            
        GigabitEthernet.text = kwargs.pop('GigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_TenGigabitEthernet_TenGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        TenGigabitEthernet = ET.SubElement(interfacetype, "TenGigabitEthernet")
        if kwargs.pop('delete_TenGigabitEthernet', False) is True:
            delete_TenGigabitEthernet = config.find('.//*TenGigabitEthernet')
            delete_TenGigabitEthernet.set('operation', 'delete')
            
        TenGigabitEthernet = ET.SubElement(TenGigabitEthernet, "TenGigabitEthernet")
        if kwargs.pop('delete_TenGigabitEthernet', False) is True:
            delete_TenGigabitEthernet = config.find('.//*TenGigabitEthernet')
            delete_TenGigabitEthernet.set('operation', 'delete')
            
        TenGigabitEthernet.text = kwargs.pop('TenGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_FortyGigabitEthernet_FortyGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        FortyGigabitEthernet = ET.SubElement(interfacetype, "FortyGigabitEthernet")
        if kwargs.pop('delete_FortyGigabitEthernet', False) is True:
            delete_FortyGigabitEthernet = config.find('.//*FortyGigabitEthernet')
            delete_FortyGigabitEthernet.set('operation', 'delete')
            
        FortyGigabitEthernet = ET.SubElement(FortyGigabitEthernet, "FortyGigabitEthernet")
        if kwargs.pop('delete_FortyGigabitEthernet', False) is True:
            delete_FortyGigabitEthernet = config.find('.//*FortyGigabitEthernet')
            delete_FortyGigabitEthernet.set('operation', 'delete')
            
        FortyGigabitEthernet.text = kwargs.pop('FortyGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_HundredGigabitEthernet_HundredGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        HundredGigabitEthernet = ET.SubElement(interfacetype, "HundredGigabitEthernet")
        if kwargs.pop('delete_HundredGigabitEthernet', False) is True:
            delete_HundredGigabitEthernet = config.find('.//*HundredGigabitEthernet')
            delete_HundredGigabitEthernet.set('operation', 'delete')
            
        HundredGigabitEthernet = ET.SubElement(HundredGigabitEthernet, "HundredGigabitEthernet")
        if kwargs.pop('delete_HundredGigabitEthernet', False) is True:
            delete_HundredGigabitEthernet = config.find('.//*HundredGigabitEthernet')
            delete_HundredGigabitEthernet.set('operation', 'delete')
            
        HundredGigabitEthernet.text = kwargs.pop('HundredGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_Ve_Ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        if kwargs.pop('delete_hide_arp_holder', False) is True:
            delete_hide_arp_holder = config.find('.//*hide-arp-holder')
            delete_hide_arp_holder.set('operation', 'delete')
            
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        if kwargs.pop('delete_arp_ip_address', False) is True:
            delete_arp_ip_address = config.find('.//*arp-ip-address')
            delete_arp_ip_address.set('operation', 'delete')
                
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        if kwargs.pop('delete_interfacetype', False) is True:
            delete_interfacetype = config.find('.//*interfacetype')
            delete_interfacetype.set('operation', 'delete')
            
        Ve = ET.SubElement(interfacetype, "Ve")
        if kwargs.pop('delete_Ve', False) is True:
            delete_Ve = config.find('.//*Ve')
            delete_Ve.set('operation', 'delete')
            
        Ve = ET.SubElement(Ve, "Ve")
        if kwargs.pop('delete_Ve', False) is True:
            delete_Ve = config.find('.//*Ve')
            delete_Ve.set('operation', 'delete')
            
        Ve.text = kwargs.pop('Ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        input = ET.SubElement(get_arp, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        input_type = ET.SubElement(input, "input-type")
        if kwargs.pop('delete_input_type', False) is True:
            delete_input_type = config.find('.//*input-type')
            delete_input_type.set('operation', 'delete')
            
        interface = ET.SubElement(input_type, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        input = ET.SubElement(get_arp, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        input_type = ET.SubElement(input, "input-type")
        if kwargs.pop('delete_input_type', False) is True:
            delete_input_type = config.find('.//*input-type')
            delete_input_type.set('operation', 'delete')
            
        interface = ET.SubElement(input_type, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_dynamic_dynamic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        input = ET.SubElement(get_arp, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        input_type = ET.SubElement(input, "input-type")
        if kwargs.pop('delete_input_type', False) is True:
            delete_input_type = config.find('.//*input-type')
            delete_input_type.set('operation', 'delete')
            
        dynamic = ET.SubElement(input_type, "dynamic")
        if kwargs.pop('delete_dynamic', False) is True:
            delete_dynamic = config.find('.//*dynamic')
            delete_dynamic.set('operation', 'delete')
            
        dynamic = ET.SubElement(dynamic, "dynamic")
        if kwargs.pop('delete_dynamic', False) is True:
            delete_dynamic = config.find('.//*dynamic')
            delete_dynamic.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_static_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        input = ET.SubElement(get_arp, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        input_type = ET.SubElement(input, "input-type")
        if kwargs.pop('delete_input_type', False) is True:
            delete_input_type = config.find('.//*input-type')
            delete_input_type.set('operation', 'delete')
            
        static = ET.SubElement(input_type, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            
        static = ET.SubElement(static, "static")
        if kwargs.pop('delete_static', False) is True:
            delete_static = config.find('.//*static')
            delete_static.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_ip_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        input = ET.SubElement(get_arp, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        input_type = ET.SubElement(input, "input-type")
        if kwargs.pop('delete_input_type', False) is True:
            delete_input_type = config.find('.//*input-type')
            delete_input_type.set('operation', 'delete')
            
        ip = ET.SubElement(input_type, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip_address = ET.SubElement(ip, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address = ET.SubElement(arp_entry, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        mac_address = ET.SubElement(arp_entry, "mac-address")
        if kwargs.pop('delete_mac_address', False) is True:
            delete_mac_address = config.find('.//*mac-address')
            delete_mac_address.set('operation', 'delete')
            
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        interface_type = ET.SubElement(arp_entry, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        interface_name = ET.SubElement(arp_entry, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_is_resolved(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        is_resolved = ET.SubElement(arp_entry, "is-resolved")
        if kwargs.pop('delete_is_resolved', False) is True:
            delete_is_resolved = config.find('.//*is-resolved')
            delete_is_resolved.set('operation', 'delete')
            
        is_resolved.text = kwargs.pop('is_resolved')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        age = ET.SubElement(arp_entry, "age")
        if kwargs.pop('delete_age', False) is True:
            delete_age = config.find('.//*age')
            delete_age.set('operation', 'delete')
            
        age.text = kwargs.pop('age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_entry_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        if kwargs.pop('delete_get_arp', False) is True:
            delete_get_arp = config.find('.//*get-arp')
            delete_get_arp.set('operation', 'delete')
            
        output = ET.SubElement(get_arp, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        arp_entry = ET.SubElement(output, "arp-entry")
        if kwargs.pop('delete_arp_entry', False) is True:
            delete_arp_entry = config.find('.//*arp-entry')
            delete_arp_entry.set('operation', 'delete')
            
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
                
        entry_type = ET.SubElement(arp_entry, "entry-type")
        if kwargs.pop('delete_entry_type', False) is True:
            delete_entry_type = config.find('.//*entry-type')
            delete_entry_type.set('operation', 'delete')
            
        entry_type.text = kwargs.pop('entry_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        