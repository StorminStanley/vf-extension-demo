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


def overlay_gateway_name(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
    if kwargs.pop('delete_overlay_gateway', False) is True:
        overlay_gateway.set('operation', 'delete')
        
    name = ET.SubElement(overlay_gateway, "name")
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
        
    name.text = kwargs.pop('name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_name_act(Action):
    def run(self, delete_overlay_gateway, name, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_name(name=name, delete_name=delete_name, delete_overlay_gateway=delete_overlay_gateway, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    
