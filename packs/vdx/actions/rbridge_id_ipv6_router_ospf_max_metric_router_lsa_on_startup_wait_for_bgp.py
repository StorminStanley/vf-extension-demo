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


def rbridge_id_ipv6_router_ospf_max_metric_router_lsa_on_startup_wait_for_bgp(**kwargs):
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
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    router = ET.SubElement(ipv6, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    max_metric = ET.SubElement(ospf, "max-metric")
    if kwargs.pop('delete_max_metric', False) is True:
        delete_max_metric = config.find('.//*max-metric')
        delete_max_metric.set('operation', 'delete')
        
    router_lsa = ET.SubElement(max_metric, "router-lsa")
    if kwargs.pop('delete_router_lsa', False) is True:
        delete_router_lsa = config.find('.//*router-lsa')
        delete_router_lsa.set('operation', 'delete')
        
    on_startup = ET.SubElement(router_lsa, "on-startup")
    if kwargs.pop('delete_on_startup', False) is True:
        delete_on_startup = config.find('.//*on-startup')
        delete_on_startup.set('operation', 'delete')
        
    wait_for_bgp = ET.SubElement(on_startup, "wait-for-bgp")
    if kwargs.pop('delete_wait_for_bgp', False) is True:
        delete_wait_for_bgp = config.find('.//*wait-for-bgp')
        delete_wait_for_bgp.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_max_metric_router_lsa_on_startup_wait_for_bgp_act(Action):
    def run(self, delete_on_startup, rbridge_id, delete_ospf, delete_vrf, delete_router_lsa, delete_max_metric, delete_wait_for_bgp, vrf, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_max_metric_router_lsa_on_startup_wait_for_bgp(delete_max_metric=delete_max_metric, delete_router_lsa=delete_router_lsa, username=username, delete_router=delete_router, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_on_startup=delete_on_startup, delete_ospf=delete_ospf, vrf=vrf, host=host, delete_wait_for_bgp=delete_wait_for_bgp, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    