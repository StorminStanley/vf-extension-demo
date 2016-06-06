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


def rbridge_id_ip_rtm_config_route_static_bfd_holdover_interval(**kwargs):
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
            
    ip = ET.SubElement(rbridge_id, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
    if kwargs.pop('delete_rtm_config', False) is True:
        delete_rtm_config = config.find('.//*rtm-config')
        delete_rtm_config.set('operation', 'delete')
        
    route = ET.SubElement(rtm_config, "route")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    static = ET.SubElement(route, "static")
    if kwargs.pop('delete_static', False) is True:
        delete_static = config.find('.//*static')
        delete_static.set('operation', 'delete')
        
    bfd = ET.SubElement(static, "bfd")
    if kwargs.pop('delete_bfd', False) is True:
        delete_bfd = config.find('.//*bfd')
        delete_bfd.set('operation', 'delete')
        
    holdover_interval = ET.SubElement(bfd, "holdover-interval")
    if kwargs.pop('delete_holdover_interval', False) is True:
        delete_holdover_interval = config.find('.//*holdover-interval')
        delete_holdover_interval.set('operation', 'delete')
        
    holdover_interval.text = kwargs.pop('holdover_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_rtm_config_route_static_bfd_holdover_interval_act(Action):
    def run(self, rbridge_id, delete_ip, delete_route, holdover_interval, delete_static, delete_rtm_config, delete_rbridge_id, delete_bfd, delete_holdover_interval, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_rtm_config_route_static_bfd_holdover_interval(delete_static=delete_static, delete_route=delete_route, username=username, delete_ip=delete_ip, rbridge_id=rbridge_id, holdover_interval=holdover_interval, password=password, delete_rtm_config=delete_rtm_config, host=host, delete_holdover_interval=delete_holdover_interval, delete_rbridge_id=delete_rbridge_id, delete_bfd=delete_bfd, callback=_callback, mgr=mgr)
        return 0
    