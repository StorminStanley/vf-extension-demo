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


def rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ipv6s_neighbor_ipv6_addr_remove_private_as(**kwargs):
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
        
    router_bgp_attributes = ET.SubElement(router_bgp, "router-bgp-attributes")
    if kwargs.pop('delete_router_bgp_attributes', False) is True:
        delete_router_bgp_attributes = config.find('.//*router-bgp-attributes')
        delete_router_bgp_attributes.set('operation', 'delete')
        
    neighbor = ET.SubElement(router_bgp_attributes, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    neighbor_ipv6s = ET.SubElement(neighbor, "neighbor-ipv6s")
    if kwargs.pop('delete_neighbor_ipv6s', False) is True:
        delete_neighbor_ipv6s = config.find('.//*neighbor-ipv6s')
        delete_neighbor_ipv6s.set('operation', 'delete')
        
    neighbor_ipv6_addr = ET.SubElement(neighbor_ipv6s, "neighbor-ipv6-addr")
    if kwargs.pop('delete_neighbor_ipv6_addr', False) is True:
        delete_neighbor_ipv6_addr = config.find('.//*neighbor-ipv6-addr')
        delete_neighbor_ipv6_addr.set('operation', 'delete')
        
    router_bgp_neighbor_ipv6_address_key = ET.SubElement(neighbor_ipv6_addr, "router-bgp-neighbor-ipv6-address")
    router_bgp_neighbor_ipv6_address_key.text = kwargs.pop('router_bgp_neighbor_ipv6_address')
    if kwargs.pop('delete_router_bgp_neighbor_ipv6_address', False) is True:
        delete_router_bgp_neighbor_ipv6_address = config.find('.//*router-bgp-neighbor-ipv6-address')
        delete_router_bgp_neighbor_ipv6_address.set('operation', 'delete')
            
    remove_private_as = ET.SubElement(neighbor_ipv6_addr, "remove-private-as")
    if kwargs.pop('delete_remove_private_as', False) is True:
        delete_remove_private_as = config.find('.//*remove-private-as')
        delete_remove_private_as.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ipv6s_neighbor_ipv6_addr_remove_private_as_act(Action):
    def run(self, delete_router_bgp, rbridge_id, delete_router_bgp_attributes, delete_rbridge_id, delete_remove_private_as, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ipv6s_neighbor_ipv6_addr_remove_private_as(delete_router_bgp=delete_router_bgp, delete_neighbor=delete_neighbor, username=username, rbridge_id=rbridge_id, delete_router=delete_router, delete_remove_private_as=delete_remove_private_as, host=host, delete_router_bgp_attributes=delete_router_bgp_attributes, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    