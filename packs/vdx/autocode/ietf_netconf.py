#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        if kwargs.pop('delete_get_config', False) is True:
            delete_get_config = config.find('.//*get-config')
            delete_get_config.set('operation', 'delete')
            
        input = ET.SubElement(get_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        candidate = ET.SubElement(config_source, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        if kwargs.pop('delete_get_config', False) is True:
            delete_get_config = config.find('.//*get-config')
            delete_get_config.set('operation', 'delete')
            
        input = ET.SubElement(get_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        running = ET.SubElement(config_source, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        if kwargs.pop('delete_get_config', False) is True:
            delete_get_config = config.find('.//*get-config')
            delete_get_config.set('operation', 'delete')
            
        input = ET.SubElement(get_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        startup = ET.SubElement(config_source, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        if kwargs.pop('delete_get_config', False) is True:
            delete_get_config = config.find('.//*get-config')
            delete_get_config.set('operation', 'delete')
            
        input = ET.SubElement(get_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        if kwargs.pop('delete_with_defaults', False) is True:
            delete_with_defaults = config.find('.//*with-defaults')
            delete_with_defaults.set('operation', 'delete')
            
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        candidate = ET.SubElement(config_target, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        running = ET.SubElement(config_target, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_default_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        default_operation = ET.SubElement(input, "default-operation")
        if kwargs.pop('delete_default_operation', False) is True:
            delete_default_operation = config.find('.//*default-operation')
            delete_default_operation.set('operation', 'delete')
            
        default_operation.text = kwargs.pop('default_operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_test_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        test_option = ET.SubElement(input, "test-option")
        if kwargs.pop('delete_test_option', False) is True:
            delete_test_option = config.find('.//*test-option')
            delete_test_option.set('operation', 'delete')
            
        test_option.text = kwargs.pop('test_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_error_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        error_option = ET.SubElement(input, "error-option")
        if kwargs.pop('delete_error_option', False) is True:
            delete_error_option = config.find('.//*error-option')
            delete_error_option.set('operation', 'delete')
            
        error_option.text = kwargs.pop('error_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_edit_content_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        if kwargs.pop('delete_edit_config', False) is True:
            delete_edit_config = config.find('.//*edit-config')
            delete_edit_config.set('operation', 'delete')
            
        input = ET.SubElement(edit_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        edit_content = ET.SubElement(input, "edit-content")
        if kwargs.pop('delete_edit_content', False) is True:
            delete_edit_content = config.find('.//*edit-content')
            delete_edit_content.set('operation', 'delete')
            
        url = ET.SubElement(edit_content, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url = ET.SubElement(url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        candidate = ET.SubElement(config_target, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        running = ET.SubElement(config_target, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        startup = ET.SubElement(config_target, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        url = ET.SubElement(config_target, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url = ET.SubElement(url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        candidate = ET.SubElement(config_source, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        running = ET.SubElement(config_source, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        startup = ET.SubElement(config_source, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        url = ET.SubElement(config_source, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url = ET.SubElement(url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        if kwargs.pop('delete_copy_config', False) is True:
            delete_copy_config = config.find('.//*copy-config')
            delete_copy_config.set('operation', 'delete')
            
        input = ET.SubElement(copy_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        if kwargs.pop('delete_with_defaults', False) is True:
            delete_with_defaults = config.find('.//*with-defaults')
            delete_with_defaults.set('operation', 'delete')
            
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        if kwargs.pop('delete_delete_config', False) is True:
            delete_delete_config = config.find('.//*delete-config')
            delete_delete_config.set('operation', 'delete')
            
        input = ET.SubElement(delete_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        startup = ET.SubElement(config_target, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        if kwargs.pop('delete_delete_config', False) is True:
            delete_delete_config = config.find('.//*delete-config')
            delete_delete_config.set('operation', 'delete')
            
        input = ET.SubElement(delete_config, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        url = ET.SubElement(config_target, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url = ET.SubElement(url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        if kwargs.pop('delete_lock', False) is True:
            delete_lock = config.find('.//*lock')
            delete_lock.set('operation', 'delete')
            
        input = ET.SubElement(lock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        candidate = ET.SubElement(config_target, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        if kwargs.pop('delete_lock', False) is True:
            delete_lock = config.find('.//*lock')
            delete_lock.set('operation', 'delete')
            
        input = ET.SubElement(lock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        running = ET.SubElement(config_target, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        if kwargs.pop('delete_lock', False) is True:
            delete_lock = config.find('.//*lock')
            delete_lock.set('operation', 'delete')
            
        input = ET.SubElement(lock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        startup = ET.SubElement(config_target, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        if kwargs.pop('delete_unlock', False) is True:
            delete_unlock = config.find('.//*unlock')
            delete_unlock.set('operation', 'delete')
            
        input = ET.SubElement(unlock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        candidate = ET.SubElement(config_target, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        if kwargs.pop('delete_unlock', False) is True:
            delete_unlock = config.find('.//*unlock')
            delete_unlock.set('operation', 'delete')
            
        input = ET.SubElement(unlock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        running = ET.SubElement(config_target, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        if kwargs.pop('delete_unlock', False) is True:
            delete_unlock = config.find('.//*unlock')
            delete_unlock.set('operation', 'delete')
            
        input = ET.SubElement(unlock, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        target = ET.SubElement(input, "target")
        if kwargs.pop('delete_target', False) is True:
            delete_target = config.find('.//*target')
            delete_target.set('operation', 'delete')
            
        config_target = ET.SubElement(target, "config-target")
        if kwargs.pop('delete_config_target', False) is True:
            delete_config_target = config.find('.//*config-target')
            delete_config_target.set('operation', 'delete')
            
        startup = ET.SubElement(config_target, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get = ET.Element("get")
        config = get
        if kwargs.pop('delete_get', False) is True:
            delete_get = config.find('.//*get')
            delete_get.set('operation', 'delete')
            
        input = ET.SubElement(get, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        if kwargs.pop('delete_with_defaults', False) is True:
            delete_with_defaults = config.find('.//*with-defaults')
            delete_with_defaults.set('operation', 'delete')
            
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def kill_session_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        kill_session = ET.Element("kill_session")
        config = kill_session
        if kwargs.pop('delete_kill_session', False) is True:
            delete_kill_session = config.find('.//*kill-session')
            delete_kill_session.set('operation', 'delete')
            
        input = ET.SubElement(kill_session, "input")
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
        
    def commit_input_confirmed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        if kwargs.pop('delete_commit', False) is True:
            delete_commit = config.find('.//*commit')
            delete_commit.set('operation', 'delete')
            
        input = ET.SubElement(commit, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        confirmed = ET.SubElement(input, "confirmed")
        if kwargs.pop('delete_confirmed', False) is True:
            delete_confirmed = config.find('.//*confirmed')
            delete_confirmed.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_confirm_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        if kwargs.pop('delete_commit', False) is True:
            delete_commit = config.find('.//*commit')
            delete_commit.set('operation', 'delete')
            
        input = ET.SubElement(commit, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        confirm_timeout = ET.SubElement(input, "confirm-timeout")
        if kwargs.pop('delete_confirm_timeout', False) is True:
            delete_confirm_timeout = config.find('.//*confirm-timeout')
            delete_confirm_timeout.set('operation', 'delete')
            
        confirm_timeout.text = kwargs.pop('confirm_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        if kwargs.pop('delete_commit', False) is True:
            delete_commit = config.find('.//*commit')
            delete_commit.set('operation', 'delete')
            
        input = ET.SubElement(commit, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        persist = ET.SubElement(input, "persist")
        if kwargs.pop('delete_persist', False) is True:
            delete_persist = config.find('.//*persist')
            delete_persist.set('operation', 'delete')
            
        persist.text = kwargs.pop('persist')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        if kwargs.pop('delete_commit', False) is True:
            delete_commit = config.find('.//*commit')
            delete_commit.set('operation', 'delete')
            
        input = ET.SubElement(commit, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        persist_id = ET.SubElement(input, "persist-id")
        if kwargs.pop('delete_persist_id', False) is True:
            delete_persist_id = config.find('.//*persist-id')
            delete_persist_id.set('operation', 'delete')
            
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cancel_commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cancel_commit = ET.Element("cancel_commit")
        config = cancel_commit
        if kwargs.pop('delete_cancel_commit', False) is True:
            delete_cancel_commit = config.find('.//*cancel-commit')
            delete_cancel_commit.set('operation', 'delete')
            
        input = ET.SubElement(cancel_commit, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        persist_id = ET.SubElement(input, "persist-id")
        if kwargs.pop('delete_persist_id', False) is True:
            delete_persist_id = config.find('.//*persist-id')
            delete_persist_id.set('operation', 'delete')
            
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        if kwargs.pop('delete_validate', False) is True:
            delete_validate = config.find('.//*validate')
            delete_validate.set('operation', 'delete')
            
        input = ET.SubElement(validate, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        candidate = ET.SubElement(config_source, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            
        candidate = ET.SubElement(candidate, "candidate")
        if kwargs.pop('delete_candidate', False) is True:
            delete_candidate = config.find('.//*candidate')
            delete_candidate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        if kwargs.pop('delete_validate', False) is True:
            delete_validate = config.find('.//*validate')
            delete_validate.set('operation', 'delete')
            
        input = ET.SubElement(validate, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        running = ET.SubElement(config_source, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            
        running = ET.SubElement(running, "running")
        if kwargs.pop('delete_running', False) is True:
            delete_running = config.find('.//*running')
            delete_running.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        if kwargs.pop('delete_validate', False) is True:
            delete_validate = config.find('.//*validate')
            delete_validate.set('operation', 'delete')
            
        input = ET.SubElement(validate, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        startup = ET.SubElement(config_source, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            
        startup = ET.SubElement(startup, "startup")
        if kwargs.pop('delete_startup', False) is True:
            delete_startup = config.find('.//*startup')
            delete_startup.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        if kwargs.pop('delete_validate', False) is True:
            delete_validate = config.find('.//*validate')
            delete_validate.set('operation', 'delete')
            
        input = ET.SubElement(validate, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        source = ET.SubElement(input, "source")
        if kwargs.pop('delete_source', False) is True:
            delete_source = config.find('.//*source')
            delete_source.set('operation', 'delete')
            
        config_source = ET.SubElement(source, "config-source")
        if kwargs.pop('delete_config_source', False) is True:
            delete_config_source = config.find('.//*config-source')
            delete_config_source.set('operation', 'delete')
            
        url = ET.SubElement(config_source, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url = ET.SubElement(url, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        