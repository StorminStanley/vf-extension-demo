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


def rbridge_id_router_ospf_area_prefix_list_direction_in_prefix_list_direction_in(**kwargs):
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
            
    prefix_list = ET.SubElement(area, "prefix-list")
    if kwargs.pop('delete_prefix_list', False) is True:
        delete_prefix_list = config.find('.//*prefix-list')
        delete_prefix_list.set('operation', 'delete')
        
    direction_in = ET.SubElement(prefix_list, "direction-in")
    if kwargs.pop('delete_direction_in', False) is True:
        delete_direction_in = config.find('.//*direction-in')
        delete_direction_in.set('operation', 'delete')
        
    prefix_list_direction_in = ET.SubElement(direction_in, "prefix-list-direction-in")
    if kwargs.pop('delete_prefix_list_direction_in', False) is True:
        delete_prefix_list_direction_in = config.find('.//*prefix-list-direction-in')
        delete_prefix_list_direction_in.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_area_prefix_list_direction_in_prefix_list_direction_in_act(Action):
    def run(self, delete_direction_in, area_id, rbridge_id, delete_ospf, delete_vrf, delete_prefix_list_direction_in, delete_area_id, delete_area, vrf, delete_prefix_list, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_area_prefix_list_direction_in_prefix_list_direction_in(delete_prefix_list=delete_prefix_list, username=username, delete_direction_in=delete_direction_in, delete_vrf=delete_vrf, rbridge_id=rbridge_id, delete_prefix_list_direction_in=delete_prefix_list_direction_in, delete_area=delete_area, delete_router=delete_router, delete_ospf=delete_ospf, password=password, vrf=vrf, host=host, delete_rbridge_id=delete_rbridge_id, area_id=area_id, delete_area_id=delete_area_id, callback=_callback, mgr=mgr)
        return 0
    