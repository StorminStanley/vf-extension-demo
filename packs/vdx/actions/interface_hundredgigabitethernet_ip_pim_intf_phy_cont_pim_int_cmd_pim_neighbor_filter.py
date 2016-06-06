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


def interface_hundredgigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_pim_neighbor_filter(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(hundredgigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    pim_intf_phy_cont = ET.SubElement(ip, "pim-intf-phy-cont", xmlns="urn:brocade.com:mgmt:brocade-pim")
    if kwargs.pop('delete_pim_intf_phy_cont', False) is True:
        delete_pim_intf_phy_cont = config.find('.//*pim-intf-phy-cont')
        delete_pim_intf_phy_cont.set('operation', 'delete')
        
    pim_int_cmd = ET.SubElement(pim_intf_phy_cont, "pim-int-cmd")
    if kwargs.pop('delete_pim_int_cmd', False) is True:
        delete_pim_int_cmd = config.find('.//*pim-int-cmd')
        delete_pim_int_cmd.set('operation', 'delete')
        
    pim = ET.SubElement(pim_int_cmd, "pim")
    if kwargs.pop('delete_pim', False) is True:
        delete_pim = config.find('.//*pim')
        delete_pim.set('operation', 'delete')
        
    neighbor_filter = ET.SubElement(pim, "neighbor-filter")
    if kwargs.pop('delete_neighbor_filter', False) is True:
        delete_neighbor_filter = config.find('.//*neighbor-filter')
        delete_neighbor_filter.set('operation', 'delete')
        
    neighbor_filter.text = kwargs.pop('neighbor_filter')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_pim_neighbor_filter_act(Action):
    def run(self, delete_pim, delete_pim_intf_phy_cont, delete_ip, delete_neighbor_filter, delete_interface, delete_name, delete_hundredgigabitethernet, delete_pim_int_cmd, neighbor_filter, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_pim_neighbor_filter(name=name, delete_name=delete_name, delete_pim=delete_pim, neighbor_filter=neighbor_filter, delete_ip=delete_ip, delete_neighbor_filter=delete_neighbor_filter, delete_pim_int_cmd=delete_pim_int_cmd, delete_hundredgigabitethernet=delete_hundredgigabitethernet, delete_pim_intf_phy_cont=delete_pim_intf_phy_cont, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    