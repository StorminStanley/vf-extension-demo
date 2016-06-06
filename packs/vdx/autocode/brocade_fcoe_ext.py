#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fcoe_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcoe_get_interface_input_fcoe_intf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_interface, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_intf_name = ET.SubElement(input, "fcoe-intf-name")
        if kwargs.pop('delete_fcoe_intf_name', False) is True:
            delete_fcoe_intf_name = config.find('.//*fcoe-intf-name')
            delete_fcoe_intf_name.set('operation', 'delete')
            
        fcoe_intf_name.text = kwargs.pop('fcoe_intf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_interface, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_intf_rbridge_id = ET.SubElement(input, "fcoe-intf-rbridge-id")
        if kwargs.pop('delete_fcoe_intf_rbridge_id', False) is True:
            delete_fcoe_intf_rbridge_id = config.find('.//*fcoe-intf-rbridge-id')
            delete_fcoe_intf_rbridge_id.set('operation', 'delete')
            
        fcoe_intf_rbridge_id.text = kwargs.pop('fcoe_intf_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_include_stats(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_interface, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_intf_include_stats = ET.SubElement(input, "fcoe-intf-include-stats")
        if kwargs.pop('delete_fcoe_intf_include_stats', False) is True:
            delete_fcoe_intf_include_stats = config.find('.//*fcoe-intf-include-stats')
            delete_fcoe_intf_include_stats.set('operation', 'delete')
            
        fcoe_intf_include_stats.text = kwargs.pop('fcoe_intf_include_stats')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fcoe_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id.text = kwargs.pop('fcoe_intf_fcoe_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-type")
        if kwargs.pop('delete_fcoe_intf_port_type', False) is True:
            delete_fcoe_intf_port_type = config.find('.//*fcoe-intf-port-type')
            delete_fcoe_intf_port_type.set('operation', 'delete')
            
        fcoe_intf_port_type.text = kwargs.pop('fcoe_intf_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_config_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_config_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-config-port-type")
        if kwargs.pop('delete_fcoe_intf_config_port_type', False) is True:
            delete_fcoe_intf_config_port_type = config.find('.//*fcoe-intf-config-port-type')
            delete_fcoe_intf_config_port_type.set('operation', 'delete')
            
        fcoe_intf_config_port_type.text = kwargs.pop('fcoe_intf_config_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_port_state = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-state")
        if kwargs.pop('delete_fcoe_intf_port_state', False) is True:
            delete_fcoe_intf_port_state = config.find('.//*fcoe-intf-port-state')
            delete_fcoe_intf_port_state.set('operation', 'delete')
            
        fcoe_intf_port_state.text = kwargs.pop('fcoe_intf_port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_fabric_map_name = ET.SubElement(fcoe_intf_list, "fcoe-intf-fabric-map-name")
        if kwargs.pop('delete_fcoe_intf_fabric_map_name', False) is True:
            delete_fcoe_intf_fabric_map_name = config.find('.//*fcoe-intf-fabric-map-name')
            delete_fcoe_intf_fabric_map_name.set('operation', 'delete')
            
        fcoe_intf_fabric_map_name.text = kwargs.pop('fcoe_intf_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_eth_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_eth_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-eth-port-id")
        if kwargs.pop('delete_fcoe_intf_eth_port_id', False) is True:
            delete_fcoe_intf_eth_port_id = config.find('.//*fcoe-intf-eth-port-id')
            delete_fcoe_intf_eth_port_id.set('operation', 'delete')
            
        fcoe_intf_eth_port_id.text = kwargs.pop('fcoe_intf_eth_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        interface_type = ET.SubElement(fcoe_intf_list, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        interface_name = ET.SubElement(fcoe_intf_list, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_admin_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_admin_status = ET.SubElement(fcoe_intf_list, "fcoe-intf-admin-status")
        if kwargs.pop('delete_fcoe_intf_admin_status', False) is True:
            delete_fcoe_intf_admin_status = config.find('.//*fcoe-intf-admin-status')
            delete_fcoe_intf_admin_status.set('operation', 'delete')
            
        fcoe_intf_admin_status.text = kwargs.pop('fcoe_intf_admin_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_peer_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_peer_fcf_mac = ET.SubElement(fcoe_intf_list, "fcoe-intf-peer-fcf-mac")
        if kwargs.pop('delete_fcoe_intf_peer_fcf_mac', False) is True:
            delete_fcoe_intf_peer_fcf_mac = config.find('.//*fcoe-intf-peer-fcf-mac')
            delete_fcoe_intf_peer_fcf_mac.set('operation', 'delete')
            
        fcoe_intf_peer_fcf_mac.text = kwargs.pop('fcoe_intf_peer_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_device_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_device_count = ET.SubElement(fcoe_intf_list, "fcoe-intf-device-count")
        if kwargs.pop('delete_fcoe_intf_device_count', False) is True:
            delete_fcoe_intf_device_count = config.find('.//*fcoe-intf-device-count')
            delete_fcoe_intf_device_count.set('operation', 'delete')
            
        fcoe_intf_device_count.text = kwargs.pop('fcoe_intf_device_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_ifindex = ET.SubElement(fcoe_intf_list, "fcoe-intf-ifindex")
        if kwargs.pop('delete_fcoe_intf_ifindex', False) is True:
            delete_fcoe_intf_ifindex = config.find('.//*fcoe-intf-ifindex')
            delete_fcoe_intf_ifindex.set('operation', 'delete')
            
        fcoe_intf_ifindex.text = kwargs.pop('fcoe_intf_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_wwn = ET.SubElement(fcoe_intf_list, "fcoe-intf-wwn")
        if kwargs.pop('delete_fcoe_intf_wwn', False) is True:
            delete_fcoe_intf_wwn = config.find('.//*fcoe-intf-wwn')
            delete_fcoe_intf_wwn.set('operation', 'delete')
            
        fcoe_intf_wwn.text = kwargs.pop('fcoe_intf_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_enode_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-bind-type")
        if kwargs.pop('delete_fcoe_intf_enode_bind_type', False) is True:
            delete_fcoe_intf_enode_bind_type = config.find('.//*fcoe-intf-enode-bind-type')
            delete_fcoe_intf_enode_bind_type.set('operation', 'delete')
            
        fcoe_intf_enode_bind_type.text = kwargs.pop('fcoe_intf_enode_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_port_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-bind-type")
        if kwargs.pop('delete_fcoe_intf_port_bind_type', False) is True:
            delete_fcoe_intf_port_bind_type = config.find('.//*fcoe-intf-port-bind-type')
            delete_fcoe_intf_port_bind_type.set('operation', 'delete')
            
        fcoe_intf_port_bind_type.text = kwargs.pop('fcoe_intf_port_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_enode_mac_address = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-mac-address")
        if kwargs.pop('delete_fcoe_intf_enode_mac_address', False) is True:
            delete_fcoe_intf_enode_mac_address = config.find('.//*fcoe-intf-enode-mac-address')
            delete_fcoe_intf_enode_mac_address.set('operation', 'delete')
            
        fcoe_intf_enode_mac_address.text = kwargs.pop('fcoe_intf_enode_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vlan_disc_req(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_vlan_disc_req = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vlan-disc-req")
        if kwargs.pop('delete_fcoe_intf_rx_vlan_disc_req', False) is True:
            delete_fcoe_intf_rx_vlan_disc_req = config.find('.//*fcoe-intf-rx-vlan-disc-req')
            delete_fcoe_intf_rx_vlan_disc_req.set('operation', 'delete')
            
        fcoe_intf_rx_vlan_disc_req.text = kwargs.pop('fcoe_intf_rx_vlan_disc_req')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_disc_solicitations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_disc_solicitations = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-disc-solicitations")
        if kwargs.pop('delete_fcoe_intf_rx_disc_solicitations', False) is True:
            delete_fcoe_intf_rx_disc_solicitations = config.find('.//*fcoe-intf-rx-disc-solicitations')
            delete_fcoe_intf_rx_disc_solicitations.set('operation', 'delete')
            
        fcoe_intf_rx_disc_solicitations.text = kwargs.pop('fcoe_intf_rx_disc_solicitations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_flogi(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_flogi = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-flogi")
        if kwargs.pop('delete_fcoe_intf_rx_flogi', False) is True:
            delete_fcoe_intf_rx_flogi = config.find('.//*fcoe-intf-rx-flogi')
            delete_fcoe_intf_rx_flogi.set('operation', 'delete')
            
        fcoe_intf_rx_flogi.text = kwargs.pop('fcoe_intf_rx_flogi')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_fdiscs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_fdiscs = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-fdiscs")
        if kwargs.pop('delete_fcoe_intf_rx_fdiscs', False) is True:
            delete_fcoe_intf_rx_fdiscs = config.find('.//*fcoe-intf-rx-fdiscs')
            delete_fcoe_intf_rx_fdiscs.set('operation', 'delete')
            
        fcoe_intf_rx_fdiscs.text = kwargs.pop('fcoe_intf_rx_fdiscs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_logo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_logo = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-logo")
        if kwargs.pop('delete_fcoe_intf_rx_logo', False) is True:
            delete_fcoe_intf_rx_logo = config.find('.//*fcoe-intf-rx-logo')
            delete_fcoe_intf_rx_logo.set('operation', 'delete')
            
        fcoe_intf_rx_logo.text = kwargs.pop('fcoe_intf_rx_logo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_errors = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-errors")
        if kwargs.pop('delete_fcoe_intf_rx_errors', False) is True:
            delete_fcoe_intf_rx_errors = config.find('.//*fcoe-intf-rx-errors')
            delete_fcoe_intf_rx_errors.set('operation', 'delete')
            
        fcoe_intf_rx_errors.text = kwargs.pop('fcoe_intf_rx_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_vlan_disc_resp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_vlan_disc_resp = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-vlan-disc-resp")
        if kwargs.pop('delete_fcoe_intf_tx_vlan_disc_resp', False) is True:
            delete_fcoe_intf_tx_vlan_disc_resp = config.find('.//*fcoe-intf-tx-vlan-disc-resp')
            delete_fcoe_intf_tx_vlan_disc_resp.set('operation', 'delete')
            
        fcoe_intf_tx_vlan_disc_resp.text = kwargs.pop('fcoe_intf_tx_vlan_disc_resp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_sol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_disc_sol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-sol-adv")
        if kwargs.pop('delete_fcoe_intf_tx_disc_sol_adv', False) is True:
            delete_fcoe_intf_tx_disc_sol_adv = config.find('.//*fcoe-intf-tx-disc-sol-adv')
            delete_fcoe_intf_tx_disc_sol_adv.set('operation', 'delete')
            
        fcoe_intf_tx_disc_sol_adv.text = kwargs.pop('fcoe_intf_tx_disc_sol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_unsol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_disc_unsol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-unsol-adv")
        if kwargs.pop('delete_fcoe_intf_tx_disc_unsol_adv', False) is True:
            delete_fcoe_intf_tx_disc_unsol_adv = config.find('.//*fcoe-intf-tx-disc-unsol-adv')
            delete_fcoe_intf_tx_disc_unsol_adv.set('operation', 'delete')
            
        fcoe_intf_tx_disc_unsol_adv.text = kwargs.pop('fcoe_intf_tx_disc_unsol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_enode_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_enode_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-enode-ka")
        if kwargs.pop('delete_fcoe_intf_rx_enode_ka', False) is True:
            delete_fcoe_intf_rx_enode_ka = config.find('.//*fcoe-intf-rx-enode-ka')
            delete_fcoe_intf_rx_enode_ka.set('operation', 'delete')
            
        fcoe_intf_rx_enode_ka.text = kwargs.pop('fcoe_intf_rx_enode_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vnport_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_rx_vnport_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vnport-ka")
        if kwargs.pop('delete_fcoe_intf_rx_vnport_ka', False) is True:
            delete_fcoe_intf_rx_vnport_ka = config.find('.//*fcoe-intf-rx-vnport-ka')
            delete_fcoe_intf_rx_vnport_ka.set('operation', 'delete')
            
        fcoe_intf_rx_vnport_ka.text = kwargs.pop('fcoe_intf_rx_vnport_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_accepts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_accepts = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-accepts")
        if kwargs.pop('delete_fcoe_intf_tx_accepts', False) is True:
            delete_fcoe_intf_tx_accepts = config.find('.//*fcoe-intf-tx-accepts')
            delete_fcoe_intf_tx_accepts.set('operation', 'delete')
            
        fcoe_intf_tx_accepts.text = kwargs.pop('fcoe_intf_tx_accepts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_ls_rjt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_ls_rjt = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-ls-rjt")
        if kwargs.pop('delete_fcoe_intf_tx_ls_rjt', False) is True:
            delete_fcoe_intf_tx_ls_rjt = config.find('.//*fcoe-intf-tx-ls-rjt')
            delete_fcoe_intf_tx_ls_rjt.set('operation', 'delete')
            
        fcoe_intf_tx_ls_rjt.text = kwargs.pop('fcoe_intf_tx_ls_rjt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_time_since_last_change(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_time_since_last_change = ET.SubElement(fcoe_intf_list, "fcoe-intf-time-since-last-change")
        if kwargs.pop('delete_fcoe_intf_time_since_last_change', False) is True:
            delete_fcoe_intf_time_since_last_change = config.find('.//*fcoe-intf-time-since-last-change')
            delete_fcoe_intf_time_since_last_change.set('operation', 'delete')
            
        fcoe_intf_time_since_last_change.text = kwargs.pop('fcoe_intf_time_since_last_change')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_last_counters_cleared(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_last_counters_cleared = ET.SubElement(fcoe_intf_list, "fcoe-intf-last-counters-cleared")
        if kwargs.pop('delete_fcoe_intf_last_counters_cleared', False) is True:
            delete_fcoe_intf_last_counters_cleared = config.find('.//*fcoe-intf-last-counters-cleared')
            delete_fcoe_intf_last_counters_cleared.set('operation', 'delete')
            
        fcoe_intf_last_counters_cleared.text = kwargs.pop('fcoe_intf_last_counters_cleared')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_cvls(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        if kwargs.pop('delete_fcoe_intf_list', False) is True:
            delete_fcoe_intf_list = config.find('.//*fcoe-intf-list')
            delete_fcoe_intf_list.set('operation', 'delete')
            
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        if kwargs.pop('delete_fcoe_intf_fcoe_port_id', False) is True:
            delete_fcoe_intf_fcoe_port_id = config.find('.//*fcoe-intf-fcoe-port-id')
            delete_fcoe_intf_fcoe_port_id.set('operation', 'delete')
                
        fcoe_intf_tx_cvls = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-cvls")
        if kwargs.pop('delete_fcoe_intf_tx_cvls', False) is True:
            delete_fcoe_intf_tx_cvls = config.find('.//*fcoe-intf-tx-cvls')
            delete_fcoe_intf_tx_cvls.set('operation', 'delete')
            
        fcoe_intf_tx_cvls.text = kwargs.pop('fcoe_intf_tx_cvls')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_total_interfaces(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        if kwargs.pop('delete_fcoe_get_interface', False) is True:
            delete_fcoe_get_interface = config.find('.//*fcoe-get-interface')
            delete_fcoe_get_interface.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_intf_total_interfaces = ET.SubElement(output, "fcoe-intf-total-interfaces")
        if kwargs.pop('delete_fcoe_intf_total_interfaces', False) is True:
            delete_fcoe_intf_total_interfaces = config.find('.//*fcoe-intf-total-interfaces')
            delete_fcoe_intf_total_interfaces.set('operation', 'delete')
            
        fcoe_intf_total_interfaces.text = kwargs.pop('fcoe_intf_total_interfaces')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_login, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_login_interface = ET.SubElement(input, "fcoe-login-interface")
        if kwargs.pop('delete_fcoe_login_interface', False) is True:
            delete_fcoe_login_interface = config.find('.//*fcoe-login-interface')
            delete_fcoe_login_interface.set('operation', 'delete')
            
        fcoe_login_interface.text = kwargs.pop('fcoe_login_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vfid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_login, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_login_vfid = ET.SubElement(input, "fcoe-login-vfid")
        if kwargs.pop('delete_fcoe_login_vfid', False) is True:
            delete_fcoe_login_vfid = config.find('.//*fcoe-login-vfid')
            delete_fcoe_login_vfid.set('operation', 'delete')
            
        fcoe_login_vfid.text = kwargs.pop('fcoe_login_vfid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_login, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_login_vlan = ET.SubElement(input, "fcoe-login-vlan")
        if kwargs.pop('delete_fcoe_login_vlan', False) is True:
            delete_fcoe_login_vlan = config.find('.//*fcoe-login-vlan')
            delete_fcoe_login_vlan.set('operation', 'delete')
            
        fcoe_login_vlan.text = kwargs.pop('fcoe_login_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        input = ET.SubElement(fcoe_get_login, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        fcoe_login_rbridge_id = ET.SubElement(input, "fcoe-login-rbridge-id")
        if kwargs.pop('delete_fcoe_login_rbridge_id', False) is True:
            delete_fcoe_login_rbridge_id = config.find('.//*fcoe-login-rbridge-id')
            delete_fcoe_login_rbridge_id.set('operation', 'delete')
            
        fcoe_login_rbridge_id.text = kwargs.pop('fcoe_login_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_session_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
            
        fcoe_login_session_mac.text = kwargs.pop('fcoe_login_session_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_fcoe_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_fcoe_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-fcoe-interface-name")
        if kwargs.pop('delete_fcoe_login_fcoe_interface_name', False) is True:
            delete_fcoe_login_fcoe_interface_name = config.find('.//*fcoe-login-fcoe-interface-name')
            delete_fcoe_login_fcoe_interface_name.set('operation', 'delete')
            
        fcoe_login_fcoe_interface_name.text = kwargs.pop('fcoe_login_fcoe_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-interface-name")
        if kwargs.pop('delete_fcoe_login_interface_name', False) is True:
            delete_fcoe_login_interface_name = config.find('.//*fcoe-login-interface-name')
            delete_fcoe_login_interface_name.set('operation', 'delete')
            
        fcoe_login_interface_name.text = kwargs.pop('fcoe_login_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        interface_type = ET.SubElement(fcoe_login_list, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        interface_name = ET.SubElement(fcoe_login_list, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_device_wwn = ET.SubElement(fcoe_login_list, "fcoe-login-device-wwn")
        if kwargs.pop('delete_fcoe_login_device_wwn', False) is True:
            delete_fcoe_login_device_wwn = config.find('.//*fcoe-login-device-wwn')
            delete_fcoe_login_device_wwn.set('operation', 'delete')
            
        fcoe_login_device_wwn.text = kwargs.pop('fcoe_login_device_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_device_mac = ET.SubElement(fcoe_login_list, "fcoe-login-device-mac")
        if kwargs.pop('delete_fcoe_login_device_mac', False) is True:
            delete_fcoe_login_device_mac = config.find('.//*fcoe-login-device-mac')
            delete_fcoe_login_device_mac.set('operation', 'delete')
            
        fcoe_login_device_mac.text = kwargs.pop('fcoe_login_device_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_direct_attached(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_direct_attached = ET.SubElement(fcoe_login_list, "fcoe-login-direct-attached")
        if kwargs.pop('delete_fcoe_login_direct_attached', False) is True:
            delete_fcoe_login_direct_attached = config.find('.//*fcoe-login-direct-attached')
            delete_fcoe_login_direct_attached.set('operation', 'delete')
            
        fcoe_login_direct_attached.text = kwargs.pop('fcoe_login_direct_attached')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_connected_peer_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        if kwargs.pop('delete_fcoe_login_list', False) is True:
            delete_fcoe_login_list = config.find('.//*fcoe-login-list')
            delete_fcoe_login_list.set('operation', 'delete')
            
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        if kwargs.pop('delete_fcoe_login_session_mac', False) is True:
            delete_fcoe_login_session_mac = config.find('.//*fcoe-login-session-mac')
            delete_fcoe_login_session_mac.set('operation', 'delete')
                
        fcoe_login_connected_peer_type = ET.SubElement(fcoe_login_list, "fcoe-login-connected-peer-type")
        if kwargs.pop('delete_fcoe_login_connected_peer_type', False) is True:
            delete_fcoe_login_connected_peer_type = config.find('.//*fcoe-login-connected-peer-type')
            delete_fcoe_login_connected_peer_type.set('operation', 'delete')
            
        fcoe_login_connected_peer_type.text = kwargs.pop('fcoe_login_connected_peer_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_total_logins(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        if kwargs.pop('delete_fcoe_get_login', False) is True:
            delete_fcoe_get_login = config.find('.//*fcoe-get-login')
            delete_fcoe_get_login.set('operation', 'delete')
            
        output = ET.SubElement(fcoe_get_login, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        fcoe_login_total_logins = ET.SubElement(output, "fcoe-login-total-logins")
        if kwargs.pop('delete_fcoe_login_total_logins', False) is True:
            delete_fcoe_login_total_logins = config.find('.//*fcoe-login-total-logins')
            delete_fcoe_login_total_logins.set('operation', 'delete')
            
        fcoe_login_total_logins.text = kwargs.pop('fcoe_login_total_logins')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        