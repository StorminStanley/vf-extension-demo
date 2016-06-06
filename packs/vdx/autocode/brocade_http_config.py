#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_http_config(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def http_sa_http_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        if kwargs.pop('delete_http_sa', False) is True:
            delete_http_sa = config.find('.//*http-sa')
            delete_http_sa.set('operation', 'delete')
            
        http = ET.SubElement(http_sa, "http")
        if kwargs.pop('delete_http', False) is True:
            delete_http = config.find('.//*http')
            delete_http.set('operation', 'delete')
            
        server = ET.SubElement(http, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        shutdown = ET.SubElement(server, "shutdown")
        if kwargs.pop('delete_shutdown', False) is True:
            delete_shutdown = config.find('.//*shutdown')
            delete_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def http_sa_http_server_http_vrf_cont_use_vrf_use_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        if kwargs.pop('delete_http_sa', False) is True:
            delete_http_sa = config.find('.//*http-sa')
            delete_http_sa.set('operation', 'delete')
            
        http = ET.SubElement(http_sa, "http")
        if kwargs.pop('delete_http', False) is True:
            delete_http = config.find('.//*http')
            delete_http.set('operation', 'delete')
            
        server = ET.SubElement(http, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        if kwargs.pop('delete_http_vrf_cont', False) is True:
            delete_http_vrf_cont = config.find('.//*http-vrf-cont')
            delete_http_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
            
        use_vrf_name.text = kwargs.pop('use_vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def http_sa_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        if kwargs.pop('delete_http_sa', False) is True:
            delete_http_sa = config.find('.//*http-sa')
            delete_http_sa.set('operation', 'delete')
            
        http = ET.SubElement(http_sa, "http")
        if kwargs.pop('delete_http', False) is True:
            delete_http = config.find('.//*http')
            delete_http.set('operation', 'delete')
            
        server = ET.SubElement(http, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        if kwargs.pop('delete_http_vrf_cont', False) is True:
            delete_http_vrf_cont = config.find('.//*http-vrf-cont')
            delete_http_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name_key.text = kwargs.pop('use_vrf_name')
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
                
        http_vrf_shutdown = ET.SubElement(use_vrf, "http-vrf-shutdown")
        if kwargs.pop('delete_http_vrf_shutdown', False) is True:
            delete_http_vrf_shutdown = config.find('.//*http-vrf-shutdown')
            delete_http_vrf_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        