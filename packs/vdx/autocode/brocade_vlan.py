#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_vlan(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def vlan_classifier_rule_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        rule = ET.SubElement(classifier, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        ruleid = ET.SubElement(rule, "ruleid")
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
            
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_mac_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        rule = ET.SubElement(classifier, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        class_type = ET.SubElement(rule, "class-type")
        if kwargs.pop('delete_class_type', False) is True:
            delete_class_type = config.find('.//*class-type')
            delete_class_type.set('operation', 'delete')
            
        mac = ET.SubElement(class_type, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac = ET.SubElement(mac, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        address = ET.SubElement(mac, "address")
        if kwargs.pop('delete_address', False) is True:
            delete_address = config.find('.//*address')
            delete_address.set('operation', 'delete')
            
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_proto_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        rule = ET.SubElement(classifier, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        class_type = ET.SubElement(rule, "class-type")
        if kwargs.pop('delete_class_type', False) is True:
            delete_class_type = config.find('.//*class-type')
            delete_class_type.set('operation', 'delete')
            
        proto = ET.SubElement(class_type, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        proto = ET.SubElement(proto, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        proto_val = ET.SubElement(proto, "proto-val")
        if kwargs.pop('delete_proto_val', False) is True:
            delete_proto_val = config.find('.//*proto-val')
            delete_proto_val.set('operation', 'delete')
            
        proto_val.text = kwargs.pop('proto_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_encap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        rule = ET.SubElement(classifier, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        class_type = ET.SubElement(rule, "class-type")
        if kwargs.pop('delete_class_type', False) is True:
            delete_class_type = config.find('.//*class-type')
            delete_class_type.set('operation', 'delete')
            
        proto = ET.SubElement(class_type, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        proto = ET.SubElement(proto, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        encap = ET.SubElement(proto, "encap")
        if kwargs.pop('delete_encap', False) is True:
            delete_encap = config.find('.//*encap')
            delete_encap.set('operation', 'delete')
            
        encap.text = kwargs.pop('encap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_groupid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        group = ET.SubElement(classifier, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        if kwargs.pop('delete_oper', False) is True:
            delete_oper = config.find('.//*oper')
            delete_oper.set('operation', 'delete')
                
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        if kwargs.pop('delete_rule_name', False) is True:
            delete_rule_name = config.find('.//*rule-name')
            delete_rule_name.set('operation', 'delete')
                
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        groupid = ET.SubElement(group, "groupid")
        if kwargs.pop('delete_groupid', False) is True:
            delete_groupid = config.find('.//*groupid')
            delete_groupid.set('operation', 'delete')
            
        groupid.text = kwargs.pop('groupid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_oper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        group = ET.SubElement(classifier, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        if kwargs.pop('delete_groupid', False) is True:
            delete_groupid = config.find('.//*groupid')
            delete_groupid.set('operation', 'delete')
                
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        if kwargs.pop('delete_rule_name', False) is True:
            delete_rule_name = config.find('.//*rule-name')
            delete_rule_name.set('operation', 'delete')
                
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        oper = ET.SubElement(group, "oper")
        if kwargs.pop('delete_oper', False) is True:
            delete_oper = config.find('.//*oper')
            delete_oper.set('operation', 'delete')
            
        oper.text = kwargs.pop('oper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        group = ET.SubElement(classifier, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        if kwargs.pop('delete_groupid', False) is True:
            delete_groupid = config.find('.//*groupid')
            delete_groupid.set('operation', 'delete')
                
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        if kwargs.pop('delete_oper', False) is True:
            delete_oper = config.find('.//*oper')
            delete_oper.set('operation', 'delete')
                
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
                
        rule_name = ET.SubElement(group, "rule-name")
        if kwargs.pop('delete_rule_name', False) is True:
            delete_rule_name = config.find('.//*rule-name')
            delete_rule_name.set('operation', 'delete')
            
        rule_name.text = kwargs.pop('rule_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        classifier = ET.SubElement(vlan, "classifier")
        if kwargs.pop('delete_classifier', False) is True:
            delete_classifier = config.find('.//*classifier')
            delete_classifier.set('operation', 'delete')
            
        group = ET.SubElement(classifier, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        if kwargs.pop('delete_groupid', False) is True:
            delete_groupid = config.find('.//*groupid')
            delete_groupid.set('operation', 'delete')
                
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        if kwargs.pop('delete_oper', False) is True:
            delete_oper = config.find('.//*oper')
            delete_oper.set('operation', 'delete')
                
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        if kwargs.pop('delete_rule_name', False) is True:
            delete_rule_name = config.find('.//*rule-name')
            delete_rule_name.set('operation', 'delete')
                
        ruleid = ET.SubElement(group, "ruleid")
        if kwargs.pop('delete_ruleid', False) is True:
            delete_ruleid = config.find('.//*ruleid')
            delete_ruleid.set('operation', 'delete')
            
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_dot1q_tag_native(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        dot1q = ET.SubElement(vlan, "dot1q")
        if kwargs.pop('delete_dot1q', False) is True:
            delete_dot1q = config.find('.//*dot1q')
            delete_dot1q.set('operation', 'delete')
            
        tag = ET.SubElement(dot1q, "tag")
        if kwargs.pop('delete_tag', False) is True:
            delete_tag = config.find('.//*tag')
            delete_tag.set('operation', 'delete')
            
        native = ET.SubElement(tag, "native")
        if kwargs.pop('delete_native', False) is True:
            delete_native = config.find('.//*native')
            delete_native.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        