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


def rbridge_id_threshold_monitor_interface_policy_area_threshold_buffer(**kwargs):
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

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_threshold_monitor_interface_policy_area_threshold_buffer_act(Action):
    def run(self, delete_policy_name, area_value, rbridge_id, buffer, delete_buffer, delete_area_value, policy_name, delete_area, delete_interface, delete_type, delete_threshold_monitor, delete_policy, type, delete_rbridge_id, delete_threshold, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_threshold_monitor_interface_policy_area_threshold_buffer(delete_area_value=delete_area_value, type=type, delete_threshold=delete_threshold, delete_type=delete_type, delete_policy_name=delete_policy_name, username=username, rbridge_id=rbridge_id, delete_buffer=delete_buffer, delete_area=delete_area, buffer=buffer, host=host, area_value=area_value, policy_name=policy_name, delete_policy=delete_policy, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, password=password, delete_threshold_monitor=delete_threshold_monitor, callback=_callback, mgr=mgr)
        return 0
    