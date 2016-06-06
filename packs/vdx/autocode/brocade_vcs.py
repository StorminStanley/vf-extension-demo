#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_vcs(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def vcsmode_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcsmode', False) is True:
            delete_vcsmode = config.find('.//*vcsmode')
            delete_vcsmode.set('operation', 'delete')
            
        vcs_mode = ET.SubElement(vcsmode, "vcs-mode")
        if kwargs.pop('delete_vcs_mode', False) is True:
            delete_vcs_mode = config.find('.//*vcs-mode')
            delete_vcs_mode.set('operation', 'delete')
            
        vcs_mode.text = kwargs.pop('vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsmode_vcs_cluster_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcsmode', False) is True:
            delete_vcsmode = config.find('.//*vcsmode')
            delete_vcsmode.set('operation', 'delete')
            
        vcs_cluster_mode = ET.SubElement(vcsmode, "vcs-cluster-mode")
        if kwargs.pop('delete_vcs_cluster_mode', False) is True:
            delete_vcs_cluster_mode = config.find('.//*vcs-cluster-mode')
            delete_vcs_cluster_mode.set('operation', 'delete')
            
        vcs_cluster_mode.text = kwargs.pop('vcs_cluster_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def local_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        local_node = ET.SubElement(config, "local-node", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_local_node', False) is True:
            delete_local_node = config.find('.//*local-node')
            delete_local_node.set('operation', 'delete')
            
        swbd_number = ET.SubElement(local_node, "swbd-number")
        if kwargs.pop('delete_swbd_number', False) is True:
            delete_swbd_number = config.find('.//*swbd-number')
            delete_swbd_number.set('operation', 'delete')
            
        swbd_number.text = kwargs.pop('swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_output_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time = ET.Element("get_last_config_update_time")
        config = get_last_config_update_time
        if kwargs.pop('delete_get_last_config_update_time', False) is True:
            delete_get_last_config_update_time = config.find('.//*get-last-config-update-time')
            delete_get_last_config_update_time.set('operation', 'delete')
            
        output = ET.SubElement(get_last_config_update_time, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_config_update_time = ET.SubElement(output, "last-config-update-time")
        if kwargs.pop('delete_last_config_update_time', False) is True:
            delete_last_config_update_time = config.find('.//*last-config-update-time')
            delete_last_config_update_time.set('operation', 'delete')
            
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        principal_switch_wwn = ET.SubElement(output, "principal-switch-wwn")
        if kwargs.pop('delete_principal_switch_wwn', False) is True:
            delete_principal_switch_wwn = config.find('.//*principal-switch-wwn')
            delete_principal_switch_wwn.set('operation', 'delete')
            
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        co_ordinator_wwn = ET.SubElement(output, "co-ordinator-wwn")
        if kwargs.pop('delete_co_ordinator_wwn', False) is True:
            delete_co_ordinator_wwn = config.find('.//*co-ordinator-wwn')
            delete_co_ordinator_wwn.set('operation', 'delete')
            
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_cluster_type_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_cluster_type_info = ET.SubElement(output, "vcs-cluster-type-info")
        if kwargs.pop('delete_vcs_cluster_type_info', False) is True:
            delete_vcs_cluster_type_info = config.find('.//*vcs-cluster-type-info')
            delete_vcs_cluster_type_info.set('operation', 'delete')
            
        vcs_cluster_type_info.text = kwargs.pop('vcs_cluster_type_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_guid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_guid = ET.SubElement(output, "vcs-guid")
        if kwargs.pop('delete_vcs_guid', False) is True:
            delete_vcs_guid = config.find('.//*vcs-guid')
            delete_vcs_guid.set('operation', 'delete')
            
        vcs_guid.text = kwargs.pop('vcs_guid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_virtual_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        virtual_ip_address = ET.SubElement(output, "virtual-ip-address")
        if kwargs.pop('delete_virtual_ip_address', False) is True:
            delete_virtual_ip_address = config.find('.//*virtual-ip-address')
            delete_virtual_ip_address.set('operation', 'delete')
            
        virtual_ip_address.text = kwargs.pop('virtual_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_virtual_ipv6_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        virtual_ipv6_address = ET.SubElement(output, "virtual-ipv6-address")
        if kwargs.pop('delete_virtual_ipv6_address', False) is True:
            delete_virtual_ipv6_address = config.find('.//*virtual-ipv6-address')
            delete_virtual_ipv6_address.set('operation', 'delete')
            
        virtual_ipv6_address.text = kwargs.pop('virtual_ipv6_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_total_nodes_in_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        total_nodes_in_cluster = ET.SubElement(output, "total-nodes-in-cluster")
        if kwargs.pop('delete_total_nodes_in_cluster', False) is True:
            delete_total_nodes_in_cluster = config.find('.//*total-nodes-in-cluster')
            delete_total_nodes_in_cluster.set('operation', 'delete')
            
        total_nodes_in_cluster.text = kwargs.pop('total_nodes_in_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_nodes_disconnected_from_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        nodes_disconnected_from_cluster = ET.SubElement(output, "nodes-disconnected-from-cluster")
        if kwargs.pop('delete_nodes_disconnected_from_cluster', False) is True:
            delete_nodes_disconnected_from_cluster = config.find('.//*nodes-disconnected-from-cluster')
            delete_nodes_disconnected_from_cluster.set('operation', 'delete')
            
        nodes_disconnected_from_cluster.text = kwargs.pop('nodes_disconnected_from_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_generic_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_generic_status = ET.SubElement(output, "cluster-generic-status")
        if kwargs.pop('delete_cluster_generic_status', False) is True:
            delete_cluster_generic_status = config.find('.//*cluster-generic-status')
            delete_cluster_generic_status.set('operation', 'delete')
            
        cluster_generic_status.text = kwargs.pop('cluster_generic_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_specific_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cluster_specific_status = ET.SubElement(output, "cluster-specific-status")
        if kwargs.pop('delete_cluster_specific_status', False) is True:
            delete_cluster_specific_status = config.find('.//*cluster-specific-status')
            delete_cluster_specific_status.set('operation', 'delete')
            
        cluster_specific_status.text = kwargs.pop('cluster_specific_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_num = ET.SubElement(vcs_node_info, "node-num")
        if kwargs.pop('delete_node_num', False) is True:
            delete_node_num = config.find('.//*node-num')
            delete_node_num.set('operation', 'delete')
            
        node_num.text = kwargs.pop('node_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_serial_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_serial_num = ET.SubElement(vcs_node_info, "node-serial-num")
        if kwargs.pop('delete_node_serial_num', False) is True:
            delete_node_serial_num = config.find('.//*node-serial-num')
            delete_node_serial_num.set('operation', 'delete')
            
        node_serial_num.text = kwargs.pop('node_serial_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_condition(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_condition = ET.SubElement(vcs_node_info, "node-condition")
        if kwargs.pop('delete_node_condition', False) is True:
            delete_node_condition = config.find('.//*node-condition')
            delete_node_condition.set('operation', 'delete')
            
        node_condition.text = kwargs.pop('node_condition')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_status = ET.SubElement(vcs_node_info, "node-status")
        if kwargs.pop('delete_node_status', False) is True:
            delete_node_status = config.find('.//*node-status')
            delete_node_status.set('operation', 'delete')
            
        node_status.text = kwargs.pop('node_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_hw_sync_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_hw_sync_state = ET.SubElement(vcs_node_info, "node-hw-sync-state")
        if kwargs.pop('delete_node_hw_sync_state', False) is True:
            delete_node_hw_sync_state = config.find('.//*node-hw-sync-state')
            delete_node_hw_sync_state.set('operation', 'delete')
            
        node_hw_sync_state.text = kwargs.pop('node_hw_sync_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_vcs_mode = ET.SubElement(vcs_node_info, "node-vcs-mode")
        if kwargs.pop('delete_node_vcs_mode', False) is True:
            delete_node_vcs_mode = config.find('.//*node-vcs-mode')
            delete_node_vcs_mode.set('operation', 'delete')
            
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_vcs_id = ET.SubElement(vcs_node_info, "node-vcs-id")
        if kwargs.pop('delete_node_vcs_id', False) is True:
            delete_node_vcs_id = config.find('.//*node-vcs-id')
            delete_node_vcs_id.set('operation', 'delete')
            
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_rbridge_id = ET.SubElement(vcs_node_info, "node-rbridge-id")
        if kwargs.pop('delete_node_rbridge_id', False) is True:
            delete_node_rbridge_id = config.find('.//*node-rbridge-id')
            delete_node_rbridge_id.set('operation', 'delete')
            
        node_rbridge_id.text = kwargs.pop('node_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_is_principal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_is_principal = ET.SubElement(vcs_node_info, "node-is-principal")
        if kwargs.pop('delete_node_is_principal', False) is True:
            delete_node_is_principal = config.find('.//*node-is-principal')
            delete_node_is_principal.set('operation', 'delete')
            
        node_is_principal.text = kwargs.pop('node_is_principal')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_co_ordinator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        co_ordinator = ET.SubElement(vcs_node_info, "co-ordinator")
        if kwargs.pop('delete_co_ordinator', False) is True:
            delete_co_ordinator = config.find('.//*co-ordinator')
            delete_co_ordinator.set('operation', 'delete')
            
        co_ordinator.text = kwargs.pop('co_ordinator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switch_mac = ET.SubElement(vcs_node_info, "node-switch-mac")
        if kwargs.pop('delete_node_switch_mac', False) is True:
            delete_node_switch_mac = config.find('.//*node-switch-mac')
            delete_node_switch_mac.set('operation', 'delete')
            
        node_switch_mac.text = kwargs.pop('node_switch_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switch_wwn = ET.SubElement(vcs_node_info, "node-switch-wwn")
        if kwargs.pop('delete_node_switch_wwn', False) is True:
            delete_node_switch_wwn = config.find('.//*node-switch-wwn')
            delete_node_switch_wwn.set('operation', 'delete')
            
        node_switch_wwn.text = kwargs.pop('node_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_switch_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        switch_fcf_mac = ET.SubElement(vcs_node_info, "switch-fcf-mac")
        if kwargs.pop('delete_switch_fcf_mac', False) is True:
            delete_switch_fcf_mac = config.find('.//*switch-fcf-mac')
            delete_switch_fcf_mac.set('operation', 'delete')
            
        switch_fcf_mac.text = kwargs.pop('switch_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_internal_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_internal_ip_address = ET.SubElement(vcs_node_info, "node-internal-ip-address")
        if kwargs.pop('delete_node_internal_ip_address', False) is True:
            delete_node_internal_ip_address = config.find('.//*node-internal-ip-address')
            delete_node_internal_ip_address.set('operation', 'delete')
            
        node_internal_ip_address.text = kwargs.pop('node_internal_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ip_addresses_node_public_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_public_ip_addresses = ET.SubElement(vcs_node_info, "node-public-ip-addresses")
        if kwargs.pop('delete_node_public_ip_addresses', False) is True:
            delete_node_public_ip_addresses = config.find('.//*node-public-ip-addresses')
            delete_node_public_ip_addresses.set('operation', 'delete')
            
        node_public_ip_address = ET.SubElement(node_public_ip_addresses, "node-public-ip-address")
        if kwargs.pop('delete_node_public_ip_address', False) is True:
            delete_node_public_ip_address = config.find('.//*node-public-ip-address')
            delete_node_public_ip_address.set('operation', 'delete')
            
        node_public_ip_address.text = kwargs.pop('node_public_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ipv6_addresses_node_public_ipv6_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_public_ipv6_addresses = ET.SubElement(vcs_node_info, "node-public-ipv6-addresses")
        if kwargs.pop('delete_node_public_ipv6_addresses', False) is True:
            delete_node_public_ipv6_addresses = config.find('.//*node-public-ipv6-addresses')
            delete_node_public_ipv6_addresses.set('operation', 'delete')
            
        node_public_ipv6_address = ET.SubElement(node_public_ipv6_addresses, "node-public-ipv6-address")
        if kwargs.pop('delete_node_public_ipv6_address', False) is True:
            delete_node_public_ipv6_address = config.find('.//*node-public-ipv6-address')
            delete_node_public_ipv6_address.set('operation', 'delete')
            
        node_public_ipv6_address.text = kwargs.pop('node_public_ipv6_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_firmware_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        firmware_version = ET.SubElement(vcs_node_info, "firmware-version")
        if kwargs.pop('delete_firmware_version', False) is True:
            delete_firmware_version = config.find('.//*firmware-version')
            delete_firmware_version.set('operation', 'delete')
            
        firmware_version.text = kwargs.pop('firmware_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_swbd_number = ET.SubElement(vcs_node_info, "node-swbd-number")
        if kwargs.pop('delete_node_swbd_number', False) is True:
            delete_node_swbd_number = config.find('.//*node-swbd-number')
            delete_node_swbd_number.set('operation', 'delete')
            
        node_swbd_number.text = kwargs.pop('node_swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switchname = ET.SubElement(vcs_node_info, "node-switchname")
        if kwargs.pop('delete_node_switchname', False) is True:
            delete_node_switchname = config.find('.//*node-switchname')
            delete_node_switchname.set('operation', 'delete')
            
        node_switchname.text = kwargs.pop('node_switchname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchtype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switchtype = ET.SubElement(vcs_node_info, "node-switchtype")
        if kwargs.pop('delete_node_switchtype', False) is True:
            delete_node_switchtype = config.find('.//*node-switchtype')
            delete_node_switchtype.set('operation', 'delete')
            
        node_switchtype.text = kwargs.pop('node_switchtype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_subtype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switch_subtype = ET.SubElement(vcs_node_info, "node-switch-subtype")
        if kwargs.pop('delete_node_switch_subtype', False) is True:
            delete_node_switch_subtype = config.find('.//*node-switch-subtype')
            delete_node_switch_subtype.set('operation', 'delete')
            
        node_switch_subtype.text = kwargs.pop('node_switch_subtype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_switch_description = ET.SubElement(vcs_node_info, "node-switch-description")
        if kwargs.pop('delete_node_switch_description', False) is True:
            delete_node_switch_description = config.find('.//*node-switch-description')
            delete_node_switch_description.set('operation', 'delete')
            
        node_switch_description.text = kwargs.pop('node_switch_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_manufacturer_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        manufacturer_name = ET.SubElement(vcs_node_info, "manufacturer-name")
        if kwargs.pop('delete_manufacturer_name', False) is True:
            delete_manufacturer_name = config.find('.//*manufacturer-name')
            delete_manufacturer_name.set('operation', 'delete')
            
        manufacturer_name.text = kwargs.pop('manufacturer_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_state = ET.SubElement(vcs_node_info, "node-state")
        if kwargs.pop('delete_node_state', False) is True:
            delete_node_state = config.find('.//*node-state')
            delete_node_state.set('operation', 'delete')
            
        node_state.text = kwargs.pop('node_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_fabric_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        if kwargs.pop('delete_show_vcs', False) is True:
            delete_show_vcs = config.find('.//*show-vcs')
            delete_show_vcs.set('operation', 'delete')
            
        output = ET.SubElement(show_vcs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        if kwargs.pop('delete_vcs_nodes', False) is True:
            delete_vcs_nodes = config.find('.//*vcs-nodes')
            delete_vcs_nodes.set('operation', 'delete')
            
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        if kwargs.pop('delete_vcs_node_info', False) is True:
            delete_vcs_node_info = config.find('.//*vcs-node-info')
            delete_vcs_node_info.set('operation', 'delete')
            
        node_fabric_state = ET.SubElement(vcs_node_info, "node-fabric-state")
        if kwargs.pop('delete_node_fabric_state', False) is True:
            delete_node_fabric_state = config.find('.//*node-fabric-state')
            delete_node_fabric_state.set('operation', 'delete')
            
        node_fabric_state.text = kwargs.pop('node_fabric_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        principal_switch_wwn = ET.SubElement(vcs_details, "principal-switch-wwn")
        if kwargs.pop('delete_principal_switch_wwn', False) is True:
            delete_principal_switch_wwn = config.find('.//*principal-switch-wwn')
            delete_principal_switch_wwn.set('operation', 'delete')
            
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        co_ordinator_wwn = ET.SubElement(vcs_details, "co-ordinator-wwn")
        if kwargs.pop('delete_co_ordinator_wwn', False) is True:
            delete_co_ordinator_wwn = config.find('.//*co-ordinator-wwn')
            delete_co_ordinator_wwn.set('operation', 'delete')
            
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_local_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        local_switch_wwn = ET.SubElement(vcs_details, "local-switch-wwn")
        if kwargs.pop('delete_local_switch_wwn', False) is True:
            delete_local_switch_wwn = config.find('.//*local-switch-wwn')
            delete_local_switch_wwn.set('operation', 'delete')
            
        local_switch_wwn.text = kwargs.pop('local_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        node_vcs_mode = ET.SubElement(vcs_details, "node-vcs-mode")
        if kwargs.pop('delete_node_vcs_mode', False) is True:
            delete_node_vcs_mode = config.find('.//*node-vcs-mode')
            delete_node_vcs_mode.set('operation', 'delete')
            
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        node_vcs_type = ET.SubElement(vcs_details, "node-vcs-type")
        if kwargs.pop('delete_node_vcs_type', False) is True:
            delete_node_vcs_type = config.find('.//*node-vcs-type')
            delete_node_vcs_type.set('operation', 'delete')
            
        node_vcs_type.text = kwargs.pop('node_vcs_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        if kwargs.pop('delete_get_vcs_details', False) is True:
            delete_get_vcs_details = config.find('.//*get-vcs-details')
            delete_get_vcs_details.set('operation', 'delete')
            
        output = ET.SubElement(get_vcs_details, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vcs_details = ET.SubElement(output, "vcs-details")
        if kwargs.pop('delete_vcs_details', False) is True:
            delete_vcs_details = config.find('.//*vcs-details')
            delete_vcs_details.set('operation', 'delete')
            
        node_vcs_id = ET.SubElement(vcs_details, "node-vcs-id")
        if kwargs.pop('delete_node_vcs_id', False) is True:
            delete_node_vcs_id = config.find('.//*node-vcs-id')
            delete_node_vcs_id.set('operation', 'delete')
            
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_rbridge_config_input_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs_rbridge_config = ET.Element("vcs_rbridge_config")
        config = vcs_rbridge_config
        if kwargs.pop('delete_vcs_rbridge_config', False) is True:
            delete_vcs_rbridge_config = config.find('.//*vcs-rbridge-config')
            delete_vcs_rbridge_config.set('operation', 'delete')
            
        input = ET.SubElement(vcs_rbridge_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcs_id = ET.SubElement(input, "vcs-id")
        if kwargs.pop('delete_vcs_id', False) is True:
            delete_vcs_id = config.find('.//*vcs-id')
            delete_vcs_id.set('operation', 'delete')
            
        vcs_id.text = kwargs.pop('vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_rbridge_config_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs_rbridge_config = ET.Element("vcs_rbridge_config")
        config = vcs_rbridge_config
        if kwargs.pop('delete_vcs_rbridge_config', False) is True:
            delete_vcs_rbridge_config = config.find('.//*vcs-rbridge-config')
            delete_vcs_rbridge_config.set('operation', 'delete')
            
        input = ET.SubElement(vcs_rbridge_config, "input")
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
        
    def vcs_rbridge_context_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs_rbridge_context = ET.Element("vcs_rbridge_context")
        config = vcs_rbridge_context
        if kwargs.pop('delete_vcs_rbridge_context', False) is True:
            delete_vcs_rbridge_context = config.find('.//*vcs-rbridge-context')
            delete_vcs_rbridge_context.set('operation', 'delete')
            
        input = ET.SubElement(vcs_rbridge_context, "input")
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
        
    def get_last_config_update_time_for_xpaths_input_xpath_strings_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        if kwargs.pop('delete_get_last_config_update_time_for_xpaths', False) is True:
            delete_get_last_config_update_time_for_xpaths = config.find('.//*get-last-config-update-time-for-xpaths')
            delete_get_last_config_update_time_for_xpaths.set('operation', 'delete')
            
        input = ET.SubElement(get_last_config_update_time_for_xpaths, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        xpath_strings = ET.SubElement(input, "xpath-strings")
        if kwargs.pop('delete_xpath_strings', False) is True:
            delete_xpath_strings = config.find('.//*xpath-strings')
            delete_xpath_strings.set('operation', 'delete')
            
        xpath_string = ET.SubElement(xpath_strings, "xpath-string")
        if kwargs.pop('delete_xpath_string', False) is True:
            delete_xpath_string = config.find('.//*xpath-string')
            delete_xpath_string.set('operation', 'delete')
            
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        if kwargs.pop('delete_get_last_config_update_time_for_xpaths', False) is True:
            delete_get_last_config_update_time_for_xpaths = config.find('.//*get-last-config-update-time-for-xpaths')
            delete_get_last_config_update_time_for_xpaths.set('operation', 'delete')
            
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        if kwargs.pop('delete_last_config_update_time_for_xpaths', False) is True:
            delete_last_config_update_time_for_xpaths = config.find('.//*last-config-update-time-for-xpaths')
            delete_last_config_update_time_for_xpaths.set('operation', 'delete')
            
        xpath_string = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        if kwargs.pop('delete_xpath_string', False) is True:
            delete_xpath_string = config.find('.//*xpath-string')
            delete_xpath_string.set('operation', 'delete')
            
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        if kwargs.pop('delete_get_last_config_update_time_for_xpaths', False) is True:
            delete_get_last_config_update_time_for_xpaths = config.find('.//*get-last-config-update-time-for-xpaths')
            delete_get_last_config_update_time_for_xpaths.set('operation', 'delete')
            
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        if kwargs.pop('delete_last_config_update_time_for_xpaths', False) is True:
            delete_last_config_update_time_for_xpaths = config.find('.//*last-config-update-time-for-xpaths')
            delete_last_config_update_time_for_xpaths.set('operation', 'delete')
            
        xpath_string_key = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        xpath_string_key.text = kwargs.pop('xpath_string')
        if kwargs.pop('delete_xpath_string', False) is True:
            delete_xpath_string = config.find('.//*xpath-string')
            delete_xpath_string.set('operation', 'delete')
                
        last_config_update_time = ET.SubElement(last_config_update_time_for_xpaths, "last-config-update-time")
        if kwargs.pop('delete_last_config_update_time', False) is True:
            delete_last_config_update_time = config.find('.//*last-config-update-time')
            delete_last_config_update_time.set('operation', 'delete')
            
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        virtual = ET.SubElement(vcs, "virtual")
        if kwargs.pop('delete_virtual', False) is True:
            delete_virtual = config.find('.//*virtual')
            delete_virtual.set('operation', 'delete')
            
        ip = ET.SubElement(virtual, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        address = ET.SubElement(ip, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address = ET.SubElement(address, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_inband_interface_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        virtual = ET.SubElement(vcs, "virtual")
        if kwargs.pop('delete_virtual', False) is True:
            delete_virtual = config.find('.//*virtual')
            delete_virtual.set('operation', 'delete')
            
        ip = ET.SubElement(virtual, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        address = ET.SubElement(ip, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address_key = ET.SubElement(address, "address")
        address_key.text = kwargs.pop('address')
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
                
        inband = ET.SubElement(address, "inband")
        if kwargs.pop('delete_inband', False) is True:
            delete_inband = config.find('.//*inband')
            delete_inband.set('operation', 'delete')
            
        interface = ET.SubElement(inband, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        ve = ET.SubElement(interface, "ve")
        if kwargs.pop('delete_ve', False) is True:
            delete_ve = config.find('.//*ve')
            delete_ve.set('operation', 'delete')
            
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ipv6_address_ipv6address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        virtual = ET.SubElement(vcs, "virtual")
        if kwargs.pop('delete_virtual', False) is True:
            delete_virtual = config.find('.//*virtual')
            delete_virtual.set('operation', 'delete')
            
        ipv6 = ET.SubElement(virtual, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        address = ET.SubElement(ipv6, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        ipv6address = ET.SubElement(address, "ipv6address")
        if kwargs.pop('delete_ipv6address', False) is True:
            delete_ipv6address = config.find('.//*ipv6address')
            delete_ipv6address.set('operation', 'delete')
            
        ipv6address.text = kwargs.pop('ipv6address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_fabric_vfab_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcs', False) is True:
            delete_vcs = config.find('.//*vcs')
            delete_vcs.set('operation', 'delete')
            
        virtual_fabric = ET.SubElement(vcs, "virtual-fabric")
        if kwargs.pop('delete_virtual_fabric', False) is True:
            delete_virtual_fabric = config.find('.//*virtual-fabric')
            delete_virtual_fabric.set('operation', 'delete')
            
        vfab_enable = ET.SubElement(virtual_fabric, "vfab-enable")
        if kwargs.pop('delete_vfab_enable', False) is True:
            delete_vfab_enable = config.find('.//*vfab-enable')
            delete_vfab_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsNodeState_nodeRbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsNodeState = ET.SubElement(config, "vcsNodeState", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcsNodeState', False) is True:
            delete_vcsNodeState = config.find('.//*vcsNodeState')
            delete_vcsNodeState.set('operation', 'delete')
            
        nodeRbridgeid = ET.SubElement(vcsNodeState, "nodeRbridgeid")
        if kwargs.pop('delete_nodeRbridgeid', False) is True:
            delete_nodeRbridgeid = config.find('.//*nodeRbridgeid')
            delete_nodeRbridgeid.set('operation', 'delete')
            
        nodeRbridgeid.text = kwargs.pop('nodeRbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsNodeState_nodeState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsNodeState = ET.SubElement(config, "vcsNodeState", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        if kwargs.pop('delete_vcsNodeState', False) is True:
            delete_vcsNodeState = config.find('.//*vcsNodeState')
            delete_vcsNodeState.set('operation', 'delete')
            
        nodeState = ET.SubElement(vcsNodeState, "nodeState")
        if kwargs.pop('delete_nodeState', False) is True:
            delete_nodeState = config.find('.//*nodeState')
            delete_nodeState.set('operation', 'delete')
            
        nodeState.text = kwargs.pop('nodeState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        