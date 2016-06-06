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


def rbridge_id_ipv6_static_ag_ipv6_config_anycast_gateway_mac_ipv6_anycast_gateway_mac(**kwargs):
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
        
    static_ag_ipv6_config = ET.SubElement(ipv6, "static-ag-ipv6-config", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_static_ag_ipv6_config', False) is True:
        delete_static_ag_ipv6_config = config.find('.//*static-ag-ipv6-config')
        delete_static_ag_ipv6_config.set('operation', 'delete')
        
    anycast_gateway_mac = ET.SubElement(static_ag_ipv6_config, "anycast-gateway-mac")
    if kwargs.pop('delete_anycast_gateway_mac', False) is True:
        delete_anycast_gateway_mac = config.find('.//*anycast-gateway-mac')
        delete_anycast_gateway_mac.set('operation', 'delete')
        
    ipv6_anycast_gateway_mac = ET.SubElement(anycast_gateway_mac, "ipv6-anycast-gateway-mac")
    if kwargs.pop('delete_ipv6_anycast_gateway_mac', False) is True:
        delete_ipv6_anycast_gateway_mac = config.find('.//*ipv6-anycast-gateway-mac')
        delete_ipv6_anycast_gateway_mac.set('operation', 'delete')
        
    ipv6_anycast_gateway_mac.text = kwargs.pop('ipv6_anycast_gateway_mac')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_static_ag_ipv6_config_anycast_gateway_mac_ipv6_anycast_gateway_mac_act(Action):
    def run(self, delete_anycast_gateway_mac, delete_rbridge_id, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_static_ag_ipv6_config_anycast_gateway_mac_ipv6_anycast_gateway_mac(delete_anycast_gateway_mac=delete_anycast_gateway_mac, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    