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


def rbridge_id_evpn_instance_route_target_imprt_ignore_as(**kwargs):
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
            
    evpn_instance = ET.SubElement(rbridge_id, "evpn-instance", xmlns="urn:brocade.com:mgmt:brocade-bgp")
    if kwargs.pop('delete_evpn_instance', False) is True:
        delete_evpn_instance = config.find('.//*evpn-instance')
        delete_evpn_instance.set('operation', 'delete')
        
    instance_name_key = ET.SubElement(evpn_instance, "instance-name")
    instance_name_key.text = kwargs.pop('instance_name')
    if kwargs.pop('delete_instance_name', False) is True:
        delete_instance_name = config.find('.//*instance-name')
        delete_instance_name.set('operation', 'delete')
            
    route_target = ET.SubElement(evpn_instance, "route-target")
    if kwargs.pop('delete_route_target', False) is True:
        delete_route_target = config.find('.//*route-target')
        delete_route_target.set('operation', 'delete')
        
    imprt = ET.SubElement(route_target, "import")
    if kwargs.pop('delete_imprt', False) is True:
        delete_imprt = config.find('.//*import')
        delete_imprt.set('operation', 'delete')
        
    target_community_key = ET.SubElement(imprt, "target-community")
    target_community_key.text = kwargs.pop('target_community')
    if kwargs.pop('delete_target_community', False) is True:
        delete_target_community = config.find('.//*target-community')
        delete_target_community.set('operation', 'delete')
            
    ignore_as = ET.SubElement(imprt, "ignore-as")
    if kwargs.pop('delete_ignore_as', False) is True:
        delete_ignore_as = config.find('.//*ignore-as')
        delete_ignore_as.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_evpn_instance_route_target_imprt_ignore_as_act(Action):
    def run(self, delete_evpn_instance, rbridge_id, target_community, delete_target_community, delete_instance_name, instance_name, delete_imprt, delete_rbridge_id, delete_route_target, delete_ignore_as, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_evpn_instance_route_target_imprt_ignore_as(delete_target_community=delete_target_community, delete_route_target=delete_route_target, delete_evpn_instance=delete_evpn_instance, instance_name=instance_name, username=username, rbridge_id=rbridge_id, delete_imprt=delete_imprt, delete_instance_name=delete_instance_name, host=host, target_community=target_community, delete_rbridge_id=delete_rbridge_id, delete_ignore_as=delete_ignore_as, password=password, callback=_callback, mgr=mgr)
        return 0
    