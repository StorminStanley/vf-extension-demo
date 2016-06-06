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


def rbridge_id_evpn_instance_duplicate_mac_timer_duplicate_mac_timer_value(**kwargs):
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
            
    evpn_instance = ET.SubElement(rbridge_id, "evpn-instance", xmlns="urn:brocade.com:mgmt:brocade-bgp")
    if kwargs.pop('delete_evpn_instance', False) is True:
        delete_evpn_instance = config.find('.//*evpn-instance')
        delete_evpn_instance.set('operation', 'delete')
        
    instance_name_key = ET.SubElement(evpn_instance, "instance-name")
    instance_name_key.text = kwargs.pop('instance_name')
    if kwargs.pop('delete_instance_name', False) is True:
        delete_instance_name = config.find('.//*instance-name')
        delete_instance_name.set('operation', 'delete')
            
    duplicate_mac_timer = ET.SubElement(evpn_instance, "duplicate-mac-timer")
    if kwargs.pop('delete_duplicate_mac_timer', False) is True:
        delete_duplicate_mac_timer = config.find('.//*duplicate-mac-timer')
        delete_duplicate_mac_timer.set('operation', 'delete')
        
    duplicate_mac_timer_value = ET.SubElement(duplicate_mac_timer, "duplicate-mac-timer-value")
    if kwargs.pop('delete_duplicate_mac_timer_value', False) is True:
        delete_duplicate_mac_timer_value = config.find('.//*duplicate-mac-timer-value')
        delete_duplicate_mac_timer_value.set('operation', 'delete')
        
    duplicate_mac_timer_value.text = kwargs.pop('duplicate_mac_timer_value')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_evpn_instance_duplicate_mac_timer_duplicate_mac_timer_value_act(Action):
    def run(self, delete_evpn_instance, rbridge_id, delete_duplicate_mac_timer, delete_duplicate_mac_timer_value, instance_name, duplicate_mac_timer_value, delete_rbridge_id, delete_instance_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_evpn_instance_duplicate_mac_timer_duplicate_mac_timer_value(username=username, instance_name=instance_name, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_instance_name=delete_instance_name, delete_duplicate_mac_timer=delete_duplicate_mac_timer, host=host, password=password, delete_evpn_instance=delete_evpn_instance, duplicate_mac_timer_value=duplicate_mac_timer_value, delete_duplicate_mac_timer_value=delete_duplicate_mac_timer_value, callback=_callback, mgr=mgr)
        return 0
    