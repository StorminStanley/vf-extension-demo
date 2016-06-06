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


def interface_tengigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_key(**kwargs):
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
            
    ipv6 = ET.SubElement(tengigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    interface_ospfv3_conf = ET.SubElement(ipv6, "interface-ospfv3-conf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_interface_ospfv3_conf', False) is True:
        delete_interface_ospfv3_conf = config.find('.//*interface-ospfv3-conf')
        delete_interface_ospfv3_conf.set('operation', 'delete')
        
    authentication = ET.SubElement(interface_ospfv3_conf, "authentication")
    if kwargs.pop('delete_authentication', False) is True:
        delete_authentication = config.find('.//*authentication')
        delete_authentication.set('operation', 'delete')
        
    ipsec_auth_key_config = ET.SubElement(authentication, "ipsec-auth-key-config")
    if kwargs.pop('delete_ipsec_auth_key_config', False) is True:
        delete_ipsec_auth_key_config = config.find('.//*ipsec-auth-key-config')
        delete_ipsec_auth_key_config.set('operation', 'delete')
        
    ch_algorithm = ET.SubElement(ipsec_auth_key_config, "ch-algorithm")
    if kwargs.pop('delete_ch_algorithm', False) is True:
        delete_ch_algorithm = config.find('.//*ch-algorithm')
        delete_ch_algorithm.set('operation', 'delete')
        
    ca_esp_algorithm = ET.SubElement(ch_algorithm, "ca-esp-algorithm")
    if kwargs.pop('delete_ca_esp_algorithm', False) is True:
        delete_ca_esp_algorithm = config.find('.//*ca-esp-algorithm')
        delete_ca_esp_algorithm.set('operation', 'delete')
        
    esp_key = ET.SubElement(ca_esp_algorithm, "esp-key")
    if kwargs.pop('delete_esp_key', False) is True:
        delete_esp_key = config.find('.//*esp-key')
        delete_esp_key.set('operation', 'delete')
        
    esp_key.text = kwargs.pop('esp_key')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_key_act(Action):
    def run(self, name, esp_key, delete_ipsec_auth_key_config, delete_ca_esp_algorithm, delete_authentication, delete_name, delete_tengigabitethernet, delete_ch_algorithm, delete_esp_key, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_esp_algorithm_esp_key(delete_ca_esp_algorithm=delete_ca_esp_algorithm, delete_ipsec_auth_key_config=delete_ipsec_auth_key_config, name=name, delete_name=delete_name, username=username, esp_key=esp_key, delete_authentication=delete_authentication, host=host, delete_ch_algorithm=delete_ch_algorithm, delete_tengigabitethernet=delete_tengigabitethernet, delete_interface=delete_interface, delete_esp_key=delete_esp_key, password=password, callback=_callback, mgr=mgr)
        return 0
    