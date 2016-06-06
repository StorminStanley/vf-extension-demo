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


def interface_fortygigabitethernet_openflow_interface_cfg_logical_instance_id(**kwargs):
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
            
    openflow_interface_cfg = ET.SubElement(fortygigabitethernet, "openflow-interface-cfg", xmlns="urn:brocade.com:mgmt:brocade-openflow")
    if kwargs.pop('delete_openflow_interface_cfg', False) is True:
        delete_openflow_interface_cfg = config.find('.//*openflow-interface-cfg')
        delete_openflow_interface_cfg.set('operation', 'delete')
        
    logical_instance_id = ET.SubElement(openflow_interface_cfg, "logical-instance-id")
    if kwargs.pop('delete_logical_instance_id', False) is True:
        delete_logical_instance_id = config.find('.//*logical-instance-id')
        delete_logical_instance_id.set('operation', 'delete')
        
    logical_instance_id.text = kwargs.pop('logical_instance_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_openflow_interface_cfg_logical_instance_id_act(Action):
    def run(self, name, delete_fortygigabitethernet, delete_logical_instance_id, delete_openflow_interface_cfg, logical_instance_id, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_openflow_interface_cfg_logical_instance_id(name=name, delete_openflow_interface_cfg=delete_openflow_interface_cfg, delete_name=delete_name, delete_logical_instance_id=delete_logical_instance_id, host=host, logical_instance_id=logical_instance_id, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    