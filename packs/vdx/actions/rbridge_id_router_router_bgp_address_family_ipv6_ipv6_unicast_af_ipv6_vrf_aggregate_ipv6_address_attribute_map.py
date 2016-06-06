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


def rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_aggregate_ipv6_address_attribute_map(**kwargs):
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
        
    af_ipv6_vrf = ET.SubElement(ipv6_unicast, "af-ipv6-vrf")
    if kwargs.pop('delete_af_ipv6_vrf', False) is True:
        delete_af_ipv6_vrf = config.find('.//*af-ipv6-vrf')
        delete_af_ipv6_vrf.set('operation', 'delete')
        
    af_ipv6_vrf_name_key = ET.SubElement(af_ipv6_vrf, "af-ipv6-vrf-name")
    af_ipv6_vrf_name_key.text = kwargs.pop('af_ipv6_vrf_name')
    if kwargs.pop('delete_af_ipv6_vrf_name', False) is True:
        delete_af_ipv6_vrf_name = config.find('.//*af-ipv6-vrf-name')
        delete_af_ipv6_vrf_name.set('operation', 'delete')
            
    aggregate_ipv6_address = ET.SubElement(af_ipv6_vrf, "aggregate-ipv6-address")
    if kwargs.pop('delete_aggregate_ipv6_address', False) is True:
        delete_aggregate_ipv6_address = config.find('.//*aggregate-ipv6-address')
        delete_aggregate_ipv6_address.set('operation', 'delete')
        
    aggregate_ip_prefix_key = ET.SubElement(aggregate_ipv6_address, "aggregate-ip-prefix")
    aggregate_ip_prefix_key.text = kwargs.pop('aggregate_ip_prefix')
    if kwargs.pop('delete_aggregate_ip_prefix', False) is True:
        delete_aggregate_ip_prefix = config.find('.//*aggregate-ip-prefix')
        delete_aggregate_ip_prefix.set('operation', 'delete')
            
    attribute_map = ET.SubElement(aggregate_ipv6_address, "attribute-map")
    if kwargs.pop('delete_attribute_map', False) is True:
        delete_attribute_map = config.find('.//*attribute-map')
        delete_attribute_map.set('operation', 'delete')
        
    attribute_map.text = kwargs.pop('attribute_map')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_aggregate_ipv6_address_attribute_map_act(Action):
    def run(self, delete_address_family, delete_attribute_map, delete_router_bgp, aggregate_ip_prefix, attribute_map, delete_aggregate_ip_prefix, delete_rbridge_id, delete_router, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_aggregate_ipv6_address_attribute_map(aggregate_ip_prefix=aggregate_ip_prefix, delete_router_bgp=delete_router_bgp, username=username, delete_router=delete_router, rbridge_id=rbridge_id, attribute_map=attribute_map, host=host, delete_attribute_map=delete_attribute_map, delete_aggregate_ip_prefix=delete_aggregate_ip_prefix, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    