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


def overlay_gateway_site_tunnel_dst_address(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
    if kwargs.pop('delete_overlay_gateway', False) is True:
        delete_overlay_gateway = config.find('.//*overlay-gateway')
        delete_overlay_gateway.set('operation', 'delete')
        
    name_key = ET.SubElement(overlay_gateway, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    site = ET.SubElement(overlay_gateway, "site")
    if kwargs.pop('delete_site', False) is True:
        delete_site = config.find('.//*site')
        delete_site.set('operation', 'delete')
        
    site_name_key = ET.SubElement(site, "name")
    site_name_key.text = kwargs.pop('site_name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    tunnel_dst = ET.SubElement(site, "tunnel-dst")
    if kwargs.pop('delete_tunnel_dst', False) is True:
        delete_tunnel_dst = config.find('.//*tunnel-dst')
        delete_tunnel_dst.set('operation', 'delete')
        
    address = ET.SubElement(tunnel_dst, "address")
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
        
    address.text = kwargs.pop('address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_site_tunnel_dst_address_act(Action):
    def run(self, name, delete_site, delete_name, address, delete_overlay_gateway, delete_address, delete_tunnel_dst, host, username, password, site_name):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_site_tunnel_dst_address(name=name, site_name=site_name, delete_name=delete_name, username=username, address=address, delete_tunnel_dst=delete_tunnel_dst, delete_overlay_gateway=delete_overlay_gateway, host=host, delete_address=delete_address, delete_site=delete_site, password=password, callback=_callback, mgr=mgr)
        return 0
    
