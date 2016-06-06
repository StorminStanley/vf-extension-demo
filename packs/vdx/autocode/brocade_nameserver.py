#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_nameserver(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_nameserver_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        input = ET.SubElement(get_nameserver_detail, "input")
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
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid = ET.SubElement(show_nameserver, "nameserver-portid")
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
            
        nameserver_portid.text = kwargs.pop('nameserver_portid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_portname = ET.SubElement(show_nameserver, "nameserver-portname")
        if kwargs.pop('delete_nameserver_portname', False) is True:
            delete_nameserver_portname = config.find('.//*nameserver-portname')
            delete_nameserver_portname.set('operation', 'delete')
            
        nameserver_portname.text = kwargs.pop('nameserver_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_nodename = ET.SubElement(show_nameserver, "nameserver-nodename")
        if kwargs.pop('delete_nameserver_nodename', False) is True:
            delete_nameserver_nodename = config.find('.//*nameserver-nodename')
            delete_nameserver_nodename.set('operation', 'delete')
            
        nameserver_nodename.text = kwargs.pop('nameserver_nodename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_scr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_scr = ET.SubElement(show_nameserver, "nameserver-scr")
        if kwargs.pop('delete_nameserver_scr', False) is True:
            delete_nameserver_scr = config.find('.//*nameserver-scr')
            delete_nameserver_scr.set('operation', 'delete')
            
        nameserver_scr.text = kwargs.pop('nameserver_scr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fc4s(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_fc4s = ET.SubElement(show_nameserver, "nameserver-fc4s")
        if kwargs.pop('delete_nameserver_fc4s', False) is True:
            delete_nameserver_fc4s = config.find('.//*nameserver-fc4s')
            delete_nameserver_fc4s.set('operation', 'delete')
            
        nameserver_fc4s.text = kwargs.pop('nameserver_fc4s')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portsymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_portsymb = ET.SubElement(show_nameserver, "nameserver-portsymb")
        if kwargs.pop('delete_nameserver_portsymb', False) is True:
            delete_nameserver_portsymb = config.find('.//*nameserver-portsymb')
            delete_nameserver_portsymb.set('operation', 'delete')
            
        nameserver_portsymb.text = kwargs.pop('nameserver_portsymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodesymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_nodesymb = ET.SubElement(show_nameserver, "nameserver-nodesymb")
        if kwargs.pop('delete_nameserver_nodesymb', False) is True:
            delete_nameserver_nodesymb = config.find('.//*nameserver-nodesymb')
            delete_nameserver_nodesymb.set('operation', 'delete')
            
        nameserver_nodesymb.text = kwargs.pop('nameserver_nodesymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fabric_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_fabric_portname = ET.SubElement(show_nameserver, "nameserver-fabric-portname")
        if kwargs.pop('delete_nameserver_fabric_portname', False) is True:
            delete_nameserver_fabric_portname = config.find('.//*nameserver-fabric-portname')
            delete_nameserver_fabric_portname.set('operation', 'delete')
            
        nameserver_fabric_portname.text = kwargs.pop('nameserver_fabric_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_permanent_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_permanent_portname = ET.SubElement(show_nameserver, "nameserver-permanent-portname")
        if kwargs.pop('delete_nameserver_permanent_portname', False) is True:
            delete_nameserver_permanent_portname = config.find('.//*nameserver-permanent-portname')
            delete_nameserver_permanent_portname.set('operation', 'delete')
            
        nameserver_permanent_portname.text = kwargs.pop('nameserver_permanent_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_devicetype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_devicetype = ET.SubElement(show_nameserver, "nameserver-devicetype")
        if kwargs.pop('delete_nameserver_devicetype', False) is True:
            delete_nameserver_devicetype = config.find('.//*nameserver-devicetype')
            delete_nameserver_devicetype.set('operation', 'delete')
            
        nameserver_devicetype.text = kwargs.pop('nameserver_devicetype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_index = ET.SubElement(show_nameserver, "nameserver-index")
        if kwargs.pop('delete_nameserver_index', False) is True:
            delete_nameserver_index = config.find('.//*nameserver-index')
            delete_nameserver_index.set('operation', 'delete')
            
        nameserver_index.text = kwargs.pop('nameserver_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_porttype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_porttype = ET.SubElement(show_nameserver, "nameserver-porttype")
        if kwargs.pop('delete_nameserver_porttype', False) is True:
            delete_nameserver_porttype = config.find('.//*nameserver-porttype')
            delete_nameserver_porttype.set('operation', 'delete')
            
        nameserver_porttype.text = kwargs.pop('nameserver_porttype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_cos = ET.SubElement(show_nameserver, "nameserver-cos")
        if kwargs.pop('delete_nameserver_cos', False) is True:
            delete_nameserver_cos = config.find('.//*nameserver-cos')
            delete_nameserver_cos.set('operation', 'delete')
            
        nameserver_cos.text = kwargs.pop('nameserver_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_sharearea(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_sharearea = ET.SubElement(show_nameserver, "nameserver-sharearea")
        if kwargs.pop('delete_nameserver_sharearea', False) is True:
            delete_nameserver_sharearea = config.find('.//*nameserver-sharearea')
            delete_nameserver_sharearea.set('operation', 'delete')
            
        nameserver_sharearea.text = kwargs.pop('nameserver_sharearea')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_redirect(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_redirect = ET.SubElement(show_nameserver, "nameserver-redirect")
        if kwargs.pop('delete_nameserver_redirect', False) is True:
            delete_nameserver_redirect = config.find('.//*nameserver-redirect')
            delete_nameserver_redirect.set('operation', 'delete')
            
        nameserver_redirect.text = kwargs.pop('nameserver_redirect')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_xlatedomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_xlatedomain = ET.SubElement(show_nameserver, "nameserver-xlatedomain")
        if kwargs.pop('delete_nameserver_xlatedomain', False) is True:
            delete_nameserver_xlatedomain = config.find('.//*nameserver-xlatedomain')
            delete_nameserver_xlatedomain.set('operation', 'delete')
            
        nameserver_xlatedomain.text = kwargs.pop('nameserver_xlatedomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_connected_via_ag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_connected_via_ag = ET.SubElement(show_nameserver, "nameserver-connected-via-ag")
        if kwargs.pop('delete_nameserver_connected_via_ag', False) is True:
            delete_nameserver_connected_via_ag = config.find('.//*nameserver-connected-via-ag')
            delete_nameserver_connected_via_ag.set('operation', 'delete')
            
        nameserver_connected_via_ag.text = kwargs.pop('nameserver_connected_via_ag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_ag_base_device(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_ag_base_device = ET.SubElement(show_nameserver, "nameserver-ag-base-device")
        if kwargs.pop('delete_nameserver_ag_base_device', False) is True:
            delete_nameserver_ag_base_device = config.find('.//*nameserver-ag-base-device')
            delete_nameserver_ag_base_device.set('operation', 'delete')
            
        nameserver_ag_base_device.text = kwargs.pop('nameserver_ag_base_device')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_real(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_real = ET.SubElement(show_nameserver, "nameserver-real")
        if kwargs.pop('delete_nameserver_real', False) is True:
            delete_nameserver_real = config.find('.//*nameserver-real')
            delete_nameserver_real.set('operation', 'delete')
            
        nameserver_real.text = kwargs.pop('nameserver_real')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cascaded(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        if kwargs.pop('delete_get_nameserver_detail', False) is True:
            delete_get_nameserver_detail = config.find('.//*get-nameserver-detail')
            delete_get_nameserver_detail.set('operation', 'delete')
            
        output = ET.SubElement(get_nameserver_detail, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_nameserver = ET.SubElement(output, "show-nameserver")
        if kwargs.pop('delete_show_nameserver', False) is True:
            delete_show_nameserver = config.find('.//*show-nameserver')
            delete_show_nameserver.set('operation', 'delete')
            
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        if kwargs.pop('delete_nameserver_portid', False) is True:
            delete_nameserver_portid = config.find('.//*nameserver-portid')
            delete_nameserver_portid.set('operation', 'delete')
                
        nameserver_cascaded = ET.SubElement(show_nameserver, "nameserver-cascaded")
        if kwargs.pop('delete_nameserver_cascaded', False) is True:
            delete_nameserver_cascaded = config.find('.//*nameserver-cascaded')
            delete_nameserver_cascaded.set('operation', 'delete')
            
        nameserver_cascaded.text = kwargs.pop('nameserver_cascaded')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        