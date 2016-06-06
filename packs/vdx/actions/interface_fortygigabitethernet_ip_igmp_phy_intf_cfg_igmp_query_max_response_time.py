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


def interface_fortygigabitethernet_ip_igmp_phy_intf_cfg_igmp_query_max_response_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(fortygigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    igmp_phy_intf_cfg = ET.SubElement(ip, "igmp-phy-intf-cfg", xmlns="urn:brocade.com:mgmt:brocade-igmp")
    if kwargs.pop('delete_igmp_phy_intf_cfg', False) is True:
        delete_igmp_phy_intf_cfg = config.find('.//*igmp-phy-intf-cfg')
        delete_igmp_phy_intf_cfg.set('operation', 'delete')
        
    igmp = ET.SubElement(igmp_phy_intf_cfg, "igmp")
    if kwargs.pop('delete_igmp', False) is True:
        delete_igmp = config.find('.//*igmp')
        delete_igmp.set('operation', 'delete')
        
    query_max_response_time = ET.SubElement(igmp, "query-max-response-time")
    if kwargs.pop('delete_query_max_response_time', False) is True:
        delete_query_max_response_time = config.find('.//*query-max-response-time')
        delete_query_max_response_time.set('operation', 'delete')
        
    query_max_response_time.text = kwargs.pop('query_max_response_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_ip_igmp_phy_intf_cfg_igmp_query_max_response_time_act(Action):
    def run(self, name, delete_ip, delete_fortygigabitethernet, delete_igmp_phy_intf_cfg, delete_query_max_response_time, delete_igmp, delete_interface, delete_name, query_max_response_time, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_ip_igmp_phy_intf_cfg_igmp_query_max_response_time(delete_igmp_phy_intf_cfg=delete_igmp_phy_intf_cfg, query_max_response_time=query_max_response_time, name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_igmp=delete_igmp, delete_ip=delete_ip, delete_query_max_response_time=delete_query_max_response_time, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    