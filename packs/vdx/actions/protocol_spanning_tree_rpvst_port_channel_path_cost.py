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


def protocol_spanning_tree_rpvst_port_channel_path_cost(**kwargs):
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
        
    rpvst = ET.SubElement(spanning_tree, "rpvst")
    if kwargs.pop('delete_rpvst', False) is True:
        delete_rpvst = config.find('.//*rpvst')
        delete_rpvst.set('operation', 'delete')
        
    port_channel = ET.SubElement(rpvst, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    path_cost = ET.SubElement(port_channel, "path-cost")
    if kwargs.pop('delete_path_cost', False) is True:
        delete_path_cost = config.find('.//*path-cost')
        delete_path_cost.set('operation', 'delete')
        
    path_cost.text = kwargs.pop('path_cost')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_spanning_tree_rpvst_port_channel_path_cost_act(Action):
    def run(self, path_cost, delete_protocol, delete_rpvst, delete_path_cost, delete_port_channel, delete_spanning_tree, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_spanning_tree_rpvst_port_channel_path_cost(delete_rpvst=delete_rpvst, path_cost=path_cost, delete_spanning_tree=delete_spanning_tree, delete_port_channel=delete_port_channel, delete_protocol=delete_protocol, delete_path_cost=delete_path_cost, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    