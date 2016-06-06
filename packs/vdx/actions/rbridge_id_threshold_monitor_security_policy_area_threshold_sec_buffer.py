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


def rbridge_id_threshold_monitor_security_policy_area_threshold_sec_buffer(**kwargs):
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

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_threshold_monitor_security_policy_area_threshold_sec_buffer_act(Action):
    def run(self, delete_sec_policy_name, sec_policy_name, delete_threshold, sec_area_value, delete_policy, delete_security, sec_buffer, delete_area, delete_sec_buffer, delete_threshold_monitor, delete_rbridge_id, delete_sec_area_value, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_threshold_monitor_security_policy_area_threshold_sec_buffer(sec_area_value=sec_area_value, username=username, delete_sec_buffer=delete_sec_buffer, delete_threshold_monitor=delete_threshold_monitor, sec_policy_name=sec_policy_name, delete_sec_policy_name=delete_sec_policy_name, delete_sec_area_value=delete_sec_area_value, delete_area=delete_area, delete_policy=delete_policy, host=host, delete_threshold=delete_threshold, sec_buffer=sec_buffer, delete_rbridge_id=delete_rbridge_id, delete_security=delete_security, rbridge_id=rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    