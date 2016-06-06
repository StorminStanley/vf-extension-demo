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


def interface_port_channel_port_profile_to_interface_associations_port_profile_port_port_to_port_profile_associations_port_to_port_profile_association(**kwargs):
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
            
    port_profile_to_interface_associations = ET.SubElement(port_channel, "port-profile-to-interface-associations", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
    if kwargs.pop('delete_port_profile_to_interface_associations', False) is True:
        delete_port_profile_to_interface_associations = config.find('.//*port-profile-to-interface-associations')
        delete_port_profile_to_interface_associations.set('operation', 'delete')
        
    port_profile_port = ET.SubElement(port_profile_to_interface_associations, "port-profile-port")
    if kwargs.pop('delete_port_profile_port', False) is True:
        delete_port_profile_port = config.find('.//*port-profile-port')
        delete_port_profile_port.set('operation', 'delete')
        
    port_to_port_profile_associations = ET.SubElement(port_profile_port, "port-to-port-profile-associations")
    if kwargs.pop('delete_port_to_port_profile_associations', False) is True:
        delete_port_to_port_profile_associations = config.find('.//*port-to-port-profile-associations')
        delete_port_to_port_profile_associations.set('operation', 'delete')
        
    port_to_port_profile_association = ET.SubElement(port_to_port_profile_associations, "port-to-port-profile-association")
    if kwargs.pop('delete_port_to_port_profile_association', False) is True:
        delete_port_to_port_profile_association = config.find('.//*port-to-port-profile-association')
        delete_port_to_port_profile_association.set('operation', 'delete')
        
    port_to_port_profile_association.text = kwargs.pop('port_to_port_profile_association')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_port_profile_to_interface_associations_port_profile_port_port_to_port_profile_associations_port_to_port_profile_association_act(Action):
    def run(self, delete_port_to_port_profile_associations, name, delete_port_to_port_profile_association, delete_port_profile_to_interface_associations, delete_port_channel, delete_port_profile_port, delete_interface, delete_name, port_to_port_profile_association, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_port_profile_to_interface_associations_port_profile_port_port_to_port_profile_associations_port_to_port_profile_association(name=name, delete_port_to_port_profile_associations=delete_port_to_port_profile_associations, delete_port_profile_port=delete_port_profile_port, delete_port_channel=delete_port_channel, delete_port_profile_to_interface_associations=delete_port_profile_to_interface_associations, host=host, port_to_port_profile_association=port_to_port_profile_association, delete_port_to_port_profile_association=delete_port_to_port_profile_association, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    