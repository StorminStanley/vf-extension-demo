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


def rbridge_id_router_hide_pim_holder_pim_nbr_agtimeout(**kwargs):
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
        
    nbr_agtimeout = ET.SubElement(pim, "nbr-agtimeout")
    if kwargs.pop('delete_nbr_agtimeout', False) is True:
        delete_nbr_agtimeout = config.find('.//*nbr-agtimeout')
        delete_nbr_agtimeout.set('operation', 'delete')
        
    nbr_agtimeout.text = kwargs.pop('nbr_agtimeout')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_hide_pim_holder_pim_nbr_agtimeout_act(Action):
    def run(self, delete_pim, nbr_agtimeout, delete_nbr_agtimeout, rbridge_id, delete_hide_pim_holder, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_hide_pim_holder_pim_nbr_agtimeout(nbr_agtimeout=nbr_agtimeout, delete_pim=delete_pim, username=username, rbridge_id=rbridge_id, delete_router=delete_router, delete_hide_pim_holder=delete_hide_pim_holder, delete_nbr_agtimeout=delete_nbr_agtimeout, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    