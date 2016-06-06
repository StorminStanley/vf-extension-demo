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


def rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_neighbor_route_map_neighbor_route_map_direction_out_neighbor_route_map_name_direction_out(**kwargs):
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
        
    neighbor = ET.SubElement(default_vrf, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    af_ipv4_neighbor_address_holder = ET.SubElement(neighbor, "af-ipv4-neighbor-address-holder")
    if kwargs.pop('delete_af_ipv4_neighbor_address_holder', False) is True:
        delete_af_ipv4_neighbor_address_holder = config.find('.//*af-ipv4-neighbor-address-holder')
        delete_af_ipv4_neighbor_address_holder.set('operation', 'delete')
        
    af_ipv4_neighbor_address = ET.SubElement(af_ipv4_neighbor_address_holder, "af-ipv4-neighbor-address")
    if kwargs.pop('delete_af_ipv4_neighbor_address', False) is True:
        delete_af_ipv4_neighbor_address = config.find('.//*af-ipv4-neighbor-address')
        delete_af_ipv4_neighbor_address.set('operation', 'delete')
        
    af_ipv4_neighbor_address_key = ET.SubElement(af_ipv4_neighbor_address, "af-ipv4-neighbor-address")
    af_ipv4_neighbor_address_key.text = kwargs.pop('af_ipv4_neighbor_address')
    if kwargs.pop('delete_af_ipv4_neighbor_address', False) is True:
        delete_af_ipv4_neighbor_address = config.find('.//*af-ipv4-neighbor-address')
        delete_af_ipv4_neighbor_address.set('operation', 'delete')
            
    neighbor_route_map = ET.SubElement(af_ipv4_neighbor_address, "neighbor-route-map")
    if kwargs.pop('delete_neighbor_route_map', False) is True:
        delete_neighbor_route_map = config.find('.//*neighbor-route-map')
        delete_neighbor_route_map.set('operation', 'delete')
        
    neighbor_route_map_direction_out = ET.SubElement(neighbor_route_map, "neighbor-route-map-direction-out")
    if kwargs.pop('delete_neighbor_route_map_direction_out', False) is True:
        delete_neighbor_route_map_direction_out = config.find('.//*neighbor-route-map-direction-out')
        delete_neighbor_route_map_direction_out.set('operation', 'delete')
        
    neighbor_route_map_name_direction_out = ET.SubElement(neighbor_route_map_direction_out, "neighbor-route-map-name-direction-out")
    if kwargs.pop('delete_neighbor_route_map_name_direction_out', False) is True:
        delete_neighbor_route_map_name_direction_out = config.find('.//*neighbor-route-map-name-direction-out')
        delete_neighbor_route_map_name_direction_out.set('operation', 'delete')
        
    neighbor_route_map_name_direction_out.text = kwargs.pop('neighbor_route_map_name_direction_out')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_neighbor_route_map_neighbor_route_map_direction_out_neighbor_route_map_name_direction_out_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, neighbor_route_map_name_direction_out, delete_neighbor_route_map_name_direction_out, delete_neighbor_route_map, delete_default_vrf, delete_rbridge_id, delete_neighbor_route_map_direction_out, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_neighbor_route_map_neighbor_route_map_direction_out_neighbor_route_map_name_direction_out(delete_neighbor_route_map_direction_out=delete_neighbor_route_map_direction_out, delete_router_bgp=delete_router_bgp, username=username, delete_neighbor=delete_neighbor, delete_neighbor_route_map_name_direction_out=delete_neighbor_route_map_name_direction_out, rbridge_id=rbridge_id, delete_neighbor_route_map=delete_neighbor_route_map, delete_router=delete_router, host=host, delete_default_vrf=delete_default_vrf, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, neighbor_route_map_name_direction_out=neighbor_route_map_name_direction_out, password=password, callback=_callback, mgr=mgr)
        return 0
    