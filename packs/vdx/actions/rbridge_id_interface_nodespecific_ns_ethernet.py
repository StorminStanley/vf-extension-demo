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


def rbridge_id_interface_nodespecific_ns_ethernet(**kwargs):
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
            
    interface_nodespecific = ET.SubElement(rbridge_id, "interface-nodespecific")
    if kwargs.pop('delete_interface_nodespecific', False) is True:
        delete_interface_nodespecific = config.find('.//*interface-nodespecific')
        delete_interface_nodespecific.set('operation', 'delete')
        
    ns_ethernet = ET.SubElement(interface_nodespecific, "ns-ethernet")
    if kwargs.pop('delete_ns_ethernet', False) is True:
        delete_ns_ethernet = config.find('.//*ns-ethernet')
        delete_ns_ethernet.set('operation', 'delete')
        
    ns_ethernet.text = kwargs.pop('ns_ethernet')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_nodespecific_ns_ethernet_act(Action):
    def run(self, delete_interface_nodespecific, delete_rbridge_id, delete_ns_ethernet, rbridge_id, ns_ethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_nodespecific_ns_ethernet(username=username, rbridge_id=rbridge_id, ns_ethernet=ns_ethernet, host=host, delete_interface_nodespecific=delete_interface_nodespecific, delete_ns_ethernet=delete_ns_ethernet, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    