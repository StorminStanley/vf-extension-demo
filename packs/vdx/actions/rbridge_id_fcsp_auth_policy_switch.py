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


def rbridge_id_fcsp_auth_policy_switch(**kwargs):
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
            
    fcsp = ET.SubElement(rbridge_id, "fcsp", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
    if kwargs.pop('delete_fcsp', False) is True:
        delete_fcsp = config.find('.//*fcsp')
        delete_fcsp.set('operation', 'delete')
        
    auth = ET.SubElement(fcsp, "auth")
    if kwargs.pop('delete_auth', False) is True:
        delete_auth = config.find('.//*auth')
        delete_auth.set('operation', 'delete')
        
    policy = ET.SubElement(auth, "policy")
    if kwargs.pop('delete_policy', False) is True:
        delete_policy = config.find('.//*policy')
        delete_policy.set('operation', 'delete')
        
    switch = ET.SubElement(policy, "switch")
    if kwargs.pop('delete_switch', False) is True:
        delete_switch = config.find('.//*switch')
        delete_switch.set('operation', 'delete')
        
    switch.text = kwargs.pop('switch')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fcsp_auth_policy_switch_act(Action):
    def run(self, delete_switch, delete_fcsp, delete_policy, switch, delete_auth, delete_rbridge_id, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fcsp_auth_policy_switch(delete_fcsp=delete_fcsp, username=username, delete_switch=delete_switch, rbridge_id=rbridge_id, switch=switch, delete_policy=delete_policy, host=host, delete_auth=delete_auth, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    