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


def rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_ipv4_uc_and_vrf_cmds_call_point_holder_redistribute_bgp_bgp_route_map(**kwargs):
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
        
    ipv4 = ET.SubElement(address_family, "ipv4")
    if kwargs.pop('delete_ipv4', False) is True:
        delete_ipv4 = config.find('.//*ipv4')
        delete_ipv4.set('operation', 'delete')
        
    ipv4_unicast = ET.SubElement(ipv4, "ipv4-unicast")
    if kwargs.pop('delete_ipv4_unicast', False) is True:
        delete_ipv4_unicast = config.find('.//*ipv4-unicast')
        delete_ipv4_unicast.set('operation', 'delete')
        
    default_vrf = ET.SubElement(ipv4_unicast, "default-vrf")
    if kwargs.pop('delete_default_vrf', False) is True:
        delete_default_vrf = config.find('.//*default-vrf')
        delete_default_vrf.set('operation', 'delete')
        
    af_ipv4_uc_and_vrf_cmds_call_point_holder = ET.SubElement(default_vrf, "af-ipv4-uc-and-vrf-cmds-call-point-holder")
    if kwargs.pop('delete_af_ipv4_uc_and_vrf_cmds_call_point_holder', False) is True:
        delete_af_ipv4_uc_and_vrf_cmds_call_point_holder = config.find('.//*af-ipv4-uc-and-vrf-cmds-call-point-holder')
        delete_af_ipv4_uc_and_vrf_cmds_call_point_holder.set('operation', 'delete')
        
    redistribute = ET.SubElement(af_ipv4_uc_and_vrf_cmds_call_point_holder, "redistribute")
    if kwargs.pop('delete_redistribute', False) is True:
        delete_redistribute = config.find('.//*redistribute')
        delete_redistribute.set('operation', 'delete')
        
    bgp = ET.SubElement(redistribute, "bgp")
    if kwargs.pop('delete_bgp', False) is True:
        delete_bgp = config.find('.//*bgp')
        delete_bgp.set('operation', 'delete')
        
    bgp_route_map = ET.SubElement(bgp, "bgp-route-map")
    if kwargs.pop('delete_bgp_route_map', False) is True:
        delete_bgp_route_map = config.find('.//*bgp-route-map')
        delete_bgp_route_map.set('operation', 'delete')
        
    bgp_route_map.text = kwargs.pop('bgp_route_map')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_ipv4_uc_and_vrf_cmds_call_point_holder_redistribute_bgp_bgp_route_map_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, delete_bgp, delete_redistribute, bgp_route_map, delete_bgp_route_map, delete_default_vrf, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_ipv4_uc_and_vrf_cmds_call_point_holder_redistribute_bgp_bgp_route_map(delete_router_bgp=delete_router_bgp, username=username, delete_default_vrf=delete_default_vrf, rbridge_id=rbridge_id, delete_redistribute=delete_redistribute, delete_router=delete_router, delete_bgp_route_map=delete_bgp_route_map, host=host, delete_address_family=delete_address_family, delete_bgp=delete_bgp, delete_rbridge_id=delete_rbridge_id, bgp_route_map=bgp_route_map, password=password, callback=_callback, mgr=mgr)
        return 0
    