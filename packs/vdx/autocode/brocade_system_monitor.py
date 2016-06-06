#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system_monitor(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def system_monitor_fan_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        fan = ET.SubElement(system_monitor, "fan")
        if kwargs.pop('delete_fan', False) is True:
            delete_fan = config.find('.//*fan')
            delete_fan.set('operation', 'delete')
            
        threshold = ET.SubElement(fan, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        fan = ET.SubElement(system_monitor, "fan")
        if kwargs.pop('delete_fan', False) is True:
            delete_fan = config.find('.//*fan')
            delete_fan.set('operation', 'delete')
            
        threshold = ET.SubElement(fan, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        fan = ET.SubElement(system_monitor, "fan")
        if kwargs.pop('delete_fan', False) is True:
            delete_fan = config.find('.//*fan')
            delete_fan.set('operation', 'delete')
            
        alert = ET.SubElement(fan, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        state = ET.SubElement(alert, "state")
        if kwargs.pop('delete_state', False) is True:
            delete_state = config.find('.//*state')
            delete_state.set('operation', 'delete')
            
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        fan = ET.SubElement(system_monitor, "fan")
        if kwargs.pop('delete_fan', False) is True:
            delete_fan = config.find('.//*fan')
            delete_fan.set('operation', 'delete')
            
        alert = ET.SubElement(fan, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        action = ET.SubElement(alert, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        power = ET.SubElement(system_monitor, "power")
        if kwargs.pop('delete_power', False) is True:
            delete_power = config.find('.//*power')
            delete_power.set('operation', 'delete')
            
        threshold = ET.SubElement(power, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        power = ET.SubElement(system_monitor, "power")
        if kwargs.pop('delete_power', False) is True:
            delete_power = config.find('.//*power')
            delete_power.set('operation', 'delete')
            
        threshold = ET.SubElement(power, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        power = ET.SubElement(system_monitor, "power")
        if kwargs.pop('delete_power', False) is True:
            delete_power = config.find('.//*power')
            delete_power.set('operation', 'delete')
            
        alert = ET.SubElement(power, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        state = ET.SubElement(alert, "state")
        if kwargs.pop('delete_state', False) is True:
            delete_state = config.find('.//*state')
            delete_state.set('operation', 'delete')
            
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        power = ET.SubElement(system_monitor, "power")
        if kwargs.pop('delete_power', False) is True:
            delete_power = config.find('.//*power')
            delete_power.set('operation', 'delete')
            
        alert = ET.SubElement(power, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        action = ET.SubElement(alert, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        temp = ET.SubElement(system_monitor, "temp")
        if kwargs.pop('delete_temp', False) is True:
            delete_temp = config.find('.//*temp')
            delete_temp.set('operation', 'delete')
            
        threshold = ET.SubElement(temp, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        temp = ET.SubElement(system_monitor, "temp")
        if kwargs.pop('delete_temp', False) is True:
            delete_temp = config.find('.//*temp')
            delete_temp.set('operation', 'delete')
            
        threshold = ET.SubElement(temp, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        cid_card = ET.SubElement(system_monitor, "cid-card")
        if kwargs.pop('delete_cid_card', False) is True:
            delete_cid_card = config.find('.//*cid-card')
            delete_cid_card.set('operation', 'delete')
            
        threshold = ET.SubElement(cid_card, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        cid_card = ET.SubElement(system_monitor, "cid-card")
        if kwargs.pop('delete_cid_card', False) is True:
            delete_cid_card = config.find('.//*cid-card')
            delete_cid_card.set('operation', 'delete')
            
        threshold = ET.SubElement(cid_card, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        cid_card = ET.SubElement(system_monitor, "cid-card")
        if kwargs.pop('delete_cid_card', False) is True:
            delete_cid_card = config.find('.//*cid-card')
            delete_cid_card.set('operation', 'delete')
            
        alert = ET.SubElement(cid_card, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        state = ET.SubElement(alert, "state")
        if kwargs.pop('delete_state', False) is True:
            delete_state = config.find('.//*state')
            delete_state.set('operation', 'delete')
            
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        cid_card = ET.SubElement(system_monitor, "cid-card")
        if kwargs.pop('delete_cid_card', False) is True:
            delete_cid_card = config.find('.//*cid-card')
            delete_cid_card.set('operation', 'delete')
            
        alert = ET.SubElement(cid_card, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        action = ET.SubElement(alert, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(system_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        alert = ET.SubElement(sfp, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        state = ET.SubElement(alert, "state")
        if kwargs.pop('delete_state', False) is True:
            delete_state = config.find('.//*state')
            delete_state.set('operation', 'delete')
            
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        sfp = ET.SubElement(system_monitor, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        alert = ET.SubElement(sfp, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        action = ET.SubElement(alert, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        if kwargs.pop('delete_compact_flash', False) is True:
            delete_compact_flash = config.find('.//*compact-flash')
            delete_compact_flash.set('operation', 'delete')
            
        threshold = ET.SubElement(compact_flash, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        if kwargs.pop('delete_compact_flash', False) is True:
            delete_compact_flash = config.find('.//*compact-flash')
            delete_compact_flash.set('operation', 'delete')
            
        threshold = ET.SubElement(compact_flash, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        MM = ET.SubElement(system_monitor, "MM")
        if kwargs.pop('delete_MM', False) is True:
            delete_MM = config.find('.//*MM')
            delete_MM.set('operation', 'delete')
            
        threshold = ET.SubElement(MM, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        MM = ET.SubElement(system_monitor, "MM")
        if kwargs.pop('delete_MM', False) is True:
            delete_MM = config.find('.//*MM')
            delete_MM.set('operation', 'delete')
            
        threshold = ET.SubElement(MM, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        LineCard = ET.SubElement(system_monitor, "LineCard")
        if kwargs.pop('delete_LineCard', False) is True:
            delete_LineCard = config.find('.//*LineCard')
            delete_LineCard.set('operation', 'delete')
            
        threshold = ET.SubElement(LineCard, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        LineCard = ET.SubElement(system_monitor, "LineCard")
        if kwargs.pop('delete_LineCard', False) is True:
            delete_LineCard = config.find('.//*LineCard')
            delete_LineCard.set('operation', 'delete')
            
        threshold = ET.SubElement(LineCard, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        LineCard = ET.SubElement(system_monitor, "LineCard")
        if kwargs.pop('delete_LineCard', False) is True:
            delete_LineCard = config.find('.//*LineCard')
            delete_LineCard.set('operation', 'delete')
            
        alert = ET.SubElement(LineCard, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        state = ET.SubElement(alert, "state")
        if kwargs.pop('delete_state', False) is True:
            delete_state = config.find('.//*state')
            delete_state.set('operation', 'delete')
            
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        LineCard = ET.SubElement(system_monitor, "LineCard")
        if kwargs.pop('delete_LineCard', False) is True:
            delete_LineCard = config.find('.//*LineCard')
            delete_LineCard.set('operation', 'delete')
            
        alert = ET.SubElement(LineCard, "alert")
        if kwargs.pop('delete_alert', False) is True:
            delete_alert = config.find('.//*alert')
            delete_alert.set('operation', 'delete')
            
        action = ET.SubElement(alert, "action")
        if kwargs.pop('delete_action', False) is True:
            delete_action = config.find('.//*action')
            delete_action.set('operation', 'delete')
            
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        SFM = ET.SubElement(system_monitor, "SFM")
        if kwargs.pop('delete_SFM', False) is True:
            delete_SFM = config.find('.//*SFM')
            delete_SFM.set('operation', 'delete')
            
        threshold = ET.SubElement(SFM, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        if kwargs.pop('delete_marginal_threshold', False) is True:
            delete_marginal_threshold = config.find('.//*marginal-threshold')
            delete_marginal_threshold.set('operation', 'delete')
            
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor', False) is True:
            delete_system_monitor = config.find('.//*system-monitor')
            delete_system_monitor.set('operation', 'delete')
            
        SFM = ET.SubElement(system_monitor, "SFM")
        if kwargs.pop('delete_SFM', False) is True:
            delete_SFM = config.find('.//*SFM')
            delete_SFM.set('operation', 'delete')
            
        threshold = ET.SubElement(SFM, "threshold")
        if kwargs.pop('delete_threshold', False) is True:
            delete_threshold = config.find('.//*threshold')
            delete_threshold.set('operation', 'delete')
            
        down_threshold = ET.SubElement(threshold, "down-threshold")
        if kwargs.pop('delete_down_threshold', False) is True:
            delete_down_threshold = config.find('.//*down-threshold')
            delete_down_threshold.set('operation', 'delete')
            
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        fru = ET.SubElement(system_monitor_mail, "fru")
        if kwargs.pop('delete_fru', False) is True:
            delete_fru = config.find('.//*fru')
            delete_fru.set('operation', 'delete')
            
        enable = ET.SubElement(fru, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        fru = ET.SubElement(system_monitor_mail, "fru")
        if kwargs.pop('delete_fru', False) is True:
            delete_fru = config.find('.//*fru')
            delete_fru.set('operation', 'delete')
            
        email_list = ET.SubElement(fru, "email-list")
        if kwargs.pop('delete_email_list', False) is True:
            delete_email_list = config.find('.//*email-list')
            delete_email_list.set('operation', 'delete')
            
        email = ET.SubElement(email_list, "email")
        if kwargs.pop('delete_email', False) is True:
            delete_email = config.find('.//*email')
            delete_email.set('operation', 'delete')
            
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        enable = ET.SubElement(sfp, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        if kwargs.pop('delete_sfp', False) is True:
            delete_sfp = config.find('.//*sfp')
            delete_sfp.set('operation', 'delete')
            
        email_list = ET.SubElement(sfp, "email-list")
        if kwargs.pop('delete_email_list', False) is True:
            delete_email_list = config.find('.//*email-list')
            delete_email_list.set('operation', 'delete')
            
        email = ET.SubElement(email_list, "email")
        if kwargs.pop('delete_email', False) is True:
            delete_email = config.find('.//*email')
            delete_email.set('operation', 'delete')
            
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        security = ET.SubElement(system_monitor_mail, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        enable = ET.SubElement(security, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        security = ET.SubElement(system_monitor_mail, "security")
        if kwargs.pop('delete_security', False) is True:
            delete_security = config.find('.//*security')
            delete_security.set('operation', 'delete')
            
        email_list = ET.SubElement(security, "email-list")
        if kwargs.pop('delete_email_list', False) is True:
            delete_email_list = config.find('.//*email-list')
            delete_email_list.set('operation', 'delete')
            
        email = ET.SubElement(email_list, "email")
        if kwargs.pop('delete_email', False) is True:
            delete_email = config.find('.//*email')
            delete_email.set('operation', 'delete')
            
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        interface = ET.SubElement(system_monitor_mail, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        enable = ET.SubElement(interface, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        interface = ET.SubElement(system_monitor_mail, "interface")
        if kwargs.pop('delete_interface', False) is True:
            delete_interface = config.find('.//*interface')
            delete_interface.set('operation', 'delete')
            
        email_list = ET.SubElement(interface, "email-list")
        if kwargs.pop('delete_email_list', False) is True:
            delete_email_list = config.find('.//*email-list')
            delete_email_list.set('operation', 'delete')
            
        email = ET.SubElement(email_list, "email")
        if kwargs.pop('delete_email', False) is True:
            delete_email = config.find('.//*email')
            delete_email.set('operation', 'delete')
            
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        relay = ET.SubElement(system_monitor_mail, "relay")
        if kwargs.pop('delete_relay', False) is True:
            delete_relay = config.find('.//*relay')
            delete_relay.set('operation', 'delete')
            
        host_ip = ET.SubElement(relay, "host-ip")
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
            
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        if kwargs.pop('delete_system_monitor_mail', False) is True:
            delete_system_monitor_mail = config.find('.//*system-monitor-mail')
            delete_system_monitor_mail.set('operation', 'delete')
            
        relay = ET.SubElement(system_monitor_mail, "relay")
        if kwargs.pop('delete_relay', False) is True:
            delete_relay = config.find('.//*relay')
            delete_relay.set('operation', 'delete')
            
        host_ip_key = ET.SubElement(relay, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        if kwargs.pop('delete_host_ip', False) is True:
            delete_host_ip = config.find('.//*host-ip')
            delete_host_ip.set('operation', 'delete')
                
        domain_name = ET.SubElement(relay, "domain-name")
        if kwargs.pop('delete_domain_name', False) is True:
            delete_domain_name = config.find('.//*domain-name')
            delete_domain_name.set('operation', 'delete')
            
        domain_name.text = kwargs.pop('domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        