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


def rbridge_id_router_ospf_distance_dist_value(**kwargs):
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
            
    distance = ET.SubElement(ospf, "distance")
    if kwargs.pop('delete_distance', False) is True:
        delete_distance = config.find('.//*distance')
        delete_distance.set('operation', 'delete')
        
    route_type_key = ET.SubElement(distance, "route-type")
    route_type_key.text = kwargs.pop('route_type')
    if kwargs.pop('delete_route_type', False) is True:
        delete_route_type = config.find('.//*route-type')
        delete_route_type.set('operation', 'delete')
            
    dist_value = ET.SubElement(distance, "dist-value")
    if kwargs.pop('delete_dist_value', False) is True:
        delete_dist_value = config.find('.//*dist-value')
        delete_dist_value.set('operation', 'delete')
        
    dist_value.text = kwargs.pop('dist_value')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_distance_dist_value_act(Action):
    def run(self, delete_distance, rbridge_id, delete_ospf, delete_vrf, delete_route_type, route_type, delete_dist_value, vrf, delete_rbridge_id, dist_value, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_distance_dist_value(delete_route_type=delete_route_type, route_type=route_type, dist_value=dist_value, username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_router=delete_router, delete_ospf=delete_ospf, host=host, vrf=vrf, delete_dist_value=delete_dist_value, delete_distance=delete_distance, password=password, callback=_callback, mgr=mgr)
        return 0
    