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


def rbridge_id_router_hide_pim_holder_pim_rp_candidate_rp_cand_grp_prefix_rp_cand_grp_prefix_ip(**kwargs):
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
        
    hide_pim_holder = ET.SubElement(router, "hide-pim-holder", xmlns="urn:brocade.com:mgmt:brocade-pim")
    if kwargs.pop('delete_hide_pim_holder', False) is True:
        delete_hide_pim_holder = config.find('.//*hide-pim-holder')
        delete_hide_pim_holder.set('operation', 'delete')
        
    pim = ET.SubElement(hide_pim_holder, "pim")
    if kwargs.pop('delete_pim', False) is True:
        delete_pim = config.find('.//*pim')
        delete_pim.set('operation', 'delete')
        
    rp_candidate = ET.SubElement(pim, "rp-candidate")
    if kwargs.pop('delete_rp_candidate', False) is True:
        delete_rp_candidate = config.find('.//*rp-candidate')
        delete_rp_candidate.set('operation', 'delete')
        
    rp_cand_grp_prefix = ET.SubElement(rp_candidate, "rp-cand-grp-prefix")
    if kwargs.pop('delete_rp_cand_grp_prefix', False) is True:
        delete_rp_cand_grp_prefix = config.find('.//*rp-cand-grp-prefix')
        delete_rp_cand_grp_prefix.set('operation', 'delete')
        
    rp_cand_grp_prefix_length_key = ET.SubElement(rp_cand_grp_prefix, "rp-cand-grp-prefix-length")
    rp_cand_grp_prefix_length_key.text = kwargs.pop('rp_cand_grp_prefix_length')
    if kwargs.pop('delete_rp_cand_grp_prefix_length', False) is True:
        delete_rp_cand_grp_prefix_length = config.find('.//*rp-cand-grp-prefix-length')
        delete_rp_cand_grp_prefix_length.set('operation', 'delete')
            
    rp_cand_grp_prefix_ip = ET.SubElement(rp_cand_grp_prefix, "rp-cand-grp-prefix-ip")
    if kwargs.pop('delete_rp_cand_grp_prefix_ip', False) is True:
        delete_rp_cand_grp_prefix_ip = config.find('.//*rp-cand-grp-prefix-ip')
        delete_rp_cand_grp_prefix_ip.set('operation', 'delete')
        
    rp_cand_grp_prefix_ip.text = kwargs.pop('rp_cand_grp_prefix_ip')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_hide_pim_holder_pim_rp_candidate_rp_cand_grp_prefix_rp_cand_grp_prefix_ip_act(Action):
    def run(self, delete_pim, rp_cand_grp_prefix_ip, rbridge_id, delete_hide_pim_holder, delete_rp_cand_grp_prefix, delete_rp_cand_grp_prefix_ip, rp_cand_grp_prefix_length, delete_rbridge_id, delete_rp_cand_grp_prefix_length, delete_router, delete_rp_candidate, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_hide_pim_holder_pim_rp_candidate_rp_cand_grp_prefix_rp_cand_grp_prefix_ip(delete_rp_cand_grp_prefix_ip=delete_rp_cand_grp_prefix_ip, username=username, delete_rp_cand_grp_prefix_length=delete_rp_cand_grp_prefix_length, delete_pim=delete_pim, rp_cand_grp_prefix_length=rp_cand_grp_prefix_length, rbridge_id=rbridge_id, delete_router=delete_router, delete_hide_pim_holder=delete_hide_pim_holder, delete_rp_candidate=delete_rp_candidate, delete_rp_cand_grp_prefix=delete_rp_cand_grp_prefix, host=host, delete_rbridge_id=delete_rbridge_id, rp_cand_grp_prefix_ip=rp_cand_grp_prefix_ip, password=password, callback=_callback, mgr=mgr)
        return 0
    