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


def rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_authentication_ipsec_auth_key_config_spi(**kwargs):
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
        
    authentication = ET.SubElement(link_properties, "authentication")
    if kwargs.pop('delete_authentication', False) is True:
        delete_authentication = config.find('.//*authentication')
        delete_authentication.set('operation', 'delete')
        
    ipsec_auth_key_config = ET.SubElement(authentication, "ipsec-auth-key-config")
    if kwargs.pop('delete_ipsec_auth_key_config', False) is True:
        delete_ipsec_auth_key_config = config.find('.//*ipsec-auth-key-config')
        delete_ipsec_auth_key_config.set('operation', 'delete')
        
    spi = ET.SubElement(ipsec_auth_key_config, "spi")
    if kwargs.pop('delete_spi', False) is True:
        delete_spi = config.find('.//*spi')
        delete_spi.set('operation', 'delete')
        
    spi.text = kwargs.pop('spi')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_authentication_ipsec_auth_key_config_spi_act(Action):
    def run(self, area_id, delete_virtual_link, rbridge_id, delete_ospf, delete_vrf, delete_area_id, delete_virtual_link_neighbor, virtual_link_neighbor, delete_ipsec_auth_key_config, delete_area, vrf, delete_link_properties, delete_spi, delete_rbridge_id, spi, delete_router, delete_authentication, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_area_virtual_link_link_properties_authentication_ipsec_auth_key_config_spi(delete_spi=delete_spi, username=username, spi=spi, delete_area=delete_area, area_id=area_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_authentication=delete_authentication, password=password, delete_ipsec_auth_key_config=delete_ipsec_auth_key_config, delete_router=delete_router, delete_ospf=delete_ospf, host=host, delete_virtual_link_neighbor=delete_virtual_link_neighbor, vrf=vrf, delete_link_properties=delete_link_properties, delete_rbridge_id=delete_rbridge_id, delete_virtual_link=delete_virtual_link, virtual_link_neighbor=virtual_link_neighbor, delete_area_id=delete_area_id, callback=_callback, mgr=mgr)
        return 0
    