#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_entity(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_contained_in_ID_output_contained_in_ID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_contained_in_ID = ET.Element("get_contained_in_ID")
        config = get_contained_in_ID
        if kwargs.pop('delete_get_contained_in_ID', False) is True:
            delete_get_contained_in_ID = config.find('.//*get-contained-in-ID')
            delete_get_contained_in_ID.set('operation', 'delete')
            
        output = ET.SubElement(get_contained_in_ID, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        contained_in_ID = ET.SubElement(output, "contained-in-ID")
        if kwargs.pop('delete_contained_in_ID', False) is True:
            delete_contained_in_ID = config.find('.//*contained-in-ID')
            delete_contained_in_ID.set('operation', 'delete')
            
        contained_in_ID.text = kwargs.pop('contained_in_ID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        