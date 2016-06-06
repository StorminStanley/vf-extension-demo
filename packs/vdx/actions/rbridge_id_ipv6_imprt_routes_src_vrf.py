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


def rbridge_id_ipv6_imprt_routes_src_vrf(**kwargs):
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
        
    imprt = ET.SubElement(ipv6, "import", xmlns="urn:brocade.com:mgmt:brocade-ipv6-rtm")
    if kwargs.pop('delete_imprt', False) is True:
        delete_imprt = config.find('.//*import')
        delete_imprt.set('operation', 'delete')
        
    routes = ET.SubElement(imprt, "routes")
    if kwargs.pop('delete_routes', False) is True:
        delete_routes = config.find('.//*routes')
        delete_routes.set('operation', 'delete')
        
    route_map_key = ET.SubElement(routes, "route-map")
    route_map_key.text = kwargs.pop('route_map')
    if kwargs.pop('delete_route_map', False) is True:
        delete_route_map = config.find('.//*route-map')
        delete_route_map.set('operation', 'delete')
            
    src_vrf = ET.SubElement(routes, "src-vrf")
    if kwargs.pop('delete_src_vrf', False) is True:
        delete_src_vrf = config.find('.//*src-vrf')
        delete_src_vrf.set('operation', 'delete')
        
    src_vrf.text = kwargs.pop('src_vrf')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_imprt_routes_src_vrf_act(Action):
    def run(self, delete_src_vrf, rbridge_id, route_map, delete_route_map, src_vrf, delete_imprt, delete_rbridge_id, delete_routes, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_imprt_routes_src_vrf(src_vrf=src_vrf, delete_routes=delete_routes, delete_src_vrf=delete_src_vrf, username=username, rbridge_id=rbridge_id, delete_imprt=delete_imprt, delete_route_map=delete_route_map, route_map=route_map, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    