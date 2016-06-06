#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_interface_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_vlan_brief_input_request_type_get_request_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        input = ET.SubElement(get_vlan_brief, "input")
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
            
        vlan_id = ET.SubElement(get_request, "vlan-id")
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
            
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_input_request_type_get_next_request_last_rcvd_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        input = ET.SubElement(get_vlan_brief, "input")
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
            
        last_rcvd_vlan_id = ET.SubElement(get_next_request, "last-rcvd-vlan-id")
        if kwargs.pop('delete_last_rcvd_vlan_id', False) is True:
            delete_last_rcvd_vlan_id = config.find('.//*last-rcvd-vlan-id')
            delete_last_rcvd_vlan_id.set('operation', 'delete')
            
        last_rcvd_vlan_id.text = kwargs.pop('last_rcvd_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_configured_vlans_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        configured_vlans_count = ET.SubElement(output, "configured-vlans-count")
        if kwargs.pop('delete_configured_vlans_count', False) is True:
            delete_configured_vlans_count = config.find('.//*configured-vlans-count')
            delete_configured_vlans_count.set('operation', 'delete')
            
        configured_vlans_count.text = kwargs.pop('configured_vlans_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_provisioned_vlans_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        provisioned_vlans_count = ET.SubElement(output, "provisioned-vlans-count")
        if kwargs.pop('delete_provisioned_vlans_count', False) is True:
            delete_provisioned_vlans_count = config.find('.//*provisioned-vlans-count')
            delete_provisioned_vlans_count.set('operation', 'delete')
            
        provisioned_vlans_count.text = kwargs.pop('provisioned_vlans_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_unprovisioned_vlans_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        unprovisioned_vlans_count = ET.SubElement(output, "unprovisioned-vlans-count")
        if kwargs.pop('delete_unprovisioned_vlans_count', False) is True:
            delete_unprovisioned_vlans_count = config.find('.//*unprovisioned-vlans-count')
            delete_unprovisioned_vlans_count.set('operation', 'delete')
            
        unprovisioned_vlans_count.text = kwargs.pop('unprovisioned_vlans_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id = ET.SubElement(vlan, "vlan-id")
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
            
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        vlan_type = ET.SubElement(vlan, "vlan-type")
        if kwargs.pop('delete_vlan_type', False) is True:
            delete_vlan_type = config.find('.//*vlan-type')
            delete_vlan_type.set('operation', 'delete')
            
        vlan_type.text = kwargs.pop('vlan_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        vlan_name = ET.SubElement(vlan, "vlan-name")
        if kwargs.pop('delete_vlan_name', False) is True:
            delete_vlan_name = config.find('.//*vlan-name')
            delete_vlan_name.set('operation', 'delete')
            
        vlan_name.text = kwargs.pop('vlan_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        vlan_state = ET.SubElement(vlan, "vlan-state")
        if kwargs.pop('delete_vlan_state', False) is True:
            delete_vlan_state = config.find('.//*vlan-state')
            delete_vlan_state.set('operation', 'delete')
            
        vlan_state.text = kwargs.pop('vlan_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        interface = ET.SubElement(vlan, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        interface = ET.SubElement(vlan, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        interface = ET.SubElement(vlan, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        tag = ET.SubElement(interface, "tag")
        if kwargs.pop('delete_tag', False) is True:
            delete_tag = config.find('.//*tag')
            delete_tag.set('operation', 'delete')
            
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        interface = ET.SubElement(vlan, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        classification = ET.SubElement(interface, "classification")
        if kwargs.pop('delete_classification', False) is True:
            delete_classification = config.find('.//*classification')
            delete_classification.set('operation', 'delete')
            
        classification_value_key = ET.SubElement(classification, "classification-value")
        classification_value_key.text = kwargs.pop('classification_value')
        if kwargs.pop('delete_classification_value', False) is True:
            delete_classification_value = config.find('.//*classification-value')
            delete_classification_value.set('operation', 'delete')
                
        classification_type = ET.SubElement(classification, "classification-type")
        if kwargs.pop('delete_classification_type', False) is True:
            delete_classification_type = config.find('.//*classification-type')
            delete_classification_type.set('operation', 'delete')
            
        classification_type.text = kwargs.pop('classification_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vlan = ET.SubElement(output, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        if kwargs.pop('delete_vlan_id', False) is True:
            delete_vlan_id = config.find('.//*vlan-id')
            delete_vlan_id.set('operation', 'delete')
                
        interface = ET.SubElement(vlan, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        classification = ET.SubElement(interface, "classification")
        if kwargs.pop('delete_classification', False) is True:
            delete_classification = config.find('.//*classification')
            delete_classification.set('operation', 'delete')
            
        classification_type_key = ET.SubElement(classification, "classification-type")
        classification_type_key.text = kwargs.pop('classification_type')
        if kwargs.pop('delete_classification_type', False) is True:
            delete_classification_type = config.find('.//*classification-type')
            delete_classification_type.set('operation', 'delete')
                
        classification_value = ET.SubElement(classification, "classification-value")
        if kwargs.pop('delete_classification_value', False) is True:
            delete_classification_value = config.find('.//*classification-value')
            delete_classification_value.set('operation', 'delete')
            
        classification_value.text = kwargs.pop('classification_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        last_vlan_id = ET.SubElement(output, "last-vlan-id")
        if kwargs.pop('delete_last_vlan_id', False) is True:
            delete_last_vlan_id = config.find('.//*last-vlan-id')
            delete_last_vlan_id.set('operation', 'delete')
            
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        if kwargs.pop('delete_get_vlan_brief', False) is True:
            delete_get_vlan_brief = config.find('.//*get-vlan-brief')
            delete_get_vlan_brief.set('operation', 'delete')
            
        output = ET.SubElement(get_vlan_brief, "output")
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
        
    def get_interface_switchport_output_switchport_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(switchport, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(switchport, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        mode = ET.SubElement(switchport, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_fcoe_port_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        fcoe_port_enabled = ET.SubElement(switchport, "fcoe-port-enabled")
        if kwargs.pop('delete_fcoe_port_enabled', False) is True:
            delete_fcoe_port_enabled = config.find('.//*fcoe-port-enabled')
            delete_fcoe_port_enabled.set('operation', 'delete')
            
        fcoe_port_enabled.text = kwargs.pop('fcoe_port_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_ingress_filter_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ingress_filter_enabled = ET.SubElement(switchport, "ingress-filter-enabled")
        if kwargs.pop('delete_ingress_filter_enabled', False) is True:
            delete_ingress_filter_enabled = config.find('.//*ingress-filter-enabled')
            delete_ingress_filter_enabled.set('operation', 'delete')
            
        ingress_filter_enabled.text = kwargs.pop('ingress_filter_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_acceptable_frame_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        acceptable_frame_type = ET.SubElement(switchport, "acceptable-frame-type")
        if kwargs.pop('delete_acceptable_frame_type', False) is True:
            delete_acceptable_frame_type = config.find('.//*acceptable-frame-type')
            delete_acceptable_frame_type.set('operation', 'delete')
            
        acceptable_frame_type.text = kwargs.pop('acceptable_frame_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_default_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        if kwargs.pop('delete_get_interface_switchport', False) is True:
            delete_get_interface_switchport = config.find('.//*get-interface-switchport')
            delete_get_interface_switchport.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_switchport, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        switchport = ET.SubElement(output, "switchport")
        if kwargs.pop('delete_switchport', False) is True:
            delete_switchport = config.find('.//*switchport')
            delete_switchport.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        default_vlan = ET.SubElement(switchport, "default-vlan")
        if kwargs.pop('delete_default_vlan', False) is True:
            delete_default_vlan = config.find('.//*default-vlan')
            delete_default_vlan.set('operation', 'delete')
            
        default_vlan.text = kwargs.pop('default_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        input = ET.SubElement(get_ip_interface, "input")
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
        
    def get_ip_interface_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        input = ET.SubElement(get_ip_interface, "input")
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
        
    def get_ip_interface_input_request_type_get_request_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        input = ET.SubElement(get_ip_interface, "input")
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
            
        rbridge_id = ET.SubElement(get_request, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        if_name = ET.SubElement(interface, "if-name")
        if kwargs.pop('delete_if_name', False) is True:
            delete_if_name = config.find('.//*if-name')
            delete_if_name.set('operation', 'delete')
            
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ip_address = ET.SubElement(interface, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ipv4 = ET.SubElement(ip_address, "ipv4")
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
            
        ipv4.text = kwargs.pop('ipv4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ip_address = ET.SubElement(interface, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
                
        ipv4_type = ET.SubElement(ip_address, "ipv4-type")
        if kwargs.pop('delete_ipv4_type', False) is True:
            delete_ipv4_type = config.find('.//*ipv4-type')
            delete_ipv4_type.set('operation', 'delete')
            
        ipv4_type.text = kwargs.pop('ipv4_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_broadcast(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ip_address = ET.SubElement(interface, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
                
        broadcast = ET.SubElement(ip_address, "broadcast")
        if kwargs.pop('delete_broadcast', False) is True:
            delete_broadcast = config.find('.//*broadcast')
            delete_broadcast.set('operation', 'delete')
            
        broadcast.text = kwargs.pop('broadcast')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ip_address = ET.SubElement(interface, "ip-address")
        if kwargs.pop('delete_ip_address', False) is True:
            delete_ip_address = config.find('.//*ip-address')
            delete_ip_address.set('operation', 'delete')
            
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        if kwargs.pop('delete_ipv4', False) is True:
            delete_ipv4 = config.find('.//*ipv4')
            delete_ipv4.set('operation', 'delete')
                
        ip_mtu = ET.SubElement(ip_address, "ip-mtu")
        if kwargs.pop('delete_ip_mtu', False) is True:
            delete_ip_mtu = config.find('.//*ip-mtu')
            delete_ip_mtu.set('operation', 'delete')
            
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        if_state = ET.SubElement(interface, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        if kwargs.pop('delete_line_protocol_state', False) is True:
            delete_line_protocol_state = config.find('.//*line-protocol-state')
            delete_line_protocol_state.set('operation', 'delete')
            
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_proxy_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        proxy_arp = ET.SubElement(interface, "proxy-arp")
        if kwargs.pop('delete_proxy_arp', False) is True:
            delete_proxy_arp = config.find('.//*proxy-arp')
            delete_proxy_arp.set('operation', 'delete')
            
        proxy_arp.text = kwargs.pop('proxy_arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        vrf = ET.SubElement(interface, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        if kwargs.pop('delete_get_ip_interface', False) is True:
            delete_get_ip_interface = config.find('.//*get-ip-interface')
            delete_get_ip_interface.set('operation', 'delete')
            
        output = ET.SubElement(get_ip_interface, "output")
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
        
    def get_interface_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_interface_detail, "input")
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
        
    def get_interface_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_interface_detail, "input")
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
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_interface_detail, "input")
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
            
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        if kwargs.pop('delete_last_rcvd_interface', False) is True:
            delete_last_rcvd_interface = config.find('.//*last-rcvd-interface')
            delete_last_rcvd_interface.set('operation', 'delete')
            
        interface_type = ET.SubElement(last_rcvd_interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_interface_detail, "input")
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
            
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        if kwargs.pop('delete_last_rcvd_interface', False) is True:
            delete_last_rcvd_interface = config.find('.//*last-rcvd-interface')
            delete_last_rcvd_interface.set('operation', 'delete')
            
        interface_name = ET.SubElement(last_rcvd_interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifindex = ET.SubElement(interface, "ifindex")
        if kwargs.pop('delete_ifindex', False) is True:
            delete_ifindex = config.find('.//*ifindex')
            delete_ifindex.set('operation', 'delete')
            
        ifindex.text = kwargs.pop('ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        mtu = ET.SubElement(interface, "mtu")
        if kwargs.pop('delete_mtu', False) is True:
            delete_mtu = config.find('.//*mtu')
            delete_mtu.set('operation', 'delete')
            
        mtu.text = kwargs.pop('mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ip_mtu = ET.SubElement(interface, "ip-mtu")
        if kwargs.pop('delete_ip_mtu', False) is True:
            delete_ip_mtu = config.find('.//*ip-mtu')
            delete_ip_mtu.set('operation', 'delete')
            
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        if_name = ET.SubElement(interface, "if-name")
        if kwargs.pop('delete_if_name', False) is True:
            delete_if_name = config.find('.//*if-name')
            delete_if_name.set('operation', 'delete')
            
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        if_state = ET.SubElement(interface, "if-state")
        if kwargs.pop('delete_if_state', False) is True:
            delete_if_state = config.find('.//*if-state')
            delete_if_state.set('operation', 'delete')
            
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        if kwargs.pop('delete_line_protocol_state', False) is True:
            delete_line_protocol_state = config.find('.//*line-protocol-state')
            delete_line_protocol_state.set('operation', 'delete')
            
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        line_protocol_state_info = ET.SubElement(interface, "line-protocol-state-info")
        if kwargs.pop('delete_line_protocol_state_info', False) is True:
            delete_line_protocol_state_info = config.find('.//*line-protocol-state-info')
            delete_line_protocol_state_info.set('operation', 'delete')
            
        line_protocol_state_info.text = kwargs.pop('line_protocol_state_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_exception_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        line_protocol_exception_info = ET.SubElement(interface, "line-protocol-exception-info")
        if kwargs.pop('delete_line_protocol_exception_info', False) is True:
            delete_line_protocol_exception_info = config.find('.//*line-protocol-exception-info')
            delete_line_protocol_exception_info.set('operation', 'delete')
            
        line_protocol_exception_info.text = kwargs.pop('line_protocol_exception_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_hardware_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        hardware_type = ET.SubElement(interface, "hardware-type")
        if kwargs.pop('delete_hardware_type', False) is True:
            delete_hardware_type = config.find('.//*hardware-type')
            delete_hardware_type.set('operation', 'delete')
            
        hardware_type.text = kwargs.pop('hardware_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_logical_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        logical_hardware_address = ET.SubElement(interface, "logical-hardware-address")
        if kwargs.pop('delete_logical_hardware_address', False) is True:
            delete_logical_hardware_address = config.find('.//*logical-hardware-address')
            delete_logical_hardware_address.set('operation', 'delete')
            
        logical_hardware_address.text = kwargs.pop('logical_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_current_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        current_hardware_address = ET.SubElement(interface, "current-hardware-address")
        if kwargs.pop('delete_current_hardware_address', False) is True:
            delete_current_hardware_address = config.find('.//*current-hardware-address')
            delete_current_hardware_address.set('operation', 'delete')
            
        current_hardware_address.text = kwargs.pop('current_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_media_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        media_type = ET.SubElement(interface, "media-type")
        if kwargs.pop('delete_media_type', False) is True:
            delete_media_type = config.find('.//*media-type')
            delete_media_type.set('operation', 'delete')
            
        media_type.text = kwargs.pop('media_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        wavelength = ET.SubElement(interface, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        if_description = ET.SubElement(interface, "if-description")
        if kwargs.pop('delete_if_description', False) is True:
            delete_if_description = config.find('.//*if-description')
            delete_if_description.set('operation', 'delete')
            
        if_description.text = kwargs.pop('if_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_actual_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        actual_line_speed = ET.SubElement(interface, "actual-line-speed")
        if kwargs.pop('delete_actual_line_speed', False) is True:
            delete_actual_line_speed = config.find('.//*actual-line-speed')
            delete_actual_line_speed.set('operation', 'delete')
            
        actual_line_speed.text = kwargs.pop('actual_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_configured_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        configured_line_speed = ET.SubElement(interface, "configured-line-speed")
        if kwargs.pop('delete_configured_line_speed', False) is True:
            delete_configured_line_speed = config.find('.//*configured-line-speed')
            delete_configured_line_speed.set('operation', 'delete')
            
        configured_line_speed.text = kwargs.pop('configured_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_duplex_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        line_duplex_state = ET.SubElement(interface, "line-duplex-state")
        if kwargs.pop('delete_line_duplex_state', False) is True:
            delete_line_duplex_state = config.find('.//*line-duplex-state')
            delete_line_duplex_state.set('operation', 'delete')
            
        line_duplex_state.text = kwargs.pop('line_duplex_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_flow_control(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        flow_control = ET.SubElement(interface, "flow-control")
        if kwargs.pop('delete_flow_control', False) is True:
            delete_flow_control = config.find('.//*flow-control')
            delete_flow_control.set('operation', 'delete')
            
        flow_control.text = kwargs.pop('flow_control')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_queuing_strategy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        queuing_strategy = ET.SubElement(interface, "queuing-strategy")
        if kwargs.pop('delete_queuing_strategy', False) is True:
            delete_queuing_strategy = config.find('.//*queuing-strategy')
            delete_queuing_strategy.set('operation', 'delete')
            
        queuing_strategy.text = kwargs.pop('queuing_strategy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        port_role = ET.SubElement(interface, "port-role")
        if kwargs.pop('delete_port_role', False) is True:
            delete_port_role = config.find('.//*port-role')
            delete_port_role.set('operation', 'delete')
            
        port_role.text = kwargs.pop('port_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        port_mode = ET.SubElement(interface, "port-mode")
        if kwargs.pop('delete_port_mode', False) is True:
            delete_port_mode = config.find('.//*port-mode')
            delete_port_mode.set('operation', 'delete')
            
        port_mode.text = kwargs.pop('port_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCInOctets = ET.SubElement(interface, "ifHCInOctets")
        if kwargs.pop('delete_ifHCInOctets', False) is True:
            delete_ifHCInOctets = config.find('.//*ifHCInOctets')
            delete_ifHCInOctets.set('operation', 'delete')
            
        ifHCInOctets.text = kwargs.pop('ifHCInOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCInUcastPkts = ET.SubElement(interface, "ifHCInUcastPkts")
        if kwargs.pop('delete_ifHCInUcastPkts', False) is True:
            delete_ifHCInUcastPkts = config.find('.//*ifHCInUcastPkts')
            delete_ifHCInUcastPkts.set('operation', 'delete')
            
        ifHCInUcastPkts.text = kwargs.pop('ifHCInUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCInMulticastPkts = ET.SubElement(interface, "ifHCInMulticastPkts")
        if kwargs.pop('delete_ifHCInMulticastPkts', False) is True:
            delete_ifHCInMulticastPkts = config.find('.//*ifHCInMulticastPkts')
            delete_ifHCInMulticastPkts.set('operation', 'delete')
            
        ifHCInMulticastPkts.text = kwargs.pop('ifHCInMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCInBroadcastPkts = ET.SubElement(interface, "ifHCInBroadcastPkts")
        if kwargs.pop('delete_ifHCInBroadcastPkts', False) is True:
            delete_ifHCInBroadcastPkts = config.find('.//*ifHCInBroadcastPkts')
            delete_ifHCInBroadcastPkts.set('operation', 'delete')
            
        ifHCInBroadcastPkts.text = kwargs.pop('ifHCInBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCInErrors = ET.SubElement(interface, "ifHCInErrors")
        if kwargs.pop('delete_ifHCInErrors', False) is True:
            delete_ifHCInErrors = config.find('.//*ifHCInErrors')
            delete_ifHCInErrors.set('operation', 'delete')
            
        ifHCInErrors.text = kwargs.pop('ifHCInErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCOutOctets = ET.SubElement(interface, "ifHCOutOctets")
        if kwargs.pop('delete_ifHCOutOctets', False) is True:
            delete_ifHCOutOctets = config.find('.//*ifHCOutOctets')
            delete_ifHCOutOctets.set('operation', 'delete')
            
        ifHCOutOctets.text = kwargs.pop('ifHCOutOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCOutUcastPkts = ET.SubElement(interface, "ifHCOutUcastPkts")
        if kwargs.pop('delete_ifHCOutUcastPkts', False) is True:
            delete_ifHCOutUcastPkts = config.find('.//*ifHCOutUcastPkts')
            delete_ifHCOutUcastPkts.set('operation', 'delete')
            
        ifHCOutUcastPkts.text = kwargs.pop('ifHCOutUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCOutMulticastPkts = ET.SubElement(interface, "ifHCOutMulticastPkts")
        if kwargs.pop('delete_ifHCOutMulticastPkts', False) is True:
            delete_ifHCOutMulticastPkts = config.find('.//*ifHCOutMulticastPkts')
            delete_ifHCOutMulticastPkts.set('operation', 'delete')
            
        ifHCOutMulticastPkts.text = kwargs.pop('ifHCOutMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCOutBroadcastPkts = ET.SubElement(interface, "ifHCOutBroadcastPkts")
        if kwargs.pop('delete_ifHCOutBroadcastPkts', False) is True:
            delete_ifHCOutBroadcastPkts = config.find('.//*ifHCOutBroadcastPkts')
            delete_ifHCOutBroadcastPkts.set('operation', 'delete')
            
        ifHCOutBroadcastPkts.text = kwargs.pop('ifHCOutBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        ifHCOutErrors = ET.SubElement(interface, "ifHCOutErrors")
        if kwargs.pop('delete_ifHCOutErrors', False) is True:
            delete_ifHCOutErrors = config.find('.//*ifHCOutErrors')
            delete_ifHCOutErrors.set('operation', 'delete')
            
        ifHCOutErrors.text = kwargs.pop('ifHCOutErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        if kwargs.pop('delete_get_interface_detail', False) is True:
            delete_get_interface_detail = config.find('.//*get-interface-detail')
            delete_get_interface_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_interface_detail, "output")
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
        
    def get_media_detail_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_media_detail, "input")
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
        
    def get_media_detail_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_media_detail, "input")
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
        
    def get_media_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_media_detail, "input")
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
        
    def get_media_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_type = ET.SubElement(interface, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name = ET.SubElement(interface, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        speed = ET.SubElement(sfp, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        connector = ET.SubElement(sfp, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        encoding = ET.SubElement(sfp, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        vendor_name = ET.SubElement(sfp, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(sfp, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(sfp, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(sfp, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        distance = ET.SubElement(sfp, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(sfp, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        wavelength = ET.SubElement(sfp, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        serial_no = ET.SubElement(sfp, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        date_code = ET.SubElement(sfp, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        temperature = ET.SubElement(sfp, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        voltage = ET.SubElement(sfp, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        current = ET.SubElement(sfp, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        tx_power = ET.SubElement(sfp, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        sfp = ET.SubElement(interface_identifier, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        sfp = ET.SubElement(sfp, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        rx_power = ET.SubElement(sfp, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        speed = ET.SubElement(on_board, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        connector = ET.SubElement(on_board, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        encoding = ET.SubElement(on_board, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        vendor_name = ET.SubElement(on_board, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(on_board, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(on_board, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        on_board = ET.SubElement(interface_identifier, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        on_board = ET.SubElement(on_board, "on-board")
        if kwargs.pop('delete_on_board', False) is True:
            delete_on_board = config.find('.//*on-board')
            delete_on_board.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(on_board, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        gbic = ET.SubElement(interface_identifier, "gbic")
        if kwargs.pop('delete_gbic', False) is True:
            delete_gbic = config.find('.//*gbic')
            delete_gbic.set('operation', 'delete')
            
        gbc = ET.SubElement(gbic, "gbc")
        if kwargs.pop('delete_gbc', False) is True:
            delete_gbc = config.find('.//*gbc')
            delete_gbc.set('operation', 'delete')
            
        vendor_name = ET.SubElement(gbc, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        gbic = ET.SubElement(interface_identifier, "gbic")
        if kwargs.pop('delete_gbic', False) is True:
            delete_gbic = config.find('.//*gbic')
            delete_gbic.set('operation', 'delete')
            
        gbc = ET.SubElement(gbic, "gbc")
        if kwargs.pop('delete_gbc', False) is True:
            delete_gbc = config.find('.//*gbc')
            delete_gbc.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(gbc, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        gbic = ET.SubElement(interface_identifier, "gbic")
        if kwargs.pop('delete_gbic', False) is True:
            delete_gbic = config.find('.//*gbic')
            delete_gbic.set('operation', 'delete')
            
        gbc = ET.SubElement(gbic, "gbc")
        if kwargs.pop('delete_gbc', False) is True:
            delete_gbc = config.find('.//*gbc')
            delete_gbc.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(gbc, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        gbic = ET.SubElement(interface_identifier, "gbic")
        if kwargs.pop('delete_gbic', False) is True:
            delete_gbic = config.find('.//*gbic')
            delete_gbic.set('operation', 'delete')
            
        gbc = ET.SubElement(gbic, "gbc")
        if kwargs.pop('delete_gbc', False) is True:
            delete_gbc = config.find('.//*gbc')
            delete_gbc.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(gbc, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfp = ET.SubElement(interface_identifier, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        xfp = ET.SubElement(xfp, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        vendor_name = ET.SubElement(xfp, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfp = ET.SubElement(interface_identifier, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        xfp = ET.SubElement(xfp, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(xfp, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfp = ET.SubElement(interface_identifier, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        xfp = ET.SubElement(xfp, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(xfp, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfp = ET.SubElement(interface_identifier, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        xfp = ET.SubElement(xfp, "xfp")
        if kwargs.pop('delete_xfp', False) is True:
            delete_xfp = config.find('.//*xfp')
            delete_xfp.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(xfp, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xff = ET.SubElement(interface_identifier, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        xff = ET.SubElement(xff, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        vendor_name = ET.SubElement(xff, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xff = ET.SubElement(interface_identifier, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        xff = ET.SubElement(xff, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(xff, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xff = ET.SubElement(interface_identifier, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        xff = ET.SubElement(xff, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(xff, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xff = ET.SubElement(interface_identifier, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        xff = ET.SubElement(xff, "xff")
        if kwargs.pop('delete_xff', False) is True:
            delete_xff = config.find('.//*xff')
            delete_xff.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(xff, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        xfpe = ET.SubElement(xfpe, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        vendor_name = ET.SubElement(xfpe, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        xfpe = ET.SubElement(xfpe, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(xfpe, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        xfpe = ET.SubElement(xfpe, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(xfpe, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        xfpe = ET.SubElement(xfpe, "xfpe")
        if kwargs.pop('delete_xfpe', False) is True:
            delete_xfpe = config.find('.//*xfpe')
            delete_xfpe.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(xfpe, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        unknown = ET.SubElement(interface_identifier, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        unknown = ET.SubElement(unknown, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        vendor_name = ET.SubElement(unknown, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        unknown = ET.SubElement(interface_identifier, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        unknown = ET.SubElement(unknown, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(unknown, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        unknown = ET.SubElement(interface_identifier, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        unknown = ET.SubElement(unknown, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(unknown, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        unknown = ET.SubElement(interface_identifier, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        unknown = ET.SubElement(unknown, "unknown")
        if kwargs.pop('delete_unknown', False) is True:
            delete_unknown = config.find('.//*unknown')
            delete_unknown.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(unknown, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        speed = ET.SubElement(qsfp, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        connector = ET.SubElement(qsfp, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        encoding = ET.SubElement(qsfp, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        vendor_name = ET.SubElement(qsfp, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(qsfp, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(qsfp, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(qsfp, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        distance = ET.SubElement(qsfp, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(qsfp, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        wavelength = ET.SubElement(qsfp, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        serial_no = ET.SubElement(qsfp, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        date_code = ET.SubElement(qsfp, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        temperature = ET.SubElement(qsfp, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        voltage = ET.SubElement(qsfp, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        current = ET.SubElement(qsfp, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        tx_power = ET.SubElement(qsfp, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        qsfp = ET.SubElement(qsfp, "qsfp")
        if kwargs.pop('delete_qsfp', False) is True:
            delete_qsfp = config.find('.//*qsfp')
            delete_qsfp.set('operation', 'delete')
            
        rx_power = ET.SubElement(qsfp, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        speed = ET.SubElement(qsfpp, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        connector = ET.SubElement(qsfpp, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        encoding = ET.SubElement(qsfpp, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        vendor_name = ET.SubElement(qsfpp, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(qsfpp, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(qsfpp, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(qsfpp, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        distance = ET.SubElement(qsfpp, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(qsfpp, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        wavelength = ET.SubElement(qsfpp, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        serial_no = ET.SubElement(qsfpp, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        date_code = ET.SubElement(qsfpp, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        temperature = ET.SubElement(qsfpp, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        voltage = ET.SubElement(qsfpp, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        current = ET.SubElement(qsfpp, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        tx_power = ET.SubElement(qsfpp, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        if kwargs.pop('delete_qsfpp', False) is True:
            delete_qsfpp = config.find('.//*qsfpp')
            delete_qsfpp.set('operation', 'delete')
            
        rx_power = ET.SubElement(qsfpp, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        speed = ET.SubElement(cfp, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        connector = ET.SubElement(cfp, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        encoding = ET.SubElement(cfp, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        vendor_name = ET.SubElement(cfp, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(cfp, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(cfp, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(cfp, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        distance = ET.SubElement(cfp, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(cfp, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        wavelength = ET.SubElement(cfp, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        serial_no = ET.SubElement(cfp, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        date_code = ET.SubElement(cfp, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        temperature = ET.SubElement(cfp, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        voltage = ET.SubElement(cfp, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        current = ET.SubElement(cfp, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        tx_power = ET.SubElement(cfp, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp = ET.SubElement(interface_identifier, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        cfp = ET.SubElement(cfp, "cfp")
        if kwargs.pop('delete_cfp', False) is True:
            delete_cfp = config.find('.//*cfp')
            delete_cfp.set('operation', 'delete')
            
        rx_power = ET.SubElement(cfp, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        speed = ET.SubElement(cfp2, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        connector = ET.SubElement(cfp2, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        encoding = ET.SubElement(cfp2, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        vendor_name = ET.SubElement(cfp2, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(cfp2, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(cfp2, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(cfp2, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        distance = ET.SubElement(cfp2, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(cfp2, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        wavelength = ET.SubElement(cfp2, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        serial_no = ET.SubElement(cfp2, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        date_code = ET.SubElement(cfp2, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        temperature = ET.SubElement(cfp2, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        voltage = ET.SubElement(cfp2, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        current = ET.SubElement(cfp2, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        tx_power = ET.SubElement(cfp2, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        cfp2 = ET.SubElement(cfp2, "cfp2")
        if kwargs.pop('delete_cfp2', False) is True:
            delete_cfp2 = config.find('.//*cfp2')
            delete_cfp2.set('operation', 'delete')
            
        rx_power = ET.SubElement(cfp2, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        speed = ET.SubElement(qsfp28, "speed")
        if kwargs.pop('delete_speed', False) is True:
            delete_speed = config.find('.//*speed')
            delete_speed.set('operation', 'delete')
            
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        connector = ET.SubElement(qsfp28, "connector")
        if kwargs.pop('delete_connector', False) is True:
            delete_connector = config.find('.//*connector')
            delete_connector.set('operation', 'delete')
            
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        encoding = ET.SubElement(qsfp28, "encoding")
        if kwargs.pop('delete_encoding', False) is True:
            delete_encoding = config.find('.//*encoding')
            delete_encoding.set('operation', 'delete')
            
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        vendor_name = ET.SubElement(qsfp28, "vendor-name")
        if kwargs.pop('delete_vendor_name', False) is True:
            delete_vendor_name = config.find('.//*vendor-name')
            delete_vendor_name.set('operation', 'delete')
            
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        vendor_oui = ET.SubElement(qsfp28, "vendor-oui")
        if kwargs.pop('delete_vendor_oui', False) is True:
            delete_vendor_oui = config.find('.//*vendor-oui')
            delete_vendor_oui.set('operation', 'delete')
            
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        vendor_pn = ET.SubElement(qsfp28, "vendor-pn")
        if kwargs.pop('delete_vendor_pn', False) is True:
            delete_vendor_pn = config.find('.//*vendor-pn')
            delete_vendor_pn.set('operation', 'delete')
            
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        vendor_rev = ET.SubElement(qsfp28, "vendor-rev")
        if kwargs.pop('delete_vendor_rev', False) is True:
            delete_vendor_rev = config.find('.//*vendor-rev')
            delete_vendor_rev.set('operation', 'delete')
            
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        distance = ET.SubElement(qsfp28, "distance")
        if kwargs.pop('delete_distance', False) is True:
            delete_distance = config.find('.//*distance')
            delete_distance.set('operation', 'delete')
            
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        media_form_factor = ET.SubElement(qsfp28, "media-form-factor")
        if kwargs.pop('delete_media_form_factor', False) is True:
            delete_media_form_factor = config.find('.//*media-form-factor')
            delete_media_form_factor.set('operation', 'delete')
            
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        wavelength = ET.SubElement(qsfp28, "wavelength")
        if kwargs.pop('delete_wavelength', False) is True:
            delete_wavelength = config.find('.//*wavelength')
            delete_wavelength.set('operation', 'delete')
            
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        serial_no = ET.SubElement(qsfp28, "serial-no")
        if kwargs.pop('delete_serial_no', False) is True:
            delete_serial_no = config.find('.//*serial-no')
            delete_serial_no.set('operation', 'delete')
            
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        date_code = ET.SubElement(qsfp28, "date-code")
        if kwargs.pop('delete_date_code', False) is True:
            delete_date_code = config.find('.//*date-code')
            delete_date_code.set('operation', 'delete')
            
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        temperature = ET.SubElement(qsfp28, "temperature")
        if kwargs.pop('delete_temperature', False) is True:
            delete_temperature = config.find('.//*temperature')
            delete_temperature.set('operation', 'delete')
            
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        voltage = ET.SubElement(qsfp28, "voltage")
        if kwargs.pop('delete_voltage', False) is True:
            delete_voltage = config.find('.//*voltage')
            delete_voltage.set('operation', 'delete')
            
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        current = ET.SubElement(qsfp28, "current")
        if kwargs.pop('delete_current', False) is True:
            delete_current = config.find('.//*current')
            delete_current.set('operation', 'delete')
            
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        tx_power = ET.SubElement(qsfp28, "tx-power")
        if kwargs.pop('delete_tx_power', False) is True:
            delete_tx_power = config.find('.//*tx-power')
            delete_tx_power.set('operation', 'delete')
            
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp28_qsfp28_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        if kwargs.pop('delete_get_media_detail', False) is True:
            delete_get_media_detail = config.find('.//*get-media-detail')
            delete_get_media_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_media_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        interface = ET.SubElement(output, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
                
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
                
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        if kwargs.pop('delete_interface_identifier', False) is True:
            delete_interface_identifier = config.find('.//*interface-identifier')
            delete_interface_identifier.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(interface_identifier, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        qsfp28 = ET.SubElement(qsfp28, "qsfp28")
        if kwargs.pop('delete_qsfp28', False) is True:
            delete_qsfp28 = config.find('.//*qsfp28')
            delete_qsfp28.set('operation', 'delete')
            
        rx_power = ET.SubElement(qsfp28, "rx-power")
        if kwargs.pop('delete_rx_power', False) is True:
            delete_rx_power = config.find('.//*rx-power')
            delete_rx_power.set('operation', 'delete')
            
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        