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


def interface_hundredgigabitethernet_ipv6_interface_ospfv3_conf_cost(**kwargs):
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
            
    ipv6 = ET.SubElement(hundredgigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    interface_ospfv3_conf = ET.SubElement(ipv6, "interface-ospfv3-conf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_interface_ospfv3_conf', False) is True:
        delete_interface_ospfv3_conf = config.find('.//*interface-ospfv3-conf')
        delete_interface_ospfv3_conf.set('operation', 'delete')
        
    cost = ET.SubElement(interface_ospfv3_conf, "cost")
    if kwargs.pop('delete_cost', False) is True:
        delete_cost = config.find('.//*cost')
        delete_cost.set('operation', 'delete')
        
    cost.text = kwargs.pop('cost')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ipv6_interface_ospfv3_conf_cost_act(Action):
    def run(self, name, delete_cost, cost, delete_interface, delete_name, delete_hundredgigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ipv6_interface_ospfv3_conf_cost(delete_cost=delete_cost, name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, cost=cost, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    