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


def rbridge_id_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop(**kwargs):
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
            
    route_map = ET.SubElement(rbridge_id, "route-map", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_route_map', False) is True:
        delete_route_map = config.find('.//*route-map')
        delete_route_map.set('operation', 'delete')
        
    name_key = ET.SubElement(route_map, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    action_rm_key = ET.SubElement(route_map, "action-rm")
    action_rm_key.text = kwargs.pop('action_rm')
    if kwargs.pop('delete_action_rm', False) is True:
        delete_action_rm = config.find('.//*action-rm')
        delete_action_rm.set('operation', 'delete')
            
    instance_key = ET.SubElement(route_map, "instance")
    instance_key.text = kwargs.pop('instance')
    if kwargs.pop('delete_instance', False) is True:
        delete_instance = config.find('.//*instance')
        delete_instance.set('operation', 'delete')
            
    content = ET.SubElement(route_map, "content")
    if kwargs.pop('delete_content', False) is True:
        delete_content = config.find('.//*content')
        delete_content.set('operation', 'delete')
        
    set = ET.SubElement(content, "set")
    if kwargs.pop('delete_set', False) is True:
        delete_set = config.find('.//*set')
        delete_set.set('operation', 'delete')
        
    ip = ET.SubElement(set, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    next_vrf = ET.SubElement(ip, "next-vrf")
    if kwargs.pop('delete_next_vrf', False) is True:
        delete_next_vrf = config.find('.//*next-vrf')
        delete_next_vrf.set('operation', 'delete')
        
    next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
    if kwargs.pop('delete_next_vrf_list', False) is True:
        delete_next_vrf_list = config.find('.//*next-vrf-list')
        delete_next_vrf_list.set('operation', 'delete')
        
    vrf_key = ET.SubElement(next_vrf_list, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    next_hop = ET.SubElement(next_vrf_list, "next-hop")
    if kwargs.pop('delete_next_hop', False) is True:
        delete_next_hop = config.find('.//*next-hop')
        delete_next_hop.set('operation', 'delete')
        
    next_hop.text = kwargs.pop('next_hop')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop_act(Action):
    def run(self, next_hop, delete_next_hop, rbridge_id, delete_set, delete_next_vrf, delete_vrf, delete_route_map, delete_content, instance, delete_instance, action_rm, vrf, delete_name, delete_next_vrf_list, delete_rbridge_id, delete_ip, delete_action_rm, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop(delete_instance=delete_instance, delete_route_map=delete_route_map, name=name, action_rm=action_rm, username=username, delete_action_rm=delete_action_rm, delete_vrf=delete_vrf, rbridge_id=rbridge_id, delete_next_vrf=delete_next_vrf, password=password, delete_next_hop=delete_next_hop, delete_next_vrf_list=delete_next_vrf_list, delete_content=delete_content, delete_set=delete_set, instance=instance, host=host, vrf=vrf, delete_name=delete_name, delete_ip=delete_ip, delete_rbridge_id=delete_rbridge_id, next_hop=next_hop, callback=_callback, mgr=mgr)
        return 0
    