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


def rbridge_id_ip_dhcp_relay_information_option(**kwargs):
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
            
    ip = ET.SubElement(rbridge_id, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    dhcp = ET.SubElement(ip, "dhcp", xmlns="urn:brocade.com:mgmt:brocade-dhcp")
    if kwargs.pop('delete_dhcp', False) is True:
        delete_dhcp = config.find('.//*dhcp')
        delete_dhcp.set('operation', 'delete')
        
    relay = ET.SubElement(dhcp, "relay")
    if kwargs.pop('delete_relay', False) is True:
        delete_relay = config.find('.//*relay')
        delete_relay.set('operation', 'delete')
        
    information = ET.SubElement(relay, "information")
    if kwargs.pop('delete_information', False) is True:
        delete_information = config.find('.//*information')
        delete_information.set('operation', 'delete')
        
    option = ET.SubElement(information, "option")
    if kwargs.pop('delete_option', False) is True:
        delete_option = config.find('.//*option')
        delete_option.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_dhcp_relay_information_option_act(Action):
    def run(self, rbridge_id, delete_ip, delete_option, delete_information, delete_dhcp, delete_relay, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_dhcp_relay_information_option(delete_option=delete_option, delete_relay=delete_relay, username=username, delete_ip=delete_ip, rbridge_id=rbridge_id, delete_dhcp=delete_dhcp, delete_information=delete_information, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    