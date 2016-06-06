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


def rbridge_id_qos_tx_queue_tx_queue_limit(**kwargs):
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
            
    qos = ET.SubElement(rbridge_id, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
    if kwargs.pop('delete_qos', False) is True:
        delete_qos = config.find('.//*qos')
        delete_qos.set('operation', 'delete')
        
    tx_queue = ET.SubElement(qos, "tx-queue")
    if kwargs.pop('delete_tx_queue', False) is True:
        delete_tx_queue = config.find('.//*tx-queue')
        delete_tx_queue.set('operation', 'delete')
        
    tx_queue_limit = ET.SubElement(tx_queue, "tx-queue-limit")
    if kwargs.pop('delete_tx_queue_limit', False) is True:
        delete_tx_queue_limit = config.find('.//*tx-queue-limit')
        delete_tx_queue_limit.set('operation', 'delete')
        
    tx_queue_limit.text = kwargs.pop('tx_queue_limit')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_qos_tx_queue_tx_queue_limit_act(Action):
    def run(self, delete_qos, rbridge_id, delete_tx_queue_limit, tx_queue_limit, delete_tx_queue, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_qos_tx_queue_tx_queue_limit(delete_qos=delete_qos, delete_tx_queue_limit=delete_tx_queue_limit, tx_queue_limit=tx_queue_limit, username=username, rbridge_id=rbridge_id, delete_tx_queue=delete_tx_queue, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    