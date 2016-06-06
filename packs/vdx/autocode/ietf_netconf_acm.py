#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_acm(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def nacm_enable_nacm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        enable_nacm = ET.SubElement(nacm, "enable-nacm")
        if kwargs.pop('delete_enable_nacm', False) is True:
            delete_enable_nacm = config.find('.//*enable-nacm')
            delete_enable_nacm.set('operation', 'delete')
            
        enable_nacm.text = kwargs.pop('enable_nacm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        read_default = ET.SubElement(nacm, "read-default")
        if kwargs.pop('delete_read_default', False) is True:
            delete_read_default = config.find('.//*read-default')
            delete_read_default.set('operation', 'delete')
            
        read_default.text = kwargs.pop('read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_write_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        write_default = ET.SubElement(nacm, "write-default")
        if kwargs.pop('delete_write_default', False) is True:
            delete_write_default = config.find('.//*write-default')
            delete_write_default.set('operation', 'delete')
            
        write_default.text = kwargs.pop('write_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        exec_default = ET.SubElement(nacm, "exec-default")
        if kwargs.pop('delete_exec_default', False) is True:
            delete_exec_default = config.find('.//*exec-default')
            delete_exec_default.set('operation', 'delete')
            
        exec_default.text = kwargs.pop('exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_enable_external_groups(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        enable_external_groups = ET.SubElement(nacm, "enable-external-groups")
        if kwargs.pop('delete_enable_external_groups', False) is True:
            delete_enable_external_groups = config.find('.//*enable-external-groups')
            delete_enable_external_groups.set('operation', 'delete')
            
        enable_external_groups.text = kwargs.pop('enable_external_groups')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        denied_operations = ET.SubElement(nacm, "denied-operations")
        if kwargs.pop('delete_denied_operations', False) is True:
            delete_denied_operations = config.find('.//*denied-operations')
            delete_denied_operations.set('operation', 'delete')
            
        denied_operations.text = kwargs.pop('denied_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_data_writes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        denied_data_writes = ET.SubElement(nacm, "denied-data-writes")
        if kwargs.pop('delete_denied_data_writes', False) is True:
            delete_denied_data_writes = config.find('.//*denied-data-writes')
            delete_denied_data_writes.set('operation', 'delete')
            
        denied_data_writes.text = kwargs.pop('denied_data_writes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        denied_notifications = ET.SubElement(nacm, "denied-notifications")
        if kwargs.pop('delete_denied_notifications', False) is True:
            delete_denied_notifications = config.find('.//*denied-notifications')
            delete_denied_notifications.set('operation', 'delete')
            
        denied_notifications.text = kwargs.pop('denied_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        groups = ET.SubElement(nacm, "groups")
        if kwargs.pop('delete_groups', False) is True:
            delete_groups = config.find('.//*groups')
            delete_groups.set('operation', 'delete')
            
        group = ET.SubElement(groups, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        name = ET.SubElement(group, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_gid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        groups = ET.SubElement(nacm, "groups")
        if kwargs.pop('delete_groups', False) is True:
            delete_groups = config.find('.//*groups')
            delete_groups.set('operation', 'delete')
            
        group = ET.SubElement(groups, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        name_key = ET.SubElement(group, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        gid = ET.SubElement(group, "gid", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_gid', False) is True:
            delete_gid = config.find('.//*gid')
            delete_gid.set('operation', 'delete')
            
        gid.text = kwargs.pop('gid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name = ET.SubElement(rule_list, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name = ET.SubElement(rule, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_module_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        module_name = ET.SubElement(rule, "module-name")
        if kwargs.pop('delete_module_name', False) is True:
            delete_module_name = config.find('.//*module-name')
            delete_module_name.set('operation', 'delete')
            
        module_name.text = kwargs.pop('module_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_protocol_operation_rpc_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule_type = ET.SubElement(rule, "rule-type")
        if kwargs.pop('delete_rule_type', False) is True:
            delete_rule_type = config.find('.//*rule-type')
            delete_rule_type.set('operation', 'delete')
            
        protocol_operation = ET.SubElement(rule_type, "protocol-operation")
        if kwargs.pop('delete_protocol_operation', False) is True:
            delete_protocol_operation = config.find('.//*protocol-operation')
            delete_protocol_operation.set('operation', 'delete')
            
        rpc_name = ET.SubElement(protocol_operation, "rpc-name")
        if kwargs.pop('delete_rpc_name', False) is True:
            delete_rpc_name = config.find('.//*rpc-name')
            delete_rpc_name.set('operation', 'delete')
            
        rpc_name.text = kwargs.pop('rpc_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_notification_notification_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule_type = ET.SubElement(rule, "rule-type")
        if kwargs.pop('delete_rule_type', False) is True:
            delete_rule_type = config.find('.//*rule-type')
            delete_rule_type.set('operation', 'delete')
            
        notification = ET.SubElement(rule_type, "notification")
        if kwargs.pop('delete_notification', False) is True:
            delete_notification = config.find('.//*notification')
            delete_notification.set('operation', 'delete')
            
        notification_name = ET.SubElement(notification, "notification-name")
        if kwargs.pop('delete_notification_name', False) is True:
            delete_notification_name = config.find('.//*notification-name')
            delete_notification_name.set('operation', 'delete')
            
        notification_name.text = kwargs.pop('notification_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_data_node_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule_type = ET.SubElement(rule, "rule-type")
        if kwargs.pop('delete_rule_type', False) is True:
            delete_rule_type = config.find('.//*rule-type')
            delete_rule_type.set('operation', 'delete')
            
        data_node = ET.SubElement(rule_type, "data-node")
        if kwargs.pop('delete_data_node', False) is True:
            delete_data_node = config.find('.//*data-node')
            delete_data_node.set('operation', 'delete')
            
        path = ET.SubElement(data_node, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_operations = ET.SubElement(rule, "access-operations")
        if kwargs.pop('delete_access_operations', False) is True:
            delete_access_operations = config.find('.//*access-operations')
            delete_access_operations.set('operation', 'delete')
            
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action = ET.SubElement(rule, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        comment = ET.SubElement(rule, "comment")
        if kwargs.pop('delete_comment', False) is True:
            delete_comment = config.find('.//*comment')
            delete_comment.set('operation', 'delete')
            
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        context = ET.SubElement(rule, "context", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        rule = ET.SubElement(rule_list, "rule")
        if kwargs.pop('delete_rule', False) is True:
            delete_rule = config.find('.//*rule')
            delete_rule.set('operation', 'delete')
            
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        log_if_permit = ET.SubElement(rule, "log-if-permit", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_log_if_permit', False) is True:
            delete_log_if_permit = config.find('.//*log-if-permit')
            delete_log_if_permit.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name = ET.SubElement(cmdrule, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        context = ET.SubElement(cmdrule, "context")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_command(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        command = ET.SubElement(cmdrule, "command")
        if kwargs.pop('delete_command', False) is True:
            delete_command = config.find('.//*command')
            delete_command.set('operation', 'delete')
            
        command.text = kwargs.pop('command')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        access_operations = ET.SubElement(cmdrule, "access-operations")
        if kwargs.pop('delete_access_operations', False) is True:
            delete_access_operations = config.find('.//*access-operations')
            delete_access_operations.set('operation', 'delete')
            
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        action = ET.SubElement(cmdrule, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        log_if_permit = ET.SubElement(cmdrule, "log-if-permit")
        if kwargs.pop('delete_log_if_permit', False) is True:
            delete_log_if_permit = config.find('.//*log-if-permit')
            delete_log_if_permit.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        rule_list = ET.SubElement(nacm, "rule-list")
        if kwargs.pop('delete_rule_list', False) is True:
            delete_rule_list = config.find('.//*rule-list')
            delete_rule_list.set('operation', 'delete')
            
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmdrule', False) is True:
            delete_cmdrule = config.find('.//*cmdrule')
            delete_cmdrule.set('operation', 'delete')
            
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        comment = ET.SubElement(cmdrule, "comment")
        if kwargs.pop('delete_comment', False) is True:
            delete_comment = config.find('.//*comment')
            delete_comment.set('operation', 'delete')
            
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        cmd_read_default = ET.SubElement(nacm, "cmd-read-default", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmd_read_default', False) is True:
            delete_cmd_read_default = config.find('.//*cmd-read-default')
            delete_cmd_read_default.set('operation', 'delete')
            
        cmd_read_default.text = kwargs.pop('cmd_read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        cmd_exec_default = ET.SubElement(nacm, "cmd-exec-default", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_cmd_exec_default', False) is True:
            delete_cmd_exec_default = config.find('.//*cmd-exec-default')
            delete_cmd_exec_default.set('operation', 'delete')
            
        cmd_exec_default.text = kwargs.pop('cmd_exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_log_if_default_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        if kwargs.pop('delete_nacm', False) is True:
            delete_nacm = config.find('.//*nacm')
            delete_nacm.set('operation', 'delete')
            
        log_if_default_permit = ET.SubElement(nacm, "log-if-default-permit", xmlns="http://tail-f.com/yang/acm")
        if kwargs.pop('delete_log_if_default_permit', False) is True:
            delete_log_if_default_permit = config.find('.//*log-if-default-permit')
            delete_log_if_default_permit.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        