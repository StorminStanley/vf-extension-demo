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


def interface_port_channel_ip_igmp_po_intf_cfg_igmp_last_member_query_count(**kwargs):
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
        
    igmp_po_intf_cfg = ET.SubElement(ip, "igmp-po-intf-cfg", xmlns="urn:brocade.com:mgmt:brocade-igmp")
    if kwargs.pop('delete_igmp_po_intf_cfg', False) is True:
        delete_igmp_po_intf_cfg = config.find('.//*igmp-po-intf-cfg')
        delete_igmp_po_intf_cfg.set('operation', 'delete')
        
    igmp = ET.SubElement(igmp_po_intf_cfg, "igmp")
    if kwargs.pop('delete_igmp', False) is True:
        delete_igmp = config.find('.//*igmp')
        delete_igmp.set('operation', 'delete')
        
    last_member_query_count = ET.SubElement(igmp, "last-member-query-count")
    if kwargs.pop('delete_last_member_query_count', False) is True:
        delete_last_member_query_count = config.find('.//*last-member-query-count')
        delete_last_member_query_count.set('operation', 'delete')
        
    last_member_query_count.text = kwargs.pop('last_member_query_count')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ip_igmp_po_intf_cfg_igmp_last_member_query_count_act(Action):
    def run(self, name, delete_ip, delete_igmp_po_intf_cfg, delete_last_member_query_count, delete_port_channel, delete_igmp, delete_interface, delete_name, last_member_query_count, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ip_igmp_po_intf_cfg_igmp_last_member_query_count(delete_igmp_po_intf_cfg=delete_igmp_po_intf_cfg, name=name, delete_name=delete_name, delete_igmp=delete_igmp, delete_ip=delete_ip, delete_port_channel=delete_port_channel, delete_last_member_query_count=delete_last_member_query_count, host=host, last_member_query_count=last_member_query_count, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    