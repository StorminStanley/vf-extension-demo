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


def rbridge_id_router_ospf_area_virtual_link_authentication_key_no_encrypt_auth_key_table_no_encrypt_auth_key(**kwargs):
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
            
    authentication_key = ET.SubElement(virtual_link, "authentication-key")
    if kwargs.pop('delete_authentication_key', False) is True:
        delete_authentication_key = config.find('.//*authentication-key')
        delete_authentication_key.set('operation', 'delete')
        
    no_encrypt_auth_key_table = ET.SubElement(authentication_key, "no-encrypt-auth-key-table")
    if kwargs.pop('delete_no_encrypt_auth_key_table', False) is True:
        delete_no_encrypt_auth_key_table = config.find('.//*no-encrypt-auth-key-table')
        delete_no_encrypt_auth_key_table.set('operation', 'delete')
        
    no_encrypt_auth_key = ET.SubElement(no_encrypt_auth_key_table, "no-encrypt-auth-key")
    if kwargs.pop('delete_no_encrypt_auth_key', False) is True:
        delete_no_encrypt_auth_key = config.find('.//*no-encrypt-auth-key')
        delete_no_encrypt_auth_key.set('operation', 'delete')
        
    no_encrypt_auth_key.text = kwargs.pop('no_encrypt_auth_key')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_area_virtual_link_authentication_key_no_encrypt_auth_key_table_no_encrypt_auth_key_act(Action):
    def run(self, area_id, delete_virtual_link, rbridge_id, delete_ospf, delete_vrf, delete_no_encrypt_auth_key_table, no_encrypt_auth_key, delete_area_id, delete_no_encrypt_auth_key, delete_area, vrf, delete_virt_link_neighbor, delete_rbridge_id, virt_link_neighbor, delete_router, delete_authentication_key, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_area_virtual_link_authentication_key_no_encrypt_auth_key_table_no_encrypt_auth_key(delete_virt_link_neighbor=delete_virt_link_neighbor, no_encrypt_auth_key=no_encrypt_auth_key, username=username, virt_link_neighbor=virt_link_neighbor, delete_area=delete_area, area_id=area_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, password=password, delete_no_encrypt_auth_key=delete_no_encrypt_auth_key, delete_authentication_key=delete_authentication_key, delete_router=delete_router, delete_ospf=delete_ospf, delete_area_id=delete_area_id, vrf=vrf, host=host, delete_rbridge_id=delete_rbridge_id, delete_virtual_link=delete_virtual_link, delete_no_encrypt_auth_key_table=delete_no_encrypt_auth_key_table, callback=_callback, mgr=mgr)
        return 0
    