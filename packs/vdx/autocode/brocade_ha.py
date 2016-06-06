#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ha(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def redundancy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        if kwargs.pop('delete_redundancy', False) is True:
            delete_redundancy = config.find('.//*redundancy')
            delete_redundancy.set('operation', 'delete')
            
        input = ET.SubElement(redundancy, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(input, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        if kwargs.pop('delete_redundancy', False) is True:
            delete_redundancy = config.find('.//*redundancy')
            delete_redundancy.set('operation', 'delete')
            
        output = ET.SubElement(redundancy, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rd_status = ET.SubElement(output, "rd_status")
        if kwargs.pop('delete_rd_status', False) is True:
            delete_rd_status = config.find('.//*rd_status')
            delete_rd_status.set('operation', 'delete')
            
        rd_status.text = kwargs.pop('rd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_mesg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        if kwargs.pop('delete_redundancy', False) is True:
            delete_redundancy = config.find('.//*redundancy')
            delete_redundancy.set('operation', 'delete')
            
        output = ET.SubElement(redundancy, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        rd_mesg = ET.SubElement(output, "rd_mesg")
        if kwargs.pop('delete_rd_mesg', False) is True:
            delete_rd_mesg = config.find('.//*rd_mesg')
            delete_rd_mesg.set('operation', 'delete')
            
        rd_mesg.text = kwargs.pop('rd_mesg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        if kwargs.pop('delete_reload', False) is True:
            delete_reload = config.find('.//*reload')
            delete_reload.set('operation', 'delete')
            
        input = ET.SubElement(reload, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(input, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_system(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        if kwargs.pop('delete_reload', False) is True:
            delete_reload = config.find('.//*reload')
            delete_reload.set('operation', 'delete')
            
        input = ET.SubElement(reload, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        system = ET.SubElement(input, "system")
        if kwargs.pop('delete_system', False) is True:
            delete_system = config.find('.//*system')
            delete_system.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_standby(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        if kwargs.pop('delete_reload', False) is True:
            delete_reload = config.find('.//*reload')
            delete_reload.set('operation', 'delete')
            
        input = ET.SubElement(reload, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        standby = ET.SubElement(input, "standby")
        if kwargs.pop('delete_standby', False) is True:
            delete_standby = config.find('.//*standby')
            delete_standby.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        