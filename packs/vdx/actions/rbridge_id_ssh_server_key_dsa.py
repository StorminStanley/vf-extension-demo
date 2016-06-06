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


def rbridge_id_ssh_server_key_dsa(**kwargs):
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
        
    server = ET.SubElement(ssh, "server")
    if kwargs.pop('delete_server', False) is True:
        delete_server = config.find('.//*server')
        delete_server.set('operation', 'delete')
        
    key = ET.SubElement(server, "key")
    if kwargs.pop('delete_key', False) is True:
        delete_key = config.find('.//*key')
        delete_key.set('operation', 'delete')
        
    dsa = ET.SubElement(key, "dsa")
    if kwargs.pop('delete_dsa', False) is True:
        delete_dsa = config.find('.//*dsa')
        delete_dsa.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ssh_server_key_dsa_act(Action):
    def run(self, rbridge_id, delete_server, delete_key, delete_ssh, delete_rbridge_id, delete_dsa, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ssh_server_key_dsa(delete_server=delete_server, username=username, rbridge_id=rbridge_id, delete_ssh=delete_ssh, delete_dsa=delete_dsa, host=host, delete_key=delete_key, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    