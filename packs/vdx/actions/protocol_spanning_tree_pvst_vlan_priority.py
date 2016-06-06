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


def protocol_spanning_tree_pvst_vlan_priority(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    spanning_tree = ET.SubElement(protocol, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    pvst = ET.SubElement(spanning_tree, "pvst")
    if kwargs.pop('delete_pvst', False) is True:
        delete_pvst = config.find('.//*pvst')
        delete_pvst.set('operation', 'delete')
        
    vlan = ET.SubElement(pvst, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    id_key = ET.SubElement(vlan, "id")
    id_key.text = kwargs.pop('id')
    if kwargs.pop('delete_id', False) is True:
        delete_id = config.find('.//*id')
        delete_id.set('operation', 'delete')
            
    priority = ET.SubElement(vlan, "priority")
    if kwargs.pop('delete_priority', False) is True:
        delete_priority = config.find('.//*priority')
        delete_priority.set('operation', 'delete')
        
    priority.text = kwargs.pop('priority')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_spanning_tree_pvst_vlan_priority_act(Action):
    def run(self, delete_vlan, priority, delete_protocol, delete_spanning_tree, delete_pvst, delete_id, delete_priority, id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_spanning_tree_pvst_vlan_priority(delete_pvst=delete_pvst, username=username, delete_vlan=delete_vlan, delete_id=delete_id, priority=priority, delete_spanning_tree=delete_spanning_tree, delete_protocol=delete_protocol, host=host, id=id, delete_priority=delete_priority, password=password, callback=_callback, mgr=mgr)
        return 0
    