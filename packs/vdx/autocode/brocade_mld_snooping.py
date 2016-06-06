#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mld_snooping(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mld_snooping_ipv6_pim_snooping_pimv6_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mld_snooping = ET.SubElement(config, "mld-snooping", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
        if kwargs.pop('delete_mld_snooping', False) is True:
            delete_mld_snooping = config.find('.//*mld-snooping')
            delete_mld_snooping.set('operation', 'delete')
            
        ipv6 = ET.SubElement(mld_snooping, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        pim = ET.SubElement(ipv6, "pim")
        if kwargs.pop('delete_pim', False) is True:
            delete_pim = config.find('.//*pim')
            delete_pim.set('operation', 'delete')
            
        snooping = ET.SubElement(pim, "snooping")
        if kwargs.pop('delete_snooping', False) is True:
            delete_snooping = config.find('.//*snooping')
            delete_snooping.set('operation', 'delete')
            
        pimv6_enable = ET.SubElement(snooping, "pimv6-enable")
        if kwargs.pop('delete_pimv6_enable', False) is True:
            delete_pimv6_enable = config.find('.//*pimv6-enable')
            delete_pimv6_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mld_snooping_ipv6_mld_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mld_snooping = ET.SubElement(config, "mld-snooping", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
        if kwargs.pop('delete_mld_snooping', False) is True:
            delete_mld_snooping = config.find('.//*mld-snooping')
            delete_mld_snooping.set('operation', 'delete')
            
        ipv6 = ET.SubElement(mld_snooping, "ipv6")
        if kwargs.pop('delete_ipv6', False) is True:
            delete_ipv6 = config.find('.//*ipv6')
            delete_ipv6.set('operation', 'delete')
            
        mld = ET.SubElement(ipv6, "mld")
        if kwargs.pop('delete_mld', False) is True:
            delete_mld = config.find('.//*mld')
            delete_mld.set('operation', 'delete')
            
        snooping = ET.SubElement(mld, "snooping")
        if kwargs.pop('delete_snooping', False) is True:
            delete_snooping = config.find('.//*snooping')
            delete_snooping.set('operation', 'delete')
            
        enable = ET.SubElement(snooping, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        