#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_rmon(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def rmon_event_entry_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        event_entry = ET.SubElement(rmon, "event-entry")
        if kwargs.pop('delete_event_entry', False) is True:
            delete_event_entry = config.find('.//*event-entry')
            delete_event_entry.set('operation', 'delete')
            
        event_index = ET.SubElement(event_entry, "event-index")
        if kwargs.pop('delete_event_index', False) is True:
            delete_event_index = config.find('.//*event-index')
            delete_event_index.set('operation', 'delete')
            
        event_index.text = kwargs.pop('event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        event_entry = ET.SubElement(rmon, "event-entry")
        if kwargs.pop('delete_event_entry', False) is True:
            delete_event_entry = config.find('.//*event-entry')
            delete_event_entry.set('operation', 'delete')
            
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        if kwargs.pop('delete_event_index', False) is True:
            delete_event_index = config.find('.//*event-index')
            delete_event_index.set('operation', 'delete')
                
        event_description = ET.SubElement(event_entry, "event-description")
        if kwargs.pop('delete_event_description', False) is True:
            delete_event_description = config.find('.//*event-description')
            delete_event_description.set('operation', 'delete')
            
        event_description.text = kwargs.pop('event_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        event_entry = ET.SubElement(rmon, "event-entry")
        if kwargs.pop('delete_event_entry', False) is True:
            delete_event_entry = config.find('.//*event-entry')
            delete_event_entry.set('operation', 'delete')
            
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        if kwargs.pop('delete_event_index', False) is True:
            delete_event_index = config.find('.//*event-index')
            delete_event_index.set('operation', 'delete')
                
        log = ET.SubElement(event_entry, "log")
        if kwargs.pop('delete_log', False) is True:
            delete_log = config.find('.//*log')
            delete_log.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        event_entry = ET.SubElement(rmon, "event-entry")
        if kwargs.pop('delete_event_entry', False) is True:
            delete_event_entry = config.find('.//*event-entry')
            delete_event_entry.set('operation', 'delete')
            
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        if kwargs.pop('delete_event_index', False) is True:
            delete_event_index = config.find('.//*event-index')
            delete_event_index.set('operation', 'delete')
                
        event_community = ET.SubElement(event_entry, "event-community")
        if kwargs.pop('delete_event_community', False) is True:
            delete_event_community = config.find('.//*event-community')
            delete_event_community.set('operation', 'delete')
            
        event_community.text = kwargs.pop('event_community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        event_entry = ET.SubElement(rmon, "event-entry")
        if kwargs.pop('delete_event_entry', False) is True:
            delete_event_entry = config.find('.//*event-entry')
            delete_event_entry.set('operation', 'delete')
            
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        if kwargs.pop('delete_event_index', False) is True:
            delete_event_index = config.find('.//*event-index')
            delete_event_index.set('operation', 'delete')
                
        event_owner = ET.SubElement(event_entry, "event-owner")
        if kwargs.pop('delete_event_owner', False) is True:
            delete_event_owner = config.find('.//*event-owner')
            delete_event_owner.set('operation', 'delete')
            
        event_owner.text = kwargs.pop('event_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index = ET.SubElement(alarm_entry, "alarm-index")
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
            
        alarm_index.text = kwargs.pop('alarm_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_snmp_oid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        snmp_oid = ET.SubElement(alarm_entry, "snmp-oid")
        if kwargs.pop('delete_snmp_oid', False) is True:
            delete_snmp_oid = config.find('.//*snmp-oid')
            delete_snmp_oid.set('operation', 'delete')
            
        snmp_oid.text = kwargs.pop('snmp_oid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_interval = ET.SubElement(alarm_entry, "alarm-interval")
        if kwargs.pop('delete_alarm_interval', False) is True:
            delete_alarm_interval = config.find('.//*alarm-interval')
            delete_alarm_interval.set('operation', 'delete')
            
        alarm_interval.text = kwargs.pop('alarm_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_sample(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_sample = ET.SubElement(alarm_entry, "alarm-sample")
        if kwargs.pop('delete_alarm_sample', False) is True:
            delete_alarm_sample = config.find('.//*alarm-sample')
            delete_alarm_sample.set('operation', 'delete')
            
        alarm_sample.text = kwargs.pop('alarm_sample')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_rising_threshold = ET.SubElement(alarm_entry, "alarm-rising-threshold")
        if kwargs.pop('delete_alarm_rising_threshold', False) is True:
            delete_alarm_rising_threshold = config.find('.//*alarm-rising-threshold')
            delete_alarm_rising_threshold.set('operation', 'delete')
            
        alarm_rising_threshold.text = kwargs.pop('alarm_rising_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_rising_event_index = ET.SubElement(alarm_entry, "alarm-rising-event-index")
        if kwargs.pop('delete_alarm_rising_event_index', False) is True:
            delete_alarm_rising_event_index = config.find('.//*alarm-rising-event-index')
            delete_alarm_rising_event_index.set('operation', 'delete')
            
        alarm_rising_event_index.text = kwargs.pop('alarm_rising_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_falling_threshold = ET.SubElement(alarm_entry, "alarm-falling-threshold")
        if kwargs.pop('delete_alarm_falling_threshold', False) is True:
            delete_alarm_falling_threshold = config.find('.//*alarm-falling-threshold')
            delete_alarm_falling_threshold.set('operation', 'delete')
            
        alarm_falling_threshold.text = kwargs.pop('alarm_falling_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_falling_event_index = ET.SubElement(alarm_entry, "alarm-falling-event-index")
        if kwargs.pop('delete_alarm_falling_event_index', False) is True:
            delete_alarm_falling_event_index = config.find('.//*alarm-falling-event-index')
            delete_alarm_falling_event_index.set('operation', 'delete')
            
        alarm_falling_event_index.text = kwargs.pop('alarm_falling_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        if kwargs.pop('delete_rmon', False) is True:
            delete_rmon = config.find('.//*rmon')
            delete_rmon.set('operation', 'delete')
            
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        if kwargs.pop('delete_alarm_entry', False) is True:
            delete_alarm_entry = config.find('.//*alarm-entry')
            delete_alarm_entry.set('operation', 'delete')
            
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        if kwargs.pop('delete_alarm_index', False) is True:
            delete_alarm_index = config.find('.//*alarm-index')
            delete_alarm_index.set('operation', 'delete')
                
        alarm_owner = ET.SubElement(alarm_entry, "alarm-owner")
        if kwargs.pop('delete_alarm_owner', False) is True:
            delete_alarm_owner = config.find('.//*alarm-owner')
            delete_alarm_owner.set('operation', 'delete')
            
        alarm_owner.text = kwargs.pop('alarm_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        