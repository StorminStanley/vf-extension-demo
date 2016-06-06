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


def interface_fortygigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_ah_algorithm_ah_key(**kwargs):
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
            
    ipv6 = ET.SubElement(fortygigabitethernet, "ipv6")
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
        
    ca_ah_algorithm = ET.SubElement(ch_algorithm, "ca-ah-algorithm")
    if kwargs.pop('delete_ca_ah_algorithm', False) is True:
        delete_ca_ah_algorithm = config.find('.//*ca-ah-algorithm')
        delete_ca_ah_algorithm.set('operation', 'delete')
        
    ah_key = ET.SubElement(ca_ah_algorithm, "ah-key")
    if kwargs.pop('delete_ah_key', False) is True:
        delete_ah_key = config.find('.//*ah-key')
        delete_ah_key.set('operation', 'delete')
        
    ah_key.text = kwargs.pop('ah_key')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_ah_algorithm_ah_key_act(Action):
    def run(self, name, delete_ipsec_auth_key_config, delete_fortygigabitethernet, delete_ca_ah_algorithm, delete_ah_key, delete_authentication, delete_name, delete_ch_algorithm, ah_key, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_auth_key_config_ch_algorithm_ca_ah_algorithm_ah_key(delete_ca_ah_algorithm=delete_ca_ah_algorithm, name=name, delete_ah_key=delete_ah_key, delete_name=delete_name, delete_ipsec_auth_key_config=delete_ipsec_auth_key_config, delete_authentication=delete_authentication, host=host, delete_ch_algorithm=delete_ch_algorithm, delete_fortygigabitethernet=delete_fortygigabitethernet, ah_key=ah_key, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    