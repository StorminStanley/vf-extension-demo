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


def rbridge_id_filter_change_update_delay_filter_delay_value(**kwargs):
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
            
    filter_change_update_delay = ET.SubElement(rbridge_id, "filter-change-update-delay", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_filter_change_update_delay', False) is True:
        delete_filter_change_update_delay = config.find('.//*filter-change-update-delay')
        delete_filter_change_update_delay.set('operation', 'delete')
        
    filter_delay_value = ET.SubElement(filter_change_update_delay, "filter-delay-value")
    if kwargs.pop('delete_filter_delay_value', False) is True:
        delete_filter_delay_value = config.find('.//*filter-delay-value')
        delete_filter_delay_value.set('operation', 'delete')
        
    filter_delay_value.text = kwargs.pop('filter_delay_value')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_filter_change_update_delay_filter_delay_value_act(Action):
    def run(self, filter_delay_value, delete_rbridge_id, rbridge_id, delete_filter_change_update_delay, delete_filter_delay_value, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_filter_change_update_delay_filter_delay_value(username=username, rbridge_id=rbridge_id, delete_filter_change_update_delay=delete_filter_change_update_delay, filter_delay_value=filter_delay_value, host=host, delete_filter_delay_value=delete_filter_delay_value, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    