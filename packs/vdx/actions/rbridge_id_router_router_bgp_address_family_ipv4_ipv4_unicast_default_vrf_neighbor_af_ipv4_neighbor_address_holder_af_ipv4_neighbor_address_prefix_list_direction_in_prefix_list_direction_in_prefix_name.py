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


def rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_prefix_list_direction_in_prefix_list_direction_in_prefix_name(**kwargs):
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
            
    prefix_list = ET.SubElement(af_ipv4_neighbor_address, "prefix-list")
    if kwargs.pop('delete_prefix_list', False) is True:
        delete_prefix_list = config.find('.//*prefix-list')
        delete_prefix_list.set('operation', 'delete')
        
    direction_in = ET.SubElement(prefix_list, "direction-in")
    if kwargs.pop('delete_direction_in', False) is True:
        delete_direction_in = config.find('.//*direction-in')
        delete_direction_in.set('operation', 'delete')
        
    prefix_list_direction_in_prefix_name = ET.SubElement(direction_in, "prefix-list-direction-in-prefix-name")
    if kwargs.pop('delete_prefix_list_direction_in_prefix_name', False) is True:
        delete_prefix_list_direction_in_prefix_name = config.find('.//*prefix-list-direction-in-prefix-name')
        delete_prefix_list_direction_in_prefix_name.set('operation', 'delete')
        
    prefix_list_direction_in_prefix_name.text = kwargs.pop('prefix_list_direction_in_prefix_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_prefix_list_direction_in_prefix_list_direction_in_prefix_name_act(Action):
    def run(self, delete_direction_in, delete_address_family, delete_router_bgp, rbridge_id, prefix_list_direction_in_prefix_name, delete_prefix_list_direction_in_prefix_name, delete_default_vrf, delete_prefix_list, delete_rbridge_id, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_neighbor_af_ipv4_neighbor_address_holder_af_ipv4_neighbor_address_prefix_list_direction_in_prefix_list_direction_in_prefix_name(prefix_list_direction_in_prefix_name=prefix_list_direction_in_prefix_name, delete_prefix_list=delete_prefix_list, delete_router_bgp=delete_router_bgp, username=username, delete_direction_in=delete_direction_in, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_router=delete_router, delete_neighbor=delete_neighbor, host=host, password=password, delete_address_family=delete_address_family, delete_default_vrf=delete_default_vrf, delete_prefix_list_direction_in_prefix_name=delete_prefix_list_direction_in_prefix_name, callback=_callback, mgr=mgr)
        return 0
    