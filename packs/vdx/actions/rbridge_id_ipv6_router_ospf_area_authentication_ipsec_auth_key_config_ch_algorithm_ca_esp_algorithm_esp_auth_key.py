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


def rbridge_id_ipv6_router_ospf_area_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_auth_key(**kwargs):
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
            
    authentication = ET.SubElement(area, "authentication")
    if kwargs.pop('delete_authentication', False) is True:
        delete_authentication = config.find('.//*authentication')
        delete_authentication.set('operation', 'delete')
        
    ipsec_auth_key_config = ET.SubElement(authentication, "ipsec-auth-key-config")
    if kwargs.pop('delete_ipsec_auth_key_config', False) is True:
        delete_ipsec_auth_key_config = config.find('.//*ipsec-auth-key-config')
        delete_ipsec_auth_key_config.set('operation', 'delete')
        
    ch_algorithm = ET.SubElement(ipsec_auth_key_config, "ch-algorithm")
    if kwargs.pop('delete_ch_algorithm', False) is True:
        delete_ch_algorithm = config.find('.//*ch-algorithm')
        delete_ch_algorithm.set('operation', 'delete')
        
    ca_esp_algorithm = ET.SubElement(ch_algorithm, "ca-esp-algorithm")
    if kwargs.pop('delete_ca_esp_algorithm', False) is True:
        delete_ca_esp_algorithm = config.find('.//*ca-esp-algorithm')
        delete_ca_esp_algorithm.set('operation', 'delete')
        
    esp_auth_key = ET.SubElement(ca_esp_algorithm, "esp-auth-key")
    if kwargs.pop('delete_esp_auth_key', False) is True:
        delete_esp_auth_key = config.find('.//*esp-auth-key')
        delete_esp_auth_key.set('operation', 'delete')
        
    esp_auth_key.text = kwargs.pop('esp_auth_key')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_area_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_auth_key_act(Action):
    def run(self, area_id, rbridge_id, delete_esp_auth_key, delete_ospf, delete_vrf, delete_area_id, delete_ca_esp_algorithm, delete_ipsec_auth_key_config, delete_area, vrf, delete_rbridge_id, delete_ch_algorithm, esp_auth_key, delete_router, delete_authentication, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_area_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_auth_key(delete_ca_esp_algorithm=delete_ca_esp_algorithm, username=username, delete_esp_auth_key=delete_esp_auth_key, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, password=password, delete_ipsec_auth_key_config=delete_ipsec_auth_key_config, delete_area=delete_area, delete_router=delete_router, delete_ospf=delete_ospf, host=host, esp_auth_key=esp_auth_key, vrf=vrf, delete_authentication=delete_authentication, area_id=area_id, delete_area_id=delete_area_id, delete_ch_algorithm=delete_ch_algorithm, callback=_callback, mgr=mgr)
        return 0
    