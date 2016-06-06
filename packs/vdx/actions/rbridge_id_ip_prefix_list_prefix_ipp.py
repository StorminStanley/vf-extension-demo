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


def rbridge_id_ip_prefix_list_prefix_ipp(**kwargs):
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
        
    prefix_list = ET.SubElement(ip, "prefix-list", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_prefix_list', False) is True:
        delete_prefix_list = config.find('.//*prefix-list')
        delete_prefix_list.set('operation', 'delete')
        
    name_key = ET.SubElement(prefix_list, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
    seq_keyword_key.text = kwargs.pop('seq_keyword')
    if kwargs.pop('delete_seq_keyword', False) is True:
        delete_seq_keyword = config.find('.//*seq-keyword')
        delete_seq_keyword.set('operation', 'delete')
            
    instance_key = ET.SubElement(prefix_list, "instance")
    instance_key.text = kwargs.pop('instance')
    if kwargs.pop('delete_instance', False) is True:
        delete_instance = config.find('.//*instance')
        delete_instance.set('operation', 'delete')
            
    prefix_ipp = ET.SubElement(prefix_list, "prefix-ipp")
    if kwargs.pop('delete_prefix_ipp', False) is True:
        delete_prefix_ipp = config.find('.//*prefix-ipp')
        delete_prefix_ipp.set('operation', 'delete')
        
    prefix_ipp.text = kwargs.pop('prefix_ipp')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_prefix_list_prefix_ipp_act(Action):
    def run(self, rbridge_id, delete_ip, prefix_ipp, delete_prefix_ipp, delete_seq_keyword, instance, delete_instance, delete_name, delete_prefix_list, delete_rbridge_id, seq_keyword, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_prefix_list_prefix_ipp(delete_instance=delete_instance, delete_prefix_list=delete_prefix_list, delete_name=delete_name, delete_seq_keyword=delete_seq_keyword, username=username, prefix_ipp=prefix_ipp, seq_keyword=seq_keyword, rbridge_id=rbridge_id, delete_ip=delete_ip, name=name, delete_prefix_ipp=delete_prefix_ipp, host=host, password=password, delete_rbridge_id=delete_rbridge_id, instance=instance, callback=_callback, mgr=mgr)
        return 0
    