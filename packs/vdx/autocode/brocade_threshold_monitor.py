#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_threshold_monitor(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def threshold_monitor_hidden_threshold_monitor_sfp_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        apply = ET.SubElement(sfp, "apply")
        if kwargs.pop('delete_apply', False) is True:
            delete_apply = config.find('.//*apply')
            delete_apply.set('operation', 'delete')
            
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        pause = ET.SubElement(sfp, "pause")
        if kwargs.pop('delete_pause', False) is True:
            delete_pause = config.find('.//*pause')
            delete_pause.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name = ET.SubElement(policy, "policy_name")
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
            
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        type = ET.SubElement(area, "type")
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
            
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value = ET.SubElement(area, "area_value")
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
            
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        high_threshold = ET.SubElement(threshold, "high-threshold")
        if kwargs.pop('delete_high_threshold', False) is True:
            delete_high_threshold = config.find('.//*high-threshold')
            delete_high_threshold.set('operation', 'delete')
            
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        low_threshold = ET.SubElement(threshold, "low-threshold")
        if kwargs.pop('delete_low_threshold', False) is True:
            delete_low_threshold = config.find('.//*low-threshold')
            delete_low_threshold.set('operation', 'delete')
            
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        buffer = ET.SubElement(threshold, "buffer")
        if kwargs.pop('delete_buffer', False) is True:
            delete_buffer = config.find('.//*buffer')
            delete_buffer.set('operation', 'delete')
            
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        above = ET.SubElement(alert, "above")
        if kwargs.pop('delete_above', False) is True:
            delete_above = config.find('.//*above')
            delete_above.set('operation', 'delete')
            
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        if kwargs.pop('delete_above_highthresh_action', False) is True:
            delete_above_highthresh_action = config.find('.//*above-highthresh-action')
            delete_above_highthresh_action.set('operation', 'delete')
            
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        if kwargs.pop('delete_below_highthresh_action', False) is True:
            delete_below_highthresh_action = config.find('.//*below-highthresh-action')
            delete_below_highthresh_action.set('operation', 'delete')
            
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(threshold_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        policy = ET.SubElement(sfp, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        if kwargs.pop('delete_below_lowthresh_action', False) is True:
            delete_below_lowthresh_action = config.find('.//*below-lowthresh-action')
            delete_below_lowthresh_action.set('operation', 'delete')
            
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        apply = ET.SubElement(security, "apply")
        if kwargs.pop('delete_apply', False) is True:
            delete_apply = config.find('.//*apply')
            delete_apply.set('operation', 'delete')
            
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        pause = ET.SubElement(security, "pause")
        if kwargs.pop('delete_pause', False) is True:
            delete_pause = config.find('.//*pause')
            delete_pause.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_sec_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name = ET.SubElement(policy, "sec_policy_name")
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
            
        sec_policy_name.text = kwargs.pop('sec_policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_sec_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value = ET.SubElement(area, "sec_area_value")
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
            
        sec_area_value.text = kwargs.pop('sec_area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        timebase = ET.SubElement(area, "timebase")
        if kwargs.pop('delete_timebase', False) is True:
            delete_timebase = config.find('.//*timebase')
            delete_timebase.set('operation', 'delete')
            
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        sec_high_threshold = ET.SubElement(threshold, "sec-high-threshold")
        if kwargs.pop('delete_sec_high_threshold', False) is True:
            delete_sec_high_threshold = config.find('.//*sec-high-threshold')
            delete_sec_high_threshold.set('operation', 'delete')
            
        sec_high_threshold.text = kwargs.pop('sec_high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        sec_low_threshold = ET.SubElement(threshold, "sec-low-threshold")
        if kwargs.pop('delete_sec_low_threshold', False) is True:
            delete_sec_low_threshold = config.find('.//*sec-low-threshold')
            delete_sec_low_threshold.set('operation', 'delete')
            
        sec_low_threshold.text = kwargs.pop('sec_low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        sec_buffer = ET.SubElement(threshold, "sec-buffer")
        if kwargs.pop('delete_sec_buffer', False) is True:
            delete_sec_buffer = config.find('.//*sec-buffer')
            delete_sec_buffer.set('operation', 'delete')
            
        sec_buffer.text = kwargs.pop('sec_buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_above_sec_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        above = ET.SubElement(alert, "above")
        if kwargs.pop('delete_above', False) is True:
            delete_above = config.find('.//*above')
            delete_above.set('operation', 'delete')
            
        sec_above_highthresh_action = ET.SubElement(above, "sec-above-highthresh-action")
        if kwargs.pop('delete_sec_above_highthresh_action', False) is True:
            delete_sec_above_highthresh_action = config.find('.//*sec-above-highthresh-action')
            delete_sec_above_highthresh_action.set('operation', 'delete')
            
        sec_above_highthresh_action.text = kwargs.pop('sec_above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        sec_below_highthresh_action = ET.SubElement(below, "sec-below-highthresh-action")
        if kwargs.pop('delete_sec_below_highthresh_action', False) is True:
            delete_sec_below_highthresh_action = config.find('.//*sec-below-highthresh-action')
            delete_sec_below_highthresh_action.set('operation', 'delete')
            
        sec_below_highthresh_action.text = kwargs.pop('sec_below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        security = ET.SubElement(threshold_monitor, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        policy = ET.SubElement(security, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        if kwargs.pop('delete_sec_policy_name', False) is True:
            delete_sec_policy_name = config.find('.//*sec_policy_name')
            delete_sec_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        if kwargs.pop('delete_sec_area_value', False) is True:
            delete_sec_area_value = config.find('.//*sec_area_value')
            delete_sec_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        sec_below_lowthresh_action = ET.SubElement(below, "sec-below-lowthresh-action")
        if kwargs.pop('delete_sec_below_lowthresh_action', False) is True:
            delete_sec_below_lowthresh_action = config.find('.//*sec-below-lowthresh-action')
            delete_sec_below_lowthresh_action.set('operation', 'delete')
            
        sec_below_lowthresh_action.text = kwargs.pop('sec_below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        if kwargs.pop('delete_Cpu', False) is True:
            delete_Cpu = config.find('.//*Cpu')
            delete_Cpu.set('operation', 'delete')
            
        poll = ET.SubElement(Cpu, "poll")
        if kwargs.pop('delete_poll', False) is True:
            delete_poll = config.find('.//*poll')
            delete_poll.set('operation', 'delete')
            
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        if kwargs.pop('delete_Cpu', False) is True:
            delete_Cpu = config.find('.//*Cpu')
            delete_Cpu.set('operation', 'delete')
            
        retry = ET.SubElement(Cpu, "retry")
        if kwargs.pop('delete_retry', False) is True:
            delete_retry = config.find('.//*retry')
            delete_retry.set('operation', 'delete')
            
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        if kwargs.pop('delete_Cpu', False) is True:
            delete_Cpu = config.find('.//*Cpu')
            delete_Cpu.set('operation', 'delete')
            
        limit = ET.SubElement(Cpu, "limit")
        if kwargs.pop('delete_limit', False) is True:
            delete_limit = config.find('.//*limit')
            delete_limit.set('operation', 'delete')
            
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        if kwargs.pop('delete_Cpu', False) is True:
            delete_Cpu = config.find('.//*Cpu')
            delete_Cpu.set('operation', 'delete')
            
        actions = ET.SubElement(Cpu, "actions")
        if kwargs.pop('delete_actions', False) is True:
            delete_actions = config.find('.//*actions')
            delete_actions.set('operation', 'delete')
            
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        poll = ET.SubElement(Memory, "poll")
        if kwargs.pop('delete_poll', False) is True:
            delete_poll = config.find('.//*poll')
            delete_poll.set('operation', 'delete')
            
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        retry = ET.SubElement(Memory, "retry")
        if kwargs.pop('delete_retry', False) is True:
            delete_retry = config.find('.//*retry')
            delete_retry.set('operation', 'delete')
            
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        limit = ET.SubElement(Memory, "limit")
        if kwargs.pop('delete_limit', False) is True:
            delete_limit = config.find('.//*limit')
            delete_limit.set('operation', 'delete')
            
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_high_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        high_limit = ET.SubElement(Memory, "high-limit")
        if kwargs.pop('delete_high_limit', False) is True:
            delete_high_limit = config.find('.//*high-limit')
            delete_high_limit.set('operation', 'delete')
            
        high_limit.text = kwargs.pop('high_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_low_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        low_limit = ET.SubElement(Memory, "low-limit")
        if kwargs.pop('delete_low_limit', False) is True:
            delete_low_limit = config.find('.//*low-limit')
            delete_low_limit.set('operation', 'delete')
            
        low_limit.text = kwargs.pop('low_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        Memory = ET.SubElement(threshold_monitor, "Memory")
        if kwargs.pop('delete_Memory', False) is True:
            delete_Memory = config.find('.//*Memory')
            delete_Memory.set('operation', 'delete')
            
        actions = ET.SubElement(Memory, "actions")
        if kwargs.pop('delete_actions', False) is True:
            delete_actions = config.find('.//*actions')
            delete_actions.set('operation', 'delete')
            
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        apply = ET.SubElement(interface, "apply")
        if kwargs.pop('delete_apply', False) is True:
            delete_apply = config.find('.//*apply')
            delete_apply.set('operation', 'delete')
            
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        pause = ET.SubElement(interface, "pause")
        if kwargs.pop('delete_pause', False) is True:
            delete_pause = config.find('.//*pause')
            delete_pause.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name = ET.SubElement(policy, "policy_name")
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
            
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        type = ET.SubElement(area, "type")
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
            
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value = ET.SubElement(area, "area_value")
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
            
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_timebase_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        timebase_value = ET.SubElement(threshold, "timebase_value")
        if kwargs.pop('delete_timebase_value', False) is True:
            delete_timebase_value = config.find('.//*timebase_value')
            delete_timebase_value.set('operation', 'delete')
            
        timebase_value.text = kwargs.pop('timebase_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        high_threshold = ET.SubElement(threshold, "high-threshold")
        if kwargs.pop('delete_high_threshold', False) is True:
            delete_high_threshold = config.find('.//*high-threshold')
            delete_high_threshold.set('operation', 'delete')
            
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        low_threshold = ET.SubElement(threshold, "low-threshold")
        if kwargs.pop('delete_low_threshold', False) is True:
            delete_low_threshold = config.find('.//*low-threshold')
            delete_low_threshold.set('operation', 'delete')
            
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        threshold = ET.SubElement(area, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        buffer = ET.SubElement(threshold, "buffer")
        if kwargs.pop('delete_buffer', False) is True:
            delete_buffer = config.find('.//*buffer')
            delete_buffer.set('operation', 'delete')
            
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        above = ET.SubElement(alert, "above")
        if kwargs.pop('delete_above', False) is True:
            delete_above = config.find('.//*above')
            delete_above.set('operation', 'delete')
            
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        if kwargs.pop('delete_above_highthresh_action', False) is True:
            delete_above_highthresh_action = config.find('.//*above-highthresh-action')
            delete_above_highthresh_action.set('operation', 'delete')
            
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        above = ET.SubElement(alert, "above")
        if kwargs.pop('delete_above', False) is True:
            delete_above = config.find('.//*above')
            delete_above.set('operation', 'delete')
            
        above_lowthresh_action = ET.SubElement(above, "above-lowthresh-action")
        if kwargs.pop('delete_above_lowthresh_action', False) is True:
            delete_above_lowthresh_action = config.find('.//*above-lowthresh-action')
            delete_above_lowthresh_action.set('operation', 'delete')
            
        above_lowthresh_action.text = kwargs.pop('above_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        if kwargs.pop('delete_below_highthresh_action', False) is True:
            delete_below_highthresh_action = config.find('.//*below-highthresh-action')
            delete_below_highthresh_action.set('operation', 'delete')
            
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        if kwargs.pop('delete_threshold_monitor_hidden', False) is True:
            delete_threshold_monitor_hidden = config.find('.//*threshold-monitor-hidden')
            delete_threshold_monitor_hidden.set('operation', 'delete')
            
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        if kwargs.pop('delete_threshold_monitor', False) is True:
            delete_threshold_monitor = config.find('.//*threshold-monitor')
            delete_threshold_monitor.set('operation', 'delete')
            
        interface = ET.SubElement(threshold_monitor, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        policy = ET.SubElement(interface, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        if kwargs.pop('delete_policy_name', False) is True:
            delete_policy_name = config.find('.//*policy_name')
            delete_policy_name.set('operation', 'delete')
                
        area = ET.SubElement(policy, "area")
        if kwargs.pop('delete_area', False) is True:
            delete_area = config.find('.//*area')
            delete_area.set('operation', 'delete')
            
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
                
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        if kwargs.pop('delete_area_value', False) is True:
            delete_area_value = config.find('.//*area_value')
            delete_area_value.set('operation', 'delete')
                
        alert = ET.SubElement(area, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        below = ET.SubElement(alert, "below")
        if kwargs.pop('delete_below', False) is True:
            delete_below = config.find('.//*below')
            delete_below.set('operation', 'delete')
            
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        if kwargs.pop('delete_below_lowthresh_action', False) is True:
            delete_below_lowthresh_action = config.find('.//*below-lowthresh-action')
            delete_below_lowthresh_action.set('operation', 'delete')
            
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        