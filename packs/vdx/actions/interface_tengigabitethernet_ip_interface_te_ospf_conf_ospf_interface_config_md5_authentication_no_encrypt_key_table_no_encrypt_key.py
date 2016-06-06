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


def interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_md5_authentication_no_encrypt_key_table_no_encrypt_key(**kwargs):
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
            
    ip = ET.SubElement(tengigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_te_ospf_conf = ET.SubElement(ip, "interface-te-ospf-conf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_interface_te_ospf_conf', False) is True:
        delete_interface_te_ospf_conf = config.find('.//*interface-te-ospf-conf')
        delete_interface_te_ospf_conf.set('operation', 'delete')
        
    ospf_interface_config = ET.SubElement(interface_te_ospf_conf, "ospf-interface-config")
    if kwargs.pop('delete_ospf_interface_config', False) is True:
        delete_ospf_interface_config = config.find('.//*ospf-interface-config')
        delete_ospf_interface_config.set('operation', 'delete')
        
    md5_authentication = ET.SubElement(ospf_interface_config, "md5-authentication")
    if kwargs.pop('delete_md5_authentication', False) is True:
        delete_md5_authentication = config.find('.//*md5-authentication')
        delete_md5_authentication.set('operation', 'delete')
        
    no_encrypt_key_table = ET.SubElement(md5_authentication, "no-encrypt-key-table")
    if kwargs.pop('delete_no_encrypt_key_table', False) is True:
        delete_no_encrypt_key_table = config.find('.//*no-encrypt-key-table')
        delete_no_encrypt_key_table.set('operation', 'delete')
        
    no_encrypt_key = ET.SubElement(no_encrypt_key_table, "no-encrypt-key")
    if kwargs.pop('delete_no_encrypt_key', False) is True:
        delete_no_encrypt_key = config.find('.//*no-encrypt-key')
        delete_no_encrypt_key.set('operation', 'delete')
        
    no_encrypt_key.text = kwargs.pop('no_encrypt_key')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_md5_authentication_no_encrypt_key_table_no_encrypt_key_act(Action):
    def run(self, delete_interface_te_ospf_conf, name, delete_ip, delete_no_encrypt_key_table, delete_no_encrypt_key, delete_interface, delete_name, delete_tengigabitethernet, no_encrypt_key, delete_ospf_interface_config, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_md5_authentication_no_encrypt_key_table_no_encrypt_key(name=name, delete_no_encrypt_key_table=delete_no_encrypt_key_table, username=username, delete_tengigabitethernet=delete_tengigabitethernet, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, delete_no_encrypt_key=delete_no_encrypt_key, host=host, delete_name=delete_name, delete_interface=delete_interface, delete_interface_te_ospf_conf=delete_interface_te_ospf_conf, no_encrypt_key=no_encrypt_key, password=password, callback=_callback, mgr=mgr)
        return 0
    