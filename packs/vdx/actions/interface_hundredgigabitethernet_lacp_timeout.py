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


def interface_hundredgigabitethernet_lacp_agtimeout(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    lacp = ET.SubElement(hundredgigabitethernet, "lacp", xmlns="urn:brocade.com:mgmt:brocade-lacp")
    if kwargs.pop('delete_lacp', False) is True:
        delete_lacp = config.find('.//*lacp')
        delete_lacp.set('operation', 'delete')
        
    agtimeout = ET.SubElement(lacp, "agtimeout")
    if kwargs.pop('delete_agtimeout', False) is True:
        delete_agtimeout = config.find('.//*agtimeout')
        delete_agtimeout.set('operation', 'delete')
        
    agtimeout.text = kwargs.pop('agtimeout')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_lacp_agtimeout_act(Action):
    def run(self, name, delete_lacp, delete_agtimeout, delete_interface, delete_name, delete_hundredgigabitethernet, host, username, password, agtimeout_ag):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_lacp_agtimeout(agtimeout_ag=agtimeout_ag, name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_agtimeout=delete_agtimeout, delete_lacp=delete_lacp, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    