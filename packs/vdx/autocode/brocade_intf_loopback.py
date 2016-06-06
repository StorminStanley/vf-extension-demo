#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_intf_loopback(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_intf_loopback_holder_interface_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        if kwargs.pop('delete_hide_intf_loopback_holder', False) is True:
            delete_hide_intf_loopback_holder = config.find('.//*hide-intf-loopback-holder')
            delete_hide_intf_loopback_holder.set('operation', 'delete')
            
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        loopback = ET.SubElement(interface, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        id = ET.SubElement(loopback, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_vrf_forwarding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        if kwargs.pop('delete_hide_intf_loopback_holder', False) is True:
            delete_hide_intf_loopback_holder = config.find('.//*hide-intf-loopback-holder')
            delete_hide_intf_loopback_holder.set('operation', 'delete')
            
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        loopback = ET.SubElement(interface, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        vrf = ET.SubElement(loopback, "vrf")
        if kwargs.pop('delete_vrf', False) is True:
            delete_vrf = config.find('.//*vrf')
            delete_vrf.set('operation', 'delete')
            
        forwarding = ET.SubElement(vrf, "forwarding")
        if kwargs.pop('delete_forwarding', False) is True:
            delete_forwarding = config.find('.//*forwarding')
            delete_forwarding.set('operation', 'delete')
            
        forwarding.text = kwargs.pop('forwarding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_intf_loopback_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        if kwargs.pop('delete_hide_intf_loopback_holder', False) is True:
            delete_hide_intf_loopback_holder = config.find('.//*hide-intf-loopback-holder')
            delete_hide_intf_loopback_holder.set('operation', 'delete')
            
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        loopback = ET.SubElement(interface, "loopback")
        if kwargs.pop('delete_loopback', False) is True:
            delete_loopback = config.find('.//*loopback')
            delete_loopback.set('operation', 'delete')
            
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        intf_loopback = ET.SubElement(loopback, "intf-loopback")
        if kwargs.pop('delete_intf_loopback', False) is True:
            delete_intf_loopback = config.find('.//*intf-loopback')
            delete_intf_loopback.set('operation', 'delete')
            
        shutdown = ET.SubElement(intf_loopback, "shutdown")
        if kwargs.pop('delete_shutdown', False) is True:
            delete_shutdown = config.find('.//*shutdown')
            delete_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        