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


def interface_tengigabitethernet_spanning_tree_instance_restricted_tcn(**kwargs):
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
            
    spanning_tree = ET.SubElement(tengigabitethernet, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    instance = ET.SubElement(spanning_tree, "instance")
    if kwargs.pop('delete_instance', False) is True:
        delete_instance = config.find('.//*instance')
        delete_instance.set('operation', 'delete')
        
    id_key = ET.SubElement(instance, "id")
    id_key.text = kwargs.pop('id')
    if kwargs.pop('delete_id', False) is True:
        delete_id = config.find('.//*id')
        delete_id.set('operation', 'delete')
            
    restricted_tcn = ET.SubElement(instance, "restricted-tcn")
    if kwargs.pop('delete_restricted_tcn', False) is True:
        delete_restricted_tcn = config.find('.//*restricted-tcn')
        delete_restricted_tcn.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_spanning_tree_instance_restricted_tcn_act(Action):
    def run(self, name, delete_id, id, delete_instance, delete_restricted_tcn, delete_interface, delete_name, delete_tengigabitethernet, delete_spanning_tree, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_spanning_tree_instance_restricted_tcn(delete_instance=delete_instance, name=name, delete_name=delete_name, delete_restricted_tcn=delete_restricted_tcn, delete_id=delete_id, delete_spanning_tree=delete_spanning_tree, delete_tengigabitethernet=delete_tengigabitethernet, host=host, id=id, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    