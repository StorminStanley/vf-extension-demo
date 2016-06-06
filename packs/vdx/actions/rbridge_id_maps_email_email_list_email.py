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


def rbridge_id_maps_email_email_list_email(**kwargs):
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
            
    maps = ET.SubElement(rbridge_id, "maps", xmlns="urn:brocade.com:mgmt:brocade-maps")
    if kwargs.pop('delete_maps', False) is True:
        delete_maps = config.find('.//*maps')
        delete_maps.set('operation', 'delete')
        
    email = ET.SubElement(maps, "email")
    if kwargs.pop('delete_email', False) is True:
        delete_email = config.find('.//*email')
        delete_email.set('operation', 'delete')
        
    email_list = ET.SubElement(email, "email-list")
    if kwargs.pop('delete_email_list', False) is True:
        delete_email_list = config.find('.//*email-list')
        delete_email_list.set('operation', 'delete')
        
    email = ET.SubElement(email_list, "email")
    if kwargs.pop('delete_email', False) is True:
        delete_email = config.find('.//*email')
        delete_email.set('operation', 'delete')
        
    email.text = kwargs.pop('email')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_maps_email_email_list_email_act(Action):
    def run(self, rbridge_id, delete_maps, delete_email_list, delete_email, delete_rbridge_id, email, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_maps_email_email_list_email(username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_maps=delete_maps, email=email, host=host, delete_email=delete_email, delete_email_list=delete_email_list, password=password, callback=_callback, mgr=mgr)
        return 0
    