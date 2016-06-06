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


def interface_gigabitethernet_sflow_polling_interval(**kwargs):
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
            
    sflow = ET.SubElement(gigabitethernet, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
    if kwargs.pop('delete_sflow', False) is True:
        delete_sflow = config.find('.//*sflow')
        delete_sflow.set('operation', 'delete')
        
    polling_interval = ET.SubElement(sflow, "polling-interval")
    if kwargs.pop('delete_polling_interval', False) is True:
        delete_polling_interval = config.find('.//*polling-interval')
        delete_polling_interval.set('operation', 'delete')
        
    polling_interval.text = kwargs.pop('polling_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_sflow_polling_interval_act(Action):
    def run(self, delete_sflow, delete_polling_interval, name, delete_interface, delete_name, polling_interval, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_sflow_polling_interval(name=name, delete_name=delete_name, delete_sflow=delete_sflow, delete_polling_interval=delete_polling_interval, host=host, password=password, delete_gigabitethernet=delete_gigabitethernet, delete_interface=delete_interface, username=username, polling_interval=polling_interval, callback=_callback, mgr=mgr)
        return 0
    