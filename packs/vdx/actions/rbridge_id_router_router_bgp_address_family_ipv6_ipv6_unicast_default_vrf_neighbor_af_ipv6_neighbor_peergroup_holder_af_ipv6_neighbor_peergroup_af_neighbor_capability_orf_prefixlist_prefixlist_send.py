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


def rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_af_neighbor_capability_orf_prefixlist_prefixlist_send(**kwargs):
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
        
    neighbor = ET.SubElement(default_vrf, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup_holder = ET.SubElement(neighbor, "af-ipv6-neighbor-peergroup-holder")
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup_holder', False) is True:
        delete_af_ipv6_neighbor_peergroup_holder = config.find('.//*af-ipv6-neighbor-peergroup-holder')
        delete_af_ipv6_neighbor_peergroup_holder.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup = ET.SubElement(af_ipv6_neighbor_peergroup_holder, "af-ipv6-neighbor-peergroup")
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup', False) is True:
        delete_af_ipv6_neighbor_peergroup = config.find('.//*af-ipv6-neighbor-peergroup')
        delete_af_ipv6_neighbor_peergroup.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup_name_key = ET.SubElement(af_ipv6_neighbor_peergroup, "af-ipv6-neighbor-peergroup-name")
    af_ipv6_neighbor_peergroup_name_key.text = kwargs.pop('af_ipv6_neighbor_peergroup_name')
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup_name', False) is True:
        delete_af_ipv6_neighbor_peergroup_name = config.find('.//*af-ipv6-neighbor-peergroup-name')
        delete_af_ipv6_neighbor_peergroup_name.set('operation', 'delete')
            
    af_neighbor_capability = ET.SubElement(af_ipv6_neighbor_peergroup, "af-neighbor-capability")
    if kwargs.pop('delete_af_neighbor_capability', False) is True:
        delete_af_neighbor_capability = config.find('.//*af-neighbor-capability')
        delete_af_neighbor_capability.set('operation', 'delete')
        
    orf = ET.SubElement(af_neighbor_capability, "orf")
    if kwargs.pop('delete_orf', False) is True:
        delete_orf = config.find('.//*orf')
        delete_orf.set('operation', 'delete')
        
    prefixlist = ET.SubElement(orf, "prefixlist")
    if kwargs.pop('delete_prefixlist', False) is True:
        delete_prefixlist = config.find('.//*prefixlist')
        delete_prefixlist.set('operation', 'delete')
        
    prefixlist_send = ET.SubElement(prefixlist, "prefixlist-send")
    if kwargs.pop('delete_prefixlist_send', False) is True:
        delete_prefixlist_send = config.find('.//*prefixlist-send')
        delete_prefixlist_send.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_af_neighbor_capability_orf_prefixlist_prefixlist_send_act(Action):
    def run(self, delete_prefixlist, delete_address_family, delete_router_bgp, rbridge_id, delete_prefixlist_send, delete_af_neighbor_capability, delete_orf, delete_default_vrf, delete_rbridge_id, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_af_neighbor_capability_orf_prefixlist_prefixlist_send(delete_router_bgp=delete_router_bgp, delete_prefixlist_send=delete_prefixlist_send, username=username, delete_neighbor=delete_neighbor, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_router=delete_router, delete_af_neighbor_capability=delete_af_neighbor_capability, host=host, delete_prefixlist=delete_prefixlist, delete_address_family=delete_address_family, delete_default_vrf=delete_default_vrf, delete_orf=delete_orf, password=password, callback=_callback, mgr=mgr)
        return 0
    