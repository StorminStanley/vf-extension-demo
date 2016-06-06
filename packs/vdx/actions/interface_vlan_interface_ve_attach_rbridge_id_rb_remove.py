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


def interface_vlan_interface_ve_attach_rbridge_id_rb_remove(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface_vlan = ET.SubElement(config, "interface-vlan", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface_vlan', False) is True:
        delete_interface_vlan = config.find('.//*interface-vlan')
        delete_interface_vlan.set('operation', 'delete')
        
    interface = ET.SubElement(interface_vlan, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    gve_name_key = ET.SubElement(ve, "gve-name")
    gve_name_key.text = kwargs.pop('gve_name')
    if kwargs.pop('delete_gve_name', False) is True:
        delete_gve_name = config.find('.//*gve-name')
        delete_gve_name.set('operation', 'delete')
            
    attach = ET.SubElement(ve, "attach", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
    if kwargs.pop('delete_attach', False) is True:
        delete_attach = config.find('.//*attach')
        delete_attach.set('operation', 'delete')
        
    rbridge_id = ET.SubElement(attach, "rbridge-id")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rb_remove = ET.SubElement(rbridge_id, "rb-remove")
    if kwargs.pop('delete_rb_remove', False) is True:
        delete_rb_remove = config.find('.//*rb-remove')
        delete_rb_remove.set('operation', 'delete')
        
    rb_remove.text = kwargs.pop('rb_remove')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_ve_attach_rbridge_id_rb_remove_act(Action):
    def run(self, gve_name, delete_attach, delete_interface_vlan, delete_rb_remove, delete_ve, delete_interface, delete_rbridge_id, rb_remove, delete_gve_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_ve_attach_rbridge_id_rb_remove(delete_gve_name=delete_gve_name, username=username, delete_rbridge_id=delete_rbridge_id, rb_remove=rb_remove, password=password, gve_name=gve_name, delete_interface_vlan=delete_interface_vlan, host=host, delete_ve=delete_ve, delete_interface=delete_interface, delete_attach=delete_attach, delete_rb_remove=delete_rb_remove, callback=_callback, mgr=mgr)
        return 0
    