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


def rbridge_id_router_ospf_timers_throttle_spf_init_delay(**kwargs):
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
            
    timers = ET.SubElement(ospf, "timers")
    if kwargs.pop('delete_timers', False) is True:
        delete_timers = config.find('.//*timers')
        delete_timers.set('operation', 'delete')
        
    throttle = ET.SubElement(timers, "throttle")
    if kwargs.pop('delete_throttle', False) is True:
        delete_throttle = config.find('.//*throttle')
        delete_throttle.set('operation', 'delete')
        
    spf = ET.SubElement(throttle, "spf")
    if kwargs.pop('delete_spf', False) is True:
        delete_spf = config.find('.//*spf')
        delete_spf.set('operation', 'delete')
        
    init_delay = ET.SubElement(spf, "init-delay")
    if kwargs.pop('delete_init_delay', False) is True:
        delete_init_delay = config.find('.//*init-delay')
        delete_init_delay.set('operation', 'delete')
        
    init_delay.text = kwargs.pop('init_delay')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_ospf_timers_throttle_spf_init_delay_act(Action):
    def run(self, rbridge_id, delete_ospf, delete_vrf, delete_init_delay, init_delay, delete_timers, vrf, delete_rbridge_id, delete_spf, delete_router, delete_throttle, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_ospf_timers_throttle_spf_init_delay(delete_spf=delete_spf, username=username, delete_init_delay=delete_init_delay, rbridge_id=rbridge_id, delete_vrf=delete_vrf, init_delay=init_delay, delete_throttle=delete_throttle, delete_router=delete_router, delete_ospf=delete_ospf, vrf=vrf, host=host, delete_rbridge_id=delete_rbridge_id, delete_timers=delete_timers, password=password, callback=_callback, mgr=mgr)
        return 0
    