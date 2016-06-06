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


def rbridge_id_ip_extcommunity_list_extcommunity_list_num(**kwargs):
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
        
    extcommunity_list = ET.SubElement(ip, "extcommunity-list", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_extcommunity_list', False) is True:
        delete_extcommunity_list = config.find('.//*extcommunity-list')
        delete_extcommunity_list.set('operation', 'delete')
        
    extcommunity_list_num = ET.SubElement(extcommunity_list, "extcommunity-list-num")
    if kwargs.pop('delete_extcommunity_list_num', False) is True:
        delete_extcommunity_list_num = config.find('.//*extcommunity-list-num')
        delete_extcommunity_list_num.set('operation', 'delete')
        
    extcommunity_list_num.text = kwargs.pop('extcommunity_list_num')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_extcommunity_list_extcommunity_list_num_act(Action):
    def run(self, delete_extcommunity_list_num, rbridge_id, delete_ip, extcommunity_list_num, delete_rbridge_id, delete_extcommunity_list, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_extcommunity_list_extcommunity_list_num(delete_extcommunity_list_num=delete_extcommunity_list_num, delete_extcommunity_list=delete_extcommunity_list, username=username, rbridge_id=rbridge_id, delete_ip=delete_ip, extcommunity_list_num=extcommunity_list_num, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    