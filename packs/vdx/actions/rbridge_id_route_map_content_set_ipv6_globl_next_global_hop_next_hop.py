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


def rbridge_id_route_map_content_set_ipv6_globl_next_global_hop_next_hop(**kwargs):
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
        
    ipv6 = ET.SubElement(set, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    globl = ET.SubElement(ipv6, "global")
    if kwargs.pop('delete_globl', False) is True:
        delete_globl = config.find('.//*global')
        delete_globl.set('operation', 'delete')
        
    next_global_hop = ET.SubElement(globl, "next-global-hop")
    if kwargs.pop('delete_next_global_hop', False) is True:
        delete_next_global_hop = config.find('.//*next-global-hop')
        delete_next_global_hop.set('operation', 'delete')
        
    next_hop = ET.SubElement(next_global_hop, "next-hop")
    if kwargs.pop('delete_next_hop', False) is True:
        delete_next_hop = config.find('.//*next-hop')
        delete_next_hop.set('operation', 'delete')
        
    next_hop.text = kwargs.pop('next_hop')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_route_map_content_set_ipv6_globl_next_global_hop_next_hop_act(Action):
    def run(self, next_hop, rbridge_id, delete_set, delete_next_hop, delete_route_map, delete_content, instance, delete_instance, action_rm, delete_globl, delete_name, delete_next_global_hop, delete_rbridge_id, delete_action_rm, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_route_map_content_set_ipv6_globl_next_global_hop_next_hop(delete_instance=delete_instance, delete_route_map=delete_route_map, delete_next_global_hop=delete_next_global_hop, action_rm=action_rm, delete_action_rm=delete_action_rm, username=username, rbridge_id=rbridge_id, delete_globl=delete_globl, name=name, password=password, delete_next_hop=delete_next_hop, delete_content=delete_content, delete_set=delete_set, instance=instance, delete_name=delete_name, host=host, delete_rbridge_id=delete_rbridge_id, next_hop=next_hop, callback=_callback, mgr=mgr)
        return 0
    