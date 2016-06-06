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


def rbridge_id_vrf_address_family_ip_unicast_ip_imprt_routes_route_map(**kwargs):
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
            
    vrf = ET.SubElement(rbridge_id, "vrf", xmlns="urn:brocade.com:mgmt:brocade-vrf")
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
        
    vrf_name_key = ET.SubElement(vrf, "vrf-name")
    vrf_name_key.text = kwargs.pop('vrf_name')
    if kwargs.pop('delete_vrf_name', False) is True:
        delete_vrf_name = config.find('.//*vrf-name')
        delete_vrf_name.set('operation', 'delete')
            
    address_family = ET.SubElement(vrf, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    ip = ET.SubElement(address_family, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    unicast = ET.SubElement(ip, "unicast")
    if kwargs.pop('delete_unicast', False) is True:
        delete_unicast = config.find('.//*unicast')
        delete_unicast.set('operation', 'delete')
        
    ip = ET.SubElement(unicast, "ip", xmlns="urn:brocade.com:mgmt:brocade-rtm")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    imprt = ET.SubElement(ip, "import")
    if kwargs.pop('delete_imprt', False) is True:
        delete_imprt = config.find('.//*import')
        delete_imprt.set('operation', 'delete')
        
    routes = ET.SubElement(imprt, "routes")
    if kwargs.pop('delete_routes', False) is True:
        delete_routes = config.find('.//*routes')
        delete_routes.set('operation', 'delete')
        
    src_vrf_key = ET.SubElement(routes, "src-vrf")
    src_vrf_key.text = kwargs.pop('src_vrf')
    if kwargs.pop('delete_src_vrf', False) is True:
        delete_src_vrf = config.find('.//*src-vrf')
        delete_src_vrf.set('operation', 'delete')
            
    route_map = ET.SubElement(routes, "route-map")
    if kwargs.pop('delete_route_map', False) is True:
        delete_route_map = config.find('.//*route-map')
        delete_route_map.set('operation', 'delete')
        
    route_map.text = kwargs.pop('route_map')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrf_address_family_ip_unicast_ip_imprt_routes_route_map_act(Action):
    def run(self, delete_address_family, delete_src_vrf, rbridge_id, delete_ip, delete_vrf, route_map, delete_route_map, src_vrf, vrf_name, delete_routes, delete_imprt, delete_rbridge_id, delete_unicast, delete_vrf_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrf_address_family_ip_unicast_ip_imprt_routes_route_map(src_vrf=src_vrf, delete_routes=delete_routes, delete_src_vrf=delete_src_vrf, delete_address_family=delete_address_family, delete_imprt=delete_imprt, vrf_name=vrf_name, username=username, delete_vrf=delete_vrf, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_route_map=delete_route_map, route_map=route_map, delete_vrf_name=delete_vrf_name, host=host, delete_unicast=delete_unicast, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    