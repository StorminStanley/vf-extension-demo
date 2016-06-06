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


def rbridge_id_interface_ve_vrrpe_short_path_forwarding_revert_priority(**kwargs):
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
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    vrrpe = ET.SubElement(ve, "vrrpe", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_vrrpe', False) is True:
        delete_vrrpe = config.find('.//*vrrpe')
        delete_vrrpe.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrpe, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    short_path_forwarding = ET.SubElement(vrrpe, "short-path-forwarding")
    if kwargs.pop('delete_short_path_forwarding', False) is True:
        delete_short_path_forwarding = config.find('.//*short-path-forwarding')
        delete_short_path_forwarding.set('operation', 'delete')
        
    revert_priority = ET.SubElement(short_path_forwarding, "revert-priority")
    if kwargs.pop('delete_revert_priority', False) is True:
        delete_revert_priority = config.find('.//*revert-priority')
        delete_revert_priority.set('operation', 'delete')
        
    revert_priority.text = kwargs.pop('revert_priority')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_vrrpe_short_path_forwarding_revert_priority_act(Action):
    def run(self, delete_revert_priority, name, revert_priority, delete_vrid, vrid, delete_short_path_forwarding, delete_ve, delete_interface, delete_name, delete_rbridge_id, delete_vrrpe, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_vrrpe_short_path_forwarding_revert_priority(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_vrrpe=delete_vrrpe, delete_short_path_forwarding=delete_short_path_forwarding, username=username, rbridge_id=rbridge_id, delete_ve=delete_ve, vrid=vrid, revert_priority=revert_priority, host=host, delete_revert_priority=delete_revert_priority, delete_rbridge_id=delete_rbridge_id, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    