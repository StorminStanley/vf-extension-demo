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


def rbridge_id_fabric_login_policy_duplicateWWN_precedence(**kwargs):
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
            
    fabric = ET.SubElement(rbridge_id, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
    if kwargs.pop('delete_fabric', False) is True:
        delete_fabric = config.find('.//*fabric')
        delete_fabric.set('operation', 'delete')
        
    login_policy = ET.SubElement(fabric, "login-policy")
    if kwargs.pop('delete_login_policy', False) is True:
        delete_login_policy = config.find('.//*login-policy')
        delete_login_policy.set('operation', 'delete')
        
    duplicateWWN = ET.SubElement(login_policy, "duplicateWWN")
    if kwargs.pop('delete_duplicateWWN', False) is True:
        delete_duplicateWWN = config.find('.//*duplicateWWN')
        delete_duplicateWWN.set('operation', 'delete')
        
    precedence = ET.SubElement(duplicateWWN, "precedence")
    if kwargs.pop('delete_precedence', False) is True:
        delete_precedence = config.find('.//*precedence')
        delete_precedence.set('operation', 'delete')
        
    precedence.text = kwargs.pop('precedence')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fabric_login_policy_duplicateWWN_precedence_act(Action):
    def run(self, delete_precedence, rbridge_id, delete_duplicateWWN, delete_login_policy, precedence, delete_fabric, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fabric_login_policy_duplicateWWN_precedence(delete_duplicateWWN=delete_duplicateWWN, delete_fabric=delete_fabric, username=username, rbridge_id=rbridge_id, delete_login_policy=delete_login_policy, delete_precedence=delete_precedence, precedence=precedence, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    