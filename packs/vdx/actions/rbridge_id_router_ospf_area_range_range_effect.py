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


def rbridge_id_router_ospf_area_range_range_effect(**kwargs):
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
            
    area = ET.SubElement(ospf, "area")
    if kwargs.pop('delete_area', False) is True:
        delete_area = config.find('.//*area')
        delete_area.set('operation', 'delete')
        
    area_id_key = ET.SubElement(area, "area-id")
    area_id_key.text = kwargs.pop('area_id')
    if kwargs.pop('delete_area_id', False) is True:
        delete_area_id = config.find('.//*area-id')
        delete_area_id.set('operation', 'delete')
            
    range = ET.SubElement(area, "range")
    if kwargs.pop('delete_range', False) is True:
        delete_range = config.find('.//*range')
        delete_range.set('operation', 'delete')
        
    range_address_key = ET.SubElement(range, "range-address")
    range_address_key.text = kwargs.pop('range_address')
    if kwargs.pop('delete_range_address', False) is True:
        delete_range_address = config.find('.//*range-address')
        delete_range_address.set('operation', 'delete')
            
    range_mask_key = ET.SubElement(range, "range-mask")
    range_mask_key.text = kwargs.pop('range_mask')
    if kwargs.pop('delete_range_mask', False) is True:
        delete_range_mask = config.find('.//*range-mask')
        delete_range_mask.set('operation', 'delete')
            
    range_effect = ET.SubElement(range, "range-effect")
    if kwargs.pop('delete_range_effect', False) is True:
        delete_range_effect = config.find('.//*range-effect')
        delete_range_effect.set('operation', 'delete')
        
    range_effect.text = kwargs.pop('range_effect')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_area_range_range_effect_act(Action):
    def run(self, range_mask, area_id, rbridge_id, delete_ospf, delete_vrf, delete_area_id, delete_range_effect, range_effect, delete_range_address, delete_area, vrf, delete_range, delete_rbridge_id, delete_range_mask, delete_router, range_address, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_area_range_range_effect(range_address=range_address, username=username, delete_area=delete_area, delete_range_effect=delete_range_effect, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_range=delete_range, password=password, range_mask=range_mask, delete_router=delete_router, delete_range_mask=delete_range_mask, delete_ospf=delete_ospf, host=host, vrf=vrf, delete_range_address=delete_range_address, range_effect=range_effect, delete_rbridge_id=delete_rbridge_id, area_id=area_id, delete_area_id=delete_area_id, callback=_callback, mgr=mgr)
        return 0
    