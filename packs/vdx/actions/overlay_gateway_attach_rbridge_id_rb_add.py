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


def overlay_gateway_attach_rbridge_id_rb_add(**kwargs):
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
            
    attach = ET.SubElement(overlay_gateway, "attach")
    if kwargs.pop('delete_attach', False) is True:
        delete_attach = config.find('.//*attach')
        delete_attach.set('operation', 'delete')
        
    rbridge_id = ET.SubElement(attach, "rbridge-id")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rb_add = ET.SubElement(rbridge_id, "rb-add")
    if kwargs.pop('delete_rb_add', False) is True:
        delete_rb_add = config.find('.//*rb-add')
        delete_rb_add.set('operation', 'delete')
        
    rb_add.text = kwargs.pop('rb_add')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_attach_rbridge_id_rb_add_act(Action):
    def run(self, delete_rb_add, name, delete_attach, rb_add, delete_name, delete_overlay_gateway, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_attach_rbridge_id_rb_add(name=name, delete_name=delete_name, username=username, delete_rbridge_id=delete_rbridge_id, delete_overlay_gateway=delete_overlay_gateway, delete_rb_add=delete_rb_add, host=host, rb_add=rb_add, delete_attach=delete_attach, password=password, callback=_callback, mgr=mgr)
        return 0
    