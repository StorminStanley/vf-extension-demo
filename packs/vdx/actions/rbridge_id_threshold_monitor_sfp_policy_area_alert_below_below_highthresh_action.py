import sys
from ncclient import manager
from ncclient import xml_
import ncclient
from st2actions.runners.pythonrunner import Action
from xml.etree import ElementTree as ET



def _callback(call, handler='edit_config', target='running', source='startup', mgr=None):
    try:
        call = ET.tostring(call)
        if handler == 'get':
            call_element = xml_.to_ele(call)
            return ET.fromstring(str(mgr.dispatch(call_element)))
        if handler == 'edit_config':
            mgr.edit_config(target=target, config=call)
        if handler == 'delete_config':
            mgr.delete_config(target=target)
        if handler == 'copy_config':
            mgr.copy_config(target=target, source=source)
    except (ncclient.transport.TransportError,
            ncclient.transport.SessionCloseError,
            ncclient.transport.SSHError,
            ncclient.transport.AuthenticationError,
            ncclient.transport.SSHUnknownHostError) as error:
        logging.error(error)
        raise DeviceCommError


def rbridge_id_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    threshold_monitor = ET.SubElement(rbridge_id, "threshold-monitor", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
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

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action_act(Action):
    def run(self, delete_policy_name, area_value, rbridge_id, delete_area_value, policy_name, delete_alert, delete_below_highthresh_action, delete_area, below_highthresh_action, delete_type, delete_threshold_monitor, delete_sfp, type, delete_rbridge_id, delete_policy, delete_below, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action(delete_area_value=delete_area_value, delete_below_highthresh_action=delete_below_highthresh_action, username=username, type=type, delete_sfp=delete_sfp, delete_below=delete_below, delete_type=delete_type, delete_policy_name=delete_policy_name, delete_area=delete_area, rbridge_id=rbridge_id, below_highthresh_action=below_highthresh_action, delete_threshold_monitor=delete_threshold_monitor, delete_alert=delete_alert, delete_policy=delete_policy, area_value=area_value, policy_name=policy_name, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    