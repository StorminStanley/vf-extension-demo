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


def rbridge_id_ipv6_router_ospf_global_default_information_originate_global_default_information_originate_metric_type(**kwargs):
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
            
    global_default_information_originate = ET.SubElement(ospf, "global-default-information-originate")
    if kwargs.pop('delete_global_default_information_originate', False) is True:
        delete_global_default_information_originate = config.find('.//*global-default-information-originate')
        delete_global_default_information_originate.set('operation', 'delete')
        
    global_default_information_originate_metric_type = ET.SubElement(global_default_information_originate, "global-default-information-originate-metric-type")
    if kwargs.pop('delete_global_default_information_originate_metric_type', False) is True:
        delete_global_default_information_originate_metric_type = config.find('.//*global-default-information-originate-metric-type')
        delete_global_default_information_originate_metric_type.set('operation', 'delete')
        
    global_default_information_originate_metric_type.text = kwargs.pop('global_default_information_originate_metric_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_global_default_information_originate_global_default_information_originate_metric_type_act(Action):
    def run(self, rbridge_id, delete_global_default_information_originate_metric_type, delete_ospf, delete_vrf, delete_global_default_information_originate, vrf, delete_rbridge_id, global_default_information_originate_metric_type, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_global_default_information_originate_global_default_information_originate_metric_type(delete_router=delete_router, username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, vrf=vrf, global_default_information_originate_metric_type=global_default_information_originate_metric_type, delete_ospf=delete_ospf, delete_global_default_information_originate=delete_global_default_information_originate, host=host, delete_global_default_information_originate_metric_type=delete_global_default_information_originate_metric_type, password=password, callback=_callback, mgr=mgr)
        return 0
    