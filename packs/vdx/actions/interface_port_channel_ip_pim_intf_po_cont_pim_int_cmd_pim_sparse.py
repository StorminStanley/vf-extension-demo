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


def interface_port_channel_ip_pim_intf_po_cont_pim_int_cmd_pim_sparse(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(port_channel, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    pim_intf_po_cont = ET.SubElement(ip, "pim-intf-po-cont", xmlns="urn:brocade.com:mgmt:brocade-pim")
    if kwargs.pop('delete_pim_intf_po_cont', False) is True:
        delete_pim_intf_po_cont = config.find('.//*pim-intf-po-cont')
        delete_pim_intf_po_cont.set('operation', 'delete')
        
    pim_int_cmd = ET.SubElement(pim_intf_po_cont, "pim-int-cmd")
    if kwargs.pop('delete_pim_int_cmd', False) is True:
        delete_pim_int_cmd = config.find('.//*pim-int-cmd')
        delete_pim_int_cmd.set('operation', 'delete')
        
    pim_sparse = ET.SubElement(pim_int_cmd, "pim-sparse")
    if kwargs.pop('delete_pim_sparse', False) is True:
        delete_pim_sparse = config.find('.//*pim-sparse')
        delete_pim_sparse.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ip_pim_intf_po_cont_pim_int_cmd_pim_sparse_act(Action):
    def run(self, delete_pim_intf_po_cont, delete_ip, delete_port_channel, delete_pim_sparse, delete_interface, delete_name, delete_pim_int_cmd, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ip_pim_intf_po_cont_pim_int_cmd_pim_sparse(name=name, delete_pim_intf_po_cont=delete_pim_intf_po_cont, delete_ip=delete_ip, delete_pim_int_cmd=delete_pim_int_cmd, delete_port_channel=delete_port_channel, delete_pim_sparse=delete_pim_sparse, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    