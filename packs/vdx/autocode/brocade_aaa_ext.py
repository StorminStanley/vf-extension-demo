#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_aaa_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def user_session_info_output_user_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        user_session_info = ET.Element("user_session_info")
        config = user_session_info
        if kwargs.pop('delete_user_session_info', False) is True:
            delete_user_session_info = config.find('.//*user-session-info')
            delete_user_session_info.set('operation', 'delete')
            
        output = ET.SubElement(user_session_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        user_role = ET.SubElement(output, "user-role")
        if kwargs.pop('delete_user_role', False) is True:
            delete_user_role = config.find('.//*user-role')
            delete_user_role.set('operation', 'delete')
            
        user_role.text = kwargs.pop('user_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        