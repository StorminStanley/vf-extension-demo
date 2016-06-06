#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_xstp_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_stp_brief_info_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        input = ET.SubElement(get_stp_brief_info, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_stp_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        stp_mode = ET.SubElement(spanning_tree_info, "stp-mode")
        if kwargs.pop('delete_stp_mode', False) is True:
            delete_stp_mode = config.find('.//*stp-mode')
            delete_stp_mode.set('operation', 'delete')
            
        stp_mode.text = kwargs.pop('stp_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(stp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(root_bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(stp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(stp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(root_bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(stp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(root_bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(stp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        bridge = ET.SubElement(stp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        bridge = ET.SubElement(stp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        bridge = ET.SubElement(stp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        bridge = ET.SubElement(stp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        bridge = ET.SubElement(stp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        stp = ET.SubElement(spanning_tree_mode, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        stp = ET.SubElement(stp, "stp")
        if kwargs.pop('delete_stp', False) is True:
            delete_stp = config.find('.//*stp')
            delete_stp.set('operation', 'delete')
            
        port = ET.SubElement(stp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(rstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(root_bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(rstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(rstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(root_bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(rstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(root_bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(rstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        bridge = ET.SubElement(rstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        bridge = ET.SubElement(rstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        bridge = ET.SubElement(rstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        bridge = ET.SubElement(rstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        bridge = ET.SubElement(rstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        transmit_hold_count = ET.SubElement(rstp, "transmit-hold-count")
        if kwargs.pop('delete_transmit_hold_count', False) is True:
            delete_transmit_hold_count = config.find('.//*transmit-hold-count')
            delete_transmit_hold_count.set('operation', 'delete')
            
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        migrate_time = ET.SubElement(rstp, "migrate-time")
        if kwargs.pop('delete_migrate_time', False) is True:
            delete_migrate_time = config.find('.//*migrate-time')
            delete_migrate_time.set('operation', 'delete')
            
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        rstp = ET.SubElement(rstp, "rstp")
        if kwargs.pop('delete_rstp', False) is True:
            delete_rstp = config.find('.//*rstp')
            delete_rstp.set('operation', 'delete')
            
        port = ET.SubElement(rstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(mstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(root_bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(mstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(mstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(root_bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(mstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(root_bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        root_bridge = ET.SubElement(mstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        bridge = ET.SubElement(mstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        bridge = ET.SubElement(mstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        bridge = ET.SubElement(mstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        bridge = ET.SubElement(mstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        bridge = ET.SubElement(mstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        transmit_hold_count = ET.SubElement(mstp, "transmit-hold-count")
        if kwargs.pop('delete_transmit_hold_count', False) is True:
            delete_transmit_hold_count = config.find('.//*transmit-hold-count')
            delete_transmit_hold_count.set('operation', 'delete')
            
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        migrate_time = ET.SubElement(mstp, "migrate-time")
        if kwargs.pop('delete_migrate_time', False) is True:
            delete_migrate_time = config.find('.//*migrate-time')
            delete_migrate_time.set('operation', 'delete')
            
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        mstp = ET.SubElement(mstp, "mstp")
        if kwargs.pop('delete_mstp', False) is True:
            delete_mstp = config.find('.//*mstp')
            delete_mstp.set('operation', 'delete')
            
        port = ET.SubElement(mstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id = ET.SubElement(pvstp, "vlan-id")
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
            
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(root_bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(root_bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(root_bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(pvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(pvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(pvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(pvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(pvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        transmit_hold_count = ET.SubElement(pvstp, "transmit-hold-count")
        if kwargs.pop('delete_transmit_hold_count', False) is True:
            delete_transmit_hold_count = config.find('.//*transmit-hold-count')
            delete_transmit_hold_count.set('operation', 'delete')
            
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        migrate_time = ET.SubElement(pvstp, "migrate-time")
        if kwargs.pop('delete_migrate_time', False) is True:
            delete_migrate_time = config.find('.//*migrate-time')
            delete_migrate_time.set('operation', 'delete')
            
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        pvstp = ET.SubElement(pvstp, "pvstp")
        if kwargs.pop('delete_pvstp', False) is True:
            delete_pvstp = config.find('.//*pvstp')
            delete_pvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(pvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id = ET.SubElement(rpvstp, "vlan-id")
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
            
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(root_bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(root_bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(root_bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        if kwargs.pop('delete_root_bridge', False) is True:
            delete_root_bridge = config.find('.//*root-bridge')
            delete_root_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(rpvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        priority = ET.SubElement(bridge, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(rpvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        bridge_id = ET.SubElement(bridge, "bridge-id")
        if kwargs.pop('delete_bridge_id', False) is True:
            delete_bridge_id = config.find('.//*bridge-id')
            delete_bridge_id.set('operation', 'delete')
            
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(rpvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        hello_time = ET.SubElement(bridge, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(rpvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        max_age = ET.SubElement(bridge, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        bridge = ET.SubElement(rpvstp, "bridge")
        if kwargs.pop('delete_bridge', False) is True:
            delete_bridge = config.find('.//*bridge')
            delete_bridge.set('operation', 'delete')
            
        forward_delay = ET.SubElement(bridge, "forward-delay")
        if kwargs.pop('delete_forward_delay', False) is True:
            delete_forward_delay = config.find('.//*forward-delay')
            delete_forward_delay.set('operation', 'delete')
            
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        transmit_hold_count = ET.SubElement(rpvstp, "transmit-hold-count")
        if kwargs.pop('delete_transmit_hold_count', False) is True:
            delete_transmit_hold_count = config.find('.//*transmit-hold-count')
            delete_transmit_hold_count.set('operation', 'delete')
            
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        migrate_time = ET.SubElement(rpvstp, "migrate-time")
        if kwargs.pop('delete_migrate_time', False) is True:
            delete_migrate_time = config.find('.//*migrate-time')
            delete_migrate_time.set('operation', 'delete')
            
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        if kwargs.pop('delete_spanning_tree_info', False) is True:
            delete_spanning_tree_info = config.find('.//*spanning-tree-info')
            delete_spanning_tree_info.set('operation', 'delete')
            
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        if kwargs.pop('delete_spanning_tree_mode', False) is True:
            delete_spanning_tree_mode = config.find('.//*spanning-tree-mode')
            delete_spanning_tree_mode.set('operation', 'delete')
            
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        if kwargs.pop('delete_rpvstp', False) is True:
            delete_rpvstp = config.find('.//*rpvstp')
            delete_rpvstp.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        port = ET.SubElement(rpvstp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
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
        
    def get_stp_brief_info_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        if kwargs.pop('delete_get_stp_brief_info', False) is True:
            delete_get_stp_brief_info = config.find('.//*get-stp-brief-info')
            delete_get_stp_brief_info.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_brief_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_instance = ET.SubElement(output, "last-instance")
        if kwargs.pop('delete_last_instance', False) is True:
            delete_last_instance = config.find('.//*last-instance')
            delete_last_instance.set('operation', 'delete')
            
        instance_id = ET.SubElement(last_instance, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_stp_mst_detail, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        request_type = ET.SubElement(input, "request-type")
        if kwargs.pop('delete_request_type', False) is True:
            delete_request_type = config.find('.//*request-type')
            delete_request_type.set('operation', 'delete')
            
        getnext_request = ET.SubElement(request_type, "getnext-request")
        if kwargs.pop('delete_getnext_request', False) is True:
            delete_getnext_request = config.find('.//*getnext-request')
            delete_getnext_request.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        cist_root_id = ET.SubElement(cist, "cist-root-id")
        if kwargs.pop('delete_cist_root_id', False) is True:
            delete_cist_root_id = config.find('.//*cist-root-id')
            delete_cist_root_id.set('operation', 'delete')
            
        cist_root_id.text = kwargs.pop('cist_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        cist_bridge_id = ET.SubElement(cist, "cist-bridge-id")
        if kwargs.pop('delete_cist_bridge_id', False) is True:
            delete_cist_bridge_id = config.find('.//*cist-bridge-id')
            delete_cist_bridge_id.set('operation', 'delete')
            
        cist_bridge_id.text = kwargs.pop('cist_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_reg_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        cist_reg_root_id = ET.SubElement(cist, "cist-reg-root-id")
        if kwargs.pop('delete_cist_reg_root_id', False) is True:
            delete_cist_reg_root_id = config.find('.//*cist-reg-root-id')
            delete_cist_reg_root_id.set('operation', 'delete')
            
        cist_reg_root_id.text = kwargs.pop('cist_reg_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_root_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        root_forward_delay = ET.SubElement(cist, "root-forward-delay")
        if kwargs.pop('delete_root_forward_delay', False) is True:
            delete_root_forward_delay = config.find('.//*root-forward-delay')
            delete_root_forward_delay.set('operation', 'delete')
            
        root_forward_delay.text = kwargs.pop('root_forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        hello_time = ET.SubElement(cist, "hello-time")
        if kwargs.pop('delete_hello_time', False) is True:
            delete_hello_time = config.find('.//*hello-time')
            delete_hello_time.set('operation', 'delete')
            
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        max_age = ET.SubElement(cist, "max-age")
        if kwargs.pop('delete_max_age', False) is True:
            delete_max_age = config.find('.//*max-age')
            delete_max_age.set('operation', 'delete')
            
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_hops(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        max_hops = ET.SubElement(cist, "max-hops")
        if kwargs.pop('delete_max_hops', False) is True:
            delete_max_hops = config.find('.//*max-hops')
            delete_max_hops.set('operation', 'delete')
            
        max_hops.text = kwargs.pop('max_hops')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        migrate_time = ET.SubElement(cist, "migrate-time")
        if kwargs.pop('delete_migrate_time', False) is True:
            delete_migrate_time = config.find('.//*migrate-time')
            delete_migrate_time.set('operation', 'delete')
            
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        cist = ET.SubElement(output, "cist")
        if kwargs.pop('delete_cist', False) is True:
            delete_cist = config.find('.//*cist')
            delete_cist.set('operation', 'delete')
            
        port = ET.SubElement(cist, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id = ET.SubElement(msti, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        msti_root_id = ET.SubElement(msti, "msti-root-id")
        if kwargs.pop('delete_msti_root_id', False) is True:
            delete_msti_root_id = config.find('.//*msti-root-id')
            delete_msti_root_id.set('operation', 'delete')
            
        msti_root_id.text = kwargs.pop('msti_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        msti_bridge_id = ET.SubElement(msti, "msti-bridge-id")
        if kwargs.pop('delete_msti_bridge_id', False) is True:
            delete_msti_bridge_id = config.find('.//*msti-bridge-id')
            delete_msti_bridge_id.set('operation', 'delete')
            
        msti_bridge_id.text = kwargs.pop('msti_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        msti_bridge_priority = ET.SubElement(msti, "msti-bridge-priority")
        if kwargs.pop('delete_msti_bridge_priority', False) is True:
            delete_msti_bridge_priority = config.find('.//*msti-bridge-priority')
            delete_msti_bridge_priority.set('operation', 'delete')
            
        msti_bridge_priority.text = kwargs.pop('msti_bridge_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_type = ET.SubElement(port, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_name = ET.SubElement(port, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        if kwargs.pop('delete_spanningtree_enabled', False) is True:
            delete_spanningtree_enabled = config.find('.//*spanningtree-enabled')
            delete_spanningtree_enabled.set('operation', 'delete')
            
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_index = ET.SubElement(port, "if-index")
        if kwargs.pop('delete_if_index', False) is True:
            delete_if_index = config.find('.//*if-index')
            delete_if_index.set('operation', 'delete')
            
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        interface_id = ET.SubElement(port, "interface-id")
        if kwargs.pop('delete_interface_id', False) is True:
            delete_interface_id = config.find('.//*interface-id')
            delete_interface_id.set('operation', 'delete')
            
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_role = ET.SubElement(port, "if-role")
        if kwargs.pop('delete_if_role', False) is True:
            delete_if_role = config.find('.//*if-role')
            delete_if_role.set('operation', 'delete')
            
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        if_state = ET.SubElement(port, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        external_path_cost = ET.SubElement(port, "external-path-cost")
        if kwargs.pop('delete_external_path_cost', False) is True:
            delete_external_path_cost = config.find('.//*external-path-cost')
            delete_external_path_cost.set('operation', 'delete')
            
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        if kwargs.pop('delete_internal_path_cost', False) is True:
            delete_internal_path_cost = config.find('.//*internal-path-cost')
            delete_internal_path_cost.set('operation', 'delete')
            
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        if kwargs.pop('delete_configured_path_cost', False) is True:
            delete_configured_path_cost = config.find('.//*configured-path-cost')
            delete_configured_path_cost.set('operation', 'delete')
            
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_port_id = ET.SubElement(port, "designated-port-id")
        if kwargs.pop('delete_designated_port_id', False) is True:
            delete_designated_port_id = config.find('.//*designated-port-id')
            delete_designated_port_id.set('operation', 'delete')
            
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_priority = ET.SubElement(port, "port-priority")
        if kwargs.pop('delete_port_priority', False) is True:
            delete_port_priority = config.find('.//*port-priority')
            delete_port_priority.set('operation', 'delete')
            
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        if kwargs.pop('delete_designated_bridge_id', False) is True:
            delete_designated_bridge_id = config.find('.//*designated-bridge-id')
            delete_designated_bridge_id.set('operation', 'delete')
            
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port_hello_time = ET.SubElement(port, "port-hello-time")
        if kwargs.pop('delete_port_hello_time', False) is True:
            delete_port_hello_time = config.find('.//*port-hello-time')
            delete_port_hello_time.set('operation', 'delete')
            
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        if kwargs.pop('delete_forward_transitions_count', False) is True:
            delete_forward_transitions_count = config.find('.//*forward-transitions-count')
            delete_forward_transitions_count.set('operation', 'delete')
            
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        received_stp_type = ET.SubElement(port, "received-stp-type")
        if kwargs.pop('delete_received_stp_type', False) is True:
            delete_received_stp_type = config.find('.//*received-stp-type')
            delete_received_stp_type.set('operation', 'delete')
            
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        if kwargs.pop('delete_transmitted_stp_type', False) is True:
            delete_transmitted_stp_type = config.find('.//*transmitted-stp-type')
            delete_transmitted_stp_type.set('operation', 'delete')
            
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_port = ET.SubElement(port, "edge-port")
        if kwargs.pop('delete_edge_port', False) is True:
            delete_edge_port = config.find('.//*edge-port')
            delete_edge_port.set('operation', 'delete')
            
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        auto_edge = ET.SubElement(port, "auto-edge")
        if kwargs.pop('delete_auto_edge', False) is True:
            delete_auto_edge = config.find('.//*auto-edge')
            delete_auto_edge.set('operation', 'delete')
            
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        admin_edge = ET.SubElement(port, "admin-edge")
        if kwargs.pop('delete_admin_edge', False) is True:
            delete_admin_edge = config.find('.//*admin-edge')
            delete_admin_edge.set('operation', 'delete')
            
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        edge_delay = ET.SubElement(port, "edge-delay")
        if kwargs.pop('delete_edge_delay', False) is True:
            delete_edge_delay = config.find('.//*edge-delay')
            delete_edge_delay.set('operation', 'delete')
            
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        if kwargs.pop('delete_configured_root_guard', False) is True:
            delete_configured_root_guard = config.find('.//*configured-root-guard')
            delete_configured_root_guard.set('operation', 'delete')
            
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        if kwargs.pop('delete_oper_root_guard', False) is True:
            delete_oper_root_guard = config.find('.//*oper-root-guard')
            delete_oper_root_guard.set('operation', 'delete')
            
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        boundary_port = ET.SubElement(port, "boundary-port")
        if kwargs.pop('delete_boundary_port', False) is True:
            delete_boundary_port = config.find('.//*boundary-port')
            delete_boundary_port.set('operation', 'delete')
            
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        if kwargs.pop('delete_oper_bpdu_guard', False) is True:
            delete_oper_bpdu_guard = config.find('.//*oper-bpdu-guard')
            delete_oper_bpdu_guard.set('operation', 'delete')
            
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        if kwargs.pop('delete_oper_bpdu_filter', False) is True:
            delete_oper_bpdu_filter = config.find('.//*oper-bpdu-filter')
            delete_oper_bpdu_filter.set('operation', 'delete')
            
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        link_type = ET.SubElement(port, "link-type")
        if kwargs.pop('delete_link_type', False) is True:
            delete_link_type = config.find('.//*link-type')
            delete_link_type.set('operation', 'delete')
            
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        if kwargs.pop('delete_rx_bpdu_count', False) is True:
            delete_rx_bpdu_count = config.find('.//*rx-bpdu-count')
            delete_rx_bpdu_count.set('operation', 'delete')
            
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        msti = ET.SubElement(output, "msti")
        if kwargs.pop('delete_msti', False) is True:
            delete_msti = config.find('.//*msti')
            delete_msti.set('operation', 'delete')
            
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
                
        port = ET.SubElement(msti, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        if kwargs.pop('delete_tx_bpdu_count', False) is True:
            delete_tx_bpdu_count = config.find('.//*tx-bpdu-count')
            delete_tx_bpdu_count.set('operation', 'delete')
            
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
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
        
    def get_stp_mst_detail_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        if kwargs.pop('delete_get_stp_mst_detail', False) is True:
            delete_get_stp_mst_detail = config.find('.//*get-stp-mst-detail')
            delete_get_stp_mst_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_stp_mst_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_instance = ET.SubElement(output, "last-instance")
        if kwargs.pop('delete_last_instance', False) is True:
            delete_last_instance = config.find('.//*last-instance')
            delete_last_instance.set('operation', 'delete')
            
        instance_id = ET.SubElement(last_instance, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        