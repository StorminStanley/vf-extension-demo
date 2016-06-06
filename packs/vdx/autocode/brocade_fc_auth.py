#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fc_auth(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcsp_sa_fcsp_auth_proto_auth_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_fcsp_sa', False) is True:
            delete_fcsp_sa = config.find('.//*fcsp-sa')
            delete_fcsp_sa.set('operation', 'delete')
            
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        if kwargs.pop('delete_fcsp', False) is True:
            delete_fcsp = config.find('.//*fcsp')
            delete_fcsp.set('operation', 'delete')
            
        auth = ET.SubElement(fcsp, "auth")
        if kwargs.pop('delete_auth', False) is True:
            delete_auth = config.find('.//*auth')
            delete_auth.set('operation', 'delete')
            
        proto = ET.SubElement(auth, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        auth_type = ET.SubElement(proto, "auth-type")
        if kwargs.pop('delete_auth_type', False) is True:
            delete_auth_type = config.find('.//*auth-type')
            delete_auth_type.set('operation', 'delete')
            
        auth_type.text = kwargs.pop('auth_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_fcsp_sa', False) is True:
            delete_fcsp_sa = config.find('.//*fcsp-sa')
            delete_fcsp_sa.set('operation', 'delete')
            
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        if kwargs.pop('delete_fcsp', False) is True:
            delete_fcsp = config.find('.//*fcsp')
            delete_fcsp.set('operation', 'delete')
            
        auth = ET.SubElement(fcsp, "auth")
        if kwargs.pop('delete_auth', False) is True:
            delete_auth = config.find('.//*auth')
            delete_auth.set('operation', 'delete')
            
        proto = ET.SubElement(auth, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        group = ET.SubElement(proto, "group")
        if kwargs.pop('delete_group', False) is True:
            delete_group = config.find('.//*group')
            delete_group.set('operation', 'delete')
            
        group.text = kwargs.pop('group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_hash(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_fcsp_sa', False) is True:
            delete_fcsp_sa = config.find('.//*fcsp-sa')
            delete_fcsp_sa.set('operation', 'delete')
            
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        if kwargs.pop('delete_fcsp', False) is True:
            delete_fcsp = config.find('.//*fcsp')
            delete_fcsp.set('operation', 'delete')
            
        auth = ET.SubElement(fcsp, "auth")
        if kwargs.pop('delete_auth', False) is True:
            delete_auth = config.find('.//*auth')
            delete_auth.set('operation', 'delete')
            
        proto = ET.SubElement(auth, "proto")
        if kwargs.pop('delete_proto', False) is True:
            delete_proto = config.find('.//*proto')
            delete_proto.set('operation', 'delete')
            
        hash = ET.SubElement(proto, "hash")
        if kwargs.pop('delete_hash', False) is True:
            delete_hash = config.find('.//*hash')
            delete_hash.set('operation', 'delete')
            
        hash.text = kwargs.pop('hash')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_policy_switch(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_fcsp_sa', False) is True:
            delete_fcsp_sa = config.find('.//*fcsp-sa')
            delete_fcsp_sa.set('operation', 'delete')
            
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
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

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_secpolicy_sa', False) is True:
            delete_secpolicy_sa = config.find('.//*secpolicy-sa')
            delete_secpolicy_sa.set('operation', 'delete')
            
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        if kwargs.pop('delete_secpolicy', False) is True:
            delete_secpolicy = config.find('.//*secpolicy')
            delete_secpolicy.set('operation', 'delete')
            
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        if kwargs.pop('delete_defined_policy', False) is True:
            delete_defined_policy = config.find('.//*defined-policy')
            delete_defined_policy.set('operation', 'delete')
            
        policies = ET.SubElement(defined_policy, "policies")
        if kwargs.pop('delete_policies', False) is True:
            delete_policies = config.find('.//*policies')
            delete_policies.set('operation', 'delete')
            
        policy = ET.SubElement(policies, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_secpolicy_sa', False) is True:
            delete_secpolicy_sa = config.find('.//*secpolicy-sa')
            delete_secpolicy_sa.set('operation', 'delete')
            
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        if kwargs.pop('delete_secpolicy', False) is True:
            delete_secpolicy = config.find('.//*secpolicy')
            delete_secpolicy.set('operation', 'delete')
            
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        if kwargs.pop('delete_defined_policy', False) is True:
            delete_defined_policy = config.find('.//*defined-policy')
            delete_defined_policy.set('operation', 'delete')
            
        policies = ET.SubElement(defined_policy, "policies")
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

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_secpolicy_sa', False) is True:
            delete_secpolicy_sa = config.find('.//*secpolicy-sa')
            delete_secpolicy_sa.set('operation', 'delete')
            
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
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
            
        policy = ET.SubElement(policies, "policy")
        if kwargs.pop('delete_policy', False) is True:
            delete_policy = config.find('.//*policy')
            delete_policy.set('operation', 'delete')
            
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        if kwargs.pop('delete_secpolicy_sa', False) is True:
            delete_secpolicy_sa = config.find('.//*secpolicy-sa')
            delete_secpolicy_sa.set('operation', 'delete')
            
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
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

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        