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


def rbridge_id_vrrp_rbridge_global_vrrp_acceptmode_disable(**kwargs):
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
            
    vrrp_rbridge_global = ET.SubElement(rbridge_id, "vrrp-rbridge-global", xmlns="urn:brocade.com:mgmt:brocade-vrrpv3")
    if kwargs.pop('delete_vrrp_rbridge_global', False) is True:
        delete_vrrp_rbridge_global = config.find('.//*vrrp-rbridge-global')
        delete_vrrp_rbridge_global.set('operation', 'delete')
        
    vrrp_acceptmode_disable = ET.SubElement(vrrp_rbridge_global, "vrrp-acceptmode-disable")
    if kwargs.pop('delete_vrrp_acceptmode_disable', False) is True:
        delete_vrrp_acceptmode_disable = config.find('.//*vrrp-acceptmode-disable')
        delete_vrrp_acceptmode_disable.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrrp_rbridge_global_vrrp_acceptmode_disable_act(Action):
    def run(self, delete_rbridge_id, rbridge_id, delete_vrrp_rbridge_global, delete_vrrp_acceptmode_disable, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrrp_rbridge_global_vrrp_acceptmode_disable(delete_vrrp_acceptmode_disable=delete_vrrp_acceptmode_disable, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vrrp_rbridge_global=delete_vrrp_rbridge_global, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    