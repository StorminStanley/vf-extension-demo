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


def rbridge_id_interface_loopback_ip_ip_config_address_address(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    loopback = ET.SubElement(interface, "loopback", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
    id_key = ET.SubElement(loopback, "id")
    id_key.text = kwargs.pop('id')
    ip = ET.SubElement(loopback, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    ip_config = ET.SubElement(ip, "ip-config")
    address = ET.SubElement(ip_config, "address")
    address = ET.SubElement(address, "address")
    address.text = kwargs.pop('address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_loopback_ip_ip_config_address_address_act(Action):
    def run(self, rbridge_id, id, address, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.timeout = 600
        rbridge_id_interface_loopback_ip_ip_config_address_address(rbridge_id=rbridge_id, id=id, address=address, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    