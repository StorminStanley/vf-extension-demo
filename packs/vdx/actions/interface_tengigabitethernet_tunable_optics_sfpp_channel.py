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


def interface_tengigabitethernet_tunable_optics_sfpp_channel(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    tengigabitethernet = ET.SubElement(interface, "tengigabitethernet")
    if kwargs.pop('delete_tengigabitethernet', False) is True:
        delete_tengigabitethernet = config.find('.//*tengigabitethernet')
        delete_tengigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(tengigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    tunable_optics = ET.SubElement(tengigabitethernet, "tunable-optics")
    if kwargs.pop('delete_tunable_optics', False) is True:
        delete_tunable_optics = config.find('.//*tunable-optics')
        delete_tunable_optics.set('operation', 'delete')
        
    sfpp = ET.SubElement(tunable_optics, "sfpp")
    if kwargs.pop('delete_sfpp', False) is True:
        delete_sfpp = config.find('.//*sfpp')
        delete_sfpp.set('operation', 'delete')
        
    channel = ET.SubElement(sfpp, "channel")
    if kwargs.pop('delete_channel', False) is True:
        delete_channel = config.find('.//*channel')
        delete_channel.set('operation', 'delete')
        
    channel.text = kwargs.pop('channel')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_tunable_optics_sfpp_channel_act(Action):
    def run(self, name, delete_sfpp, delete_interface, delete_name, delete_tunable_optics, delete_tengigabitethernet, delete_channel, channel, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_tunable_optics_sfpp_channel(delete_tunable_optics=delete_tunable_optics, name=name, delete_name=delete_name, delete_channel=delete_channel, channel=channel, delete_tengigabitethernet=delete_tengigabitethernet, delete_sfpp=delete_sfpp, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    