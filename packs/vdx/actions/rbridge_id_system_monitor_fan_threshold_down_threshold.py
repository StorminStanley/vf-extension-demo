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


def rbridge_id_system_monitor_fan_threshold_down_threshold(**kwargs):
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
            
    system_monitor = ET.SubElement(rbridge_id, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
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

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_system_monitor_fan_threshold_down_threshold_act(Action):
    def run(self, delete_threshold, delete_fan, down_threshold, delete_system_monitor, delete_rbridge_id, delete_down_threshold, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_system_monitor_fan_threshold_down_threshold(delete_system_monitor=delete_system_monitor, delete_down_threshold=delete_down_threshold, username=username, down_threshold=down_threshold, rbridge_id=rbridge_id, host=host, delete_threshold=delete_threshold, delete_fan=delete_fan, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    