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


def rbridge_id_vrf_address_family_ipv6_unicast_max_route(**kwargs):
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
            
    vrf = ET.SubElement(rbridge_id, "vrf", xmlns="urn:brocade.com:mgmt:brocade-vrf")
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
        
    vrf_name_key = ET.SubElement(vrf, "vrf-name")
    vrf_name_key.text = kwargs.pop('vrf_name')
    if kwargs.pop('delete_vrf_name', False) is True:
        delete_vrf_name = config.find('.//*vrf-name')
        delete_vrf_name.set('operation', 'delete')
            
    address_family = ET.SubElement(vrf, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    ipv6 = ET.SubElement(address_family, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    unicast = ET.SubElement(ipv6, "unicast")
    if kwargs.pop('delete_unicast', False) is True:
        delete_unicast = config.find('.//*unicast')
        delete_unicast.set('operation', 'delete')
        
    max_route = ET.SubElement(unicast, "max-route")
    if kwargs.pop('delete_max_route', False) is True:
        delete_max_route = config.find('.//*max-route')
        delete_max_route.set('operation', 'delete')
        
    max_route.text = kwargs.pop('max_route')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrf_address_family_ipv6_unicast_max_route_act(Action):
    def run(self, delete_address_family, rbridge_id, delete_vrf, max_route, delete_max_route, vrf_name, delete_rbridge_id, delete_unicast, delete_vrf_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrf_address_family_ipv6_unicast_max_route(delete_max_route=delete_max_route, delete_address_family=delete_address_family, username=username, vrf_name=vrf_name, rbridge_id=rbridge_id, delete_vrf=delete_vrf, host=host, delete_vrf_name=delete_vrf_name, delete_unicast=delete_unicast, delete_rbridge_id=delete_rbridge_id, max_route=max_route, password=password, callback=_callback, mgr=mgr)
        return 0
    