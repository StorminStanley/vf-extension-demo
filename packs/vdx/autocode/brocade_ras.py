#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ras(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def logging_raslog_message_msgId_msgId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        message = ET.SubElement(raslog, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        msgId = ET.SubElement(message, "msgId")
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
            
        msgId = ET.SubElement(msgId, "msgId")
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
            
        msgId.text = kwargs.pop('msgId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        message = ET.SubElement(raslog, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        msgId = ET.SubElement(message, "msgId")
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
            
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
                
        severity = ET.SubElement(msgId, "severity")
        if kwargs.pop('delete_severity', False) is True:
            delete_severity = config.find('.//*severity')
            delete_severity.set('operation', 'delete')
            
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        message = ET.SubElement(raslog, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        msgId = ET.SubElement(message, "msgId")
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
            
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
                
        suppress = ET.SubElement(msgId, "suppress")
        if kwargs.pop('delete_suppress', False) is True:
            delete_suppress = config.find('.//*suppress')
            delete_suppress.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_syslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        message = ET.SubElement(raslog, "message")
        if kwargs.pop('delete_message', False) is True:
            delete_message = config.find('.//*message')
            delete_message.set('operation', 'delete')
            
        msgId = ET.SubElement(message, "msgId")
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
            
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        if kwargs.pop('delete_msgId', False) is True:
            delete_msgId = config.find('.//*msgId')
            delete_msgId.set('operation', 'delete')
                
        syslog = ET.SubElement(msgId, "syslog")
        if kwargs.pop('delete_syslog', False) is True:
            delete_syslog = config.find('.//*syslog')
            delete_syslog.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_module_modId_modId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        module = ET.SubElement(raslog, "module")
        if kwargs.pop('delete_module', False) is True:
            delete_module = config.find('.//*module')
            delete_module.set('operation', 'delete')
            
        modId = ET.SubElement(module, "modId")
        if kwargs.pop('delete_modId', False) is True:
            delete_modId = config.find('.//*modId')
            delete_modId.set('operation', 'delete')
            
        modId = ET.SubElement(modId, "modId")
        if kwargs.pop('delete_modId', False) is True:
            delete_modId = config.find('.//*modId')
            delete_modId.set('operation', 'delete')
            
        modId.text = kwargs.pop('modId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_console(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        raslog = ET.SubElement(logging, "raslog")
        if kwargs.pop('delete_raslog', False) is True:
            delete_raslog = config.find('.//*raslog')
            delete_raslog.set('operation', 'delete')
            
        console = ET.SubElement(raslog, "console")
        if kwargs.pop('delete_console', False) is True:
            delete_console = config.find('.//*console')
            delete_console.set('operation', 'delete')
            
        console.text = kwargs.pop('console')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_syslogip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_server = ET.SubElement(logging, "syslog-server")
        if kwargs.pop('delete_syslog_server', False) is True:
            delete_syslog_server = config.find('.//*syslog-server')
            delete_syslog_server.set('operation', 'delete')
            
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        syslogip = ET.SubElement(syslog_server, "syslogip")
        if kwargs.pop('delete_syslogip', False) is True:
            delete_syslogip = config.find('.//*syslogip')
            delete_syslogip.set('operation', 'delete')
            
        syslogip.text = kwargs.pop('syslogip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_server = ET.SubElement(logging, "syslog-server")
        if kwargs.pop('delete_syslog_server', False) is True:
            delete_syslog_server = config.find('.//*syslog-server')
            delete_syslog_server.set('operation', 'delete')
            
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        if kwargs.pop('delete_syslogip', False) is True:
            delete_syslogip = config.find('.//*syslogip')
            delete_syslogip.set('operation', 'delete')
                
        use_vrf = ET.SubElement(syslog_server, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_secure(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_server = ET.SubElement(logging, "syslog-server")
        if kwargs.pop('delete_syslog_server', False) is True:
            delete_syslog_server = config.find('.//*syslog-server')
            delete_syslog_server.set('operation', 'delete')
            
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        if kwargs.pop('delete_syslogip', False) is True:
            delete_syslogip = config.find('.//*syslogip')
            delete_syslogip.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        secure = ET.SubElement(syslog_server, "secure")
        if kwargs.pop('delete_secure', False) is True:
            delete_secure = config.find('.//*secure')
            delete_secure.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_server = ET.SubElement(logging, "syslog-server")
        if kwargs.pop('delete_syslog_server', False) is True:
            delete_syslog_server = config.find('.//*syslog-server')
            delete_syslog_server.set('operation', 'delete')
            
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        if kwargs.pop('delete_syslogip', False) is True:
            delete_syslogip = config.find('.//*syslogip')
            delete_syslogip.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        port = ET.SubElement(syslog_server, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_auditlog_class_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        auditlog = ET.SubElement(logging, "auditlog")
        if kwargs.pop('delete_auditlog', False) is True:
            delete_auditlog = config.find('.//*auditlog')
            delete_auditlog.set('operation', 'delete')
            
        class = ET.SubElement(auditlog, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        class = ET.SubElement(class, "class")
        if kwargs.pop('delete_class', False) is True:
            delete_class = config.find('.//*class')
            delete_class.set('operation', 'delete')
            
        class.text = kwargs.pop('class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_facility_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_facility = ET.SubElement(logging, "syslog-facility")
        if kwargs.pop('delete_syslog_facility', False) is True:
            delete_syslog_facility = config.find('.//*syslog-facility')
            delete_syslog_facility.set('operation', 'delete')
            
        local = ET.SubElement(syslog_facility, "local")
        if kwargs.pop('delete_local', False) is True:
            delete_local = config.find('.//*local')
            delete_local.set('operation', 'delete')
            
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_client_localip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_logging', False) is True:
            delete_logging = config.find('.//*logging')
            delete_logging.set('operation', 'delete')
            
        syslog_client = ET.SubElement(logging, "syslog-client")
        if kwargs.pop('delete_syslog_client', False) is True:
            delete_syslog_client = config.find('.//*syslog-client')
            delete_syslog_client.set('operation', 'delete')
            
        localip = ET.SubElement(syslog_client, "localip")
        if kwargs.pop('delete_localip', False) is True:
            delete_localip = config.find('.//*localip')
            delete_localip.set('operation', 'delete')
            
        localip.text = kwargs.pop('localip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_system', False) is True:
            delete_system = config.find('.//*system')
            delete_system.set('operation', 'delete')
            
        switch_attributes = ET.SubElement(system, "switch-attributes")
        if kwargs.pop('delete_switch_attributes', False) is True:
            delete_switch_attributes = config.find('.//*switch-attributes')
            delete_switch_attributes.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_system', False) is True:
            delete_system = config.find('.//*system')
            delete_system.set('operation', 'delete')
            
        switch_attributes = ET.SubElement(system, "switch-attributes")
        if kwargs.pop('delete_switch_attributes', False) is True:
            delete_switch_attributes = config.find('.//*switch-attributes')
            delete_switch_attributes.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        chassis_name = ET.SubElement(rbridge_id, "chassis-name")
        if kwargs.pop('delete_chassis_name', False) is True:
            delete_chassis_name = config.find('.//*chassis-name')
            delete_chassis_name.set('operation', 'delete')
            
        chassis_name.text = kwargs.pop('chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_host_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_system', False) is True:
            delete_system = config.find('.//*system')
            delete_system.set('operation', 'delete')
            
        switch_attributes = ET.SubElement(system, "switch-attributes")
        if kwargs.pop('delete_switch_attributes', False) is True:
            delete_switch_attributes = config.find('.//*switch-attributes')
            delete_switch_attributes.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        host_name = ET.SubElement(rbridge_id, "host-name")
        if kwargs.pop('delete_host_name', False) is True:
            delete_host_name = config.find('.//*host-name')
            delete_host_name.set('operation', 'delete')
            
        host_name.text = kwargs.pop('host_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        if kwargs.pop('delete_bna_config_cmd', False) is True:
            delete_bna_config_cmd = config.find('.//*bna-config-cmd')
            delete_bna_config_cmd.set('operation', 'delete')
            
        input = ET.SubElement(bna_config_cmd, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        src = ET.SubElement(input, "src")
        if kwargs.pop('delete_src', False) is True:
            delete_src = config.find('.//*src')
            delete_src.set('operation', 'delete')
            
        src.text = kwargs.pop('src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        if kwargs.pop('delete_bna_config_cmd', False) is True:
            delete_bna_config_cmd = config.find('.//*bna-config-cmd')
            delete_bna_config_cmd.set('operation', 'delete')
            
        input = ET.SubElement(bna_config_cmd, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        dest = ET.SubElement(input, "dest")
        if kwargs.pop('delete_dest', False) is True:
            delete_dest = config.find('.//*dest')
            delete_dest.set('operation', 'delete')
            
        dest.text = kwargs.pop('dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        if kwargs.pop('delete_bna_config_cmd', False) is True:
            delete_bna_config_cmd = config.find('.//*bna-config-cmd')
            delete_bna_config_cmd.set('operation', 'delete')
            
        output = ET.SubElement(bna_config_cmd, "output")
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
        
    def bna_config_cmd_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        if kwargs.pop('delete_bna_config_cmd', False) is True:
            delete_bna_config_cmd = config.find('.//*bna-config-cmd')
            delete_bna_config_cmd.set('operation', 'delete')
            
        output = ET.SubElement(bna_config_cmd, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status = ET.SubElement(output, "status")
        if kwargs.pop('delete_status', False) is True:
            delete_status = config.find('.//*status')
            delete_status.set('operation', 'delete')
            
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        if kwargs.pop('delete_bna_config_cmd', False) is True:
            delete_bna_config_cmd = config.find('.//*bna-config-cmd')
            delete_bna_config_cmd.set('operation', 'delete')
            
        output = ET.SubElement(bna_config_cmd, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status_string = ET.SubElement(output, "status-string")
        if kwargs.pop('delete_status_string', False) is True:
            delete_status_string = config.find('.//*status-string')
            delete_status_string.set('operation', 'delete')
            
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        if kwargs.pop('delete_bna_config_cmd_status', False) is True:
            delete_bna_config_cmd_status = config.find('.//*bna-config-cmd-status')
            delete_bna_config_cmd_status.set('operation', 'delete')
            
        input = ET.SubElement(bna_config_cmd_status, "input")
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
        
    def bna_config_cmd_status_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        if kwargs.pop('delete_bna_config_cmd_status', False) is True:
            delete_bna_config_cmd_status = config.find('.//*bna-config-cmd-status')
            delete_bna_config_cmd_status.set('operation', 'delete')
            
        output = ET.SubElement(bna_config_cmd_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status = ET.SubElement(output, "status")
        if kwargs.pop('delete_status', False) is True:
            delete_status = config.find('.//*status')
            delete_status.set('operation', 'delete')
            
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        if kwargs.pop('delete_bna_config_cmd_status', False) is True:
            delete_bna_config_cmd_status = config.find('.//*bna-config-cmd-status')
            delete_bna_config_cmd_status.set('operation', 'delete')
            
        output = ET.SubElement(bna_config_cmd_status, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        status_string = ET.SubElement(output, "status-string")
        if kwargs.pop('delete_status_string', False) is True:
            delete_status_string = config.find('.//*status-string')
            delete_status_string.set('operation', 'delete')
            
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload_param = ET.SubElement(support, "autoupload-param")
        if kwargs.pop('delete_autoupload_param', False) is True:
            delete_autoupload_param = config.find('.//*autoupload-param')
            delete_autoupload_param.set('operation', 'delete')
            
        hostip = ET.SubElement(autoupload_param, "hostip")
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
            
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload_param = ET.SubElement(support, "autoupload-param")
        if kwargs.pop('delete_autoupload_param', False) is True:
            delete_autoupload_param = config.find('.//*autoupload-param')
            delete_autoupload_param.set('operation', 'delete')
            
        username = ET.SubElement(autoupload_param, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload_param = ET.SubElement(support, "autoupload-param")
        if kwargs.pop('delete_autoupload_param', False) is True:
            delete_autoupload_param = config.find('.//*autoupload-param')
            delete_autoupload_param.set('operation', 'delete')
            
        directory = ET.SubElement(autoupload_param, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload_param = ET.SubElement(support, "autoupload-param")
        if kwargs.pop('delete_autoupload_param', False) is True:
            delete_autoupload_param = config.find('.//*autoupload-param')
            delete_autoupload_param.set('operation', 'delete')
            
        protocol = ET.SubElement(autoupload_param, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload_param = ET.SubElement(support, "autoupload-param")
        if kwargs.pop('delete_autoupload_param', False) is True:
            delete_autoupload_param = config.find('.//*autoupload-param')
            delete_autoupload_param.set('operation', 'delete')
            
        password = ET.SubElement(autoupload_param, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        support_param = ET.SubElement(support, "support-param")
        if kwargs.pop('delete_support_param', False) is True:
            delete_support_param = config.find('.//*support-param')
            delete_support_param.set('operation', 'delete')
            
        hostip = ET.SubElement(support_param, "hostip")
        if kwargs.pop('delete_hostip', False) is True:
            delete_hostip = config.find('.//*hostip')
            delete_hostip.set('operation', 'delete')
            
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        support_param = ET.SubElement(support, "support-param")
        if kwargs.pop('delete_support_param', False) is True:
            delete_support_param = config.find('.//*support-param')
            delete_support_param.set('operation', 'delete')
            
        username = ET.SubElement(support_param, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        support_param = ET.SubElement(support, "support-param")
        if kwargs.pop('delete_support_param', False) is True:
            delete_support_param = config.find('.//*support-param')
            delete_support_param.set('operation', 'delete')
            
        directory = ET.SubElement(support_param, "directory")
        if kwargs.pop('delete_directory', False) is True:
            delete_directory = config.find('.//*directory')
            delete_directory.set('operation', 'delete')
            
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        support_param = ET.SubElement(support, "support-param")
        if kwargs.pop('delete_support_param', False) is True:
            delete_support_param = config.find('.//*support-param')
            delete_support_param.set('operation', 'delete')
            
        protocol = ET.SubElement(support_param, "protocol")
        if kwargs.pop('delete_protocol', False) is True:
            delete_protocol = config.find('.//*protocol')
            delete_protocol.set('operation', 'delete')
            
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        support_param = ET.SubElement(support, "support-param")
        if kwargs.pop('delete_support_param', False) is True:
            delete_support_param = config.find('.//*support-param')
            delete_support_param.set('operation', 'delete')
            
        password = ET.SubElement(support_param, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        autoupload = ET.SubElement(support, "autoupload")
        if kwargs.pop('delete_autoupload', False) is True:
            delete_autoupload = config.find('.//*autoupload')
            delete_autoupload.set('operation', 'delete')
            
        enable = ET.SubElement(autoupload, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_ffdc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        if kwargs.pop('delete_support', False) is True:
            delete_support = config.find('.//*support')
            delete_support.set('operation', 'delete')
            
        ffdc = ET.SubElement(support, "ffdc")
        if kwargs.pop('delete_ffdc', False) is True:
            delete_ffdc = config.find('.//*ffdc')
            delete_ffdc.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        