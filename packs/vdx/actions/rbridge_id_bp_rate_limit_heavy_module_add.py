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


def rbridge_id_bp_rate_limit_heavy_module_add(**kwargs):
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
            
    bp_rate_limit = ET.SubElement(rbridge_id, "bp-rate-limit", xmlns="urn:brocade.com:mgmt:brocade-bprate-limit")
    if kwargs.pop('delete_bp_rate_limit', False) is True:
        delete_bp_rate_limit = config.find('.//*bp-rate-limit')
        delete_bp_rate_limit.set('operation', 'delete')
        
    heavy = ET.SubElement(bp_rate_limit, "heavy")
    if kwargs.pop('delete_heavy', False) is True:
        delete_heavy = config.find('.//*heavy')
        delete_heavy.set('operation', 'delete')
        
    module = ET.SubElement(heavy, "module")
    if kwargs.pop('delete_module', False) is True:
        delete_module = config.find('.//*module')
        delete_module.set('operation', 'delete')
        
    add = ET.SubElement(module, "add")
    if kwargs.pop('delete_add', False) is True:
        delete_add = config.find('.//*add')
        delete_add.set('operation', 'delete')
        
    add.text = kwargs.pop('add')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_bp_rate_limit_heavy_module_add_act(Action):
    def run(self, delete_module, rbridge_id, delete_heavy, delete_bp_rate_limit, add, delete_add, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_bp_rate_limit_heavy_module_add(delete_add=delete_add, username=username, rbridge_id=rbridge_id, add=add, delete_bp_rate_limit=delete_bp_rate_limit, delete_module=delete_module, password=password, host=host, delete_rbridge_id=delete_rbridge_id, delete_heavy=delete_heavy, callback=_callback, mgr=mgr)
        return 0
    