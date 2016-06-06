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


def rbridge_id_host_table_aging_mode_conversational(**kwargs):
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
            
    host_table = ET.SubElement(rbridge_id, "host-table", xmlns="urn:brocade.com:mgmt:brocade-arp")
    if kwargs.pop('delete_host_table', False) is True:
        delete_host_table = config.find('.//*host-table')
        delete_host_table.set('operation', 'delete')
        
    aging_mode = ET.SubElement(host_table, "aging-mode")
    if kwargs.pop('delete_aging_mode', False) is True:
        delete_aging_mode = config.find('.//*aging-mode')
        delete_aging_mode.set('operation', 'delete')
        
    conversational = ET.SubElement(aging_mode, "conversational")
    if kwargs.pop('delete_conversational', False) is True:
        delete_conversational = config.find('.//*conversational')
        delete_conversational.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_host_table_aging_mode_conversational_act(Action):
    def run(self, delete_rbridge_id, delete_conversational, rbridge_id, delete_host_table, delete_aging_mode, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_host_table_aging_mode_conversational(username=username, delete_conversational=delete_conversational, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_aging_mode=delete_aging_mode, host=host, delete_host_table=delete_host_table, password=password, callback=_callback, mgr=mgr)
        return 0
    