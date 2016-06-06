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


def interface_fc_port_isl_r_rdy_mode(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fc_port = ET.SubElement(interface, "fc-port")
    if kwargs.pop('delete_fc_port', False) is True:
        delete_fc_port = config.find('.//*fc-port')
        delete_fc_port.set('operation', 'delete')
        
    name_key = ET.SubElement(fc_port, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    isl_r_rdy_mode = ET.SubElement(fc_port, "isl-r_rdy-mode")
    if kwargs.pop('delete_isl_r_rdy_mode', False) is True:
        delete_isl_r_rdy_mode = config.find('.//*isl-r_rdy-mode')
        delete_isl_r_rdy_mode.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fc_port_isl_r_rdy_mode_act(Action):
    def run(self, delete_isl_r_rdy_mode, delete_name, delete_interface, name, delete_fc_port, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fc_port_isl_r_rdy_mode(name=name, delete_name=delete_name, delete_fc_port=delete_fc_port, host=host, delete_isl_r_rdy_mode=delete_isl_r_rdy_mode, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    