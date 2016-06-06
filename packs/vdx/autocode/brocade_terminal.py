#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_terminal(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def terminal_cfg_line_sessionid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        if kwargs.pop('delete_terminal_cfg', False) is True:
            delete_terminal_cfg = config.find('.//*terminal-cfg')
            delete_terminal_cfg.set('operation', 'delete')
            
        line = ET.SubElement(terminal_cfg, "line")
        if kwargs.pop('delete_line', False) is True:
            delete_line = config.find('.//*line')
            delete_line.set('operation', 'delete')
            
        sessionid = ET.SubElement(line, "sessionid")
        if kwargs.pop('delete_sessionid', False) is True:
            delete_sessionid = config.find('.//*sessionid')
            delete_sessionid.set('operation', 'delete')
            
        sessionid.text = kwargs.pop('sessionid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def terminal_cfg_line_exec_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        if kwargs.pop('delete_terminal_cfg', False) is True:
            delete_terminal_cfg = config.find('.//*terminal-cfg')
            delete_terminal_cfg.set('operation', 'delete')
            
        line = ET.SubElement(terminal_cfg, "line")
        if kwargs.pop('delete_line', False) is True:
            delete_line = config.find('.//*line')
            delete_line.set('operation', 'delete')
            
        sessionid_key = ET.SubElement(line, "sessionid")
        sessionid_key.text = kwargs.pop('sessionid')
        if kwargs.pop('delete_sessionid', False) is True:
            delete_sessionid = config.find('.//*sessionid')
            delete_sessionid.set('operation', 'delete')
                
        exec_timeout = ET.SubElement(line, "exec-timeout")
        if kwargs.pop('delete_exec_timeout', False) is True:
            delete_exec_timeout = config.find('.//*exec-timeout')
            delete_exec_timeout.set('operation', 'delete')
            
        exec_timeout.text = kwargs.pop('exec_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        