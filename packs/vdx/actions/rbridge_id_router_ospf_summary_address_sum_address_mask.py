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


def rbridge_id_router_ospf_summary_address_sum_address_mask(**kwargs):
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
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    summary_address = ET.SubElement(ospf, "summary-address")
    if kwargs.pop('delete_summary_address', False) is True:
        delete_summary_address = config.find('.//*summary-address')
        delete_summary_address.set('operation', 'delete')
        
    sum_address_key = ET.SubElement(summary_address, "sum-address")
    sum_address_key.text = kwargs.pop('sum_address')
    if kwargs.pop('delete_sum_address', False) is True:
        delete_sum_address = config.find('.//*sum-address')
        delete_sum_address.set('operation', 'delete')
            
    sum_address_mask = ET.SubElement(summary_address, "sum-address-mask")
    if kwargs.pop('delete_sum_address_mask', False) is True:
        delete_sum_address_mask = config.find('.//*sum-address-mask')
        delete_sum_address_mask.set('operation', 'delete')
        
    sum_address_mask.text = kwargs.pop('sum_address_mask')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_summary_address_sum_address_mask_act(Action):
    def run(self, rbridge_id, delete_ospf, delete_vrf, sum_address, delete_sum_address, delete_summary_address, vrf, sum_address_mask, delete_rbridge_id, delete_sum_address_mask, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_summary_address_sum_address_mask(sum_address=sum_address, username=username, delete_sum_address=delete_sum_address, delete_router=delete_router, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_summary_address=delete_summary_address, delete_sum_address_mask=delete_sum_address_mask, delete_ospf=delete_ospf, password=password, vrf=vrf, host=host, delete_rbridge_id=delete_rbridge_id, sum_address_mask=sum_address_mask, callback=_callback, mgr=mgr)
        return 0
    