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


def rbridge_id_ip_rtm_config_route_static_route_oif_vrf_static_route_next_vrf_dest(**kwargs):
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
            
    ip = ET.SubElement(rbridge_id, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
    if kwargs.pop('delete_rtm_config', False) is True:
        delete_rtm_config = config.find('.//*rtm-config')
        delete_rtm_config.set('operation', 'delete')
        
    route = ET.SubElement(rtm_config, "route")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    static_route_oif_vrf = ET.SubElement(route, "static-route-oif-vrf")
    if kwargs.pop('delete_static_route_oif_vrf', False) is True:
        delete_static_route_oif_vrf = config.find('.//*static-route-oif-vrf')
        delete_static_route_oif_vrf.set('operation', 'delete')
        
    next_hop_vrf_key = ET.SubElement(static_route_oif_vrf, "next-hop-vrf")
    next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
    if kwargs.pop('delete_next_hop_vrf', False) is True:
        delete_next_hop_vrf = config.find('.//*next-hop-vrf')
        delete_next_hop_vrf.set('operation', 'delete')
            
    static_route_oif_type_key = ET.SubElement(static_route_oif_vrf, "static-route-oif-type")
    static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
    if kwargs.pop('delete_static_route_oif_type', False) is True:
        delete_static_route_oif_type = config.find('.//*static-route-oif-type')
        delete_static_route_oif_type.set('operation', 'delete')
            
    static_route_oif_name_key = ET.SubElement(static_route_oif_vrf, "static-route-oif-name")
    static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
    if kwargs.pop('delete_static_route_oif_name', False) is True:
        delete_static_route_oif_name = config.find('.//*static-route-oif-name')
        delete_static_route_oif_name.set('operation', 'delete')
            
    static_route_next_vrf_dest = ET.SubElement(static_route_oif_vrf, "static-route-next-vrf-dest")
    if kwargs.pop('delete_static_route_next_vrf_dest', False) is True:
        delete_static_route_next_vrf_dest = config.find('.//*static-route-next-vrf-dest')
        delete_static_route_next_vrf_dest.set('operation', 'delete')
        
    static_route_next_vrf_dest.text = kwargs.pop('static_route_next_vrf_dest')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_rtm_config_route_static_route_oif_vrf_static_route_next_vrf_dest_act(Action):
    def run(self, static_route_oif_type, rbridge_id, delete_ip, delete_route, delete_next_hop_vrf, delete_static_route_next_vrf_dest, delete_static_route_oif_name, delete_static_route_oif_vrf, static_route_next_vrf_dest, next_hop_vrf, delete_rtm_config, delete_rbridge_id, delete_static_route_oif_type, static_route_oif_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_rtm_config_route_static_route_oif_vrf_static_route_next_vrf_dest(next_hop_vrf=next_hop_vrf, delete_static_route_oif_name=delete_static_route_oif_name, delete_route=delete_route, static_route_next_vrf_dest=static_route_next_vrf_dest, username=username, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_rtm_config=delete_rtm_config, delete_static_route_next_vrf_dest=delete_static_route_next_vrf_dest, delete_next_hop_vrf=delete_next_hop_vrf, delete_static_route_oif_vrf=delete_static_route_oif_vrf, static_route_oif_type=static_route_oif_type, delete_static_route_oif_type=delete_static_route_oif_type, host=host, static_route_oif_name=static_route_oif_name, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    