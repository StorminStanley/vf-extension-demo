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


def rbridge_id_interface_ve_ip_ip_local_anycast_gateway_track_interface_interface_type(**kwargs):
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
            
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(ve, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    ip_local_anycast_gateway = ET.SubElement(ip, "ip-local-anycast-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
    if kwargs.pop('delete_ip_local_anycast_gateway', False) is True:
        delete_ip_local_anycast_gateway = config.find('.//*ip-local-anycast-gateway')
        delete_ip_local_anycast_gateway.set('operation', 'delete')
        
    local_ip_gw_id_key = ET.SubElement(ip_local_anycast_gateway, "local-ip-gw-id")
    local_ip_gw_id_key.text = kwargs.pop('local_ip_gw_id')
    if kwargs.pop('delete_local_ip_gw_id', False) is True:
        delete_local_ip_gw_id = config.find('.//*local-ip-gw-id')
        delete_local_ip_gw_id.set('operation', 'delete')
            
    track = ET.SubElement(ip_local_anycast_gateway, "track")
    if kwargs.pop('delete_track', False) is True:
        delete_track = config.find('.//*track')
        delete_track.set('operation', 'delete')
        
    interface = ET.SubElement(track, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    interface_name_key = ET.SubElement(interface, "interface-name")
    interface_name_key.text = kwargs.pop('interface_name')
    if kwargs.pop('delete_interface_name', False) is True:
        delete_interface_name = config.find('.//*interface-name')
        delete_interface_name.set('operation', 'delete')
            
    interface_type = ET.SubElement(interface, "interface-type")
    if kwargs.pop('delete_interface_type', False) is True:
        delete_interface_type = config.find('.//*interface-type')
        delete_interface_type.set('operation', 'delete')
        
    interface_type.text = kwargs.pop('interface_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_ip_ip_local_anycast_gateway_track_interface_interface_type_act(Action):
    def run(self, delete_interface_type, delete_interface_name, name, delete_ip, interface_type, delete_ip_local_anycast_gateway, delete_track, delete_ve, delete_interface, delete_name, delete_rbridge_id, interface_name, local_ip_gw_id, delete_local_ip_gw_id, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_ip_ip_local_anycast_gateway_track_interface_interface_type(local_ip_gw_id=local_ip_gw_id, name=name, rbridge_id=rbridge_id, delete_name=delete_name, delete_track=delete_track, username=username, interface_name=interface_name, delete_ip=delete_ip, delete_ip_local_anycast_gateway=delete_ip_local_anycast_gateway, interface_type=interface_type, delete_interface_name=delete_interface_name, host=host, delete_interface_type=delete_interface_type, delete_ve=delete_ve, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, delete_local_ip_gw_id=delete_local_ip_gw_id, password=password, callback=_callback, mgr=mgr)
        return 0
    