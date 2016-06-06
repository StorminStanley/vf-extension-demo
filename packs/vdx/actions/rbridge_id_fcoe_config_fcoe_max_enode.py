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


def rbridge_id_fcoe_config_fcoe_max_enode(**kwargs):
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
            
    fcoe_config = ET.SubElement(rbridge_id, "fcoe-config", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
    if kwargs.pop('delete_fcoe_config', False) is True:
        delete_fcoe_config = config.find('.//*fcoe-config')
        delete_fcoe_config.set('operation', 'delete')
        
    fcoe_max_enode = ET.SubElement(fcoe_config, "fcoe-max-enode")
    if kwargs.pop('delete_fcoe_max_enode', False) is True:
        delete_fcoe_max_enode = config.find('.//*fcoe-max-enode')
        delete_fcoe_max_enode.set('operation', 'delete')
        
    fcoe_max_enode.text = kwargs.pop('fcoe_max_enode')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fcoe_config_fcoe_max_enode_act(Action):
    def run(self, delete_fcoe_config, fcoe_max_enode, delete_rbridge_id, rbridge_id, delete_fcoe_max_enode, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fcoe_config_fcoe_max_enode(fcoe_max_enode=fcoe_max_enode, delete_fcoe_max_enode=delete_fcoe_max_enode, username=username, rbridge_id=rbridge_id, delete_fcoe_config=delete_fcoe_config, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    