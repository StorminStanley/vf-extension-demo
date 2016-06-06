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


def rbridge_id_router_ospf_permit_redistribute_mask(**kwargs):
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
            
    permit = ET.SubElement(ospf, "permit")
    if kwargs.pop('delete_permit', False) is True:
        delete_permit = config.find('.//*permit')
        delete_permit.set('operation', 'delete')
        
    redistribute = ET.SubElement(permit, "redistribute")
    if kwargs.pop('delete_redistribute', False) is True:
        delete_redistribute = config.find('.//*redistribute')
        delete_redistribute.set('operation', 'delete')
        
    redist_value_key = ET.SubElement(redistribute, "redist-value")
    redist_value_key.text = kwargs.pop('redist_value')
    if kwargs.pop('delete_redist_value', False) is True:
        delete_redist_value = config.find('.//*redist-value')
        delete_redist_value.set('operation', 'delete')
            
    route_option_key = ET.SubElement(redistribute, "route-option")
    route_option_key.text = kwargs.pop('route_option')
    if kwargs.pop('delete_route_option', False) is True:
        delete_route_option = config.find('.//*route-option')
        delete_route_option.set('operation', 'delete')
            
    mask = ET.SubElement(redistribute, "mask")
    if kwargs.pop('delete_mask', False) is True:
        delete_mask = config.find('.//*mask')
        delete_mask.set('operation', 'delete')
        
    mask.text = kwargs.pop('mask')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_permit_redistribute_mask_act(Action):
    def run(self, delete_permit, redist_value, rbridge_id, delete_route_option, delete_ospf, delete_vrf, mask, delete_mask, delete_redistribute, delete_redist_value, vrf, delete_rbridge_id, delete_router, route_option, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_permit_redistribute_mask(delete_route_option=delete_route_option, username=username, route_option=route_option, delete_permit=delete_permit, delete_redistribute=delete_redistribute, rbridge_id=rbridge_id, delete_vrf=delete_vrf, mask=mask, vrf=vrf, delete_router=delete_router, delete_ospf=delete_ospf, redist_value=redist_value, delete_redist_value=delete_redist_value, host=host, delete_rbridge_id=delete_rbridge_id, delete_mask=delete_mask, password=password, callback=_callback, mgr=mgr)
        return 0
    