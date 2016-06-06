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


def rbridge_id_chassis_virtual_ipv6(**kwargs):
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
            
    chassis = ET.SubElement(rbridge_id, "chassis", xmlns="urn:brocade.com:mgmt:brocade-chassis")
    if kwargs.pop('delete_chassis', False) is True:
        delete_chassis = config.find('.//*chassis')
        delete_chassis.set('operation', 'delete')
        
    virtual_ipv6 = ET.SubElement(chassis, "virtual-ipv6")
    if kwargs.pop('delete_virtual_ipv6', False) is True:
        delete_virtual_ipv6 = config.find('.//*virtual-ipv6')
        delete_virtual_ipv6.set('operation', 'delete')
        
    virtual_ipv6.text = kwargs.pop('virtual_ipv6')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_chassis_virtual_ipv6_act(Action):
    def run(self, delete_rbridge_id, rbridge_id, delete_chassis, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_chassis_virtual_ipv6(delete_chassis=delete_chassis, rbridge_id=rbridge_id, host=host, delete_rbridge_id=delete_rbridge_id, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    