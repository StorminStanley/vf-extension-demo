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


def rbridge_id_ip_static_ag_ip_config_anycast_gateway_mac_ip_anycast_gateway_mac(**kwargs):
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
            
    ip = ET.SubElement(rbridge_id, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    static_ag_ip_config = ET.SubElement(ip, "static-ag-ip-config", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_static_ag_ip_config', False) is True:
        delete_static_ag_ip_config = config.find('.//*static-ag-ip-config')
        delete_static_ag_ip_config.set('operation', 'delete')
        
    anycast_gateway_mac = ET.SubElement(static_ag_ip_config, "anycast-gateway-mac")
    if kwargs.pop('delete_anycast_gateway_mac', False) is True:
        delete_anycast_gateway_mac = config.find('.//*anycast-gateway-mac')
        delete_anycast_gateway_mac.set('operation', 'delete')
        
    ip_anycast_gateway_mac = ET.SubElement(anycast_gateway_mac, "ip-anycast-gateway-mac")
    if kwargs.pop('delete_ip_anycast_gateway_mac', False) is True:
        delete_ip_anycast_gateway_mac = config.find('.//*ip-anycast-gateway-mac')
        delete_ip_anycast_gateway_mac.set('operation', 'delete')
        
    ip_anycast_gateway_mac.text = kwargs.pop('ip_anycast_gateway_mac')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_static_ag_ip_config_anycast_gateway_mac_ip_anycast_gateway_mac_act(Action):
    def run(self, delete_anycast_gateway_mac, rbridge_id, delete_static_ag_ip_config, ip_anycast_gateway_mac, delete_ip_anycast_gateway_mac, delete_rbridge_id, delete_ip, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_static_ag_ip_config_anycast_gateway_mac_ip_anycast_gateway_mac(delete_static_ag_ip_config=delete_static_ag_ip_config, username=username, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_ip_anycast_gateway_mac=delete_ip_anycast_gateway_mac, ip_anycast_gateway_mac=ip_anycast_gateway_mac, host=host, delete_anycast_gateway_mac=delete_anycast_gateway_mac, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    