#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_preprovision(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def preprovision_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        if kwargs.pop('delete_preprovision', False) is True:
            delete_preprovision = config.find('.//*preprovision')
            delete_preprovision.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        wwn_key = ET.SubElement(rbridge_id, "wwn")
        wwn_key.text = kwargs.pop('wwn')
        if kwargs.pop('delete_wwn', False) is True:
            delete_wwn = config.find('.//*wwn')
            delete_wwn.set('operation', 'delete')
                
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def preprovision_rbridge_id_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        if kwargs.pop('delete_preprovision', False) is True:
            delete_preprovision = config.find('.//*preprovision')
            delete_preprovision.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        wwn = ET.SubElement(rbridge_id, "wwn")
        if kwargs.pop('delete_wwn', False) is True:
            delete_wwn = config.find('.//*wwn')
            delete_wwn.set('operation', 'delete')
            
        wwn.text = kwargs.pop('wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_bare_metal_state_output_bare_metal_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_bare_metal_state = ET.Element("show_bare_metal_state")
        config = show_bare_metal_state
        if kwargs.pop('delete_show_bare_metal_state', False) is True:
            delete_show_bare_metal_state = config.find('.//*show-bare-metal-state')
            delete_show_bare_metal_state.set('operation', 'delete')
            
        output = ET.SubElement(show_bare_metal_state, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        bare_metal_state = ET.SubElement(output, "bare-metal-state")
        if kwargs.pop('delete_bare_metal_state', False) is True:
            delete_bare_metal_state = config.find('.//*bare-metal-state')
            delete_bare_metal_state.set('operation', 'delete')
            
        bare_metal_state.text = kwargs.pop('bare_metal_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        