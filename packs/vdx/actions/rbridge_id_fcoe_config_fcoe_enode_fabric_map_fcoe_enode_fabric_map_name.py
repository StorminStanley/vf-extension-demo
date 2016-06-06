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


def rbridge_id_fcoe_config_fcoe_enode_fabric_map_fcoe_enode_fabric_map_name(**kwargs):
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
        
    fcoe_enode_fabric_map = ET.SubElement(fcoe_config, "fcoe-enode-fabric-map")
    if kwargs.pop('delete_fcoe_enode_fabric_map', False) is True:
        delete_fcoe_enode_fabric_map = config.find('.//*fcoe-enode-fabric-map')
        delete_fcoe_enode_fabric_map.set('operation', 'delete')
        
    fcoe_enode_fabric_map_name = ET.SubElement(fcoe_enode_fabric_map, "fcoe-enode-fabric-map-name")
    if kwargs.pop('delete_fcoe_enode_fabric_map_name', False) is True:
        delete_fcoe_enode_fabric_map_name = config.find('.//*fcoe-enode-fabric-map-name')
        delete_fcoe_enode_fabric_map_name.set('operation', 'delete')
        
    fcoe_enode_fabric_map_name.text = kwargs.pop('fcoe_enode_fabric_map_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_fcoe_config_fcoe_enode_fabric_map_fcoe_enode_fabric_map_name_act(Action):
    def run(self, delete_fcoe_config, rbridge_id, delete_fcoe_enode_fabric_map_name, delete_fcoe_enode_fabric_map, fcoe_enode_fabric_map_name, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_fcoe_config_fcoe_enode_fabric_map_fcoe_enode_fabric_map_name(delete_fcoe_enode_fabric_map_name=delete_fcoe_enode_fabric_map_name, fcoe_enode_fabric_map_name=fcoe_enode_fabric_map_name, delete_fcoe_enode_fabric_map=delete_fcoe_enode_fabric_map, username=username, rbridge_id=rbridge_id, delete_fcoe_config=delete_fcoe_config, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    