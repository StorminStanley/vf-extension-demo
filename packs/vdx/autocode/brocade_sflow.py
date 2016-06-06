#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_sflow(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def sflow_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        enable = ET.SubElement(sflow, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        collector = ET.SubElement(sflow, "collector")
        if kwargs.pop('delete_collector', False) is True:
            delete_collector = config.find('.//*collector')
            delete_collector.set('operation', 'delete')
            
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        if kwargs.pop('delete_collector_port_number', False) is True:
            delete_collector_port_number = config.find('.//*collector-port-number')
            delete_collector_port_number.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        collector_ip_address = ET.SubElement(collector, "collector-ip-address")
        if kwargs.pop('delete_collector_ip_address', False) is True:
            delete_collector_ip_address = config.find('.//*collector-ip-address')
            delete_collector_ip_address.set('operation', 'delete')
            
        collector_ip_address.text = kwargs.pop('collector_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_port_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        collector = ET.SubElement(sflow, "collector")
        if kwargs.pop('delete_collector', False) is True:
            delete_collector = config.find('.//*collector')
            delete_collector.set('operation', 'delete')
            
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        if kwargs.pop('delete_collector_ip_address', False) is True:
            delete_collector_ip_address = config.find('.//*collector-ip-address')
            delete_collector_ip_address.set('operation', 'delete')
                
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
                
        collector_port_number = ET.SubElement(collector, "collector-port-number")
        if kwargs.pop('delete_collector_port_number', False) is True:
            delete_collector_port_number = config.find('.//*collector-port-number')
            delete_collector_port_number.set('operation', 'delete')
            
        collector_port_number.text = kwargs.pop('collector_port_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        collector = ET.SubElement(sflow, "collector")
        if kwargs.pop('delete_collector', False) is True:
            delete_collector = config.find('.//*collector')
            delete_collector.set('operation', 'delete')
            
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        if kwargs.pop('delete_collector_ip_address', False) is True:
            delete_collector_ip_address = config.find('.//*collector-ip-address')
            delete_collector_ip_address.set('operation', 'delete')
                
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        if kwargs.pop('delete_collector_port_number', False) is True:
            delete_collector_port_number = config.find('.//*collector-port-number')
            delete_collector_port_number.set('operation', 'delete')
                
        use_vrf = ET.SubElement(collector, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        source_ip = ET.SubElement(sflow, "source-ip")
        if kwargs.pop('delete_source_ip', False) is True:
            delete_source_ip = config.find('.//*source-ip')
            delete_source_ip.set('operation', 'delete')
            
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_polling_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        polling_interval = ET.SubElement(sflow, "polling-interval")
        if kwargs.pop('delete_polling_interval', False) is True:
            delete_polling_interval = config.find('.//*polling-interval')
            delete_polling_interval.set('operation', 'delete')
            
        polling_interval.text = kwargs.pop('polling_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_sample_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow', False) is True:
            delete_sflow = config.find('.//*sflow')
            delete_sflow.set('operation', 'delete')
            
        sample_rate = ET.SubElement(sflow, "sample-rate")
        if kwargs.pop('delete_sample_rate', False) is True:
            delete_sample_rate = config.find('.//*sample-rate')
            delete_sample_rate.set('operation', 'delete')
            
        sample_rate.text = kwargs.pop('sample_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow_profile', False) is True:
            delete_sflow_profile = config.find('.//*sflow-profile')
            delete_sflow_profile.set('operation', 'delete')
            
        profile_name = ET.SubElement(sflow_profile, "profile-name")
        if kwargs.pop('delete_profile_name', False) is True:
            delete_profile_name = config.find('.//*profile-name')
            delete_profile_name.set('operation', 'delete')
            
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_sampling_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        if kwargs.pop('delete_sflow_profile', False) is True:
            delete_sflow_profile = config.find('.//*sflow-profile')
            delete_sflow_profile.set('operation', 'delete')
            
        profile_name_key = ET.SubElement(sflow_profile, "profile-name")
        profile_name_key.text = kwargs.pop('profile_name')
        if kwargs.pop('delete_profile_name', False) is True:
            delete_profile_name = config.find('.//*profile-name')
            delete_profile_name.set('operation', 'delete')
                
        profile_sampling_rate = ET.SubElement(sflow_profile, "profile-sampling-rate")
        if kwargs.pop('delete_profile_sampling_rate', False) is True:
            delete_profile_sampling_rate = config.find('.//*profile-sampling-rate')
            delete_profile_sampling_rate.set('operation', 'delete')
            
        profile_sampling_rate.text = kwargs.pop('profile_sampling_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        