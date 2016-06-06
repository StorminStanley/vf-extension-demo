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


def rbridge_id_hardware_profile_route_table_predefined_routing_profiletype(**kwargs):
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
            
    hardware_profile = ET.SubElement(rbridge_id, "hardware-profile", xmlns="urn:brocade.com:mgmt:brocade-hardware")
    if kwargs.pop('delete_hardware_profile', False) is True:
        delete_hardware_profile = config.find('.//*hardware-profile')
        delete_hardware_profile.set('operation', 'delete')
        
    route_table = ET.SubElement(hardware_profile, "route-table")
    if kwargs.pop('delete_route_table', False) is True:
        delete_route_table = config.find('.//*route-table')
        delete_route_table.set('operation', 'delete')
        
    predefined = ET.SubElement(route_table, "predefined")
    if kwargs.pop('delete_predefined', False) is True:
        delete_predefined = config.find('.//*predefined')
        delete_predefined.set('operation', 'delete')
        
    routing_profiletype = ET.SubElement(predefined, "routing_profiletype")
    if kwargs.pop('delete_routing_profiletype', False) is True:
        delete_routing_profiletype = config.find('.//*routing_profiletype')
        delete_routing_profiletype.set('operation', 'delete')
        
    routing_profiletype.text = kwargs.pop('routing_profiletype')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_hardware_profile_route_table_predefined_routing_profiletype_act(Action):
    def run(self, rbridge_id, delete_predefined, delete_hardware_profile, routing_profiletype, delete_route_table, delete_rbridge_id, delete_routing_profiletype, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_hardware_profile_route_table_predefined_routing_profiletype(username=username, delete_predefined=delete_predefined, rbridge_id=rbridge_id, routing_profiletype=routing_profiletype, delete_route_table=delete_route_table, host=host, delete_hardware_profile=delete_hardware_profile, delete_routing_profiletype=delete_routing_profiletype, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    