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


def interface_fortygigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_network(**kwargs):
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
            
    ip = ET.SubElement(fortygigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_fo_ospf_conf = ET.SubElement(ip, "interface-fo-ospf-conf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_interface_fo_ospf_conf', False) is True:
        delete_interface_fo_ospf_conf = config.find('.//*interface-fo-ospf-conf')
        delete_interface_fo_ospf_conf.set('operation', 'delete')
        
    ospf_interface_config = ET.SubElement(interface_fo_ospf_conf, "ospf-interface-config")
    if kwargs.pop('delete_ospf_interface_config', False) is True:
        delete_ospf_interface_config = config.find('.//*ospf-interface-config')
        delete_ospf_interface_config.set('operation', 'delete')
        
    network = ET.SubElement(ospf_interface_config, "network")
    if kwargs.pop('delete_network', False) is True:
        delete_network = config.find('.//*network')
        delete_network.set('operation', 'delete')
        
    network.text = kwargs.pop('network')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_network_act(Action):
    def run(self, name, delete_ip, delete_interface_fo_ospf_conf, delete_fortygigabitethernet, delete_network, delete_interface, delete_name, network, delete_ospf_interface_config, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_network(name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, delete_interface_fo_ospf_conf=delete_interface_fo_ospf_conf, host=host, delete_network=delete_network, delete_name=delete_name, delete_interface=delete_interface, network=network, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    