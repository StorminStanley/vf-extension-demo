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


def rbridge_id_interface_loopback_intf_loopback_shutdown(**kwargs):
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
        
    loopback = ET.SubElement(interface, "loopback", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
    if kwargs.pop('delete_loopback', False) is True:
        delete_loopback = config.find('.//*loopback')
        delete_loopback.set('operation', 'delete')
        
    id_key = ET.SubElement(loopback, "id")
    id_key.text = kwargs.pop('id')
    if kwargs.pop('delete_id', False) is True:
        delete_id = config.find('.//*id')
        delete_id.set('operation', 'delete')
            
    intf_loopback = ET.SubElement(loopback, "intf-loopback")
    if kwargs.pop('delete_intf_loopback', False) is True:
        delete_intf_loopback = config.find('.//*intf-loopback')
        delete_intf_loopback.set('operation', 'delete')
        
    shutdown = ET.SubElement(intf_loopback, "shutdown")
    if kwargs.pop('delete_shutdown', False) is True:
        delete_shutdown = config.find('.//*shutdown')
        delete_shutdown.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_loopback_intf_loopback_shutdown_act(Action):
    def run(self, rbridge_id, delete_shutdown, delete_intf_loopback, delete_id, delete_loopback, delete_interface, delete_rbridge_id, id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_loopback_intf_loopback_shutdown(delete_shutdown=delete_shutdown, id=id, username=username, rbridge_id=rbridge_id, delete_id=delete_id, delete_loopback=delete_loopback, host=host, delete_intf_loopback=delete_intf_loopback, delete_rbridge_id=delete_rbridge_id, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    