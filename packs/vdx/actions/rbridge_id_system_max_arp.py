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


def rbridge_id_system_max_arp(**kwargs):
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
            
    system_max = ET.SubElement(rbridge_id, "system-max", xmlns="urn:brocade.com:mgmt:brocade-arp")
    if kwargs.pop('delete_system_max', False) is True:
        delete_system_max = config.find('.//*system-max')
        delete_system_max.set('operation', 'delete')
        
    arp = ET.SubElement(system_max, "arp")
    if kwargs.pop('delete_arp', False) is True:
        delete_arp = config.find('.//*arp')
        delete_arp.set('operation', 'delete')
        
    arp.text = kwargs.pop('arp')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_system_max_arp_act(Action):
    def run(self, arp, delete_system_max, delete_rbridge_id, rbridge_id, delete_arp, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_system_max_arp(username=username, rbridge_id=rbridge_id, delete_system_max=delete_system_max, host=host, arp=arp, delete_rbridge_id=delete_rbridge_id, delete_arp=delete_arp, password=password, callback=_callback, mgr=mgr)
        return 0
    