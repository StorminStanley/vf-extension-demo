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


def rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_af_ipv6_uc_and_vrf_cmds_call_point_holder_redistribute_ospf_match_ospf_internal(**kwargs):
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
            
    router = ET.SubElement(rbridge_id, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    router_bgp = ET.SubElement(router, "router-bgp", xmlns="urn:brocade.com:mgmt:brocade-bgp")
    if kwargs.pop('delete_router_bgp', False) is True:
        delete_router_bgp = config.find('.//*router-bgp')
        delete_router_bgp.set('operation', 'delete')
        
    address_family = ET.SubElement(router_bgp, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    ipv6 = ET.SubElement(address_family, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_unicast = ET.SubElement(ipv6, "ipv6-unicast")
    if kwargs.pop('delete_ipv6_unicast', False) is True:
        delete_ipv6_unicast = config.find('.//*ipv6-unicast')
        delete_ipv6_unicast.set('operation', 'delete')
        
    default_vrf = ET.SubElement(ipv6_unicast, "default-vrf")
    if kwargs.pop('delete_default_vrf', False) is True:
        delete_default_vrf = config.find('.//*default-vrf')
        delete_default_vrf.set('operation', 'delete')
        
    af_ipv6_uc_and_vrf_cmds_call_point_holder = ET.SubElement(default_vrf, "af-ipv6-uc-and-vrf-cmds-call-point-holder")
    if kwargs.pop('delete_af_ipv6_uc_and_vrf_cmds_call_point_holder', False) is True:
        delete_af_ipv6_uc_and_vrf_cmds_call_point_holder = config.find('.//*af-ipv6-uc-and-vrf-cmds-call-point-holder')
        delete_af_ipv6_uc_and_vrf_cmds_call_point_holder.set('operation', 'delete')
        
    redistribute = ET.SubElement(af_ipv6_uc_and_vrf_cmds_call_point_holder, "redistribute")
    if kwargs.pop('delete_redistribute', False) is True:
        delete_redistribute = config.find('.//*redistribute')
        delete_redistribute.set('operation', 'delete')
        
    ospf = ET.SubElement(redistribute, "ospf")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    match = ET.SubElement(ospf, "match")
    if kwargs.pop('delete_match', False) is True:
        delete_match = config.find('.//*match')
        delete_match.set('operation', 'delete')
        
    ospf_internal = ET.SubElement(match, "ospf-internal")
    if kwargs.pop('delete_ospf_internal', False) is True:
        delete_ospf_internal = config.find('.//*ospf-internal')
        delete_ospf_internal.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_af_ipv6_uc_and_vrf_cmds_call_point_holder_redistribute_ospf_match_ospf_internal_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, delete_ospf, delete_match, delete_redistribute, delete_default_vrf, delete_ospf_internal, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_af_ipv6_uc_and_vrf_cmds_call_point_holder_redistribute_ospf_match_ospf_internal(delete_router_bgp=delete_router_bgp, username=username, delete_ospf_internal=delete_ospf_internal, rbridge_id=rbridge_id, delete_redistribute=delete_redistribute, delete_router=delete_router, delete_ospf=delete_ospf, host=host, delete_match=delete_match, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, delete_default_vrf=delete_default_vrf, password=password, callback=_callback, mgr=mgr)
        return 0
    