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


def rbridge_id_ipv6_ipv6route_route_next_ipv6_hop_next_hop(**kwargs):
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
        
    ipv6route = ET.SubElement(ipv6, "ipv6route", xmlns="urn:brocade.com:mgmt:brocade-ip-forward")
    if kwargs.pop('delete_ipv6route', False) is True:
        delete_ipv6route = config.find('.//*ipv6route')
        delete_ipv6route.set('operation', 'delete')
        
    route = ET.SubElement(ipv6route, "route")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    dest_key = ET.SubElement(route, "dest")
    dest_key.text = kwargs.pop('dest')
    if kwargs.pop('delete_dest', False) is True:
        delete_dest = config.find('.//*dest')
        delete_dest.set('operation', 'delete')
            
    next = ET.SubElement(route, "next")
    if kwargs.pop('delete_next', False) is True:
        delete_next = config.find('.//*next')
        delete_next.set('operation', 'delete')
        
    ipv6_hop = ET.SubElement(next, "ipv6-hop")
    if kwargs.pop('delete_ipv6_hop', False) is True:
        delete_ipv6_hop = config.find('.//*ipv6-hop')
        delete_ipv6_hop.set('operation', 'delete')
        
    next_hop = ET.SubElement(ipv6_hop, "next-hop")
    if kwargs.pop('delete_next_hop', False) is True:
        delete_next_hop = config.find('.//*next-hop')
        delete_next_hop.set('operation', 'delete')
        
    next_hop.text = kwargs.pop('next_hop')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_ipv6route_route_next_ipv6_hop_next_hop_act(Action):
    def run(self, delete_dest, rbridge_id, delete_route, dest, delete_next_hop, next_hop, delete_rbridge_id, delete_next, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_ipv6route_route_next_ipv6_hop_next_hop(username=username, delete_route=delete_route, delete_next=delete_next, delete_dest=delete_dest, rbridge_id=rbridge_id, delete_next_hop=delete_next_hop, host=host, password=password, delete_rbridge_id=delete_rbridge_id, dest=dest, next_hop=next_hop, callback=_callback, mgr=mgr)
        return 0
    