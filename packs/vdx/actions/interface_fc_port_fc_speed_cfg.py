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


def interface_fc_port_fc_speed_cfg(**kwargs):
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
            
    fc_speed_cfg = ET.SubElement(fc_port, "fc-speed-cfg")
    if kwargs.pop('delete_fc_speed_cfg', False) is True:
        delete_fc_speed_cfg = config.find('.//*fc-speed-cfg')
        delete_fc_speed_cfg.set('operation', 'delete')
        
    fc_speed_cfg.text = kwargs.pop('fc_speed_cfg')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fc_port_fc_speed_cfg_act(Action):
    def run(self, delete_name, delete_fc_port, delete_interface, fc_speed_cfg, delete_fc_speed_cfg, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fc_port_fc_speed_cfg(name=name, delete_fc_speed_cfg=delete_fc_speed_cfg, delete_fc_port=delete_fc_port, host=host, fc_speed_cfg=fc_speed_cfg, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    