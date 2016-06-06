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


def overlay_gateway_map_vlan_vni_auto(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
    if kwargs.pop('delete_overlay_gateway', False) is True:
        delete_overlay_gateway = config.find('.//*overlay-gateway')
        delete_overlay_gateway.set('operation', 'delete')
        
    name_key = ET.SubElement(overlay_gateway, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    map = ET.SubElement(overlay_gateway, "map")
    if kwargs.pop('delete_map', False) is True:
        delete_map = config.find('.//*map')
        delete_map.set('operation', 'delete')
        
    vlan = ET.SubElement(map, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    vni = ET.SubElement(vlan, "vni")
    if kwargs.pop('delete_vni', False) is True:
        delete_vni = config.find('.//*vni')
        delete_vni.set('operation', 'delete')
        
    auto = ET.SubElement(vni, "auto")
    if kwargs.pop('delete_auto', False) is True:
        delete_auto = config.find('.//*auto')
        delete_auto.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class overlay_gateway_map_vlan_vni_auto_act(Action):
    def run(self, delete_vlan, name, delete_map, delete_auto, delete_vni, delete_name, delete_overlay_gateway, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        overlay_gateway_map_vlan_vni_auto(name=name, delete_name=delete_name, delete_vlan=delete_vlan, delete_overlay_gateway=delete_overlay_gateway, delete_auto=delete_auto, delete_vni=delete_vni, delete_map=delete_map, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    