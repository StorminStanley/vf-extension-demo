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


def interface_gigabitethernet_ip_interface_gi_ospf_conf_ospf_interface_config_md5_authentication_key_table_key_id(**kwargs):
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
            
    ip = ET.SubElement(gigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_gi_ospf_conf = ET.SubElement(ip, "interface-gi-ospf-conf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_interface_gi_ospf_conf', False) is True:
        delete_interface_gi_ospf_conf = config.find('.//*interface-gi-ospf-conf')
        delete_interface_gi_ospf_conf.set('operation', 'delete')
        
    ospf_interface_config = ET.SubElement(interface_gi_ospf_conf, "ospf-interface-config")
    if kwargs.pop('delete_ospf_interface_config', False) is True:
        delete_ospf_interface_config = config.find('.//*ospf-interface-config')
        delete_ospf_interface_config.set('operation', 'delete')
        
    md5_authentication = ET.SubElement(ospf_interface_config, "md5-authentication")
    if kwargs.pop('delete_md5_authentication', False) is True:
        delete_md5_authentication = config.find('.//*md5-authentication')
        delete_md5_authentication.set('operation', 'delete')
        
    key_table = ET.SubElement(md5_authentication, "key-table")
    if kwargs.pop('delete_key_table', False) is True:
        delete_key_table = config.find('.//*key-table')
        delete_key_table.set('operation', 'delete')
        
    key_id = ET.SubElement(key_table, "key-id")
    if kwargs.pop('delete_key_id', False) is True:
        delete_key_id = config.find('.//*key-id')
        delete_key_id.set('operation', 'delete')
        
    key_id.text = kwargs.pop('key_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_ip_interface_gi_ospf_conf_ospf_interface_config_md5_authentication_key_table_key_id_act(Action):
    def run(self, name, delete_ip, delete_interface_gi_ospf_conf, delete_key_table, delete_interface, delete_name, delete_key_id, key_id, delete_gigabitethernet, delete_ospf_interface_config, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_ip_interface_gi_ospf_conf_ospf_interface_config_md5_authentication_key_table_key_id(delete_interface_gi_ospf_conf=delete_interface_gi_ospf_conf, name=name, delete_key_table=delete_key_table, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, key_id=key_id, host=host, delete_gigabitethernet=delete_gigabitethernet, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_key_id=delete_key_id, password=password, callback=_callback, mgr=mgr)
        return 0
    