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


def rbridge_id_interface_ve_ip_pim_intf_vlan_cont_pim_int_cmd_pim_sparse(**kwargs):
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
            
    ip = ET.SubElement(ve, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    pim_intf_vlan_cont = ET.SubElement(ip, "pim-intf-vlan-cont", xmlns="urn:brocade.com:mgmt:brocade-pim")
    if kwargs.pop('delete_pim_intf_vlan_cont', False) is True:
        delete_pim_intf_vlan_cont = config.find('.//*pim-intf-vlan-cont')
        delete_pim_intf_vlan_cont.set('operation', 'delete')
        
    pim_int_cmd = ET.SubElement(pim_intf_vlan_cont, "pim-int-cmd")
    if kwargs.pop('delete_pim_int_cmd', False) is True:
        delete_pim_int_cmd = config.find('.//*pim-int-cmd')
        delete_pim_int_cmd.set('operation', 'delete')
        
    pim_sparse = ET.SubElement(pim_int_cmd, "pim-sparse")
    if kwargs.pop('delete_pim_sparse', False) is True:
        delete_pim_sparse = config.find('.//*pim-sparse')
        delete_pim_sparse.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_ip_pim_intf_vlan_cont_pim_int_cmd_pim_sparse_act(Action):
    def run(self, name, delete_ip, delete_ve, delete_pim_sparse, delete_interface, delete_name, delete_pim_intf_vlan_cont, delete_rbridge_id, delete_pim_int_cmd, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_ip_pim_intf_vlan_cont_pim_int_cmd_pim_sparse(name=name, delete_name=delete_name, username=username, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_pim_int_cmd=delete_pim_int_cmd, delete_ve=delete_ve, host=host, delete_pim_sparse=delete_pim_sparse, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, password=password, delete_pim_intf_vlan_cont=delete_pim_intf_vlan_cont, callback=_callback, mgr=mgr)
        return 0
    