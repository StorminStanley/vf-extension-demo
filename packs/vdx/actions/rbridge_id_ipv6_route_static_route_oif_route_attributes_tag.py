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


def rbridge_id_ipv6_route_static_route_oif_route_attributes_tag(**kwargs):
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
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    route = ET.SubElement(ipv6, "route", xmlns="urn:brocade.com:mgmt:brocade-ipv6-rtm")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    static_route_oif = ET.SubElement(route, "static-route-oif")
    if kwargs.pop('delete_static_route_oif', False) is True:
        delete_static_route_oif = config.find('.//*static-route-oif')
        delete_static_route_oif.set('operation', 'delete')
        
    static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
    static_route_dest_key.text = kwargs.pop('static_route_dest')
    if kwargs.pop('delete_static_route_dest', False) is True:
        delete_static_route_dest = config.find('.//*static-route-dest')
        delete_static_route_dest.set('operation', 'delete')
            
    static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
    static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
    if kwargs.pop('delete_static_route_oif_type', False) is True:
        delete_static_route_oif_type = config.find('.//*static-route-oif-type')
        delete_static_route_oif_type.set('operation', 'delete')
            
    static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
    static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
    if kwargs.pop('delete_static_route_oif_name', False) is True:
        delete_static_route_oif_name = config.find('.//*static-route-oif-name')
        delete_static_route_oif_name.set('operation', 'delete')
            
    route_attributes = ET.SubElement(static_route_oif, "route-attributes")
    if kwargs.pop('delete_route_attributes', False) is True:
        delete_route_attributes = config.find('.//*route-attributes')
        delete_route_attributes.set('operation', 'delete')
        
    tag = ET.SubElement(route_attributes, "tag")
    if kwargs.pop('delete_tag', False) is True:
        delete_tag = config.find('.//*tag')
        delete_tag.set('operation', 'delete')
        
    tag.text = kwargs.pop('tag')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_route_static_route_oif_route_attributes_tag_act(Action):
    def run(self, delete_static_route_oif, delete_route_attributes, static_route_oif_type, rbridge_id, delete_static_route_oif_type, delete_route, delete_static_route_oif_name, tag, delete_static_route_dest, static_route_dest, static_route_oif_name, delete_rbridge_id, delete_tag, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_route_static_route_oif_route_attributes_tag(delete_route_attributes=delete_route_attributes, delete_tag=delete_tag, delete_static_route_oif_name=delete_static_route_oif_name, delete_route=delete_route, username=username, tag=tag, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_static_route_oif=delete_static_route_oif, delete_static_route_oif_type=delete_static_route_oif_type, host=host, static_route_oif_type=static_route_oif_type, static_route_oif_name=static_route_oif_name, static_route_dest=static_route_dest, delete_static_route_dest=delete_static_route_dest, password=password, callback=_callback, mgr=mgr)
        return 0
    