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


def rbridge_id_maps_policy_ruleaction_policyaction(**kwargs):
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
            
    maps = ET.SubElement(rbridge_id, "maps", xmlns="urn:brocade.com:mgmt:brocade-maps")
    if kwargs.pop('delete_maps', False) is True:
        delete_maps = config.find('.//*maps')
        delete_maps.set('operation', 'delete')
        
    policy = ET.SubElement(maps, "policy")
    if kwargs.pop('delete_policy', False) is True:
        delete_policy = config.find('.//*policy')
        delete_policy.set('operation', 'delete')
        
    policyname_key = ET.SubElement(policy, "policyname")
    policyname_key.text = kwargs.pop('policyname')
    if kwargs.pop('delete_policyname', False) is True:
        delete_policyname = config.find('.//*policyname')
        delete_policyname.set('operation', 'delete')
            
    ruleaction = ET.SubElement(policy, "ruleaction")
    if kwargs.pop('delete_ruleaction', False) is True:
        delete_ruleaction = config.find('.//*ruleaction')
        delete_ruleaction.set('operation', 'delete')
        
    policyrule_key = ET.SubElement(ruleaction, "policyrule")
    policyrule_key.text = kwargs.pop('policyrule')
    if kwargs.pop('delete_policyrule', False) is True:
        delete_policyrule = config.find('.//*policyrule')
        delete_policyrule.set('operation', 'delete')
            
    policyaction = ET.SubElement(ruleaction, "policyaction")
    if kwargs.pop('delete_policyaction', False) is True:
        delete_policyaction = config.find('.//*policyaction')
        delete_policyaction.set('operation', 'delete')
        
    policyaction.text = kwargs.pop('policyaction')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_maps_policy_ruleaction_policyaction_act(Action):
    def run(self, policyname, policyaction, rbridge_id, delete_policyname, delete_ruleaction, delete_maps, policyrule, delete_policy, delete_policyrule, delete_policyaction, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_maps_policy_ruleaction_policyaction(policyrule=policyrule, username=username, delete_policyname=delete_policyname, policyname=policyname, delete_maps=delete_maps, delete_policyaction=delete_policyaction, delete_policy=delete_policy, host=host, policyaction=policyaction, delete_policyrule=delete_policyrule, delete_rbridge_id=delete_rbridge_id, delete_ruleaction=delete_ruleaction, rbridge_id=rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    