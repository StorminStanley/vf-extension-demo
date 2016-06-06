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


def interface_fortygigabitethernet_dot1x_agtimeout_re_authperiod(**kwargs):
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
            
    dot1x = ET.SubElement(fortygigabitethernet, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
    if kwargs.pop('delete_dot1x', False) is True:
        delete_dot1x = config.find('.//*dot1x')
        delete_dot1x.set('operation', 'delete')
        
    agtimeout = ET.SubElement(dot1x, "agtimeout")
    if kwargs.pop('delete_agtimeout', False) is True:
        delete_agtimeout = config.find('.//*agtimeout')
        delete_agtimeout.set('operation', 'delete')
        
    re_authperiod = ET.SubElement(agtimeout, "re-authperiod")
    if kwargs.pop('delete_re_authperiod', False) is True:
        delete_re_authperiod = config.find('.//*re-authperiod')
        delete_re_authperiod.set('operation', 'delete')
        
    re_authperiod.text = kwargs.pop('re_authperiod')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_dot1x_agtimeout_re_authperiod_act(Action):
    def run(self, delete_re_authperiod, name, delete_fortygigabitethernet, re_authperiod, delete_agtimeout, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_dot1x_agtimeout_re_authperiod(name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_re_authperiod=delete_re_authperiod, delete_agtimeout=delete_agtimeout, re_authperiod=re_authperiod, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    