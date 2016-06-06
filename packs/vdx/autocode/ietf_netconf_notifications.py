#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_notifications(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def netconf_config_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        server = ET.SubElement(server_or_user, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        server = ET.SubElement(server, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        username = ET.SubElement(by_user, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        session_id = ET.SubElement(by_user, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        source_host = ET.SubElement(by_user, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        datastore = ET.SubElement(netconf_config_change, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_target(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        edit = ET.SubElement(netconf_config_change, "edit")
        if kwargs.pop('delete_edit', False) is True:
            delete_edit = config.find('.//*edit')
            delete_edit.set('operation', 'delete')
            
        target = ET.SubElement(edit, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        target.text = kwargs.pop('target')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_config_change', False) is True:
            delete_netconf_config_change = config.find('.//*netconf-config-change')
            delete_netconf_config_change.set('operation', 'delete')
            
        edit = ET.SubElement(netconf_config_change, "edit")
        if kwargs.pop('delete_edit', False) is True:
            delete_edit = config.find('.//*edit')
            delete_edit.set('operation', 'delete')
            
        operation = ET.SubElement(edit, "operation")
        if kwargs.pop('delete_operation', False) is True:
            delete_operation = config.find('.//*operation')
            delete_operation.set('operation', 'delete')
            
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_capability_change', False) is True:
            delete_netconf_capability_change = config.find('.//*netconf-capability-change')
            delete_netconf_capability_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        server = ET.SubElement(server_or_user, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        server = ET.SubElement(server, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_capability_change', False) is True:
            delete_netconf_capability_change = config.find('.//*netconf-capability-change')
            delete_netconf_capability_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        username = ET.SubElement(by_user, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_capability_change', False) is True:
            delete_netconf_capability_change = config.find('.//*netconf-capability-change')
            delete_netconf_capability_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        session_id = ET.SubElement(by_user, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_capability_change', False) is True:
            delete_netconf_capability_change = config.find('.//*netconf-capability-change')
            delete_netconf_capability_change.set('operation', 'delete')
            
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        if kwargs.pop('delete_changed_by', False) is True:
            delete_changed_by = config.find('.//*changed-by')
            delete_changed_by.set('operation', 'delete')
            
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        if kwargs.pop('delete_server_or_user', False) is True:
            delete_server_or_user = config.find('.//*server-or-user')
            delete_server_or_user.set('operation', 'delete')
            
        by_user = ET.SubElement(server_or_user, "by-user")
        if kwargs.pop('delete_by_user', False) is True:
            delete_by_user = config.find('.//*by-user')
            delete_by_user.set('operation', 'delete')
            
        source_host = ET.SubElement(by_user, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_start', False) is True:
            delete_netconf_session_start = config.find('.//*netconf-session-start')
            delete_netconf_session_start.set('operation', 'delete')
            
        username = ET.SubElement(netconf_session_start, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_start', False) is True:
            delete_netconf_session_start = config.find('.//*netconf-session-start')
            delete_netconf_session_start.set('operation', 'delete')
            
        session_id = ET.SubElement(netconf_session_start, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_start', False) is True:
            delete_netconf_session_start = config.find('.//*netconf-session-start')
            delete_netconf_session_start.set('operation', 'delete')
            
        source_host = ET.SubElement(netconf_session_start, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_end', False) is True:
            delete_netconf_session_end = config.find('.//*netconf-session-end')
            delete_netconf_session_end.set('operation', 'delete')
            
        username = ET.SubElement(netconf_session_end, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_end', False) is True:
            delete_netconf_session_end = config.find('.//*netconf-session-end')
            delete_netconf_session_end.set('operation', 'delete')
            
        session_id = ET.SubElement(netconf_session_end, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_end', False) is True:
            delete_netconf_session_end = config.find('.//*netconf-session-end')
            delete_netconf_session_end.set('operation', 'delete')
            
        source_host = ET.SubElement(netconf_session_end, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_killed_by(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_end', False) is True:
            delete_netconf_session_end = config.find('.//*netconf-session-end')
            delete_netconf_session_end.set('operation', 'delete')
            
        killed_by = ET.SubElement(netconf_session_end, "killed-by")
        if kwargs.pop('delete_killed_by', False) is True:
            delete_killed_by = config.find('.//*killed-by')
            delete_killed_by.set('operation', 'delete')
            
        killed_by.text = kwargs.pop('killed_by')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_termination_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_session_end', False) is True:
            delete_netconf_session_end = config.find('.//*netconf-session-end')
            delete_netconf_session_end.set('operation', 'delete')
            
        termination_reason = ET.SubElement(netconf_session_end, "termination-reason")
        if kwargs.pop('delete_termination_reason', False) is True:
            delete_termination_reason = config.find('.//*termination-reason')
            delete_termination_reason.set('operation', 'delete')
            
        termination_reason.text = kwargs.pop('termination_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_confirmed_commit', False) is True:
            delete_netconf_confirmed_commit = config.find('.//*netconf-confirmed-commit')
            delete_netconf_confirmed_commit.set('operation', 'delete')
            
        username = ET.SubElement(netconf_confirmed_commit, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_confirmed_commit', False) is True:
            delete_netconf_confirmed_commit = config.find('.//*netconf-confirmed-commit')
            delete_netconf_confirmed_commit.set('operation', 'delete')
            
        session_id = ET.SubElement(netconf_confirmed_commit, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_confirmed_commit', False) is True:
            delete_netconf_confirmed_commit = config.find('.//*netconf-confirmed-commit')
            delete_netconf_confirmed_commit.set('operation', 'delete')
            
        source_host = ET.SubElement(netconf_confirmed_commit, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_confirm_event(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_confirmed_commit', False) is True:
            delete_netconf_confirmed_commit = config.find('.//*netconf-confirmed-commit')
            delete_netconf_confirmed_commit.set('operation', 'delete')
            
        confirm_event = ET.SubElement(netconf_confirmed_commit, "confirm-event")
        if kwargs.pop('delete_confirm_event', False) is True:
            delete_confirm_event = config.find('.//*confirm-event')
            delete_confirm_event.set('operation', 'delete')
            
        confirm_event.text = kwargs.pop('confirm_event')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        if kwargs.pop('delete_netconf_confirmed_commit', False) is True:
            delete_netconf_confirmed_commit = config.find('.//*netconf-confirmed-commit')
            delete_netconf_confirmed_commit.set('operation', 'delete')
            
        timeout = ET.SubElement(netconf_confirmed_commit, "timeout")
        if kwargs.pop('delete_timeout', False) is True:
            delete_timeout = config.find('.//*timeout')
            delete_timeout.set('operation', 'delete')
            
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        