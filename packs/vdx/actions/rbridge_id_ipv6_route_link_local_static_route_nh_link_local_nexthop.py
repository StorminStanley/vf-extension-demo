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


def rbridge_id_ipv6_route_link_local_static_route_nh_link_local_nexthop(**kwargs):
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
        
    route = ET.SubElement(ipv6, "route", xmlns="urn:brocade.com:mgmt:brocade-ipv6-rtm")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    link_local_static_route_nh = ET.SubElement(route, "link-local-static-route-nh")
    if kwargs.pop('delete_link_local_static_route_nh', False) is True:
        delete_link_local_static_route_nh = config.find('.//*link-local-static-route-nh')
        delete_link_local_static_route_nh.set('operation', 'delete')
        
    link_local_static_route_dest_key = ET.SubElement(link_local_static_route_nh, "link-local-static-route-dest")
    link_local_static_route_dest_key.text = kwargs.pop('link_local_static_route_dest')
    if kwargs.pop('delete_link_local_static_route_dest', False) is True:
        delete_link_local_static_route_dest = config.find('.//*link-local-static-route-dest')
        delete_link_local_static_route_dest.set('operation', 'delete')
            
    link_local_route_oif_type_key = ET.SubElement(link_local_static_route_nh, "link-local-route-oif-type")
    link_local_route_oif_type_key.text = kwargs.pop('link_local_route_oif_type')
    if kwargs.pop('delete_link_local_route_oif_type', False) is True:
        delete_link_local_route_oif_type = config.find('.//*link-local-route-oif-type')
        delete_link_local_route_oif_type.set('operation', 'delete')
            
    link_local_route_oif_name_key = ET.SubElement(link_local_static_route_nh, "link-local-route-oif-name")
    link_local_route_oif_name_key.text = kwargs.pop('link_local_route_oif_name')
    if kwargs.pop('delete_link_local_route_oif_name', False) is True:
        delete_link_local_route_oif_name = config.find('.//*link-local-route-oif-name')
        delete_link_local_route_oif_name.set('operation', 'delete')
            
    link_local_nexthop = ET.SubElement(link_local_static_route_nh, "link-local-nexthop")
    if kwargs.pop('delete_link_local_nexthop', False) is True:
        delete_link_local_nexthop = config.find('.//*link-local-nexthop')
        delete_link_local_nexthop.set('operation', 'delete')
        
    link_local_nexthop.text = kwargs.pop('link_local_nexthop')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_route_link_local_static_route_nh_link_local_nexthop_act(Action):
    def run(self, delete_link_local_static_route_nh, link_local_route_oif_name, rbridge_id, delete_route, delete_link_local_static_route_dest, link_local_nexthop, delete_link_local_route_oif_type, delete_link_local_route_oif_name, delete_link_local_nexthop, delete_rbridge_id, link_local_static_route_dest, link_local_route_oif_type, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_route_link_local_static_route_nh_link_local_nexthop(delete_link_local_route_oif_type=delete_link_local_route_oif_type, delete_link_local_nexthop=delete_link_local_nexthop, delete_route=delete_route, link_local_route_oif_type=link_local_route_oif_type, username=username, rbridge_id=rbridge_id, delete_link_local_route_oif_name=delete_link_local_route_oif_name, delete_link_local_static_route_dest=delete_link_local_static_route_dest, host=host, link_local_static_route_dest=link_local_static_route_dest, delete_link_local_static_route_nh=delete_link_local_static_route_nh, link_local_route_oif_name=link_local_route_oif_name, delete_rbridge_id=delete_rbridge_id, link_local_nexthop=link_local_nexthop, password=password, callback=_callback, mgr=mgr)
        return 0
    