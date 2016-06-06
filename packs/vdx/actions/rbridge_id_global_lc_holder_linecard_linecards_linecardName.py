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


def rbridge_id_global_lc_holder_linecard_linecards_linecardName(**kwargs):
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
            
    global_lc_holder = ET.SubElement(rbridge_id, "global-lc-holder", xmlns="urn:brocade.com:mgmt:brocade-linecard-management")
    if kwargs.pop('delete_global_lc_holder', False) is True:
        delete_global_lc_holder = config.find('.//*global-lc-holder')
        delete_global_lc_holder.set('operation', 'delete')
        
    linecard = ET.SubElement(global_lc_holder, "linecard")
    if kwargs.pop('delete_linecard', False) is True:
        delete_linecard = config.find('.//*linecard')
        delete_linecard.set('operation', 'delete')
        
    linecards = ET.SubElement(linecard, "linecards")
    if kwargs.pop('delete_linecards', False) is True:
        delete_linecards = config.find('.//*linecards')
        delete_linecards.set('operation', 'delete')
        
    linecardName = ET.SubElement(linecards, "linecardName")
    if kwargs.pop('delete_linecardName', False) is True:
        delete_linecardName = config.find('.//*linecardName')
        delete_linecardName.set('operation', 'delete')
        
    linecardName.text = kwargs.pop('linecardName')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_global_lc_holder_linecard_linecards_linecardName_act(Action):
    def run(self, rbridge_id, linecardName, delete_linecardName, delete_global_lc_holder, delete_rbridge_id, delete_linecard, delete_linecards, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_global_lc_holder_linecard_linecards_linecardName(username=username, delete_linecardName=delete_linecardName, delete_linecard=delete_linecard, rbridge_id=rbridge_id, linecardName=linecardName, host=host, password=password, delete_global_lc_holder=delete_global_lc_holder, delete_rbridge_id=delete_rbridge_id, delete_linecards=delete_linecards, callback=_callback, mgr=mgr)
        return 0
    