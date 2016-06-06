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


def rbridge_id_system_monitor_fan_alert_state(**kwargs):
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
        
    alert = ET.SubElement(fan, "alert")
    if kwargs.pop('delete_alert', False) is True:
        delete_alert = config.find('.//*alert')
        delete_alert.set('operation', 'delete')
        
    state = ET.SubElement(alert, "state")
    if kwargs.pop('delete_state', False) is True:
        delete_state = config.find('.//*state')
        delete_state.set('operation', 'delete')
        
    state.text = kwargs.pop('state')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_system_monitor_fan_alert_state_act(Action):
    def run(self, rbridge_id, delete_fan, state, delete_alert, delete_state, delete_rbridge_id, delete_system_monitor, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_system_monitor_fan_alert_state(delete_system_monitor=delete_system_monitor, username=username, rbridge_id=rbridge_id, delete_state=delete_state, state=state, delete_alert=delete_alert, host=host, delete_fan=delete_fan, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    