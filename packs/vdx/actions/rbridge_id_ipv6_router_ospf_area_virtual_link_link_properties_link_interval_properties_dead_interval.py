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


def rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_link_interval_properties_dead_interval(**kwargs):
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
        
    router = ET.SubElement(ipv6, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
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
            
    virtual_link = ET.SubElement(area, "virtual-link")
    if kwargs.pop('delete_virtual_link', False) is True:
        delete_virtual_link = config.find('.//*virtual-link')
        delete_virtual_link.set('operation', 'delete')
        
    virtual_link_neighbor_key = ET.SubElement(virtual_link, "virtual-link-neighbor")
    virtual_link_neighbor_key.text = kwargs.pop('virtual_link_neighbor')
    if kwargs.pop('delete_virtual_link_neighbor', False) is True:
        delete_virtual_link_neighbor = config.find('.//*virtual-link-neighbor')
        delete_virtual_link_neighbor.set('operation', 'delete')
            
    link_properties = ET.SubElement(virtual_link, "link-properties")
    if kwargs.pop('delete_link_properties', False) is True:
        delete_link_properties = config.find('.//*link-properties')
        delete_link_properties.set('operation', 'delete')
        
    link_interval_properties = ET.SubElement(link_properties, "link-interval-properties")
    if kwargs.pop('delete_link_interval_properties', False) is True:
        delete_link_interval_properties = config.find('.//*link-interval-properties')
        delete_link_interval_properties.set('operation', 'delete')
        
    dead_interval = ET.SubElement(link_interval_properties, "dead-interval")
    if kwargs.pop('delete_dead_interval', False) is True:
        delete_dead_interval = config.find('.//*dead-interval')
        delete_dead_interval.set('operation', 'delete')
        
    dead_interval.text = kwargs.pop('dead_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_link_interval_properties_dead_interval_act(Action):
    def run(self, area_id, delete_virtual_link, rbridge_id, delete_dead_interval, delete_ospf, delete_vrf, delete_area_id, delete_virtual_link_neighbor, virtual_link_neighbor, dead_interval, delete_area, vrf, delete_link_properties, delete_link_interval_properties, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_link_interval_properties_dead_interval(delete_link_interval_properties=delete_link_interval_properties, username=username, delete_area=delete_area, area_id=area_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, password=password, dead_interval=dead_interval, vrf=vrf, delete_router=delete_router, delete_ospf=delete_ospf, host=host, delete_virtual_link_neighbor=delete_virtual_link_neighbor, delete_dead_interval=delete_dead_interval, delete_link_properties=delete_link_properties, delete_rbridge_id=delete_rbridge_id, delete_virtual_link=delete_virtual_link, virtual_link_neighbor=virtual_link_neighbor, delete_area_id=delete_area_id, callback=_callback, mgr=mgr)
        return 0
    