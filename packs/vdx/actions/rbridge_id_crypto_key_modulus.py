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


def rbridge_id_crypto_key_modulus(**kwargs):
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
            
    crypto = ET.SubElement(rbridge_id, "crypto", xmlns="urn:brocade.com:mgmt:brocade-crypto")
    if kwargs.pop('delete_crypto', False) is True:
        delete_crypto = config.find('.//*crypto')
        delete_crypto.set('operation', 'delete')
        
    key = ET.SubElement(crypto, "key")
    if kwargs.pop('delete_key', False) is True:
        delete_key = config.find('.//*key')
        delete_key.set('operation', 'delete')
        
    label_key = ET.SubElement(key, "label")
    label_key.text = kwargs.pop('label')
    if kwargs.pop('delete_label', False) is True:
        delete_label = config.find('.//*label')
        delete_label.set('operation', 'delete')
            
    modulus = ET.SubElement(key, "modulus")
    if kwargs.pop('delete_modulus', False) is True:
        delete_modulus = config.find('.//*modulus')
        delete_modulus.set('operation', 'delete')
        
    modulus.text = kwargs.pop('modulus')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_crypto_key_modulus_act(Action):
    def run(self, delete_label, rbridge_id, delete_modulus, label, delete_crypto, delete_key, delete_rbridge_id, modulus, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_crypto_key_modulus(modulus=modulus, delete_modulus=delete_modulus, delete_crypto=delete_crypto, username=username, rbridge_id=rbridge_id, label=label, delete_label=delete_label, host=host, delete_key=delete_key, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    