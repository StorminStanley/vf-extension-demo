#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_diagnostics(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def diag_post_rbridge_id_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        if kwargs.pop('delete_diag', False) is True:
            delete_diag = config.find('.//*diag')
            delete_diag.set('operation', 'delete')
            
        post = ET.SubElement(diag, "post")
        if kwargs.pop('delete_post', False) is True:
            delete_post = config.find('.//*post')
            delete_post.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(post, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        enable = ET.SubElement(rbridge_id, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        if kwargs.pop('delete_diag', False) is True:
            delete_diag = config.find('.//*diag')
            delete_diag.set('operation', 'delete')
            
        post = ET.SubElement(diag, "post")
        if kwargs.pop('delete_post', False) is True:
            delete_post = config.find('.//*post')
            delete_post.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(post, "rbridge-id")
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
        
    def diag_post_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        if kwargs.pop('delete_diag', False) is True:
            delete_diag = config.find('.//*diag')
            delete_diag.set('operation', 'delete')
            
        post = ET.SubElement(diag, "post")
        if kwargs.pop('delete_post', False) is True:
            delete_post = config.find('.//*post')
            delete_post.set('operation', 'delete')
            
        enable = ET.SubElement(post, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        