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


def rbridge_id_ipv6_router_ospf_graceful_restart_helper_graceful_restart_helper_strict_lsa_checking(**kwargs):
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
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    router = ET.SubElement(ipv6, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    graceful_restart = ET.SubElement(ospf, "graceful-restart")
    if kwargs.pop('delete_graceful_restart', False) is True:
        delete_graceful_restart = config.find('.//*graceful-restart')
        delete_graceful_restart.set('operation', 'delete')
        
    helper = ET.SubElement(graceful_restart, "helper")
    if kwargs.pop('delete_helper', False) is True:
        delete_helper = config.find('.//*helper')
        delete_helper.set('operation', 'delete')
        
    graceful_restart_helper_strict_lsa_checking = ET.SubElement(helper, "graceful-restart-helper-strict-lsa-checking")
    if kwargs.pop('delete_graceful_restart_helper_strict_lsa_checking', False) is True:
        delete_graceful_restart_helper_strict_lsa_checking = config.find('.//*graceful-restart-helper-strict-lsa-checking')
        delete_graceful_restart_helper_strict_lsa_checking.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_graceful_restart_helper_graceful_restart_helper_strict_lsa_checking_act(Action):
    def run(self, delete_helper, rbridge_id, delete_graceful_restart, delete_ospf, delete_vrf, delete_graceful_restart_helper_strict_lsa_checking, vrf, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_graceful_restart_helper_graceful_restart_helper_strict_lsa_checking(delete_helper=delete_helper, username=username, delete_graceful_restart=delete_graceful_restart, delete_router=delete_router, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_ospf=delete_ospf, host=host, vrf=vrf, delete_graceful_restart_helper_strict_lsa_checking=delete_graceful_restart_helper_strict_lsa_checking, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    