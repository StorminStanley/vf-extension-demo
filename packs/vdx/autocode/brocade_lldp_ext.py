#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lldp_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_request = ET.SubElement(request_type, "get-request")
        if kwargs.pop('delete_get_request', False) is True:
            delete_get_request = config.find('.//*get-request')
            delete_get_request.set('operation', 'delete')
            
        interface_type = ET.SubElement(get_request, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_request = ET.SubElement(request_type, "get-request")
        if kwargs.pop('delete_get_request', False) is True:
            delete_get_request = config.find('.//*get-request')
            delete_get_request.set('operation', 'delete')
            
        interface_name = ET.SubElement(get_request, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_next_request_last_rcvd_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_next_request = ET.SubElement(request_type, "get-next-request")
        if kwargs.pop('delete_get_next_request', False) is True:
            delete_get_next_request = config.find('.//*get-next-request')
            delete_get_next_request.set('operation', 'delete')
            
        last_rcvd_ifindex = ET.SubElement(get_next_request, "last-rcvd-ifindex")
        if kwargs.pop('delete_last_rcvd_ifindex', False) is True:
            delete_last_rcvd_ifindex = config.find('.//*last-rcvd-ifindex')
            delete_last_rcvd_ifindex.set('operation', 'delete')
            
        last_rcvd_ifindex.text = kwargs.pop('last_rcvd_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_rbridge_specific_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        get_rbridge_specific = ET.SubElement(request_type, "get-rbridge-specific")
        if kwargs.pop('delete_get_rbridge_specific', False) is True:
            delete_get_rbridge_specific = config.find('.//*get-rbridge-specific')
            delete_get_rbridge_specific.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(get_rbridge_specific, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        local_interface_name = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
            
        local_interface_name.text = kwargs.pop('local_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        local_interface_mac = ET.SubElement(lldp_neighbor_detail, "local-interface-mac")
        if kwargs.pop('delete_local_interface_mac', False) is True:
            delete_local_interface_mac = config.find('.//*local-interface-mac')
            delete_local_interface_mac.set('operation', 'delete')
            
        local_interface_mac.text = kwargs.pop('local_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        local_interface_ifindex = ET.SubElement(lldp_neighbor_detail, "local-interface-ifindex")
        if kwargs.pop('delete_local_interface_ifindex', False) is True:
            delete_local_interface_ifindex = config.find('.//*local-interface-ifindex')
            delete_local_interface_ifindex.set('operation', 'delete')
            
        local_interface_ifindex.text = kwargs.pop('local_interface_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
            
        remote_interface_name.text = kwargs.pop('remote_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_interface_mac = ET.SubElement(lldp_neighbor_detail, "remote-interface-mac")
        if kwargs.pop('delete_remote_interface_mac', False) is True:
            delete_remote_interface_mac = config.find('.//*remote-interface-mac')
            delete_remote_interface_mac.set('operation', 'delete')
            
        remote_interface_mac.text = kwargs.pop('remote_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_management_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_management_address = ET.SubElement(lldp_neighbor_detail, "remote-management-address")
        if kwargs.pop('delete_remote_management_address', False) is True:
            delete_remote_management_address = config.find('.//*remote-management-address')
            delete_remote_management_address.set('operation', 'delete')
            
        remote_management_address.text = kwargs.pop('remote_management_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_unnum_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_unnum_interface_mac = ET.SubElement(lldp_neighbor_detail, "remote-unnum-interface-mac")
        if kwargs.pop('delete_remote_unnum_interface_mac', False) is True:
            delete_remote_unnum_interface_mac = config.find('.//*remote-unnum-interface-mac')
            delete_remote_unnum_interface_mac.set('operation', 'delete')
            
        remote_unnum_interface_mac.text = kwargs.pop('remote_unnum_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_unnum_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_unnum_ip_address = ET.SubElement(lldp_neighbor_detail, "remote-unnum-ip-address")
        if kwargs.pop('delete_remote_unnum_ip_address', False) is True:
            delete_remote_unnum_ip_address = config.find('.//*remote-unnum-ip-address')
            delete_remote_unnum_ip_address.set('operation', 'delete')
            
        remote_unnum_ip_address.text = kwargs.pop('remote_unnum_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_port_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_port_description = ET.SubElement(lldp_neighbor_detail, "remote-port-description")
        if kwargs.pop('delete_remote_port_description', False) is True:
            delete_remote_port_description = config.find('.//*remote-port-description')
            delete_remote_port_description.set('operation', 'delete')
            
        remote_port_description.text = kwargs.pop('remote_port_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_chassis_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_chassis_id = ET.SubElement(lldp_neighbor_detail, "remote-chassis-id")
        if kwargs.pop('delete_remote_chassis_id', False) is True:
            delete_remote_chassis_id = config.find('.//*remote-chassis-id')
            delete_remote_chassis_id.set('operation', 'delete')
            
        remote_chassis_id.text = kwargs.pop('remote_chassis_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_system_name = ET.SubElement(lldp_neighbor_detail, "remote-system-name")
        if kwargs.pop('delete_remote_system_name', False) is True:
            delete_remote_system_name = config.find('.//*remote-system-name')
            delete_remote_system_name.set('operation', 'delete')
            
        remote_system_name.text = kwargs.pop('remote_system_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remote_system_description = ET.SubElement(lldp_neighbor_detail, "remote-system-description")
        if kwargs.pop('delete_remote_system_description', False) is True:
            delete_remote_system_description = config.find('.//*remote-system-description')
            delete_remote_system_description.set('operation', 'delete')
            
        remote_system_description.text = kwargs.pop('remote_system_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_dead_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        dead_interval = ET.SubElement(lldp_neighbor_detail, "dead-interval")
        if kwargs.pop('delete_dead_interval', False) is True:
            delete_dead_interval = config.find('.//*dead-interval')
            delete_dead_interval.set('operation', 'delete')
            
        dead_interval.text = kwargs.pop('dead_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remaining_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        remaining_life = ET.SubElement(lldp_neighbor_detail, "remaining-life")
        if kwargs.pop('delete_remaining_life', False) is True:
            delete_remaining_life = config.find('.//*remaining-life')
            delete_remaining_life.set('operation', 'delete')
            
        remaining_life.text = kwargs.pop('remaining_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_transmitted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        lldp_pdu_transmitted = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-transmitted")
        if kwargs.pop('delete_lldp_pdu_transmitted', False) is True:
            delete_lldp_pdu_transmitted = config.find('.//*lldp-pdu-transmitted')
            delete_lldp_pdu_transmitted.set('operation', 'delete')
            
        lldp_pdu_transmitted.text = kwargs.pop('lldp_pdu_transmitted')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_received(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        if kwargs.pop('delete_lldp_neighbor_detail', False) is True:
            delete_lldp_neighbor_detail = config.find('.//*lldp-neighbor-detail')
            delete_lldp_neighbor_detail.set('operation', 'delete')
            
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        if kwargs.pop('delete_local_interface_name', False) is True:
            delete_local_interface_name = config.find('.//*local-interface-name')
            delete_local_interface_name.set('operation', 'delete')
                
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        if kwargs.pop('delete_remote_interface_name', False) is True:
            delete_remote_interface_name = config.find('.//*remote-interface-name')
            delete_remote_interface_name.set('operation', 'delete')
                
        lldp_pdu_received = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-received")
        if kwargs.pop('delete_lldp_pdu_received', False) is True:
            delete_lldp_pdu_received = config.find('.//*lldp-pdu-received')
            delete_lldp_pdu_received.set('operation', 'delete')
            
        lldp_pdu_received.text = kwargs.pop('lldp_pdu_received')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        if kwargs.pop('delete_get_lldp_neighbor_detail', False) is True:
            delete_get_lldp_neighbor_detail = config.find('.//*get-lldp-neighbor-detail')
            delete_get_lldp_neighbor_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        