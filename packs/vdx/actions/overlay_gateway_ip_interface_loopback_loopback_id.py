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


def overlay_gateway_ip_interface_loopback_loopback_id(**kwargs):
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
            
    ip = ET.SubElement(overlay_gateway, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface = ET.SubElement(ip, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    loopback = ET.SubElement(interface, "loopback")
    if kwargs.pop('delete_loopback', False) is True:
        delete_loopback = config.find('.//*loopback')
        delete_loopback.set('operation', 'delete')
        
    loopback_id = ET.SubElement(loopback, "loopback-id")
    if kwargs.pop('delete_loopback_id', False) is True:
        delete_loopback_id = config.find('.//*loopback-id')
        delete_loopback_id.set('operation', 'delete')
        
    loopback_id.text = kwargs.pop('loopback_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_ip_interface_loopback_loopback_id_act(Action):
    def run(self, name, delete_ip, loopback_id, delete_loopback, delete_interface, delete_name, delete_overlay_gateway, delete_loopback_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_ip_interface_loopback_loopback_id(name=name, delete_name=delete_name, delete_ip=delete_ip, loopback_id=loopback_id, delete_loopback=delete_loopback, delete_overlay_gateway=delete_overlay_gateway, host=host, password=password, delete_interface=delete_interface, username=username, delete_loopback_id=delete_loopback_id, callback=_callback, mgr=mgr)
        return 0
    