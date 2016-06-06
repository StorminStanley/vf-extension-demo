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


def rbridge_id_switch_attributes_chassis_name(**kwargs):
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
            
    switch_attributes = ET.SubElement(rbridge_id, "switch-attributes")
    if kwargs.pop('delete_switch_attributes', False) is True:
        delete_switch_attributes = config.find('.//*switch-attributes')
        delete_switch_attributes.set('operation', 'delete')
        
    chassis_name = ET.SubElement(switch_attributes, "chassis-name")
    if kwargs.pop('delete_chassis_name', False) is True:
        delete_chassis_name = config.find('.//*chassis-name')
        delete_chassis_name.set('operation', 'delete')
        
    chassis_name.text = kwargs.pop('chassis_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_switch_attributes_chassis_name_act(Action):
    def run(self, delete_chassis_name, delete_rbridge_id, chassis_name, delete_switch_attributes, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_switch_attributes_chassis_name(username=username, delete_chassis_name=delete_chassis_name, rbridge_id=rbridge_id, chassis_name=chassis_name, host=host, delete_switch_attributes=delete_switch_attributes, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    