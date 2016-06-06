#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_igmp_snooping(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def igmp_snooping_ip_pim_snooping_pimv4_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        igmp_snooping = ET.SubElement(config, "igmp-snooping", xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping")
        if kwargs.pop('delete_igmp_snooping', False) is True:
            delete_igmp_snooping = config.find('.//*igmp-snooping')
            delete_igmp_snooping.set('operation', 'delete')
            
        ip = ET.SubElement(igmp_snooping, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        pim = ET.SubElement(ip, "pim")
        if kwargs.pop('delete_pim', False) is True:
            delete_pim = config.find('.//*pim')
            delete_pim.set('operation', 'delete')
            
        snooping = ET.SubElement(pim, "snooping")
        if kwargs.pop('delete_snooping', False) is True:
            delete_snooping = config.find('.//*snooping')
            delete_snooping.set('operation', 'delete')
            
        pimv4_enable = ET.SubElement(snooping, "pimv4-enable")
        if kwargs.pop('delete_pimv4_enable', False) is True:
            delete_pimv4_enable = config.find('.//*pimv4-enable')
            delete_pimv4_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def igmp_snooping_ip_igmp_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        igmp_snooping = ET.SubElement(config, "igmp-snooping", xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping")
        if kwargs.pop('delete_igmp_snooping', False) is True:
            delete_igmp_snooping = config.find('.//*igmp-snooping')
            delete_igmp_snooping.set('operation', 'delete')
            
        ip = ET.SubElement(igmp_snooping, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        igmp = ET.SubElement(ip, "igmp")
        if kwargs.pop('delete_igmp', False) is True:
            delete_igmp = config.find('.//*igmp')
            delete_igmp.set('operation', 'delete')
            
        snooping = ET.SubElement(igmp, "snooping")
        if kwargs.pop('delete_snooping', False) is True:
            delete_snooping = config.find('.//*snooping')
            delete_snooping.set('operation', 'delete')
            
        enable = ET.SubElement(snooping, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        