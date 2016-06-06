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


def interface_port_channel_service_policy_in_cg(**kwargs):
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
            
    service_policy = ET.SubElement(port_channel, "service-policy", xmlns="urn:brocade.com:mgmt:brocade-policer")
    if kwargs.pop('delete_service_policy', False) is True:
        delete_service_policy = config.find('.//*service-policy')
        delete_service_policy.set('operation', 'delete')
        
    in_cg = ET.SubElement(service_policy, "in")
    if kwargs.pop('delete_in_cg', False) is True:
        delete_in_cg = config.find('.//*in')
        delete_in_cg.set('operation', 'delete')
        
    in_cg.text = kwargs.pop('in_cg')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_service_policy_in_cg_act(Action):
    def run(self, in_cg, name, delete_service_policy, delete_port_channel, delete_interface, delete_name, delete_in_cg, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_service_policy_in_cg(name=name, delete_name=delete_name, username=username, in_cg=in_cg, delete_port_channel=delete_port_channel, host=host, delete_service_policy=delete_service_policy, delete_interface=delete_interface, delete_in_cg=delete_in_cg, password=password, callback=_callback, mgr=mgr)
        return 0
    