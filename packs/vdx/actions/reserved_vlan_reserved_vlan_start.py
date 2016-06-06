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


def reserved_vlan_reserved_vlan_start(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    reserved_vlan = ET.SubElement(config, "reserved-vlan", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_reserved_vlan', False) is True:
        delete_reserved_vlan = config.find('.//*reserved-vlan')
        delete_reserved_vlan.set('operation', 'delete')
        
    reserved_vlan_start = ET.SubElement(reserved_vlan, "reserved-vlan-start")
    if kwargs.pop('delete_reserved_vlan_start', False) is True:
        delete_reserved_vlan_start = config.find('.//*reserved-vlan-start')
        delete_reserved_vlan_start.set('operation', 'delete')
        
    reserved_vlan_start.text = kwargs.pop('reserved_vlan_start')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class reserved_vlan_reserved_vlan_start_act(Action):
    def run(self, delete_reserved_vlan, delete_reserved_vlan_start, reserved_vlan_start, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        reserved_vlan_reserved_vlan_start(delete_reserved_vlan=delete_reserved_vlan, reserved_vlan_start=reserved_vlan_start, host=host, delete_reserved_vlan_start=delete_reserved_vlan_start, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    