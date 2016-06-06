#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lag(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_port_channel_detail_input_request_type_get_request_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_port_channel_detail, "input")
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
            
        aggregator_id = ET.SubElement(get_request, "aggregator-id")
        if kwargs.pop('delete_aggregator_id', False) is True:
            delete_aggregator_id = config.find('.//*aggregator-id')
            delete_aggregator_id.set('operation', 'delete')
            
        aggregator_id.text = kwargs.pop('aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_input_request_type_get_next_request_last_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_port_channel_detail, "input")
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
            
        last_aggregator_id = ET.SubElement(get_next_request, "last-aggregator-id")
        if kwargs.pop('delete_last_aggregator_id', False) is True:
            delete_last_aggregator_id = config.find('.//*last-aggregator-id')
            delete_last_aggregator_id.set('operation', 'delete')
            
        last_aggregator_id.text = kwargs.pop('last_aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggregator_id = ET.SubElement(lacp, "aggregator-id")
        if kwargs.pop('delete_aggregator_id', False) is True:
            delete_aggregator_id = config.find('.//*aggregator-id')
            delete_aggregator_id.set('operation', 'delete')
            
        aggregator_id.text = kwargs.pop('aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggregator_type = ET.SubElement(lacp, "aggregator-type")
        if kwargs.pop('delete_aggregator_type', False) is True:
            delete_aggregator_type = config.find('.//*aggregator-type')
            delete_aggregator_type.set('operation', 'delete')
            
        aggregator_type.text = kwargs.pop('aggregator_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_isvlag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        isvlag = ET.SubElement(lacp, "isvlag")
        if kwargs.pop('delete_isvlag', False) is True:
            delete_isvlag = config.find('.//*isvlag')
            delete_isvlag.set('operation', 'delete')
            
        isvlag.text = kwargs.pop('isvlag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggregator_mode = ET.SubElement(lacp, "aggregator-mode")
        if kwargs.pop('delete_aggregator_mode', False) is True:
            delete_aggregator_mode = config.find('.//*aggregator-mode')
            delete_aggregator_mode.set('operation', 'delete')
            
        aggregator_mode.text = kwargs.pop('aggregator_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        admin_key = ET.SubElement(lacp, "admin-key")
        if kwargs.pop('delete_admin_key', False) is True:
            delete_admin_key = config.find('.//*admin-key')
            delete_admin_key.set('operation', 'delete')
            
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        oper_key = ET.SubElement(lacp, "oper-key")
        if kwargs.pop('delete_oper_key', False) is True:
            delete_oper_key = config.find('.//*oper-key')
            delete_oper_key.set('operation', 'delete')
            
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        if kwargs.pop('delete_actor_system_id', False) is True:
            delete_actor_system_id = config.find('.//*actor-system-id')
            delete_actor_system_id.set('operation', 'delete')
            
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        if kwargs.pop('delete_partner_system_id', False) is True:
            delete_partner_system_id = config.find('.//*partner-system-id')
            delete_partner_system_id.set('operation', 'delete')
            
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        system_priority = ET.SubElement(lacp, "system-priority")
        if kwargs.pop('delete_system_priority', False) is True:
            delete_system_priority = config.find('.//*system-priority')
            delete_system_priority.set('operation', 'delete')
            
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        if kwargs.pop('delete_partner_oper_priority', False) is True:
            delete_partner_oper_priority = config.find('.//*partner-oper-priority')
            delete_partner_oper_priority.set('operation', 'delete')
            
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_rx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        rx_link_count = ET.SubElement(lacp, "rx-link-count")
        if kwargs.pop('delete_rx_link_count', False) is True:
            delete_rx_link_count = config.find('.//*rx-link-count')
            delete_rx_link_count.set('operation', 'delete')
            
        rx_link_count.text = kwargs.pop('rx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_tx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        tx_link_count = ET.SubElement(lacp, "tx-link-count")
        if kwargs.pop('delete_tx_link_count', False) is True:
            delete_tx_link_count = config.find('.//*tx-link-count')
            delete_tx_link_count.set('operation', 'delete')
            
        tx_link_count.text = kwargs.pop('tx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_individual_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        individual_agg = ET.SubElement(lacp, "individual-agg")
        if kwargs.pop('delete_individual_agg', False) is True:
            delete_individual_agg = config.find('.//*individual-agg')
            delete_individual_agg.set('operation', 'delete')
            
        individual_agg.text = kwargs.pop('individual_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_ready_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        ready_agg = ET.SubElement(lacp, "ready-agg")
        if kwargs.pop('delete_ready_agg', False) is True:
            delete_ready_agg = config.find('.//*ready-agg')
            delete_ready_agg.set('operation', 'delete')
            
        ready_agg.text = kwargs.pop('ready_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_oper_key = ET.SubElement(lacp, "partner-oper-key")
        if kwargs.pop('delete_partner_oper_key', False) is True:
            delete_partner_oper_key = config.find('.//*partner-oper-key')
            delete_partner_oper_key.set('operation', 'delete')
            
        partner_oper_key.text = kwargs.pop('partner_oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggr_member = ET.SubElement(lacp, "aggr-member")
        if kwargs.pop('delete_aggr_member', False) is True:
            delete_aggr_member = config.find('.//*aggr-member')
            delete_aggr_member.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(aggr_member, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggr_member = ET.SubElement(lacp, "aggr-member")
        if kwargs.pop('delete_aggr_member', False) is True:
            delete_aggr_member = config.find('.//*aggr-member')
            delete_aggr_member.set('operation', 'delete')
            
        interface_type = ET.SubElement(aggr_member, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggr_member = ET.SubElement(lacp, "aggr-member")
        if kwargs.pop('delete_aggr_member', False) is True:
            delete_aggr_member = config.find('.//*aggr-member')
            delete_aggr_member.set('operation', 'delete')
            
        interface_name = ET.SubElement(aggr_member, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggr_member = ET.SubElement(lacp, "aggr-member")
        if kwargs.pop('delete_aggr_member', False) is True:
            delete_aggr_member = config.find('.//*aggr-member')
            delete_aggr_member.set('operation', 'delete')
            
        actor_port = ET.SubElement(aggr_member, "actor-port")
        if kwargs.pop('delete_actor_port', False) is True:
            delete_actor_port = config.find('.//*actor-port')
            delete_actor_port.set('operation', 'delete')
            
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        aggr_member = ET.SubElement(lacp, "aggr-member")
        if kwargs.pop('delete_aggr_member', False) is True:
            delete_aggr_member = config.find('.//*aggr-member')
            delete_aggr_member.set('operation', 'delete')
            
        sync = ET.SubElement(aggr_member, "sync")
        if kwargs.pop('delete_sync', False) is True:
            delete_sync = config.find('.//*sync')
            delete_sync.set('operation', 'delete')
            
        sync.text = kwargs.pop('sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        if kwargs.pop('delete_get_port_channel_detail', False) is True:
            delete_get_port_channel_detail = config.find('.//*get-port-channel-detail')
            delete_get_port_channel_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_port_channel_detail, "output")
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
        
    def get_portchannel_info_by_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        interface_type = ET.SubElement(input, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        interface_name = ET.SubElement(input, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        interface_type = ET.SubElement(lacp, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        interface_name = ET.SubElement(lacp, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_port = ET.SubElement(lacp, "actor-port")
        if kwargs.pop('delete_actor_port', False) is True:
            delete_actor_port = config.find('.//*actor-port')
            delete_actor_port.set('operation', 'delete')
            
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        admin_key = ET.SubElement(lacp, "admin-key")
        if kwargs.pop('delete_admin_key', False) is True:
            delete_admin_key = config.find('.//*admin-key')
            delete_admin_key.set('operation', 'delete')
            
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        oper_key = ET.SubElement(lacp, "oper-key")
        if kwargs.pop('delete_oper_key', False) is True:
            delete_oper_key = config.find('.//*oper-key')
            delete_oper_key.set('operation', 'delete')
            
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        if kwargs.pop('delete_actor_system_id', False) is True:
            delete_actor_system_id = config.find('.//*actor-system-id')
            delete_actor_system_id.set('operation', 'delete')
            
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        if kwargs.pop('delete_partner_system_id', False) is True:
            delete_partner_system_id = config.find('.//*partner-system-id')
            delete_partner_system_id.set('operation', 'delete')
            
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        system_priority = ET.SubElement(lacp, "system-priority")
        if kwargs.pop('delete_system_priority', False) is True:
            delete_system_priority = config.find('.//*system-priority')
            delete_system_priority.set('operation', 'delete')
            
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        if kwargs.pop('delete_partner_oper_priority', False) is True:
            delete_partner_oper_priority = config.find('.//*partner-oper-priority')
            delete_partner_oper_priority.set('operation', 'delete')
            
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_priority = ET.SubElement(lacp, "actor-priority")
        if kwargs.pop('delete_actor_priority', False) is True:
            delete_actor_priority = config.find('.//*actor-priority')
            delete_actor_priority.set('operation', 'delete')
            
        actor_priority.text = kwargs.pop('actor_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_receive_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        receive_machine_state = ET.SubElement(lacp, "receive-machine-state")
        if kwargs.pop('delete_receive_machine_state', False) is True:
            delete_receive_machine_state = config.find('.//*receive-machine-state')
            delete_receive_machine_state.set('operation', 'delete')
            
        receive_machine_state.text = kwargs.pop('receive_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_periodic_transmission_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        periodic_transmission_machine_state = ET.SubElement(lacp, "periodic-transmission-machine-state")
        if kwargs.pop('delete_periodic_transmission_machine_state', False) is True:
            delete_periodic_transmission_machine_state = config.find('.//*periodic-transmission-machine-state')
            delete_periodic_transmission_machine_state.set('operation', 'delete')
            
        periodic_transmission_machine_state.text = kwargs.pop('periodic_transmission_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_mux_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        mux_machine_state = ET.SubElement(lacp, "mux-machine-state")
        if kwargs.pop('delete_mux_machine_state', False) is True:
            delete_mux_machine_state = config.find('.//*mux-machine-state')
            delete_mux_machine_state.set('operation', 'delete')
            
        mux_machine_state.text = kwargs.pop('mux_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        admin_state = ET.SubElement(lacp, "admin-state")
        if kwargs.pop('delete_admin_state', False) is True:
            delete_admin_state = config.find('.//*admin-state')
            delete_admin_state.set('operation', 'delete')
            
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        oper_state = ET.SubElement(lacp, "oper-state")
        if kwargs.pop('delete_oper_state', False) is True:
            delete_oper_state = config.find('.//*oper-state')
            delete_oper_state.set('operation', 'delete')
            
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_oper_state = ET.SubElement(lacp, "partner-oper-state")
        if kwargs.pop('delete_partner_oper_state', False) is True:
            delete_partner_oper_state = config.find('.//*partner-oper-state')
            delete_partner_oper_state.set('operation', 'delete')
            
        partner_oper_state.text = kwargs.pop('partner_oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_oper_port = ET.SubElement(lacp, "partner-oper-port")
        if kwargs.pop('delete_partner_oper_port', False) is True:
            delete_partner_oper_port = config.find('.//*partner-oper-port')
            delete_partner_oper_port.set('operation', 'delete')
            
        partner_oper_port.text = kwargs.pop('partner_oper_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_chip_number = ET.SubElement(lacp, "actor-chip-number")
        if kwargs.pop('delete_actor_chip_number', False) is True:
            delete_actor_chip_number = config.find('.//*actor-chip-number')
            delete_actor_chip_number.set('operation', 'delete')
            
        actor_chip_number.text = kwargs.pop('actor_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_max_deskew = ET.SubElement(lacp, "actor-max-deskew")
        if kwargs.pop('delete_actor_max_deskew', False) is True:
            delete_actor_max_deskew = config.find('.//*actor-max-deskew')
            delete_actor_max_deskew.set('operation', 'delete')
            
        actor_max_deskew.text = kwargs.pop('actor_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_chip_number = ET.SubElement(lacp, "partner-chip-number")
        if kwargs.pop('delete_partner_chip_number', False) is True:
            delete_partner_chip_number = config.find('.//*partner-chip-number')
            delete_partner_chip_number.set('operation', 'delete')
            
        partner_chip_number.text = kwargs.pop('partner_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_max_deskew = ET.SubElement(lacp, "partner-max-deskew")
        if kwargs.pop('delete_partner_max_deskew', False) is True:
            delete_partner_max_deskew = config.find('.//*partner-max-deskew')
            delete_partner_max_deskew.set('operation', 'delete')
            
        partner_max_deskew.text = kwargs.pop('partner_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        actor_brcd_state = ET.SubElement(lacp, "actor-brcd-state")
        if kwargs.pop('delete_actor_brcd_state', False) is True:
            delete_actor_brcd_state = config.find('.//*actor-brcd-state')
            delete_actor_brcd_state.set('operation', 'delete')
            
        actor_brcd_state.text = kwargs.pop('actor_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        if kwargs.pop('delete_get_portchannel_info_by_intf', False) is True:
            delete_get_portchannel_info_by_intf = config.find('.//*get-portchannel-info-by-intf')
            delete_get_portchannel_info_by_intf.set('operation', 'delete')
            
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        lacp = ET.SubElement(output, "lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        partner_brcd_state = ET.SubElement(lacp, "partner-brcd-state")
        if kwargs.pop('delete_partner_brcd_state', False) is True:
            delete_partner_brcd_state = config.find('.//*partner-brcd-state')
            delete_partner_brcd_state.set('operation', 'delete')
            
        partner_brcd_state.text = kwargs.pop('partner_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        if kwargs.pop('delete_port_channel_redundancy_group', False) is True:
            delete_port_channel_redundancy_group = config.find('.//*port-channel-redundancy-group')
            delete_port_channel_redundancy_group.set('operation', 'delete')
            
        group_id = ET.SubElement(port_channel_redundancy_group, "group-id")
        if kwargs.pop('delete_group_id', False) is True:
            delete_group_id = config.find('.//*group-id')
            delete_group_id.set('operation', 'delete')
            
        group_id.text = kwargs.pop('group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        if kwargs.pop('delete_port_channel_redundancy_group', False) is True:
            delete_port_channel_redundancy_group = config.find('.//*port-channel-redundancy-group')
            delete_port_channel_redundancy_group.set('operation', 'delete')
            
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        if kwargs.pop('delete_group_id', False) is True:
            delete_group_id = config.find('.//*group-id')
            delete_group_id.set('operation', 'delete')
                
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        if kwargs.pop('delete_port_channel', False) is True:
            delete_port_channel = config.find('.//*port-channel')
            delete_port_channel.set('operation', 'delete')
            
        name = ET.SubElement(port_channel, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_port_channel_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        if kwargs.pop('delete_port_channel_redundancy_group', False) is True:
            delete_port_channel_redundancy_group = config.find('.//*port-channel-redundancy-group')
            delete_port_channel_redundancy_group.set('operation', 'delete')
            
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        if kwargs.pop('delete_group_id', False) is True:
            delete_group_id = config.find('.//*group-id')
            delete_group_id.set('operation', 'delete')
                
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        if kwargs.pop('delete_port_channel', False) is True:
            delete_port_channel = config.find('.//*port-channel')
            delete_port_channel.set('operation', 'delete')
            
        name_key = ET.SubElement(port_channel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        port_channel_active = ET.SubElement(port_channel, "port-channel-active")
        if kwargs.pop('delete_port_channel_active', False) is True:
            delete_port_channel_active = config.find('.//*port-channel-active')
            delete_port_channel_active.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        if kwargs.pop('delete_port_channel_redundancy_group', False) is True:
            delete_port_channel_redundancy_group = config.find('.//*port-channel-redundancy-group')
            delete_port_channel_redundancy_group.set('operation', 'delete')
            
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        if kwargs.pop('delete_group_id', False) is True:
            delete_group_id = config.find('.//*group-id')
            delete_group_id.set('operation', 'delete')
                
        activate = ET.SubElement(port_channel_redundancy_group, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        