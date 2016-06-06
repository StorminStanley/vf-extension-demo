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


def overlay_gateway_gw_type(**kwargs):
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
            
    gw_type = ET.SubElement(overlay_gateway, "gw-type")
    if kwargs.pop('delete_gw_type', False) is True:
        delete_gw_type = config.find('.//*gw-type')
        delete_gw_type.set('operation', 'delete')
        
    gw_type.text = kwargs.pop('gw_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_gw_type_act(Action):
    def run(self, gw_type, delete_overlay_gateway, delete_gw_type, name, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_gw_type(name=name, delete_name=delete_name, delete_gw_type=delete_gw_type, delete_overlay_gateway=delete_overlay_gateway, host=host, gw_type=gw_type, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    