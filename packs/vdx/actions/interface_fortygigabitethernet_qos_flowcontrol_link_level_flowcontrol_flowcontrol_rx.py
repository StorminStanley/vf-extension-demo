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


def interface_fortygigabitethernet_qos_flowcontrol_link_level_flowcontrol_flowcontrol_rx(**kwargs):
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
            
    qos = ET.SubElement(fortygigabitethernet, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
    if kwargs.pop('delete_qos', False) is True:
        delete_qos = config.find('.//*qos')
        delete_qos.set('operation', 'delete')
        
    flowcontrol = ET.SubElement(qos, "flowcontrol")
    if kwargs.pop('delete_flowcontrol', False) is True:
        delete_flowcontrol = config.find('.//*flowcontrol')
        delete_flowcontrol.set('operation', 'delete')
        
    link_level_flowcontrol = ET.SubElement(flowcontrol, "link-level-flowcontrol")
    if kwargs.pop('delete_link_level_flowcontrol', False) is True:
        delete_link_level_flowcontrol = config.find('.//*link-level-flowcontrol')
        delete_link_level_flowcontrol.set('operation', 'delete')
        
    flowcontrol_rx = ET.SubElement(link_level_flowcontrol, "flowcontrol-rx")
    if kwargs.pop('delete_flowcontrol_rx', False) is True:
        delete_flowcontrol_rx = config.find('.//*flowcontrol-rx')
        delete_flowcontrol_rx.set('operation', 'delete')
        
    flowcontrol_rx.text = kwargs.pop('flowcontrol_rx')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_qos_flowcontrol_link_level_flowcontrol_flowcontrol_rx_act(Action):
    def run(self, delete_qos, name, flowcontrol_rx, delete_fortygigabitethernet, delete_flowcontrol, delete_link_level_flowcontrol, delete_interface, delete_name, delete_flowcontrol_rx, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_qos_flowcontrol_link_level_flowcontrol_flowcontrol_rx(delete_link_level_flowcontrol=delete_link_level_flowcontrol, delete_qos=delete_qos, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_flowcontrol_rx=delete_flowcontrol_rx, delete_flowcontrol=delete_flowcontrol, host=host, flowcontrol_rx=flowcontrol_rx, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, name=name, callback=_callback, mgr=mgr)
        return 0
    