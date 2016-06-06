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


def rbridge_id_fabric_ecmp_ecmp_load_balance(**kwargs):
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
            
    fabric = ET.SubElement(rbridge_id, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
    if kwargs.pop('delete_fabric', False) is True:
        delete_fabric = config.find('.//*fabric')
        delete_fabric.set('operation', 'delete')
        
    ecmp = ET.SubElement(fabric, "ecmp")
    if kwargs.pop('delete_ecmp', False) is True:
        delete_ecmp = config.find('.//*ecmp')
        delete_ecmp.set('operation', 'delete')
        
    ecmp_load_balance = ET.SubElement(ecmp, "ecmp-load-balance")
    if kwargs.pop('delete_ecmp_load_balance', False) is True:
        delete_ecmp_load_balance = config.find('.//*ecmp-load-balance')
        delete_ecmp_load_balance.set('operation', 'delete')
        
    ecmp_load_balance.text = kwargs.pop('ecmp_load_balance')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fabric_ecmp_ecmp_load_balance_act(Action):
    def run(self, delete_ecmp, rbridge_id, delete_ecmp_load_balance, delete_fabric, ecmp_load_balance, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fabric_ecmp_ecmp_load_balance(delete_fabric=delete_fabric, delete_ecmp=delete_ecmp, username=username, rbridge_id=rbridge_id, ecmp_load_balance=ecmp_load_balance, host=host, password=password, delete_rbridge_id=delete_rbridge_id, delete_ecmp_load_balance=delete_ecmp_load_balance, callback=_callback, mgr=mgr)
        return 0
    