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


def interface_fortygigabitethernet_tunnel_tagged_ieee_bpdu(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    tunnel = ET.SubElement(fortygigabitethernet, "tunnel", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_tunnel', False) is True:
        delete_tunnel = config.find('.//*tunnel')
        delete_tunnel.set('operation', 'delete')
        
    tagged_ieee_bpdu = ET.SubElement(tunnel, "tagged-ieee-bpdu")
    if kwargs.pop('delete_tagged_ieee_bpdu', False) is True:
        delete_tagged_ieee_bpdu = config.find('.//*tagged-ieee-bpdu')
        delete_tagged_ieee_bpdu.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_tunnel_tagged_ieee_bpdu_act(Action):
    def run(self, delete_tagged_ieee_bpdu, name, delete_fortygigabitethernet, delete_tunnel, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_tunnel_tagged_ieee_bpdu(name=name, delete_tagged_ieee_bpdu=delete_tagged_ieee_bpdu, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_tunnel=delete_tunnel, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    