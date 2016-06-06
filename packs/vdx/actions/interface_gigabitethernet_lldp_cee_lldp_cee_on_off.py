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


def interface_gigabitethernet_lldp_cee_lldp_cee_on_off(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    gigabitethernet = ET.SubElement(interface, "gigabitethernet")
    if kwargs.pop('delete_gigabitethernet', False) is True:
        delete_gigabitethernet = config.find('.//*gigabitethernet')
        delete_gigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(gigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    lldp = ET.SubElement(gigabitethernet, "lldp", xmlns="urn:brocade.com:mgmt:brocade-lldp")
    if kwargs.pop('delete_lldp', False) is True:
        delete_lldp = config.find('.//*lldp')
        delete_lldp.set('operation', 'delete')
        
    cee = ET.SubElement(lldp, "cee")
    if kwargs.pop('delete_cee', False) is True:
        delete_cee = config.find('.//*cee')
        delete_cee.set('operation', 'delete')
        
    lldp_cee_on_off = ET.SubElement(cee, "lldp-cee-on-off")
    if kwargs.pop('delete_lldp_cee_on_off', False) is True:
        delete_lldp_cee_on_off = config.find('.//*lldp-cee-on-off')
        delete_lldp_cee_on_off.set('operation', 'delete')
        
    lldp_cee_on_off.text = kwargs.pop('lldp_cee_on_off')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_lldp_cee_lldp_cee_on_off_act(Action):
    def run(self, name, delete_cee, delete_lldp, delete_lldp_cee_on_off, delete_interface, delete_name, lldp_cee_on_off, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_lldp_cee_lldp_cee_on_off(name=name, delete_name=delete_name, delete_lldp=delete_lldp, username=username, delete_cee=delete_cee, delete_lldp_cee_on_off=delete_lldp_cee_on_off, host=host, delete_gigabitethernet=delete_gigabitethernet, delete_interface=delete_interface, lldp_cee_on_off=lldp_cee_on_off, password=password, callback=_callback, mgr=mgr)
        return 0
    