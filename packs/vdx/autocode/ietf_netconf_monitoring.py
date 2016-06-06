#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_monitoring(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def netconf_state_datastores_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name = ET.SubElement(datastore, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        locks = ET.SubElement(datastore, "locks")
        if kwargs.pop('delete_locks', False) is True:
            delete_locks = config.find('.//*locks')
            delete_locks.set('operation', 'delete')
            
        lock_type = ET.SubElement(locks, "lock-type")
        if kwargs.pop('delete_lock_type', False) is True:
            delete_lock_type = config.find('.//*lock-type')
            delete_lock_type.set('operation', 'delete')
            
        global_lock = ET.SubElement(lock_type, "global-lock")
        if kwargs.pop('delete_global_lock', False) is True:
            delete_global_lock = config.find('.//*global-lock')
            delete_global_lock.set('operation', 'delete')
            
        global_lock = ET.SubElement(global_lock, "global-lock")
        if kwargs.pop('delete_global_lock', False) is True:
            delete_global_lock = config.find('.//*global-lock')
            delete_global_lock.set('operation', 'delete')
            
        locked_by_session = ET.SubElement(global_lock, "locked-by-session")
        if kwargs.pop('delete_locked_by_session', False) is True:
            delete_locked_by_session = config.find('.//*locked-by-session')
            delete_locked_by_session.set('operation', 'delete')
            
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        locks = ET.SubElement(datastore, "locks")
        if kwargs.pop('delete_locks', False) is True:
            delete_locks = config.find('.//*locks')
            delete_locks.set('operation', 'delete')
            
        lock_type = ET.SubElement(locks, "lock-type")
        if kwargs.pop('delete_lock_type', False) is True:
            delete_lock_type = config.find('.//*lock-type')
            delete_lock_type.set('operation', 'delete')
            
        global_lock = ET.SubElement(lock_type, "global-lock")
        if kwargs.pop('delete_global_lock', False) is True:
            delete_global_lock = config.find('.//*global-lock')
            delete_global_lock.set('operation', 'delete')
            
        global_lock = ET.SubElement(global_lock, "global-lock")
        if kwargs.pop('delete_global_lock', False) is True:
            delete_global_lock = config.find('.//*global-lock')
            delete_global_lock.set('operation', 'delete')
            
        locked_time = ET.SubElement(global_lock, "locked-time")
        if kwargs.pop('delete_locked_time', False) is True:
            delete_locked_time = config.find('.//*locked-time')
            delete_locked_time.set('operation', 'delete')
            
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_lock_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        locks = ET.SubElement(datastore, "locks")
        if kwargs.pop('delete_locks', False) is True:
            delete_locks = config.find('.//*locks')
            delete_locks.set('operation', 'delete')
            
        lock_type = ET.SubElement(locks, "lock-type")
        if kwargs.pop('delete_lock_type', False) is True:
            delete_lock_type = config.find('.//*lock-type')
            delete_lock_type.set('operation', 'delete')
            
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        lock_id = ET.SubElement(partial_lock, "lock-id")
        if kwargs.pop('delete_lock_id', False) is True:
            delete_lock_id = config.find('.//*lock-id')
            delete_lock_id.set('operation', 'delete')
            
        lock_id.text = kwargs.pop('lock_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        locks = ET.SubElement(datastore, "locks")
        if kwargs.pop('delete_locks', False) is True:
            delete_locks = config.find('.//*locks')
            delete_locks.set('operation', 'delete')
            
        lock_type = ET.SubElement(locks, "lock-type")
        if kwargs.pop('delete_lock_type', False) is True:
            delete_lock_type = config.find('.//*lock-type')
            delete_lock_type.set('operation', 'delete')
            
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        if kwargs.pop('delete_lock_id', False) is True:
            delete_lock_id = config.find('.//*lock-id')
            delete_lock_id.set('operation', 'delete')
                
        locked_by_session = ET.SubElement(partial_lock, "locked-by-session")
        if kwargs.pop('delete_locked_by_session', False) is True:
            delete_locked_by_session = config.find('.//*locked-by-session')
            delete_locked_by_session.set('operation', 'delete')
            
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        locks = ET.SubElement(datastore, "locks")
        if kwargs.pop('delete_locks', False) is True:
            delete_locks = config.find('.//*locks')
            delete_locks.set('operation', 'delete')
            
        lock_type = ET.SubElement(locks, "lock-type")
        if kwargs.pop('delete_lock_type', False) is True:
            delete_lock_type = config.find('.//*lock-type')
            delete_lock_type.set('operation', 'delete')
            
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        if kwargs.pop('delete_partial_lock', False) is True:
            delete_partial_lock = config.find('.//*partial-lock')
            delete_partial_lock.set('operation', 'delete')
            
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        if kwargs.pop('delete_lock_id', False) is True:
            delete_lock_id = config.find('.//*lock-id')
            delete_lock_id.set('operation', 'delete')
                
        locked_time = ET.SubElement(partial_lock, "locked-time")
        if kwargs.pop('delete_locked_time', False) is True:
            delete_locked_time = config.find('.//*locked-time')
            delete_locked_time.set('operation', 'delete')
            
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        datastores = ET.SubElement(netconf_state, "datastores")
        if kwargs.pop('delete_datastores', False) is True:
            delete_datastores = config.find('.//*datastores')
            delete_datastores.set('operation', 'delete')
            
        datastore = ET.SubElement(datastores, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        transaction_id = ET.SubElement(datastore, "transaction-id", xmlns="http://tail-f.com/yang/netconf-monitoring")
        if kwargs.pop('delete_transaction_id', False) is True:
            delete_transaction_id = config.find('.//*transaction-id')
            delete_transaction_id.set('operation', 'delete')
            
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        schemas = ET.SubElement(netconf_state, "schemas")
        if kwargs.pop('delete_schemas', False) is True:
            delete_schemas = config.find('.//*schemas')
            delete_schemas.set('operation', 'delete')
            
        schema = ET.SubElement(schemas, "schema")
        if kwargs.pop('delete_schema', False) is True:
            delete_schema = config.find('.//*schema')
            delete_schema.set('operation', 'delete')
            
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
                
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        if kwargs.pop('delete_format', False) is True:
            delete_format = config.find('.//*format')
            delete_format.set('operation', 'delete')
                
        identifier = ET.SubElement(schema, "identifier")
        if kwargs.pop('delete_identifier', False) is True:
            delete_identifier = config.find('.//*identifier')
            delete_identifier.set('operation', 'delete')
            
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        schemas = ET.SubElement(netconf_state, "schemas")
        if kwargs.pop('delete_schemas', False) is True:
            delete_schemas = config.find('.//*schemas')
            delete_schemas.set('operation', 'delete')
            
        schema = ET.SubElement(schemas, "schema")
        if kwargs.pop('delete_schema', False) is True:
            delete_schema = config.find('.//*schema')
            delete_schema.set('operation', 'delete')
            
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        if kwargs.pop('delete_identifier', False) is True:
            delete_identifier = config.find('.//*identifier')
            delete_identifier.set('operation', 'delete')
                
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        if kwargs.pop('delete_format', False) is True:
            delete_format = config.find('.//*format')
            delete_format.set('operation', 'delete')
                
        version = ET.SubElement(schema, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        schemas = ET.SubElement(netconf_state, "schemas")
        if kwargs.pop('delete_schemas', False) is True:
            delete_schemas = config.find('.//*schemas')
            delete_schemas.set('operation', 'delete')
            
        schema = ET.SubElement(schemas, "schema")
        if kwargs.pop('delete_schema', False) is True:
            delete_schema = config.find('.//*schema')
            delete_schema.set('operation', 'delete')
            
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        if kwargs.pop('delete_identifier', False) is True:
            delete_identifier = config.find('.//*identifier')
            delete_identifier.set('operation', 'delete')
                
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
                
        format = ET.SubElement(schema, "format")
        if kwargs.pop('delete_format', False) is True:
            delete_format = config.find('.//*format')
            delete_format.set('operation', 'delete')
            
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        schemas = ET.SubElement(netconf_state, "schemas")
        if kwargs.pop('delete_schemas', False) is True:
            delete_schemas = config.find('.//*schemas')
            delete_schemas.set('operation', 'delete')
            
        schema = ET.SubElement(schemas, "schema")
        if kwargs.pop('delete_schema', False) is True:
            delete_schema = config.find('.//*schema')
            delete_schema.set('operation', 'delete')
            
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        if kwargs.pop('delete_identifier', False) is True:
            delete_identifier = config.find('.//*identifier')
            delete_identifier.set('operation', 'delete')
                
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
                
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        if kwargs.pop('delete_format', False) is True:
            delete_format = config.find('.//*format')
            delete_format.set('operation', 'delete')
                
        namespace = ET.SubElement(schema, "namespace")
        if kwargs.pop('delete_namespace', False) is True:
            delete_namespace = config.find('.//*namespace')
            delete_namespace.set('operation', 'delete')
            
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id = ET.SubElement(session, "session-id")
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
            
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_transport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        transport = ET.SubElement(session, "transport")
        if kwargs.pop('delete_transport', False) is True:
            delete_transport = config.find('.//*transport')
            delete_transport.set('operation', 'delete')
            
        transport.text = kwargs.pop('transport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        username = ET.SubElement(session, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        source_host = ET.SubElement(session, "source-host")
        if kwargs.pop('delete_source_host', False) is True:
            delete_source_host = config.find('.//*source-host')
            delete_source_host.set('operation', 'delete')
            
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_login_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        login_time = ET.SubElement(session, "login-time")
        if kwargs.pop('delete_login_time', False) is True:
            delete_login_time = config.find('.//*login-time')
            delete_login_time.set('operation', 'delete')
            
        login_time.text = kwargs.pop('login_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        in_rpcs = ET.SubElement(session, "in-rpcs")
        if kwargs.pop('delete_in_rpcs', False) is True:
            delete_in_rpcs = config.find('.//*in-rpcs')
            delete_in_rpcs.set('operation', 'delete')
            
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        in_bad_rpcs = ET.SubElement(session, "in-bad-rpcs")
        if kwargs.pop('delete_in_bad_rpcs', False) is True:
            delete_in_bad_rpcs = config.find('.//*in-bad-rpcs')
            delete_in_bad_rpcs.set('operation', 'delete')
            
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        out_rpc_errors = ET.SubElement(session, "out-rpc-errors")
        if kwargs.pop('delete_out_rpc_errors', False) is True:
            delete_out_rpc_errors = config.find('.//*out-rpc-errors')
            delete_out_rpc_errors.set('operation', 'delete')
            
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        sessions = ET.SubElement(netconf_state, "sessions")
        if kwargs.pop('delete_sessions', False) is True:
            delete_sessions = config.find('.//*sessions')
            delete_sessions.set('operation', 'delete')
            
        session = ET.SubElement(sessions, "session")
        if kwargs.pop('delete_session', False) is True:
            delete_session = config.find('.//*session')
            delete_session.set('operation', 'delete')
            
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        if kwargs.pop('delete_session_id', False) is True:
            delete_session_id = config.find('.//*session-id')
            delete_session_id.set('operation', 'delete')
                
        out_notifications = ET.SubElement(session, "out-notifications")
        if kwargs.pop('delete_out_notifications', False) is True:
            delete_out_notifications = config.find('.//*out-notifications')
            delete_out_notifications.set('operation', 'delete')
            
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_netconf_start_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        netconf_start_time = ET.SubElement(statistics, "netconf-start-time")
        if kwargs.pop('delete_netconf_start_time', False) is True:
            delete_netconf_start_time = config.find('.//*netconf-start-time')
            delete_netconf_start_time.set('operation', 'delete')
            
        netconf_start_time.text = kwargs.pop('netconf_start_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_hellos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        in_bad_hellos = ET.SubElement(statistics, "in-bad-hellos")
        if kwargs.pop('delete_in_bad_hellos', False) is True:
            delete_in_bad_hellos = config.find('.//*in-bad-hellos')
            delete_in_bad_hellos.set('operation', 'delete')
            
        in_bad_hellos.text = kwargs.pop('in_bad_hellos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        in_sessions = ET.SubElement(statistics, "in-sessions")
        if kwargs.pop('delete_in_sessions', False) is True:
            delete_in_sessions = config.find('.//*in-sessions')
            delete_in_sessions.set('operation', 'delete')
            
        in_sessions.text = kwargs.pop('in_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_dropped_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        dropped_sessions = ET.SubElement(statistics, "dropped-sessions")
        if kwargs.pop('delete_dropped_sessions', False) is True:
            delete_dropped_sessions = config.find('.//*dropped-sessions')
            delete_dropped_sessions.set('operation', 'delete')
            
        dropped_sessions.text = kwargs.pop('dropped_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        in_rpcs = ET.SubElement(statistics, "in-rpcs")
        if kwargs.pop('delete_in_rpcs', False) is True:
            delete_in_rpcs = config.find('.//*in-rpcs')
            delete_in_rpcs.set('operation', 'delete')
            
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        in_bad_rpcs = ET.SubElement(statistics, "in-bad-rpcs")
        if kwargs.pop('delete_in_bad_rpcs', False) is True:
            delete_in_bad_rpcs = config.find('.//*in-bad-rpcs')
            delete_in_bad_rpcs.set('operation', 'delete')
            
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        out_rpc_errors = ET.SubElement(statistics, "out-rpc-errors")
        if kwargs.pop('delete_out_rpc_errors', False) is True:
            delete_out_rpc_errors = config.find('.//*out-rpc-errors')
            delete_out_rpc_errors.set('operation', 'delete')
            
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        statistics = ET.SubElement(netconf_state, "statistics")
        if kwargs.pop('delete_statistics', False) is True:
            delete_statistics = config.find('.//*statistics')
            delete_statistics.set('operation', 'delete')
            
        out_notifications = ET.SubElement(statistics, "out-notifications")
        if kwargs.pop('delete_out_notifications', False) is True:
            delete_out_notifications = config.find('.//*out-notifications')
            delete_out_notifications.set('operation', 'delete')
            
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        if kwargs.pop('delete_files', False) is True:
            delete_files = config.find('.//*files')
            delete_files.set('operation', 'delete')
            
        file = ET.SubElement(files, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        name = ET.SubElement(file, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_creator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        if kwargs.pop('delete_files', False) is True:
            delete_files = config.find('.//*files')
            delete_files.set('operation', 'delete')
            
        file = ET.SubElement(files, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        creator = ET.SubElement(file, "creator")
        if kwargs.pop('delete_creator', False) is True:
            delete_creator = config.find('.//*creator')
            delete_creator.set('operation', 'delete')
            
        creator.text = kwargs.pop('creator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_created(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        if kwargs.pop('delete_files', False) is True:
            delete_files = config.find('.//*files')
            delete_files.set('operation', 'delete')
            
        file = ET.SubElement(files, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        created = ET.SubElement(file, "created")
        if kwargs.pop('delete_created', False) is True:
            delete_created = config.find('.//*created')
            delete_created.set('operation', 'delete')
            
        created.text = kwargs.pop('created')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        if kwargs.pop('delete_netconf_state', False) is True:
            delete_netconf_state = config.find('.//*netconf-state')
            delete_netconf_state.set('operation', 'delete')
            
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        if kwargs.pop('delete_files', False) is True:
            delete_files = config.find('.//*files')
            delete_files.set('operation', 'delete')
            
        file = ET.SubElement(files, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        context = ET.SubElement(file, "context")
        if kwargs.pop('delete_context', False) is True:
            delete_context = config.find('.//*context')
            delete_context.set('operation', 'delete')
            
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        if kwargs.pop('delete_get_schema', False) is True:
            delete_get_schema = config.find('.//*get-schema')
            delete_get_schema.set('operation', 'delete')
            
        input = ET.SubElement(get_schema, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        identifier = ET.SubElement(input, "identifier")
        if kwargs.pop('delete_identifier', False) is True:
            delete_identifier = config.find('.//*identifier')
            delete_identifier.set('operation', 'delete')
            
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        if kwargs.pop('delete_get_schema', False) is True:
            delete_get_schema = config.find('.//*get-schema')
            delete_get_schema.set('operation', 'delete')
            
        input = ET.SubElement(get_schema, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        version = ET.SubElement(input, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        if kwargs.pop('delete_get_schema', False) is True:
            delete_get_schema = config.find('.//*get-schema')
            delete_get_schema.set('operation', 'delete')
            
        input = ET.SubElement(get_schema, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        format = ET.SubElement(input, "format")
        if kwargs.pop('delete_format', False) is True:
            delete_format = config.find('.//*format')
            delete_format.set('operation', 'delete')
            
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        