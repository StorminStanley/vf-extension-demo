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


def rbridge_id_interface_ve_ip_interface_vlan_ospf_conf_ospf_interface_config_authentication_key_auth_key_table_encrypttype(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(ve, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_vlan_ospf_conf = ET.SubElement(ip, "interface-vlan-ospf-conf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_interface_vlan_ospf_conf', False) is True:
        delete_interface_vlan_ospf_conf = config.find('.//*interface-vlan-ospf-conf')
        delete_interface_vlan_ospf_conf.set('operation', 'delete')
        
    ospf_interface_config = ET.SubElement(interface_vlan_ospf_conf, "ospf-interface-config")
    if kwargs.pop('delete_ospf_interface_config', False) is True:
        delete_ospf_interface_config = config.find('.//*ospf-interface-config')
        delete_ospf_interface_config.set('operation', 'delete')
        
    authentication_key = ET.SubElement(ospf_interface_config, "authentication-key")
    if kwargs.pop('delete_authentication_key', False) is True:
        delete_authentication_key = config.find('.//*authentication-key')
        delete_authentication_key.set('operation', 'delete')
        
    auth_key_table = ET.SubElement(authentication_key, "auth-key-table")
    if kwargs.pop('delete_auth_key_table', False) is True:
        delete_auth_key_table = config.find('.//*auth-key-table')
        delete_auth_key_table.set('operation', 'delete')
        
    encrypttype = ET.SubElement(auth_key_table, "encrypttype")
    if kwargs.pop('delete_encrypttype', False) is True:
        delete_encrypttype = config.find('.//*encrypttype')
        delete_encrypttype.set('operation', 'delete')
        
    encrypttype.text = kwargs.pop('encrypttype')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_ip_interface_vlan_ospf_conf_ospf_interface_config_authentication_key_auth_key_table_encrypttype_act(Action):
    def run(self, encrypttype, name, delete_ip, delete_encrypttype, delete_authentication_key, delete_ve, delete_interface_vlan_ospf_conf, delete_interface, delete_name, delete_rbridge_id, delete_ospf_interface_config, delete_auth_key_table, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_ip_interface_vlan_ospf_conf_ospf_interface_config_authentication_key_auth_key_table_encrypttype(encrypttype=encrypttype, name=name, delete_name=delete_name, delete_authentication_key=delete_authentication_key, username=username, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, delete_interface_vlan_ospf_conf=delete_interface_vlan_ospf_conf, delete_ve=delete_ve, host=host, delete_auth_key_table=delete_auth_key_table, delete_encrypttype=delete_encrypttype, delete_rbridge_id=delete_rbridge_id, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    