#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fabric_service(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_linkinfo_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        input = ET.SubElement(show_linkinfo, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        all = ET.SubElement(input, "all")
        if kwargs.pop('delete_all', False) is True:
            delete_all = config.find('.//*all')
            delete_all.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
            
        linkinfo_rbridgeid.text = kwargs.pop('linkinfo_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_domain_reachable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_domain_reachable = ET.SubElement(show_link_info, "linkinfo-domain-reachable")
        if kwargs.pop('delete_linkinfo_domain_reachable', False) is True:
            delete_linkinfo_domain_reachable = config.find('.//*linkinfo-domain-reachable')
            delete_linkinfo_domain_reachable.set('operation', 'delete')
            
        linkinfo_domain_reachable.text = kwargs.pop('linkinfo_domain_reachable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_wwn = ET.SubElement(show_link_info, "linkinfo-wwn")
        if kwargs.pop('delete_linkinfo_wwn', False) is True:
            delete_linkinfo_wwn = config.find('.//*linkinfo-wwn')
            delete_linkinfo_wwn.set('operation', 'delete')
            
        linkinfo_wwn.text = kwargs.pop('linkinfo_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_version = ET.SubElement(show_link_info, "linkinfo-version")
        if kwargs.pop('delete_linkinfo_version', False) is True:
            delete_linkinfo_version = config.find('.//*linkinfo-version')
            delete_linkinfo_version.set('operation', 'delete')
            
        linkinfo_version.text = kwargs.pop('linkinfo_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linknumber(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
            
        linkinfo_isl_linknumber.text = kwargs.pop('linkinfo_isl_linknumber')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destdomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_destdomain = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destdomain")
        if kwargs.pop('delete_linkinfo_isllink_destdomain', False) is True:
            delete_linkinfo_isllink_destdomain = config.find('.//*linkinfo-isllink-destdomain')
            delete_linkinfo_isllink_destdomain.set('operation', 'delete')
            
        linkinfo_isllink_destdomain.text = kwargs.pop('linkinfo_isllink_destdomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_srcport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport")
        if kwargs.pop('delete_linkinfo_isllink_srcport', False) is True:
            delete_linkinfo_isllink_srcport = config.find('.//*linkinfo-isllink-srcport')
            delete_linkinfo_isllink_srcport.set('operation', 'delete')
            
        linkinfo_isllink_srcport.text = kwargs.pop('linkinfo_isllink_srcport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_srcport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-type")
        if kwargs.pop('delete_linkinfo_isllink_srcport_type', False) is True:
            delete_linkinfo_isllink_srcport_type = config.find('.//*linkinfo-isllink-srcport-type')
            delete_linkinfo_isllink_srcport_type.set('operation', 'delete')
            
        linkinfo_isllink_srcport_type.text = kwargs.pop('linkinfo_isllink_srcport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_srcport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-interface")
        if kwargs.pop('delete_linkinfo_isllink_srcport_interface', False) is True:
            delete_linkinfo_isllink_srcport_interface = config.find('.//*linkinfo-isllink-srcport-interface')
            delete_linkinfo_isllink_srcport_interface.set('operation', 'delete')
            
        linkinfo_isllink_srcport_interface.text = kwargs.pop('linkinfo_isllink_srcport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_destport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport")
        if kwargs.pop('delete_linkinfo_isllink_destport', False) is True:
            delete_linkinfo_isllink_destport = config.find('.//*linkinfo-isllink-destport')
            delete_linkinfo_isllink_destport.set('operation', 'delete')
            
        linkinfo_isllink_destport.text = kwargs.pop('linkinfo_isllink_destport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_destport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-type")
        if kwargs.pop('delete_linkinfo_isllink_destport_type', False) is True:
            delete_linkinfo_isllink_destport_type = config.find('.//*linkinfo-isllink-destport-type')
            delete_linkinfo_isllink_destport_type.set('operation', 'delete')
            
        linkinfo_isllink_destport_type.text = kwargs.pop('linkinfo_isllink_destport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_destport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-interface")
        if kwargs.pop('delete_linkinfo_isllink_destport_interface', False) is True:
            delete_linkinfo_isllink_destport_interface = config.find('.//*linkinfo-isllink-destport-interface')
            delete_linkinfo_isllink_destport_interface.set('operation', 'delete')
            
        linkinfo_isllink_destport_interface.text = kwargs.pop('linkinfo_isllink_destport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linkcost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isl_linkcost = ET.SubElement(linkinfo_isl, "linkinfo-isl-linkcost")
        if kwargs.pop('delete_linkinfo_isl_linkcost', False) is True:
            delete_linkinfo_isl_linkcost = config.find('.//*linkinfo-isl-linkcost')
            delete_linkinfo_isl_linkcost.set('operation', 'delete')
            
        linkinfo_isl_linkcost.text = kwargs.pop('linkinfo_isl_linkcost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_costcount(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_costcount = ET.SubElement(linkinfo_isl, "linkinfo-isllink-costcount")
        if kwargs.pop('delete_linkinfo_isllink_costcount', False) is True:
            delete_linkinfo_isllink_costcount = config.find('.//*linkinfo-isllink-costcount')
            delete_linkinfo_isllink_costcount.set('operation', 'delete')
            
        linkinfo_isllink_costcount.text = kwargs.pop('linkinfo_isllink_costcount')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_isllink_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-type")
        if kwargs.pop('delete_linkinfo_isllink_type', False) is True:
            delete_linkinfo_isllink_type = config.find('.//*linkinfo-isllink-type')
            delete_linkinfo_isllink_type.set('operation', 'delete')
            
        linkinfo_isllink_type.text = kwargs.pop('linkinfo_isllink_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        if kwargs.pop('delete_show_linkinfo', False) is True:
            delete_show_linkinfo = config.find('.//*show-linkinfo')
            delete_show_linkinfo.set('operation', 'delete')
            
        output = ET.SubElement(show_linkinfo, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_link_info = ET.SubElement(output, "show-link-info")
        if kwargs.pop('delete_show_link_info', False) is True:
            delete_show_link_info = config.find('.//*show-link-info')
            delete_show_link_info.set('operation', 'delete')
            
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        if kwargs.pop('delete_linkinfo_rbridgeid', False) is True:
            delete_linkinfo_rbridgeid = config.find('.//*linkinfo-rbridgeid')
            delete_linkinfo_rbridgeid.set('operation', 'delete')
                
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        if kwargs.pop('delete_linkinfo_isl', False) is True:
            delete_linkinfo_isl = config.find('.//*linkinfo-isl')
            delete_linkinfo_isl.set('operation', 'delete')
            
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        if kwargs.pop('delete_linkinfo_isl_linknumber', False) is True:
            delete_linkinfo_isl_linknumber = config.find('.//*linkinfo-isl-linknumber')
            delete_linkinfo_isl_linknumber.set('operation', 'delete')
                
        linkinfo_trunked = ET.SubElement(linkinfo_isl, "linkinfo-trunked")
        if kwargs.pop('delete_linkinfo_trunked', False) is True:
            delete_linkinfo_trunked = config.find('.//*linkinfo-trunked')
            delete_linkinfo_trunked.set('operation', 'delete')
            
        linkinfo_trunked.text = kwargs.pop('linkinfo_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        if kwargs.pop('delete_show_portindex_interface_info', False) is True:
            delete_show_portindex_interface_info = config.find('.//*show-portindex-interface-info')
            delete_show_portindex_interface_info.set('operation', 'delete')
            
        input = ET.SubElement(show_portindex_interface_info, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        all = ET.SubElement(input, "all")
        if kwargs.pop('delete_all', False) is True:
            delete_all = config.find('.//*all')
            delete_all.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        if kwargs.pop('delete_show_portindex_interface_info', False) is True:
            delete_show_portindex_interface_info = config.find('.//*show-portindex-interface-info')
            delete_show_portindex_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_portindex_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        if kwargs.pop('delete_show_portindex_interface', False) is True:
            delete_show_portindex_interface = config.find('.//*show-portindex-interface')
            delete_show_portindex_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
            
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        if kwargs.pop('delete_show_portindex_interface_info', False) is True:
            delete_show_portindex_interface_info = config.find('.//*show-portindex-interface-info')
            delete_show_portindex_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_portindex_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        if kwargs.pop('delete_show_portindex_interface', False) is True:
            delete_show_portindex_interface = config.find('.//*show-portindex-interface')
            delete_show_portindex_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        if kwargs.pop('delete_show_portindex', False) is True:
            delete_show_portindex = config.find('.//*show-portindex')
            delete_show_portindex.set('operation', 'delete')
            
        port_index = ET.SubElement(show_portindex, "port-index")
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
            
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        if kwargs.pop('delete_show_portindex_interface_info', False) is True:
            delete_show_portindex_interface_info = config.find('.//*show-portindex-interface-info')
            delete_show_portindex_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_portindex_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        if kwargs.pop('delete_show_portindex_interface', False) is True:
            delete_show_portindex_interface = config.find('.//*show-portindex-interface')
            delete_show_portindex_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        if kwargs.pop('delete_show_portindex', False) is True:
            delete_show_portindex = config.find('.//*show-portindex')
            delete_show_portindex.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_type = ET.SubElement(show_portindex, "port-type")
        if kwargs.pop('delete_port_type', False) is True:
            delete_port_type = config.find('.//*port-type')
            delete_port_type.set('operation', 'delete')
            
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        if kwargs.pop('delete_show_portindex_interface_info', False) is True:
            delete_show_portindex_interface_info = config.find('.//*show-portindex-interface-info')
            delete_show_portindex_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_portindex_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        if kwargs.pop('delete_show_portindex_interface', False) is True:
            delete_show_portindex_interface = config.find('.//*show-portindex-interface')
            delete_show_portindex_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        if kwargs.pop('delete_show_portindex', False) is True:
            delete_show_portindex = config.find('.//*show-portindex')
            delete_show_portindex.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_interface = ET.SubElement(show_portindex, "port-interface")
        if kwargs.pop('delete_port_interface', False) is True:
            delete_port_interface = config.find('.//*port-interface')
            delete_port_interface.set('operation', 'delete')
            
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        input = ET.SubElement(show_fibrechannel_interface_info, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        all = ET.SubElement(input, "all")
        if kwargs.pop('delete_all', False) is True:
            delete_all = config.find('.//*all')
            delete_all.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
            
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_interface = ET.SubElement(show_fibrechannel_info, "port-interface")
        if kwargs.pop('delete_port_interface', False) is True:
            delete_port_interface = config.find('.//*port-interface')
            delete_port_interface.set('operation', 'delete')
            
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index = ET.SubElement(show_fibrechannel_info, "port-index")
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
            
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_type = ET.SubElement(show_fibrechannel_info, "port-type")
        if kwargs.pop('delete_port_type', False) is True:
            delete_port_type = config.find('.//*port-type')
            delete_port_type.set('operation', 'delete')
            
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_wwn = ET.SubElement(show_fibrechannel_info, "port-wwn")
        if kwargs.pop('delete_port_wwn', False) is True:
            delete_port_wwn = config.find('.//*port-wwn')
            delete_port_wwn.set('operation', 'delete')
            
        port_wwn.text = kwargs.pop('port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        remote_port_wwn = ET.SubElement(show_fibrechannel_info, "remote-port-wwn")
        if kwargs.pop('delete_remote_port_wwn', False) is True:
            delete_remote_port_wwn = config.find('.//*remote-port-wwn')
            delete_remote_port_wwn.set('operation', 'delete')
            
        remote_port_wwn.text = kwargs.pop('remote_port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_node_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        remote_node_wwn = ET.SubElement(show_fibrechannel_info, "remote-node-wwn")
        if kwargs.pop('delete_remote_node_wwn', False) is True:
            delete_remote_node_wwn = config.find('.//*remote-node-wwn')
            delete_remote_node_wwn.set('operation', 'delete')
            
        remote_node_wwn.text = kwargs.pop('remote_node_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_state = ET.SubElement(show_fibrechannel_info, "port-state")
        if kwargs.pop('delete_port_state', False) is True:
            delete_port_state = config.find('.//*port-state')
            delete_port_state.set('operation', 'delete')
            
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_status = ET.SubElement(show_fibrechannel_info, "port-status")
        if kwargs.pop('delete_port_status', False) is True:
            delete_port_status = config.find('.//*port-status')
            delete_port_status.set('operation', 'delete')
            
        port_status.text = kwargs.pop('port_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_status_message = ET.SubElement(show_fibrechannel_info, "port-status-message")
        if kwargs.pop('delete_port_status_message', False) is True:
            delete_port_status_message = config.find('.//*port-status-message')
            delete_port_status_message.set('operation', 'delete')
            
        port_status_message.text = kwargs.pop('port_status_message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_health(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_health = ET.SubElement(show_fibrechannel_info, "port-health")
        if kwargs.pop('delete_port_health', False) is True:
            delete_port_health = config.find('.//*port-health')
            delete_port_health.set('operation', 'delete')
            
        port_health.text = kwargs.pop('port_health')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_trunked = ET.SubElement(show_fibrechannel_info, "port-trunked")
        if kwargs.pop('delete_port_trunked', False) is True:
            delete_port_trunked = config.find('.//*port-trunked')
            delete_port_trunked.set('operation', 'delete')
            
        port_trunked.text = kwargs.pop('port_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunk_master(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_trunk_master = ET.SubElement(show_fibrechannel_info, "port-trunk-master")
        if kwargs.pop('delete_port_trunk_master', False) is True:
            delete_port_trunk_master = config.find('.//*port-trunk-master')
            delete_port_trunk_master.set('operation', 'delete')
            
        port_trunk_master.text = kwargs.pop('port_trunk_master')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_actual_distance = ET.SubElement(show_fibrechannel_info, "port-actual-distance")
        if kwargs.pop('delete_port_actual_distance', False) is True:
            delete_port_actual_distance = config.find('.//*port-actual-distance')
            delete_port_actual_distance.set('operation', 'delete')
            
        port_actual_distance.text = kwargs.pop('port_actual_distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_desired_credit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_desired_credit = ET.SubElement(show_fibrechannel_info, "port-desired-credit")
        if kwargs.pop('delete_port_desired_credit', False) is True:
            delete_port_desired_credit = config.find('.//*port-desired-credit')
            delete_port_desired_credit.set('operation', 'delete')
            
        port_desired_credit.text = kwargs.pop('port_desired_credit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_buffer_allocated(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_buffer_allocated = ET.SubElement(show_fibrechannel_info, "port-buffer-allocated")
        if kwargs.pop('delete_port_buffer_allocated', False) is True:
            delete_port_buffer_allocated = config.find('.//*port-buffer-allocated')
            delete_port_buffer_allocated.set('operation', 'delete')
            
        port_buffer_allocated.text = kwargs.pop('port_buffer_allocated')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_licensed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_licensed = ET.SubElement(show_fibrechannel_info, "port-licensed")
        if kwargs.pop('delete_port_licensed', False) is True:
            delete_port_licensed = config.find('.//*port-licensed')
            delete_port_licensed.set('operation', 'delete')
            
        port_licensed.text = kwargs.pop('port_licensed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_address = ET.SubElement(show_fibrechannel_info, "port-address")
        if kwargs.pop('delete_port_address', False) is True:
            delete_port_address = config.find('.//*port-address')
            delete_port_address.set('operation', 'delete')
            
        port_address.text = kwargs.pop('port_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_fec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_fec = ET.SubElement(show_fibrechannel_info, "port-fec")
        if kwargs.pop('delete_port_fec', False) is True:
            delete_port_fec = config.find('.//*port-fec')
            delete_port_fec.set('operation', 'delete')
            
        port_fec.text = kwargs.pop('port_fec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_configured_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_configured_speed = ET.SubElement(show_fibrechannel_info, "port-configured-speed")
        if kwargs.pop('delete_port_configured_speed', False) is True:
            delete_port_configured_speed = config.find('.//*port-configured-speed')
            delete_port_configured_speed.set('operation', 'delete')
            
        port_configured_speed.text = kwargs.pop('port_configured_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        if kwargs.pop('delete_show_fibrechannel_interface_info', False) is True:
            delete_show_fibrechannel_interface_info = config.find('.//*show-fibrechannel-interface-info')
            delete_show_fibrechannel_interface_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        if kwargs.pop('delete_show_fibrechannel_interface', False) is True:
            delete_show_fibrechannel_interface = config.find('.//*show-fibrechannel-interface')
            delete_show_fibrechannel_interface.set('operation', 'delete')
            
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        if kwargs.pop('delete_portsgroup_rbridgeid', False) is True:
            delete_portsgroup_rbridgeid = config.find('.//*portsgroup-rbridgeid')
            delete_portsgroup_rbridgeid.set('operation', 'delete')
                
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        if kwargs.pop('delete_show_fibrechannel_info', False) is True:
            delete_show_fibrechannel_info = config.find('.//*show-fibrechannel-info')
            delete_show_fibrechannel_info.set('operation', 'delete')
            
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        if kwargs.pop('delete_port_index', False) is True:
            delete_port_index = config.find('.//*port-index')
            delete_port_index.set('operation', 'delete')
                
        port_actual_speed = ET.SubElement(show_fibrechannel_info, "port-actual-speed")
        if kwargs.pop('delete_port_actual_speed', False) is True:
            delete_port_actual_speed = config.find('.//*port-actual-speed')
            delete_port_actual_speed.set('operation', 'delete')
            
        port_actual_speed.text = kwargs.pop('port_actual_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        input = ET.SubElement(show_fabric_trunk_info, "input")
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
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_group = ET.SubElement(trunk_list_groups, "trunk-list-group")
        if kwargs.pop('delete_trunk_list_group', False) is True:
            delete_trunk_list_group = config.find('.//*trunk-list-group')
            delete_trunk_list_group.set('operation', 'delete')
            
        trunk_list_group.text = kwargs.pop('trunk_list_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_src_port = ET.SubElement(trunk_list_member, "trunk-list-src-port")
        if kwargs.pop('delete_trunk_list_src_port', False) is True:
            delete_trunk_list_src_port = config.find('.//*trunk-list-src-port')
            delete_trunk_list_src_port.set('operation', 'delete')
            
        trunk_list_src_port.text = kwargs.pop('trunk_list_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_interface_type = ET.SubElement(trunk_list_member, "trunk-list-interface-type")
        if kwargs.pop('delete_trunk_list_interface_type', False) is True:
            delete_trunk_list_interface_type = config.find('.//*trunk-list-interface-type')
            delete_trunk_list_interface_type.set('operation', 'delete')
            
        trunk_list_interface_type.text = kwargs.pop('trunk_list_interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_src_interface = ET.SubElement(trunk_list_member, "trunk-list-src-interface")
        if kwargs.pop('delete_trunk_list_src_interface', False) is True:
            delete_trunk_list_src_interface = config.find('.//*trunk-list-src-interface')
            delete_trunk_list_src_interface.set('operation', 'delete')
            
        trunk_list_src_interface.text = kwargs.pop('trunk_list_src_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_nbr_rbridge_id = ET.SubElement(trunk_list_member, "trunk-list-nbr-rbridge-id")
        if kwargs.pop('delete_trunk_list_nbr_rbridge_id', False) is True:
            delete_trunk_list_nbr_rbridge_id = config.find('.//*trunk-list-nbr-rbridge-id')
            delete_trunk_list_nbr_rbridge_id.set('operation', 'delete')
            
        trunk_list_nbr_rbridge_id.text = kwargs.pop('trunk_list_nbr_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_nbr_port = ET.SubElement(trunk_list_member, "trunk-list-nbr-port")
        if kwargs.pop('delete_trunk_list_nbr_port', False) is True:
            delete_trunk_list_nbr_port = config.find('.//*trunk-list-nbr-port')
            delete_trunk_list_nbr_port.set('operation', 'delete')
            
        trunk_list_nbr_port.text = kwargs.pop('trunk_list_nbr_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_nbr_interface_type = ET.SubElement(trunk_list_member, "trunk-list-nbr-interface-type")
        if kwargs.pop('delete_trunk_list_nbr_interface_type', False) is True:
            delete_trunk_list_nbr_interface_type = config.find('.//*trunk-list-nbr-interface-type')
            delete_trunk_list_nbr_interface_type.set('operation', 'delete')
            
        trunk_list_nbr_interface_type.text = kwargs.pop('trunk_list_nbr_interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_nbr_interface = ET.SubElement(trunk_list_member, "trunk-list-nbr-interface")
        if kwargs.pop('delete_trunk_list_nbr_interface', False) is True:
            delete_trunk_list_nbr_interface = config.find('.//*trunk-list-nbr-interface')
            delete_trunk_list_nbr_interface.set('operation', 'delete')
            
        trunk_list_nbr_interface.text = kwargs.pop('trunk_list_nbr_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_nbr_wwn = ET.SubElement(trunk_list_member, "trunk-list-nbr-wwn")
        if kwargs.pop('delete_trunk_list_nbr_wwn', False) is True:
            delete_trunk_list_nbr_wwn = config.find('.//*trunk-list-nbr-wwn')
            delete_trunk_list_nbr_wwn.set('operation', 'delete')
            
        trunk_list_nbr_wwn.text = kwargs.pop('trunk_list_nbr_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_is_primary(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        if kwargs.pop('delete_show_fabric_trunk_info', False) is True:
            delete_show_fabric_trunk_info = config.find('.//*show-fabric-trunk-info')
            delete_show_fabric_trunk_info.set('operation', 'delete')
            
        output = ET.SubElement(show_fabric_trunk_info, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        if kwargs.pop('delete_show_trunk_list', False) is True:
            delete_show_trunk_list = config.find('.//*show-trunk-list')
            delete_show_trunk_list.set('operation', 'delete')
            
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        if kwargs.pop('delete_trunk_list_groups', False) is True:
            delete_trunk_list_groups = config.find('.//*trunk-list-groups')
            delete_trunk_list_groups.set('operation', 'delete')
            
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        if kwargs.pop('delete_trunk_list_member', False) is True:
            delete_trunk_list_member = config.find('.//*trunk-list-member')
            delete_trunk_list_member.set('operation', 'delete')
            
        trunk_list_is_primary = ET.SubElement(trunk_list_member, "trunk-list-is-primary")
        if kwargs.pop('delete_trunk_list_is_primary', False) is True:
            delete_trunk_list_is_primary = config.find('.//*trunk-list-is-primary')
            delete_trunk_list_is_primary.set('operation', 'delete')
            
        trunk_list_is_primary.text = kwargs.pop('trunk_list_is_primary')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fabric_route_mcast_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        if kwargs.pop('delete_fabric', False) is True:
            delete_fabric = config.find('.//*fabric')
            delete_fabric.set('operation', 'delete')
            
        route = ET.SubElement(fabric, "route")
        if kwargs.pop('delete_route', False) is True:
            delete_route = config.find('.//*route')
            delete_route.set('operation', 'delete')
            
        mcast = ET.SubElement(route, "mcast")
        if kwargs.pop('delete_mcast', False) is True:
            delete_mcast = config.find('.//*mcast')
            delete_mcast.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
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
        
    def fabric_route_mcast_rbridge_id_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        if kwargs.pop('delete_fabric', False) is True:
            delete_fabric = config.find('.//*fabric')
            delete_fabric.set('operation', 'delete')
            
        route = ET.SubElement(fabric, "route")
        if kwargs.pop('delete_route', False) is True:
            delete_route = config.find('.//*route')
            delete_route.set('operation', 'delete')
            
        mcast = ET.SubElement(route, "mcast")
        if kwargs.pop('delete_mcast', False) is True:
            delete_mcast = config.find('.//*mcast')
            delete_mcast.set('operation', 'delete')
            
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
            
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        if kwargs.pop('delete_rbridge_id', False) is True:
            delete_rbridge_id = config.find('.//*rbridge-id')
            delete_rbridge_id.set('operation', 'delete')
                
        priority = ET.SubElement(rbridge_id, "priority")
        if kwargs.pop('delete_priority', False) is True:
            delete_priority = config.find('.//*priority')
            delete_priority.set('operation', 'delete')
            
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        