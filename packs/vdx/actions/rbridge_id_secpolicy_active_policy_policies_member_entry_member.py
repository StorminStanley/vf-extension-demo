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


def rbridge_id_secpolicy_active_policy_policies_member_entry_member(**kwargs):
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
            
    secpolicy = ET.SubElement(rbridge_id, "secpolicy", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
    if kwargs.pop('delete_secpolicy', False) is True:
        delete_secpolicy = config.find('.//*secpolicy')
        delete_secpolicy.set('operation', 'delete')
        
    active_policy = ET.SubElement(secpolicy, "active-policy")
    if kwargs.pop('delete_active_policy', False) is True:
        delete_active_policy = config.find('.//*active-policy')
        delete_active_policy.set('operation', 'delete')
        
    policies = ET.SubElement(active_policy, "policies")
    if kwargs.pop('delete_policies', False) is True:
        delete_policies = config.find('.//*policies')
        delete_policies.set('operation', 'delete')
        
    policy_key = ET.SubElement(policies, "policy")
    policy_key.text = kwargs.pop('policy')
    if kwargs.pop('delete_policy', False) is True:
        delete_policy = config.find('.//*policy')
        delete_policy.set('operation', 'delete')
            
    member_entry = ET.SubElement(policies, "member-entry")
    if kwargs.pop('delete_member_entry', False) is True:
        delete_member_entry = config.find('.//*member-entry')
        delete_member_entry.set('operation', 'delete')
        
    member = ET.SubElement(member_entry, "member")
    if kwargs.pop('delete_member', False) is True:
        delete_member = config.find('.//*member')
        delete_member.set('operation', 'delete')
        
    member.text = kwargs.pop('member')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_secpolicy_active_policy_policies_member_entry_member_act(Action):
    def run(self, rbridge_id, delete_member, delete_policy, member, delete_active_policy, policy, delete_secpolicy, delete_rbridge_id, delete_member_entry, delete_policies, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_secpolicy_active_policy_policies_member_entry_member(delete_member=delete_member, delete_secpolicy=delete_secpolicy, delete_active_policy=delete_active_policy, username=username, rbridge_id=rbridge_id, delete_policies=delete_policies, delete_member_entry=delete_member_entry, member=member, host=host, policy=policy, delete_policy=delete_policy, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    