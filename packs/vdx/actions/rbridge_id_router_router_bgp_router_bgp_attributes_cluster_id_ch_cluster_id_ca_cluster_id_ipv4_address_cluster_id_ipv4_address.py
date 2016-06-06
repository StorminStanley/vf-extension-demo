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


def rbridge_id_router_router_bgp_router_bgp_attributes_cluster_id_ch_cluster_id_ca_cluster_id_ipv4_address_cluster_id_ipv4_address(**kwargs):
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
        
    cluster_id = ET.SubElement(router_bgp_attributes, "cluster-id")
    if kwargs.pop('delete_cluster_id', False) is True:
        delete_cluster_id = config.find('.//*cluster-id')
        delete_cluster_id.set('operation', 'delete')
        
    ch_cluster_id = ET.SubElement(cluster_id, "ch-cluster-id")
    if kwargs.pop('delete_ch_cluster_id', False) is True:
        delete_ch_cluster_id = config.find('.//*ch-cluster-id')
        delete_ch_cluster_id.set('operation', 'delete')
        
    ca_cluster_id_ipv4_address = ET.SubElement(ch_cluster_id, "ca-cluster-id-ipv4-address")
    if kwargs.pop('delete_ca_cluster_id_ipv4_address', False) is True:
        delete_ca_cluster_id_ipv4_address = config.find('.//*ca-cluster-id-ipv4-address')
        delete_ca_cluster_id_ipv4_address.set('operation', 'delete')
        
    cluster_id_ipv4_address = ET.SubElement(ca_cluster_id_ipv4_address, "cluster-id-ipv4-address")
    if kwargs.pop('delete_cluster_id_ipv4_address', False) is True:
        delete_cluster_id_ipv4_address = config.find('.//*cluster-id-ipv4-address')
        delete_cluster_id_ipv4_address.set('operation', 'delete')
        
    cluster_id_ipv4_address.text = kwargs.pop('cluster_id_ipv4_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_router_bgp_attributes_cluster_id_ch_cluster_id_ca_cluster_id_ipv4_address_cluster_id_ipv4_address_act(Action):
    def run(self, delete_cluster_id, delete_router_bgp, rbridge_id, delete_ch_cluster_id, delete_router_bgp_attributes, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_router_bgp_attributes_cluster_id_ch_cluster_id_ca_cluster_id_ipv4_address_cluster_id_ipv4_address(delete_cluster_id=delete_cluster_id, delete_ch_cluster_id=delete_ch_cluster_id, username=username, rbridge_id=rbridge_id, delete_router=delete_router, host=host, delete_router_bgp_attributes=delete_router_bgp_attributes, delete_router_bgp=delete_router_bgp, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    