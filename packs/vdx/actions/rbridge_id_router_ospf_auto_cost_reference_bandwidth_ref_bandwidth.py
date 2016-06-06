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


def rbridge_id_router_ospf_auto_cost_reference_bandwidth_ref_bandwidth(**kwargs):
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
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    auto_cost = ET.SubElement(ospf, "auto-cost")
    if kwargs.pop('delete_auto_cost', False) is True:
        delete_auto_cost = config.find('.//*auto-cost')
        delete_auto_cost.set('operation', 'delete')
        
    reference_bandwidth = ET.SubElement(auto_cost, "reference-bandwidth")
    if kwargs.pop('delete_reference_bandwidth', False) is True:
        delete_reference_bandwidth = config.find('.//*reference-bandwidth')
        delete_reference_bandwidth.set('operation', 'delete')
        
    ref_bandwidth = ET.SubElement(reference_bandwidth, "ref-bandwidth")
    if kwargs.pop('delete_ref_bandwidth', False) is True:
        delete_ref_bandwidth = config.find('.//*ref-bandwidth')
        delete_ref_bandwidth.set('operation', 'delete')
        
    ref_bandwidth.text = kwargs.pop('ref_bandwidth')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_auto_cost_reference_bandwidth_ref_bandwidth_act(Action):
    def run(self, ref_bandwidth, rbridge_id, delete_ospf, delete_vrf, delete_auto_cost, delete_reference_bandwidth, vrf, delete_rbridge_id, delete_ref_bandwidth, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_auto_cost_reference_bandwidth_ref_bandwidth(ref_bandwidth=ref_bandwidth, delete_reference_bandwidth=delete_reference_bandwidth, username=username, delete_router=delete_router, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_ospf=delete_ospf, password=password, vrf=vrf, host=host, delete_ref_bandwidth=delete_ref_bandwidth, delete_rbridge_id=delete_rbridge_id, delete_auto_cost=delete_auto_cost, callback=_callback, mgr=mgr)
        return 0
    