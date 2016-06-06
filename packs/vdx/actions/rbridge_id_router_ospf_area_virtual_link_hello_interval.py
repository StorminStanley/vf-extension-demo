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


def rbridge_id_router_ospf_area_virtual_link_hello_interval(**kwargs):
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
            
    virtual_link = ET.SubElement(area, "virtual-link")
    if kwargs.pop('delete_virtual_link', False) is True:
        delete_virtual_link = config.find('.//*virtual-link')
        delete_virtual_link.set('operation', 'delete')
        
    virt_link_neighbor_key = ET.SubElement(virtual_link, "virt-link-neighbor")
    virt_link_neighbor_key.text = kwargs.pop('virt_link_neighbor')
    if kwargs.pop('delete_virt_link_neighbor', False) is True:
        delete_virt_link_neighbor = config.find('.//*virt-link-neighbor')
        delete_virt_link_neighbor.set('operation', 'delete')
            
    hello_interval = ET.SubElement(virtual_link, "hello-interval")
    if kwargs.pop('delete_hello_interval', False) is True:
        delete_hello_interval = config.find('.//*hello-interval')
        delete_hello_interval.set('operation', 'delete')
        
    hello_interval.text = kwargs.pop('hello_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_area_virtual_link_hello_interval_act(Action):
    def run(self, area_id, delete_virtual_link, rbridge_id, delete_ospf, delete_vrf, delete_area_id, delete_area, vrf, hello_interval, delete_hello_interval, delete_virt_link_neighbor, delete_rbridge_id, virt_link_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_area_virtual_link_hello_interval(delete_virt_link_neighbor=delete_virt_link_neighbor, username=username, virt_link_neighbor=virt_link_neighbor, delete_area=delete_area, area_id=area_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, password=password, delete_router=delete_router, delete_ospf=delete_ospf, host=host, vrf=vrf, hello_interval=hello_interval, delete_rbridge_id=delete_rbridge_id, delete_virtual_link=delete_virtual_link, delete_hello_interval=delete_hello_interval, delete_area_id=delete_area_id, callback=_callback, mgr=mgr)
        return 0
    