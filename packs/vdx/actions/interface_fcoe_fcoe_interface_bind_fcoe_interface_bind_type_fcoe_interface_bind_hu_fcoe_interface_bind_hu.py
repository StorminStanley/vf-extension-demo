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


def interface_fcoe_fcoe_interface_bind_fcoe_interface_bind_type_fcoe_interface_bind_hu_fcoe_interface_bind_hu(**kwargs):
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
            
    fcoe_interface_bind = ET.SubElement(fcoe, "fcoe-interface-bind")
    if kwargs.pop('delete_fcoe_interface_bind', False) is True:
        delete_fcoe_interface_bind = config.find('.//*fcoe-interface-bind')
        delete_fcoe_interface_bind.set('operation', 'delete')
        
    fcoe_interface_bind_type = ET.SubElement(fcoe_interface_bind, "fcoe-interface-bind-type")
    if kwargs.pop('delete_fcoe_interface_bind_type', False) is True:
        delete_fcoe_interface_bind_type = config.find('.//*fcoe-interface-bind-type')
        delete_fcoe_interface_bind_type.set('operation', 'delete')
        
    fcoe_interface_bind_hu = ET.SubElement(fcoe_interface_bind_type, "fcoe-interface-bind-hu")
    if kwargs.pop('delete_fcoe_interface_bind_hu', False) is True:
        delete_fcoe_interface_bind_hu = config.find('.//*fcoe-interface-bind-hu')
        delete_fcoe_interface_bind_hu.set('operation', 'delete')
        
    fcoe_interface_bind_hu = ET.SubElement(fcoe_interface_bind_hu, "fcoe-interface-bind-hu")
    if kwargs.pop('delete_fcoe_interface_bind_hu', False) is True:
        delete_fcoe_interface_bind_hu = config.find('.//*fcoe-interface-bind-hu')
        delete_fcoe_interface_bind_hu.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fcoe_fcoe_interface_bind_fcoe_interface_bind_type_fcoe_interface_bind_hu_fcoe_interface_bind_hu_act(Action):
    def run(self, fcoe_interface_name, delete_fcoe_interface_bind, delete_fcoe_interface_bind_hu, delete_interface, delete_fcoe, delete_fcoe_interface_name, delete_fcoe_interface_bind_type, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fcoe_fcoe_interface_bind_fcoe_interface_bind_type_fcoe_interface_bind_hu_fcoe_interface_bind_hu(fcoe_interface_name=fcoe_interface_name, delete_fcoe_interface_bind_hu=delete_fcoe_interface_bind_hu, delete_fcoe_interface_bind=delete_fcoe_interface_bind, delete_fcoe_interface_bind_type=delete_fcoe_interface_bind_type, host=host, delete_fcoe_interface_name=delete_fcoe_interface_name, delete_fcoe=delete_fcoe, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    