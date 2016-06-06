#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_trilloam(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def l2traceroute_input_src_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        src_mac = ET.SubElement(input, "src-mac")
        if kwargs.pop('delete_src_mac', False) is True:
            delete_src_mac = config.find('.//*src-mac')
            delete_src_mac.set('operation', 'delete')
            
        src_mac.text = kwargs.pop('src_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_dest_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        dest_mac = ET.SubElement(input, "dest-mac")
        if kwargs.pop('delete_dest_mac', False) is True:
            delete_dest_mac = config.find('.//*dest-mac')
            delete_dest_mac.set('operation', 'delete')
            
        dest_mac.text = kwargs.pop('dest_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vlan_id = ET.SubElement(input, "vlan-id")
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
            
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(input, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocolType = ET.SubElement(input, "protocolType")
        if kwargs.pop('delete_protocolType', False) is True:
            delete_protocolType = config.find('.//*protocolType')
            delete_protocolType.set('operation', 'delete')
            
        IP = ET.SubElement(protocolType, "IP")
        if kwargs.pop('delete_IP', False) is True:
            delete_IP = config.find('.//*IP')
            delete_IP.set('operation', 'delete')
            
        src_ip = ET.SubElement(IP, "src-ip")
        if kwargs.pop('delete_src_ip', False) is True:
            delete_src_ip = config.find('.//*src-ip')
            delete_src_ip.set('operation', 'delete')
            
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocolType = ET.SubElement(input, "protocolType")
        if kwargs.pop('delete_protocolType', False) is True:
            delete_protocolType = config.find('.//*protocolType')
            delete_protocolType.set('operation', 'delete')
            
        IP = ET.SubElement(protocolType, "IP")
        if kwargs.pop('delete_IP', False) is True:
            delete_IP = config.find('.//*IP')
            delete_IP.set('operation', 'delete')
            
        dest_ip = ET.SubElement(IP, "dest-ip")
        if kwargs.pop('delete_dest_ip', False) is True:
            delete_dest_ip = config.find('.//*dest-ip')
            delete_dest_ip.set('operation', 'delete')
            
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocolType = ET.SubElement(input, "protocolType")
        if kwargs.pop('delete_protocolType', False) is True:
            delete_protocolType = config.find('.//*protocolType')
            delete_protocolType.set('operation', 'delete')
            
        IP = ET.SubElement(protocolType, "IP")
        if kwargs.pop('delete_IP', False) is True:
            delete_IP = config.find('.//*IP')
            delete_IP.set('operation', 'delete')
            
        l4protocol = ET.SubElement(IP, "l4protocol")
        if kwargs.pop('delete_l4protocol', False) is True:
            delete_l4protocol = config.find('.//*l4protocol')
            delete_l4protocol.set('operation', 'delete')
            
        l4protocol.text = kwargs.pop('l4protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocolType = ET.SubElement(input, "protocolType")
        if kwargs.pop('delete_protocolType', False) is True:
            delete_protocolType = config.find('.//*protocolType')
            delete_protocolType.set('operation', 'delete')
            
        IP = ET.SubElement(protocolType, "IP")
        if kwargs.pop('delete_IP', False) is True:
            delete_IP = config.find('.//*IP')
            delete_IP.set('operation', 'delete')
            
        l4_src_port = ET.SubElement(IP, "l4-src-port")
        if kwargs.pop('delete_l4_src_port', False) is True:
            delete_l4_src_port = config.find('.//*l4-src-port')
            delete_l4_src_port.set('operation', 'delete')
            
        l4_src_port.text = kwargs.pop('l4_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_dest_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        protocolType = ET.SubElement(input, "protocolType")
        if kwargs.pop('delete_protocolType', False) is True:
            delete_protocolType = config.find('.//*protocolType')
            delete_protocolType.set('operation', 'delete')
            
        IP = ET.SubElement(protocolType, "IP")
        if kwargs.pop('delete_IP', False) is True:
            delete_IP = config.find('.//*IP')
            delete_IP.set('operation', 'delete')
            
        l4_dest_port = ET.SubElement(IP, "l4-dest-port")
        if kwargs.pop('delete_l4_dest_port', False) is True:
            delete_l4_dest_port = config.find('.//*l4-dest-port')
            delete_l4_dest_port.set('operation', 'delete')
            
        l4_dest_port.text = kwargs.pop('l4_dest_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        session_id = ET.SubElement(output, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        if kwargs.pop('delete_l2traceroutedone', False) is True:
            delete_l2traceroutedone = config.find('.//*l2traceroutedone')
            delete_l2traceroutedone.set('operation', 'delete')
            
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        if kwargs.pop('delete_l2traceroute', False) is True:
            delete_l2traceroute = config.find('.//*l2traceroute')
            delete_l2traceroute.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        reason = ET.SubElement(output, "reason")
        if kwargs.pop('delete_reason', False) is True:
            delete_reason = config.find('.//*reason')
            delete_reason.set('operation', 'delete')
            
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        input = ET.SubElement(l2traceroute_result, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        session_id = ET.SubElement(input, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(l2_hop, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        ingress = ET.SubElement(l2_hop, "ingress")
        if kwargs.pop('delete_ingress', False) is True:
            delete_ingress = config.find('.//*ingress')
            delete_ingress.set('operation', 'delete')
            
        interface_type = ET.SubElement(ingress, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        ingress = ET.SubElement(l2_hop, "ingress")
        if kwargs.pop('delete_ingress', False) is True:
            delete_ingress = config.find('.//*ingress')
            delete_ingress.set('operation', 'delete')
            
        interface_name = ET.SubElement(ingress, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        egress = ET.SubElement(l2_hop, "egress")
        if kwargs.pop('delete_egress', False) is True:
            delete_egress = config.find('.//*egress')
            delete_egress.set('operation', 'delete')
            
        interface_type = ET.SubElement(egress, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        egress = ET.SubElement(l2_hop, "egress")
        if kwargs.pop('delete_egress', False) is True:
            delete_egress = config.find('.//*egress')
            delete_egress.set('operation', 'delete')
            
        interface_name = ET.SubElement(egress, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_roundtriptime(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        if kwargs.pop('delete_l2_hop_results', False) is True:
            delete_l2_hop_results = config.find('.//*l2-hop-results')
            delete_l2_hop_results.set('operation', 'delete')
            
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        if kwargs.pop('delete_l2_hop', False) is True:
            delete_l2_hop = config.find('.//*l2-hop')
            delete_l2_hop.set('operation', 'delete')
            
        roundtriptime = ET.SubElement(l2_hop, "roundtriptime")
        if kwargs.pop('delete_roundtriptime', False) is True:
            delete_roundtriptime = config.find('.//*roundtriptime')
            delete_roundtriptime.set('operation', 'delete')
            
        roundtriptime.text = kwargs.pop('roundtriptime')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        if kwargs.pop('delete_l2traceroutedone', False) is True:
            delete_l2traceroutedone = config.find('.//*l2traceroutedone')
            delete_l2traceroutedone.set('operation', 'delete')
            
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        if kwargs.pop('delete_l2traceroute_result', False) is True:
            delete_l2traceroute_result = config.find('.//*l2traceroute-result')
            delete_l2traceroute_result.set('operation', 'delete')
            
        output = ET.SubElement(l2traceroute_result, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        reason = ET.SubElement(output, "reason")
        if kwargs.pop('delete_reason', False) is True:
            delete_reason = config.find('.//*reason')
            delete_reason.set('operation', 'delete')
            
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        