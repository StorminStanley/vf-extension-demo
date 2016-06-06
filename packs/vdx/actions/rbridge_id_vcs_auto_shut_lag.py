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


def rbridge_id_vcs_auto_shut_lag(**kwargs):
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
            
    vcs = ET.SubElement(rbridge_id, "vcs", xmlns="http://brocade.com/ns/brocade-auto-shut-edge-port")
    if kwargs.pop('delete_vcs', False) is True:
        delete_vcs = config.find('.//*vcs')
        delete_vcs.set('operation', 'delete')
        
    auto_shut = ET.SubElement(vcs, "auto-shut")
    if kwargs.pop('delete_auto_shut', False) is True:
        delete_auto_shut = config.find('.//*auto-shut')
        delete_auto_shut.set('operation', 'delete')
        
    lag = ET.SubElement(auto_shut, "lag")
    if kwargs.pop('delete_lag', False) is True:
        delete_lag = config.find('.//*lag')
        delete_lag.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vcs_auto_shut_lag_act(Action):
    def run(self, delete_lag, delete_rbridge_id, rbridge_id, delete_vcs, delete_auto_shut, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vcs_auto_shut_lag(delete_vcs=delete_vcs, username=username, rbridge_id=rbridge_id, delete_auto_shut=delete_auto_shut, host=host, delete_lag=delete_lag, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    