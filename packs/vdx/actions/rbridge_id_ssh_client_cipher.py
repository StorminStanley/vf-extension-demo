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


def rbridge_id_ssh_client_cipher(**kwargs):
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
            
    ssh = ET.SubElement(rbridge_id, "ssh", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
    if kwargs.pop('delete_ssh', False) is True:
        delete_ssh = config.find('.//*ssh')
        delete_ssh.set('operation', 'delete')
        
    client = ET.SubElement(ssh, "client")
    if kwargs.pop('delete_client', False) is True:
        delete_client = config.find('.//*client')
        delete_client.set('operation', 'delete')
        
    cipher = ET.SubElement(client, "cipher")
    if kwargs.pop('delete_cipher', False) is True:
        delete_cipher = config.find('.//*cipher')
        delete_cipher.set('operation', 'delete')
        
    cipher.text = kwargs.pop('cipher')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ssh_client_cipher_act(Action):
    def run(self, rbridge_id, cipher, delete_client, delete_ssh, delete_rbridge_id, delete_cipher, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ssh_client_cipher(username=username, delete_client=delete_client, rbridge_id=rbridge_id, delete_ssh=delete_ssh, cipher=cipher, delete_cipher=delete_cipher, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    