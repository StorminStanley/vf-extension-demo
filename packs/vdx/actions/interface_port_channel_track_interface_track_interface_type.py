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


def interface_port_channel_track_interface_track_interface_type(**kwargs):
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
            
    track = ET.SubElement(port_channel, "track")
    if kwargs.pop('delete_track', False) is True:
        delete_track = config.find('.//*track')
        delete_track.set('operation', 'delete')
        
    interface = ET.SubElement(track, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    track_interface_name_key = ET.SubElement(interface, "track-interface-name")
    track_interface_name_key.text = kwargs.pop('track_interface_name')
    if kwargs.pop('delete_track_interface_name', False) is True:
        delete_track_interface_name = config.find('.//*track-interface-name')
        delete_track_interface_name.set('operation', 'delete')
            
    track_interface_type = ET.SubElement(interface, "track-interface-type")
    if kwargs.pop('delete_track_interface_type', False) is True:
        delete_track_interface_type = config.find('.//*track-interface-type')
        delete_track_interface_type.set('operation', 'delete')
        
    track_interface_type.text = kwargs.pop('track_interface_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_track_interface_track_interface_type_act(Action):
    def run(self, delete_track_interface_name, name, track_interface_type, track_interface_name, delete_port_channel, delete_interface, delete_name, delete_track_interface_type, delete_track, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_track_interface_track_interface_type(track_interface_type=track_interface_type, delete_track_interface_type=delete_track_interface_type, name=name, delete_name=delete_name, delete_track=delete_track, delete_track_interface_name=delete_track_interface_name, track_interface_name=track_interface_name, delete_port_channel=delete_port_channel, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    