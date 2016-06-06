#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_maps_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def maps_get_all_policy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        if kwargs.pop('delete_maps_get_all_policy', False) is True:
            delete_maps_get_all_policy = config.find('.//*maps-get-all-policy')
            delete_maps_get_all_policy.set('operation', 'delete')
            
        input = ET.SubElement(maps_get_all_policy, "input")
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
        
    def maps_get_all_policy_output_policy_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        if kwargs.pop('delete_maps_get_all_policy', False) is True:
            delete_maps_get_all_policy = config.find('.//*maps-get-all-policy')
            delete_maps_get_all_policy.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_all_policy, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        policy = ET.SubElement(output, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policyname = ET.SubElement(policy, "policyname")
        if kwargs.pop('delete_policyname', False) is True:
            delete_policyname = config.find('.//*policyname')
            delete_policyname.set('operation', 'delete')
            
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        input = ET.SubElement(maps_get_default_rules, "input")
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
        
    def maps_get_default_rules_output_rules_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        rbridgeid = ET.SubElement(rules, "rbridgeid")
        if kwargs.pop('delete_rbridgeid', False) is True:
            delete_rbridgeid = config.find('.//*rbridgeid')
            delete_rbridgeid.set('operation', 'delete')
            
        rbridgeid.text = kwargs.pop('rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_rulename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        rulename = ET.SubElement(rules, "rulename")
        if kwargs.pop('delete_rulename', False) is True:
            delete_rulename = config.find('.//*rulename')
            delete_rulename.set('operation', 'delete')
            
        rulename.text = kwargs.pop('rulename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        groupname = ET.SubElement(rules, "groupname")
        if kwargs.pop('delete_groupname', False) is True:
            delete_groupname = config.find('.//*groupname')
            delete_groupname.set('operation', 'delete')
            
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_monitor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        monitor = ET.SubElement(rules, "monitor")
        if kwargs.pop('delete_monitor', False) is True:
            delete_monitor = config.find('.//*monitor')
            delete_monitor.set('operation', 'delete')
            
        monitor.text = kwargs.pop('monitor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_op(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        op = ET.SubElement(rules, "op")
        if kwargs.pop('delete_op', False) is True:
            delete_op = config.find('.//*op')
            delete_op.set('operation', 'delete')
            
        op.text = kwargs.pop('op')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        value = ET.SubElement(rules, "value")
        if kwargs.pop('delete_value', False) is True:
            delete_value = config.find('.//*value')
            delete_value.set('operation', 'delete')
            
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        action = ET.SubElement(rules, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        timebase = ET.SubElement(rules, "timebase")
        if kwargs.pop('delete_timebase', False) is True:
            delete_timebase = config.find('.//*timebase')
            delete_timebase.set('operation', 'delete')
            
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        if kwargs.pop('delete_maps_get_default_rules', False) is True:
            delete_maps_get_default_rules = config.find('.//*maps-get-default-rules')
            delete_maps_get_default_rules.set('operation', 'delete')
            
        output = ET.SubElement(maps_get_default_rules, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rules = ET.SubElement(output, "rules")
        if kwargs.pop('delete_rules', False) is True:
            delete_rules = config.find('.//*rules')
            delete_rules.set('operation', 'delete')
            
        policyname = ET.SubElement(rules, "policyname")
        if kwargs.pop('delete_policyname', False) is True:
            delete_policyname = config.find('.//*policyname')
            delete_policyname.set('operation', 'delete')
            
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        