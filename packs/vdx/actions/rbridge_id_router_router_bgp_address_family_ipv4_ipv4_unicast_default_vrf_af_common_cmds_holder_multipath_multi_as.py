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


def rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_common_cmds_holder_multipath_multi_as(**kwargs):
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
            
    router = ET.SubElement(rbridge_id, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    router_bgp = ET.SubElement(router, "router-bgp", xmlns="urn:brocade.com:mgmt:brocade-bgp")
    if kwargs.pop('delete_router_bgp', False) is True:
        delete_router_bgp = config.find('.//*router-bgp')
        delete_router_bgp.set('operation', 'delete')
        
    address_family = ET.SubElement(router_bgp, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    ipv4 = ET.SubElement(address_family, "ipv4")
    if kwargs.pop('delete_ipv4', False) is True:
        delete_ipv4 = config.find('.//*ipv4')
        delete_ipv4.set('operation', 'delete')
        
    ipv4_unicast = ET.SubElement(ipv4, "ipv4-unicast")
    if kwargs.pop('delete_ipv4_unicast', False) is True:
        delete_ipv4_unicast = config.find('.//*ipv4-unicast')
        delete_ipv4_unicast.set('operation', 'delete')
        
    default_vrf = ET.SubElement(ipv4_unicast, "default-vrf")
    if kwargs.pop('delete_default_vrf', False) is True:
        delete_default_vrf = config.find('.//*default-vrf')
        delete_default_vrf.set('operation', 'delete')
        
    af_common_cmds_holder = ET.SubElement(default_vrf, "af-common-cmds-holder")
    if kwargs.pop('delete_af_common_cmds_holder', False) is True:
        delete_af_common_cmds_holder = config.find('.//*af-common-cmds-holder')
        delete_af_common_cmds_holder.set('operation', 'delete')
        
    multipath = ET.SubElement(af_common_cmds_holder, "multipath")
    if kwargs.pop('delete_multipath', False) is True:
        delete_multipath = config.find('.//*multipath')
        delete_multipath.set('operation', 'delete')
        
    multi_as = ET.SubElement(multipath, "multi-as")
    if kwargs.pop('delete_multi_as', False) is True:
        delete_multi_as = config.find('.//*multi-as')
        delete_multi_as.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_common_cmds_holder_multipath_multi_as_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, delete_multipath, delete_af_common_cmds_holder, delete_default_vrf, delete_rbridge_id, delete_router, delete_multi_as, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv4_ipv4_unicast_default_vrf_af_common_cmds_holder_multipath_multi_as(delete_router_bgp=delete_router_bgp, username=username, delete_default_vrf=delete_default_vrf, rbridge_id=rbridge_id, delete_router=delete_router, delete_multi_as=delete_multi_as, delete_af_common_cmds_holder=delete_af_common_cmds_holder, host=host, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, delete_multipath=delete_multipath, password=password, callback=_callback, mgr=mgr)
        return 0
    