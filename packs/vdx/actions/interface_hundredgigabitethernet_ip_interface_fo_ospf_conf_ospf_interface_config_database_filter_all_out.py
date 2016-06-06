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


def interface_hundredgigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_database_filter_all_out(**kwargs):
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
            
    ip = ET.SubElement(hundredgigabitethernet, "ip")
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
        
    database_filter = ET.SubElement(ospf_interface_config, "database-filter")
    if kwargs.pop('delete_database_filter', False) is True:
        delete_database_filter = config.find('.//*database-filter')
        delete_database_filter.set('operation', 'delete')
        
    all_out = ET.SubElement(database_filter, "all-out")
    if kwargs.pop('delete_all_out', False) is True:
        delete_all_out = config.find('.//*all-out')
        delete_all_out.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_database_filter_all_out_act(Action):
    def run(self, name, delete_ip, delete_interface_fo_ospf_conf, delete_database_filter, delete_interface, delete_name, delete_hundredgigabitethernet, delete_all_out, delete_ospf_interface_config, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ip_interface_fo_ospf_conf_ospf_interface_config_database_filter_all_out(delete_database_filter=delete_database_filter, name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_all_out=delete_all_out, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, delete_interface_fo_ospf_conf=delete_interface_fo_ospf_conf, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    