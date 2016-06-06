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


def rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_update_source_ch_update_source_ca_eth_ethernet_interface_ethernet(**kwargs):
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
        
    neighbor_ips = ET.SubElement(neighbor, "neighbor-ips")
    if kwargs.pop('delete_neighbor_ips', False) is True:
        delete_neighbor_ips = config.find('.//*neighbor-ips')
        delete_neighbor_ips.set('operation', 'delete')
        
    neighbor_addr = ET.SubElement(neighbor_ips, "neighbor-addr")
    if kwargs.pop('delete_neighbor_addr', False) is True:
        delete_neighbor_addr = config.find('.//*neighbor-addr')
        delete_neighbor_addr.set('operation', 'delete')
        
    router_bgp_neighbor_address_key = ET.SubElement(neighbor_addr, "router-bgp-neighbor-address")
    router_bgp_neighbor_address_key.text = kwargs.pop('router_bgp_neighbor_address')
    if kwargs.pop('delete_router_bgp_neighbor_address', False) is True:
        delete_router_bgp_neighbor_address = config.find('.//*router-bgp-neighbor-address')
        delete_router_bgp_neighbor_address.set('operation', 'delete')
            
    update_source = ET.SubElement(neighbor_addr, "update-source")
    if kwargs.pop('delete_update_source', False) is True:
        delete_update_source = config.find('.//*update-source')
        delete_update_source.set('operation', 'delete')
        
    ch_update_source = ET.SubElement(update_source, "ch-update-source")
    if kwargs.pop('delete_ch_update_source', False) is True:
        delete_ch_update_source = config.find('.//*ch-update-source')
        delete_ch_update_source.set('operation', 'delete')
        
    ca_eth = ET.SubElement(ch_update_source, "ca-eth")
    if kwargs.pop('delete_ca_eth', False) is True:
        delete_ca_eth = config.find('.//*ca-eth')
        delete_ca_eth.set('operation', 'delete')
        
    ethernet_interface = ET.SubElement(ca_eth, "ethernet-interface")
    if kwargs.pop('delete_ethernet_interface', False) is True:
        delete_ethernet_interface = config.find('.//*ethernet-interface')
        delete_ethernet_interface.set('operation', 'delete')
        
    ethernet = ET.SubElement(ethernet_interface, "ethernet")
    if kwargs.pop('delete_ethernet', False) is True:
        delete_ethernet = config.find('.//*ethernet')
        delete_ethernet.set('operation', 'delete')
        
    ethernet.text = kwargs.pop('ethernet')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_update_source_ch_update_source_ca_eth_ethernet_interface_ethernet_act(Action):
    def run(self, router_bgp_neighbor_address, delete_router_bgp, rbridge_id, delete_neighbor_addr, delete_update_source, delete_router_bgp_neighbor_address, delete_router_bgp_attributes, delete_ethernet, delete_ethernet_interface, delete_neighbor_ips, ethernet, delete_rbridge_id, delete_ch_update_source, delete_ca_eth, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_update_source_ch_update_source_ca_eth_ethernet_interface_ethernet(router_bgp_neighbor_address=router_bgp_neighbor_address, delete_ethernet_interface=delete_ethernet_interface, delete_router_bgp=delete_router_bgp, ethernet=ethernet, username=username, delete_ethernet=delete_ethernet, delete_neighbor_ips=delete_neighbor_ips, rbridge_id=rbridge_id, delete_router=delete_router, password=password, delete_neighbor=delete_neighbor, delete_ca_eth=delete_ca_eth, host=host, delete_router_bgp_attributes=delete_router_bgp_attributes, delete_ch_update_source=delete_ch_update_source, delete_router_bgp_neighbor_address=delete_router_bgp_neighbor_address, delete_rbridge_id=delete_rbridge_id, delete_neighbor_addr=delete_neighbor_addr, delete_update_source=delete_update_source, callback=_callback, mgr=mgr)
        return 0
    