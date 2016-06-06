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


def rbridge_id_chassis_oper_address_virtual_oper_Vip_address(**kwargs):
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
        
    oper_address = ET.SubElement(chassis, "oper-address")
    if kwargs.pop('delete_oper_address', False) is True:
        delete_oper_address = config.find('.//*oper-address')
        delete_oper_address.set('operation', 'delete')
        
    virtual_oper_Vip_address = ET.SubElement(oper_address, "virtual-oper-Vip-address")
    if kwargs.pop('delete_virtual_oper_Vip_address', False) is True:
        delete_virtual_oper_Vip_address = config.find('.//*virtual-oper-Vip-address')
        delete_virtual_oper_Vip_address.set('operation', 'delete')
        
    virtual_oper_Vip_address.text = kwargs.pop('virtual_oper_Vip_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_chassis_oper_address_virtual_oper_Vip_address_act(Action):
    def run(self, rbridge_id, delete_virtual_oper_Vip_address, delete_chassis, virtual_oper_Vip_address, delete_oper_address, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_chassis_oper_address_virtual_oper_Vip_address(username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_virtual_oper_Vip_address=delete_virtual_oper_Vip_address, delete_oper_address=delete_oper_address, host=host, delete_chassis=delete_chassis, virtual_oper_Vip_address=virtual_oper_Vip_address, password=password, callback=_callback, mgr=mgr)
        return 0
    