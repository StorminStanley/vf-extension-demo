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


def rbridge_id_host_table_aging_time_conversational_agtimeout(**kwargs):
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
        
    aging_time = ET.SubElement(host_table, "aging-time")
    if kwargs.pop('delete_aging_time', False) is True:
        delete_aging_time = config.find('.//*aging-time')
        delete_aging_time.set('operation', 'delete')
        
    conversational_agtimeout = ET.SubElement(aging_time, "conversational-agtimeout")
    if kwargs.pop('delete_conversational_agtimeout', False) is True:
        delete_conversational_agtimeout = config.find('.//*conversational-agtimeout')
        delete_conversational_agtimeout.set('operation', 'delete')
        
    conversational_agtimeout.text = kwargs.pop('conversational_agtimeout')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_host_table_aging_time_conversational_agtimeout_act(Action):
    def run(self, conversational_agtimeout, rbridge_id, delete_host_table, delete_aging_time, delete_conversational_agtimeout, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_host_table_aging_time_conversational_agtimeout(username=username, delete_host_table=delete_host_table, rbridge_id=rbridge_id, delete_aging_time=delete_aging_time, delete_conversational_agtimeout=delete_conversational_agtimeout, host=host, conversational_agtimeout=conversational_agtimeout, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    