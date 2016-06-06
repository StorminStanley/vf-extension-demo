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


def interface_port_channel_vrrp_track_interface_track_priority(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    vrrp = ET.SubElement(port_channel, "vrrp", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_vrrp', False) is True:
        delete_vrrp = config.find('.//*vrrp')
        delete_vrrp.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrp, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    version_key = ET.SubElement(vrrp, "version")
    version_key.text = kwargs.pop('version')
    if kwargs.pop('delete_version', False) is True:
        delete_version = config.find('.//*version')
        delete_version.set('operation', 'delete')
            
    track = ET.SubElement(vrrp, "track")
    if kwargs.pop('delete_track', False) is True:
        delete_track = config.find('.//*track')
        delete_track.set('operation', 'delete')
        
    interface = ET.SubElement(track, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    interface_type_key = ET.SubElement(interface, "interface-type")
    interface_type_key.text = kwargs.pop('interface_type')
    if kwargs.pop('delete_interface_type', False) is True:
        delete_interface_type = config.find('.//*interface-type')
        delete_interface_type.set('operation', 'delete')
            
    interface_name_key = ET.SubElement(interface, "interface-name")
    interface_name_key.text = kwargs.pop('interface_name')
    if kwargs.pop('delete_interface_name', False) is True:
        delete_interface_name = config.find('.//*interface-name')
        delete_interface_name.set('operation', 'delete')
            
    track_priority = ET.SubElement(interface, "track-priority")
    if kwargs.pop('delete_track_priority', False) is True:
        delete_track_priority = config.find('.//*track-priority')
        delete_track_priority.set('operation', 'delete')
        
    track_priority.text = kwargs.pop('track_priority')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_vrrp_track_interface_track_priority_act(Action):
    def run(self, delete_track_priority, delete_interface_name, name, delete_vrid, interface_type, vrid, delete_version, delete_interface_type, delete_port_channel, version, delete_interface, delete_name, delete_vrrp, interface_name, delete_track, track_priority, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_vrrp_track_interface_track_priority(delete_vrid=delete_vrid, version=version, name=name, delete_version=delete_version, delete_track=delete_track, username=username, interface_name=interface_name, delete_track_priority=delete_track_priority, delete_vrrp=delete_vrrp, delete_port_channel=delete_port_channel, delete_interface_type=delete_interface_type, delete_interface_name=delete_interface_name, host=host, vrid=vrid, interface_type=interface_type, delete_name=delete_name, delete_interface=delete_interface, track_priority=track_priority, password=password, callback=_callback, mgr=mgr)
        return 0
    