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


def rbridge_id_protocol_hide_vrrp_holder_vrrp(**kwargs):
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
            
    protocol = ET.SubElement(rbridge_id, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    hide_vrrp_holder = ET.SubElement(protocol, "hide-vrrp-holder", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_hide_vrrp_holder', False) is True:
        delete_hide_vrrp_holder = config.find('.//*hide-vrrp-holder')
        delete_hide_vrrp_holder.set('operation', 'delete')
        
    vrrp = ET.SubElement(hide_vrrp_holder, "vrrp")
    if kwargs.pop('delete_vrrp', False) is True:
        delete_vrrp = config.find('.//*vrrp')
        delete_vrrp.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_protocol_hide_vrrp_holder_vrrp_act(Action):
    def run(self, delete_hide_vrrp_holder, delete_rbridge_id, delete_vrrp, rbridge_id, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_protocol_hide_vrrp_holder_vrrp(delete_vrrp=delete_vrrp, username=username, rbridge_id=rbridge_id, delete_hide_vrrp_holder=delete_hide_vrrp_holder, delete_protocol=delete_protocol, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    