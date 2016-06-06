#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lacp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lacp = ET.SubElement(config, "lacp", xmlns="urn:brocade.com:mgmt:brocade-lacp")
        if kwargs.pop('delete_lacp', False) is True:
            delete_lacp = config.find('.//*lacp')
            delete_lacp.set('operation', 'delete')
            
        system_priority = ET.SubElement(lacp, "system-priority")
        if kwargs.pop('delete_system_priority', False) is True:
            delete_system_priority = config.find('.//*system-priority')
            delete_system_priority.set('operation', 'delete')
            
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlag_commit_mode_disable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlag_commit_mode = ET.SubElement(config, "vlag-commit-mode", xmlns="urn:brocade.com:mgmt:brocade-lacp")
        if kwargs.pop('delete_vlag_commit_mode', False) is True:
            delete_vlag_commit_mode = config.find('.//*vlag-commit-mode')
            delete_vlag_commit_mode.set('operation', 'delete')
            
        disable = ET.SubElement(vlag_commit_mode, "disable")
        if kwargs.pop('delete_disable', False) is True:
            delete_disable = config.find('.//*disable')
            delete_disable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        