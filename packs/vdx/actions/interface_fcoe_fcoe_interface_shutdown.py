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


def interface_fcoe_fcoe_interface_shutdown(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fcoe = ET.SubElement(interface, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
    if kwargs.pop('delete_fcoe', False) is True:
        delete_fcoe = config.find('.//*fcoe')
        delete_fcoe.set('operation', 'delete')
        
    fcoe_interface_name_key = ET.SubElement(fcoe, "fcoe-interface-name")
    fcoe_interface_name_key.text = kwargs.pop('fcoe_interface_name')
    if kwargs.pop('delete_fcoe_interface_name', False) is True:
        delete_fcoe_interface_name = config.find('.//*fcoe-interface-name')
        delete_fcoe_interface_name.set('operation', 'delete')
            
    fcoe_interface_shutdown = ET.SubElement(fcoe, "fcoe-interface-shutdown")
    if kwargs.pop('delete_fcoe_interface_shutdown', False) is True:
        delete_fcoe_interface_shutdown = config.find('.//*fcoe-interface-shutdown')
        delete_fcoe_interface_shutdown.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fcoe_fcoe_interface_shutdown_act(Action):
    def run(self, fcoe_interface_name, delete_fcoe_interface_shutdown, delete_interface, delete_fcoe, delete_fcoe_interface_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fcoe_fcoe_interface_shutdown(delete_fcoe=delete_fcoe, host=host, delete_fcoe_interface_name=delete_fcoe_interface_name, delete_fcoe_interface_shutdown=delete_fcoe_interface_shutdown, fcoe_interface_name=fcoe_interface_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    