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


def rbridge_id_fabric_port_channel_vlag_load_balance(**kwargs):
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
        
    port_channel = ET.SubElement(fabric, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    po_id_key = ET.SubElement(port_channel, "po-id")
    po_id_key.text = kwargs.pop('po_id')
    if kwargs.pop('delete_po_id', False) is True:
        delete_po_id = config.find('.//*po-id')
        delete_po_id.set('operation', 'delete')
            
    vlag_load_balance = ET.SubElement(port_channel, "vlag-load-balance")
    if kwargs.pop('delete_vlag_load_balance', False) is True:
        delete_vlag_load_balance = config.find('.//*vlag-load-balance')
        delete_vlag_load_balance.set('operation', 'delete')
        
    vlag_load_balance.text = kwargs.pop('vlag_load_balance')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fabric_port_channel_vlag_load_balance_act(Action):
    def run(self, rbridge_id, po_id, delete_port_channel, delete_po_id, delete_fabric, delete_vlag_load_balance, delete_rbridge_id, vlag_load_balance, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fabric_port_channel_vlag_load_balance(po_id=po_id, delete_vlag_load_balance=delete_vlag_load_balance, delete_fabric=delete_fabric, vlag_load_balance=vlag_load_balance, username=username, rbridge_id=rbridge_id, delete_port_channel=delete_port_channel, delete_po_id=delete_po_id, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    