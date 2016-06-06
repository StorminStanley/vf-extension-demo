#!/usr/bin/env python
import xml.etree.ElementTree as ET


class tailf_confd_monitoring(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def confd_state_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        version = ET.SubElement(confd_state, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_smp_number_of_threads(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        smp = ET.SubElement(confd_state, "smp")
        if kwargs.pop('delete_smp', False) is True:
            delete_smp = config.find('.//*smp')
            delete_smp.set('operation', 'delete')
            
        number_of_threads = ET.SubElement(smp, "number-of-threads")
        if kwargs.pop('delete_number_of_threads', False) is True:
            delete_number_of_threads = config.find('.//*number-of-threads')
            delete_number_of_threads.set('operation', 'delete')
            
        number_of_threads.text = kwargs.pop('number_of_threads')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_epoll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        epoll = ET.SubElement(confd_state, "epoll")
        if kwargs.pop('delete_epoll', False) is True:
            delete_epoll = config.find('.//*epoll')
            delete_epoll.set('operation', 'delete')
            
        epoll.text = kwargs.pop('epoll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_daemon_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        daemon_status = ET.SubElement(confd_state, "daemon-status")
        if kwargs.pop('delete_daemon_status', False) is True:
            delete_daemon_status = config.find('.//*daemon-status')
            delete_daemon_status.set('operation', 'delete')
            
        daemon_status.text = kwargs.pop('daemon_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_read_only_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        read_only_mode = ET.SubElement(confd_state, "read-only-mode")
        if kwargs.pop('delete_read_only_mode', False) is True:
            delete_read_only_mode = config.find('.//*read-only-mode')
            delete_read_only_mode.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_upgrade_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        upgrade_mode = ET.SubElement(confd_state, "upgrade-mode")
        if kwargs.pop('delete_upgrade_mode', False) is True:
            delete_upgrade_mode = config.find('.//*upgrade-mode')
            delete_upgrade_mode.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        ha = ET.SubElement(confd_state, "ha")
        if kwargs.pop('delete_ha', False) is True:
            delete_ha = config.find('.//*ha')
            delete_ha.set('operation', 'delete')
            
        mode = ET.SubElement(ha, "mode")
        if kwargs.pop('delete_mode', False) is True:
            delete_mode = config.find('.//*mode')
            delete_mode.set('operation', 'delete')
            
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        ha = ET.SubElement(confd_state, "ha")
        if kwargs.pop('delete_ha', False) is True:
            delete_ha = config.find('.//*ha')
            delete_ha.set('operation', 'delete')
            
        node_id = ET.SubElement(ha, "node-id")
        if kwargs.pop('delete_node_id', False) is True:
            delete_node_id = config.find('.//*node-id')
            delete_node_id.set('operation', 'delete')
            
        node_id.text = kwargs.pop('node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_master_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        ha = ET.SubElement(confd_state, "ha")
        if kwargs.pop('delete_ha', False) is True:
            delete_ha = config.find('.//*ha')
            delete_ha.set('operation', 'delete')
            
        master_node_id = ET.SubElement(ha, "master-node-id")
        if kwargs.pop('delete_master_node_id', False) is True:
            delete_master_node_id = config.find('.//*master-node-id')
            delete_master_node_id.set('operation', 'delete')
            
        master_node_id.text = kwargs.pop('master_node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        if kwargs.pop('delete_loaded_data_models', False) is True:
            delete_loaded_data_models = config.find('.//*loaded-data-models')
            delete_loaded_data_models.set('operation', 'delete')
            
        data_model = ET.SubElement(loaded_data_models, "data-model")
        if kwargs.pop('delete_data_model', False) is True:
            delete_data_model = config.find('.//*data-model')
            delete_data_model.set('operation', 'delete')
            
        name = ET.SubElement(data_model, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_revision(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        if kwargs.pop('delete_loaded_data_models', False) is True:
            delete_loaded_data_models = config.find('.//*loaded-data-models')
            delete_loaded_data_models.set('operation', 'delete')
            
        data_model = ET.SubElement(loaded_data_models, "data-model")
        if kwargs.pop('delete_data_model', False) is True:
            delete_data_model = config.find('.//*data-model')
            delete_data_model.set('operation', 'delete')
            
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        revision = ET.SubElement(data_model, "revision")
        if kwargs.pop('delete_revision', False) is True:
            delete_revision = config.find('.//*revision')
            delete_revision.set('operation', 'delete')
            
        revision.text = kwargs.pop('revision')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        if kwargs.pop('delete_loaded_data_models', False) is True:
            delete_loaded_data_models = config.find('.//*loaded-data-models')
            delete_loaded_data_models.set('operation', 'delete')
            
        data_model = ET.SubElement(loaded_data_models, "data-model")
        if kwargs.pop('delete_data_model', False) is True:
            delete_data_model = config.find('.//*data-model')
            delete_data_model.set('operation', 'delete')
            
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        namespace = ET.SubElement(data_model, "namespace")
        if kwargs.pop('delete_namespace', False) is True:
            delete_namespace = config.find('.//*namespace')
            delete_namespace.set('operation', 'delete')
            
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_prefix(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        if kwargs.pop('delete_loaded_data_models', False) is True:
            delete_loaded_data_models = config.find('.//*loaded-data-models')
            delete_loaded_data_models.set('operation', 'delete')
            
        data_model = ET.SubElement(loaded_data_models, "data-model")
        if kwargs.pop('delete_data_model', False) is True:
            delete_data_model = config.find('.//*data-model')
            delete_data_model.set('operation', 'delete')
            
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        prefix = ET.SubElement(data_model, "prefix")
        if kwargs.pop('delete_prefix', False) is True:
            delete_prefix = config.find('.//*prefix')
            delete_prefix.set('operation', 'delete')
            
        prefix.text = kwargs.pop('prefix')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_exported_exported_to_all_exported_to_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        if kwargs.pop('delete_loaded_data_models', False) is True:
            delete_loaded_data_models = config.find('.//*loaded-data-models')
            delete_loaded_data_models.set('operation', 'delete')
            
        data_model = ET.SubElement(loaded_data_models, "data-model")
        if kwargs.pop('delete_data_model', False) is True:
            delete_data_model = config.find('.//*data-model')
            delete_data_model.set('operation', 'delete')
            
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        exported = ET.SubElement(data_model, "exported")
        if kwargs.pop('delete_exported', False) is True:
            delete_exported = config.find('.//*exported')
            delete_exported.set('operation', 'delete')
            
        exported_to_all = ET.SubElement(exported, "exported-to-all")
        if kwargs.pop('delete_exported_to_all', False) is True:
            delete_exported_to_all = config.find('.//*exported-to-all')
            delete_exported_to_all.set('operation', 'delete')
            
        exported_to_all = ET.SubElement(exported_to_all, "exported-to-all")
        if kwargs.pop('delete_exported_to_all', False) is True:
            delete_exported_to_all = config.find('.//*exported-to-all')
            delete_exported_to_all.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        netconf = ET.SubElement(confd_state, "netconf")
        if kwargs.pop('delete_netconf', False) is True:
            delete_netconf = config.find('.//*netconf')
            delete_netconf.set('operation', 'delete')
            
        listen = ET.SubElement(netconf, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        ip = ET.SubElement(tcp, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        netconf = ET.SubElement(confd_state, "netconf")
        if kwargs.pop('delete_netconf', False) is True:
            delete_netconf = config.find('.//*netconf')
            delete_netconf.set('operation', 'delete')
            
        listen = ET.SubElement(netconf, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        port = ET.SubElement(tcp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        netconf = ET.SubElement(confd_state, "netconf")
        if kwargs.pop('delete_netconf', False) is True:
            delete_netconf = config.find('.//*netconf')
            delete_netconf.set('operation', 'delete')
            
        listen = ET.SubElement(netconf, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssh = ET.SubElement(listen, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        ip = ET.SubElement(ssh, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        netconf = ET.SubElement(confd_state, "netconf")
        if kwargs.pop('delete_netconf', False) is True:
            delete_netconf = config.find('.//*netconf')
            delete_netconf.set('operation', 'delete')
            
        listen = ET.SubElement(netconf, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssh = ET.SubElement(listen, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        port = ET.SubElement(ssh, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        cli = ET.SubElement(confd_state, "cli")
        if kwargs.pop('delete_cli', False) is True:
            delete_cli = config.find('.//*cli')
            delete_cli.set('operation', 'delete')
            
        listen = ET.SubElement(cli, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssh = ET.SubElement(listen, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        ip = ET.SubElement(ssh, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        cli = ET.SubElement(confd_state, "cli")
        if kwargs.pop('delete_cli', False) is True:
            delete_cli = config.find('.//*cli')
            delete_cli.set('operation', 'delete')
            
        listen = ET.SubElement(cli, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssh = ET.SubElement(listen, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        port = ET.SubElement(ssh, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        webui = ET.SubElement(confd_state, "webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        listen = ET.SubElement(webui, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        ip = ET.SubElement(tcp, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        webui = ET.SubElement(confd_state, "webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        listen = ET.SubElement(webui, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        port = ET.SubElement(tcp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        webui = ET.SubElement(confd_state, "webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        listen = ET.SubElement(webui, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssl = ET.SubElement(listen, "ssl")
        if kwargs.pop('delete_ssl', False) is True:
            delete_ssl = config.find('.//*ssl')
            delete_ssl.set('operation', 'delete')
            
        ip = ET.SubElement(ssl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        webui = ET.SubElement(confd_state, "webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        listen = ET.SubElement(webui, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssl = ET.SubElement(listen, "ssl")
        if kwargs.pop('delete_ssl', False) is True:
            delete_ssl = config.find('.//*ssl')
            delete_ssl.set('operation', 'delete')
            
        port = ET.SubElement(ssl, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        rest = ET.SubElement(confd_state, "rest")
        if kwargs.pop('delete_rest', False) is True:
            delete_rest = config.find('.//*rest')
            delete_rest.set('operation', 'delete')
            
        listen = ET.SubElement(rest, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        ip = ET.SubElement(tcp, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        rest = ET.SubElement(confd_state, "rest")
        if kwargs.pop('delete_rest', False) is True:
            delete_rest = config.find('.//*rest')
            delete_rest.set('operation', 'delete')
            
        listen = ET.SubElement(rest, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        tcp = ET.SubElement(listen, "tcp")
        if kwargs.pop('delete_tcp', False) is True:
            delete_tcp = config.find('.//*tcp')
            delete_tcp.set('operation', 'delete')
            
        port = ET.SubElement(tcp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        rest = ET.SubElement(confd_state, "rest")
        if kwargs.pop('delete_rest', False) is True:
            delete_rest = config.find('.//*rest')
            delete_rest.set('operation', 'delete')
            
        listen = ET.SubElement(rest, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssl = ET.SubElement(listen, "ssl")
        if kwargs.pop('delete_ssl', False) is True:
            delete_ssl = config.find('.//*ssl')
            delete_ssl.set('operation', 'delete')
            
        ip = ET.SubElement(ssl, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        rest = ET.SubElement(confd_state, "rest")
        if kwargs.pop('delete_rest', False) is True:
            delete_rest = config.find('.//*rest')
            delete_rest.set('operation', 'delete')
            
        listen = ET.SubElement(rest, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        ssl = ET.SubElement(listen, "ssl")
        if kwargs.pop('delete_ssl', False) is True:
            delete_ssl = config.find('.//*ssl')
            delete_ssl.set('operation', 'delete')
            
        port = ET.SubElement(ssl, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        listen = ET.SubElement(snmp, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        udp = ET.SubElement(listen, "udp")
        if kwargs.pop('delete_udp', False) is True:
            delete_udp = config.find('.//*udp')
            delete_udp.set('operation', 'delete')
            
        ip = ET.SubElement(udp, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        listen = ET.SubElement(snmp, "listen")
        if kwargs.pop('delete_listen', False) is True:
            delete_listen = config.find('.//*listen')
            delete_listen.set('operation', 'delete')
            
        udp = ET.SubElement(listen, "udp")
        if kwargs.pop('delete_udp', False) is True:
            delete_udp = config.find('.//*udp')
            delete_udp.set('operation', 'delete')
            
        port = ET.SubElement(udp, "port")
        if kwargs.pop('delete_port', False) is True:
            delete_port = config.find('.//*port')
            delete_port.set('operation', 'delete')
            
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        version = ET.SubElement(snmp, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        v1 = ET.SubElement(version, "v1")
        if kwargs.pop('delete_v1', False) is True:
            delete_v1 = config.find('.//*v1')
            delete_v1.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v2c(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        version = ET.SubElement(snmp, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        v2c = ET.SubElement(version, "v2c")
        if kwargs.pop('delete_v2c', False) is True:
            delete_v2c = config.find('.//*v2c')
            delete_v2c.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        version = ET.SubElement(snmp, "version")
        if kwargs.pop('delete_version', False) is True:
            delete_version = config.find('.//*version')
            delete_version.set('operation', 'delete')
            
        v3 = ET.SubElement(version, "v3")
        if kwargs.pop('delete_v3', False) is True:
            delete_v3 = config.find('.//*v3')
            delete_v3.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_engine_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        snmp = ET.SubElement(confd_state, "snmp")
        if kwargs.pop('delete_snmp', False) is True:
            delete_snmp = config.find('.//*snmp')
            delete_snmp.set('operation', 'delete')
            
        engine_id = ET.SubElement(snmp, "engine-id")
        if kwargs.pop('delete_engine_id', False) is True:
            delete_engine_id = config.find('.//*engine-id')
            delete_engine_id.set('operation', 'delete')
            
        engine_id.text = kwargs.pop('engine_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id = ET.SubElement(callpoint, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(callpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        callpoint = ET.SubElement(callpoints, "callpoint")
        if kwargs.pop('delete_callpoint', False) is True:
            delete_callpoint = config.find('.//*callpoint')
            delete_callpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(callpoint, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id = ET.SubElement(validationpoint, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(validationpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        if kwargs.pop('delete_validationpoint', False) is True:
            delete_validationpoint = config.find('.//*validationpoint')
            delete_validationpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(validationpoint, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id = ET.SubElement(actionpoint, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(actionpoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        if kwargs.pop('delete_actionpoint', False) is True:
            delete_actionpoint = config.find('.//*actionpoint')
            delete_actionpoint.set('operation', 'delete')
            
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(actionpoint, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id = ET.SubElement(snmp_inform_callback, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        if kwargs.pop('delete_snmp_inform_callback', False) is True:
            delete_snmp_inform_callback = config.find('.//*snmp-inform-callback')
            delete_snmp_inform_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(snmp_inform_callback, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id = ET.SubElement(snmp_notification_subscription, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        if kwargs.pop('delete_snmp_notification_subscription', False) is True:
            delete_snmp_notification_subscription = config.find('.//*snmp-notification-subscription')
            delete_snmp_notification_subscription.set('operation', 'delete')
            
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(snmp_notification_subscription, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id = ET.SubElement(error_formatting_callback, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        if kwargs.pop('delete_error_formatting_callback', False) is True:
            delete_error_formatting_callback = config.find('.//*error-formatting-callback')
            delete_error_formatting_callback.set('operation', 'delete')
            
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(error_formatting_callback, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id = ET.SubElement(typepoint, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        registration_type = ET.SubElement(typepoint, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        typepoint = ET.SubElement(callpoints, "typepoint")
        if kwargs.pop('delete_typepoint', False) is True:
            delete_typepoint = config.find('.//*typepoint')
            delete_typepoint.set('operation', 'delete')
            
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        error = ET.SubElement(typepoint, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name = ET.SubElement(notification_stream_replay, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_replay_support(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        replay_support = ET.SubElement(notification_stream_replay, "replay-support")
        if kwargs.pop('delete_replay_support', False) is True:
            delete_replay_support = config.find('.//*replay-support')
            delete_replay_support.set('operation', 'delete')
            
        replay_support.text = kwargs.pop('replay_support')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        if kwargs.pop('delete_notification_stream_replay', False) is True:
            delete_notification_stream_replay = config.find('.//*notification-stream-replay')
            delete_notification_stream_replay.set('operation', 'delete')
            
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        error = ET.SubElement(notification_stream_replay, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        enabled = ET.SubElement(authentication_callback, "enabled")
        if kwargs.pop('delete_enabled', False) is True:
            delete_enabled = config.find('.//*enabled')
            delete_enabled.set('operation', 'delete')
            
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        if kwargs.pop('delete_authentication_callback', False) is True:
            delete_authentication_callback = config.find('.//*authentication-callback')
            delete_authentication_callback.set('operation', 'delete')
            
        error = ET.SubElement(authentication_callback, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        enabled = ET.SubElement(authorization_callbacks, "enabled")
        if kwargs.pop('delete_enabled', False) is True:
            delete_enabled = config.find('.//*enabled')
            delete_enabled.set('operation', 'delete')
            
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        daemon = ET.SubElement(registration_type, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        daemon = ET.SubElement(daemon, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        path = ET.SubElement(range, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        lower = ET.SubElement(range, "lower")
        if kwargs.pop('delete_lower', False) is True:
            delete_lower = config.find('.//*lower')
            delete_lower.set('operation', 'delete')
            
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        upper = ET.SubElement(range, "upper")
        if kwargs.pop('delete_upper', False) is True:
            delete_upper = config.find('.//*upper')
            delete_upper.set('operation', 'delete')
            
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        default = ET.SubElement(range, "default")
        if kwargs.pop('delete_default', False) is True:
            delete_default = config.find('.//*default')
            delete_default.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        id = ET.SubElement(daemon, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        name = ET.SubElement(daemon, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        range = ET.SubElement(registration_type, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        range = ET.SubElement(range, "range")
        if kwargs.pop('delete_range', False) is True:
            delete_range = config.find('.//*range')
            delete_range.set('operation', 'delete')
            
        daemon = ET.SubElement(range, "daemon")
        if kwargs.pop('delete_daemon', False) is True:
            delete_daemon = config.find('.//*daemon')
            delete_daemon.set('operation', 'delete')
            
        error = ET.SubElement(daemon, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        if kwargs.pop('delete_registration_type', False) is True:
            delete_registration_type = config.find('.//*registration-type')
            delete_registration_type.set('operation', 'delete')
            
        file = ET.SubElement(registration_type, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file = ET.SubElement(file, "file")
        if kwargs.pop('delete_file', False) is True:
            delete_file = config.find('.//*file')
            delete_file.set('operation', 'delete')
            
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        callpoints = ET.SubElement(internal, "callpoints")
        if kwargs.pop('delete_callpoints', False) is True:
            delete_callpoints = config.find('.//*callpoints')
            delete_callpoints.set('operation', 'delete')
            
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        if kwargs.pop('delete_authorization_callbacks', False) is True:
            delete_authorization_callbacks = config.find('.//*authorization-callbacks')
            delete_authorization_callbacks.set('operation', 'delete')
            
        error = ET.SubElement(authorization_callbacks, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
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
        
    def confd_state_internal_cdb_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        transaction_id = ET.SubElement(datastore, "transaction-id")
        if kwargs.pop('delete_transaction_id', False) is True:
            delete_transaction_id = config.find('.//*transaction-id')
            delete_transaction_id.set('operation', 'delete')
            
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_queue(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        write_queue = ET.SubElement(datastore, "write-queue")
        if kwargs.pop('delete_write_queue', False) is True:
            delete_write_queue = config.find('.//*write-queue')
            delete_write_queue.set('operation', 'delete')
            
        write_queue.text = kwargs.pop('write_queue')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_filename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        filename = ET.SubElement(datastore, "filename")
        if kwargs.pop('delete_filename', False) is True:
            delete_filename = config.find('.//*filename')
            delete_filename.set('operation', 'delete')
            
        filename.text = kwargs.pop('filename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_disk_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        disk_size = ET.SubElement(datastore, "disk-size")
        if kwargs.pop('delete_disk_size', False) is True:
            delete_disk_size = config.find('.//*disk-size')
            delete_disk_size.set('operation', 'delete')
            
        disk_size.text = kwargs.pop('disk_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_ram_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        ram_size = ET.SubElement(datastore, "ram-size")
        if kwargs.pop('delete_ram_size', False) is True:
            delete_ram_size = config.find('.//*ram-size')
            delete_ram_size.set('operation', 'delete')
            
        ram_size.text = kwargs.pop('ram_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_read_locks(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        read_locks = ET.SubElement(datastore, "read-locks")
        if kwargs.pop('delete_read_locks', False) is True:
            delete_read_locks = config.find('.//*read-locks')
            delete_read_locks.set('operation', 'delete')
            
        read_locks.text = kwargs.pop('read_locks')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        write_lock_set = ET.SubElement(datastore, "write-lock-set")
        if kwargs.pop('delete_write_lock_set', False) is True:
            delete_write_lock_set = config.find('.//*write-lock-set')
            delete_write_lock_set.set('operation', 'delete')
            
        write_lock_set.text = kwargs.pop('write_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_subscription_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        subscription_lock_set = ET.SubElement(datastore, "subscription-lock-set")
        if kwargs.pop('delete_subscription_lock_set', False) is True:
            delete_subscription_lock_set = config.find('.//*subscription-lock-set')
            delete_subscription_lock_set.set('operation', 'delete')
            
        subscription_lock_set.text = kwargs.pop('subscription_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_waiting_for_replication_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        waiting_for_replication_sync = ET.SubElement(datastore, "waiting-for-replication-sync")
        if kwargs.pop('delete_waiting_for_replication_sync', False) is True:
            delete_waiting_for_replication_sync = config.find('.//*waiting-for-replication-sync')
            delete_waiting_for_replication_sync.set('operation', 'delete')
            
        waiting_for_replication_sync.text = kwargs.pop('waiting_for_replication_sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        if kwargs.pop('delete_pending_subscription_sync', False) is True:
            delete_pending_subscription_sync = config.find('.//*pending-subscription-sync')
            delete_pending_subscription_sync.set('operation', 'delete')
            
        priority = ET.SubElement(pending_subscription_sync, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        if kwargs.pop('delete_pending_subscription_sync', False) is True:
            delete_pending_subscription_sync = config.find('.//*pending-subscription-sync')
            delete_pending_subscription_sync.set('operation', 'delete')
            
        notification = ET.SubElement(pending_subscription_sync, "notification")
        if kwargs.pop('delete_notification', False) is True:
            delete_notification = config.find('.//*notification')
            delete_notification.set('operation', 'delete')
            
        client_name = ET.SubElement(notification, "client-name")
        if kwargs.pop('delete_client_name', False) is True:
            delete_client_name = config.find('.//*client-name')
            delete_client_name.set('operation', 'delete')
            
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_time_remaining(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        if kwargs.pop('delete_pending_subscription_sync', False) is True:
            delete_pending_subscription_sync = config.find('.//*pending-subscription-sync')
            delete_pending_subscription_sync.set('operation', 'delete')
            
        time_remaining = ET.SubElement(pending_subscription_sync, "time-remaining")
        if kwargs.pop('delete_time_remaining', False) is True:
            delete_time_remaining = config.find('.//*time-remaining')
            delete_time_remaining.set('operation', 'delete')
            
        time_remaining.text = kwargs.pop('time_remaining')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        if kwargs.pop('delete_pending_notification_queue', False) is True:
            delete_pending_notification_queue = config.find('.//*pending-notification-queue')
            delete_pending_notification_queue.set('operation', 'delete')
            
        notification = ET.SubElement(pending_notification_queue, "notification")
        if kwargs.pop('delete_notification', False) is True:
            delete_notification = config.find('.//*notification')
            delete_notification.set('operation', 'delete')
            
        priority = ET.SubElement(notification, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        datastore = ET.SubElement(cdb, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        if kwargs.pop('delete_pending_notification_queue', False) is True:
            delete_pending_notification_queue = config.find('.//*pending-notification-queue')
            delete_pending_notification_queue.set('operation', 'delete')
            
        notification = ET.SubElement(pending_notification_queue, "notification")
        if kwargs.pop('delete_notification', False) is True:
            delete_notification = config.find('.//*notification')
            delete_notification.set('operation', 'delete')
            
        client_name = ET.SubElement(notification, "client-name")
        if kwargs.pop('delete_client_name', False) is True:
            delete_client_name = config.find('.//*client-name')
            delete_client_name.set('operation', 'delete')
            
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        name = ET.SubElement(client, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        info = ET.SubElement(client, "info")
        if kwargs.pop('delete_info', False) is True:
            delete_info = config.find('.//*info')
            delete_info.set('operation', 'delete')
            
        info.text = kwargs.pop('info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        type = ET.SubElement(client, "type")
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
            
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        datastore = ET.SubElement(client, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_lock(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        lock = ET.SubElement(client, "lock")
        if kwargs.pop('delete_lock', False) is True:
            delete_lock = config.find('.//*lock')
            delete_lock.set('operation', 'delete')
            
        lock.text = kwargs.pop('lock')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        datastore = ET.SubElement(subscription, "datastore")
        if kwargs.pop('delete_datastore', False) is True:
            delete_datastore = config.find('.//*datastore')
            delete_datastore.set('operation', 'delete')
            
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_twophase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        twophase = ET.SubElement(subscription, "twophase")
        if kwargs.pop('delete_twophase', False) is True:
            delete_twophase = config.find('.//*twophase')
            delete_twophase.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        priority = ET.SubElement(subscription, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        id = ET.SubElement(subscription, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        path = ET.SubElement(subscription, "path")
        if kwargs.pop('delete_path', False) is True:
            delete_path = config.find('.//*path')
            delete_path.set('operation', 'delete')
            
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        if kwargs.pop('delete_confd_state', False) is True:
            delete_confd_state = config.find('.//*confd-state')
            delete_confd_state.set('operation', 'delete')
            
        internal = ET.SubElement(confd_state, "internal")
        if kwargs.pop('delete_internal', False) is True:
            delete_internal = config.find('.//*internal')
            delete_internal.set('operation', 'delete')
            
        cdb = ET.SubElement(internal, "cdb")
        if kwargs.pop('delete_cdb', False) is True:
            delete_cdb = config.find('.//*cdb')
            delete_cdb.set('operation', 'delete')
            
        client = ET.SubElement(cdb, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        subscription = ET.SubElement(client, "subscription")
        if kwargs.pop('delete_subscription', False) is True:
            delete_subscription = config.find('.//*subscription')
            delete_subscription.set('operation', 'delete')
            
        error = ET.SubElement(subscription, "error")
        if kwargs.pop('delete_error', False) is True:
            delete_error = config.find('.//*error')
            delete_error.set('operation', 'delete')
            
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        