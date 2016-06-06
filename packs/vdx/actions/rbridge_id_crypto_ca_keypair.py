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


def rbridge_id_crypto_ca_keypair(**kwargs):
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
        
    ca = ET.SubElement(crypto, "ca")
    if kwargs.pop('delete_ca', False) is True:
        delete_ca = config.find('.//*ca')
        delete_ca.set('operation', 'delete')
        
    trustpoint_key = ET.SubElement(ca, "trustpoint")
    trustpoint_key.text = kwargs.pop('trustpoint')
    if kwargs.pop('delete_trustpoint', False) is True:
        delete_trustpoint = config.find('.//*trustpoint')
        delete_trustpoint.set('operation', 'delete')
            
    keypair = ET.SubElement(ca, "keypair")
    if kwargs.pop('delete_keypair', False) is True:
        delete_keypair = config.find('.//*keypair')
        delete_keypair.set('operation', 'delete')
        
    keypair.text = kwargs.pop('keypair')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_crypto_ca_keypair_act(Action):
    def run(self, rbridge_id, delete_trustpoint, keypair, delete_crypto, delete_ca, delete_keypair, delete_rbridge_id, trustpoint, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_crypto_ca_keypair(trustpoint=trustpoint, delete_crypto=delete_crypto, username=username, rbridge_id=rbridge_id, keypair=keypair, delete_keypair=delete_keypair, delete_ca=delete_ca, host=host, delete_trustpoint=delete_trustpoint, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    