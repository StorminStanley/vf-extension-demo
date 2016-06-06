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


def rbridge_id_openflow_logical_instance_passive_no_ssl_passive_controller_flag(**kwargs):
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
            
    openflow = ET.SubElement(rbridge_id, "openflow", xmlns="urn:brocade.com:mgmt:brocade-openflow")
    if kwargs.pop('delete_openflow', False) is True:
        delete_openflow = config.find('.//*openflow')
        delete_openflow.set('operation', 'delete')
        
    logical_instance = ET.SubElement(openflow, "logical-instance")
    if kwargs.pop('delete_logical_instance', False) is True:
        delete_logical_instance = config.find('.//*logical-instance')
        delete_logical_instance.set('operation', 'delete')
        
    instance_id_key = ET.SubElement(logical_instance, "instance-id")
    instance_id_key.text = kwargs.pop('instance_id')
    if kwargs.pop('delete_instance_id', False) is True:
        delete_instance_id = config.find('.//*instance-id')
        delete_instance_id.set('operation', 'delete')
            
    passive = ET.SubElement(logical_instance, "passive")
    if kwargs.pop('delete_passive', False) is True:
        delete_passive = config.find('.//*passive')
        delete_passive.set('operation', 'delete')
        
    no_ssl = ET.SubElement(passive, "no-ssl")
    if kwargs.pop('delete_no_ssl', False) is True:
        delete_no_ssl = config.find('.//*no-ssl')
        delete_no_ssl.set('operation', 'delete')
        
    passive_controller_flag = ET.SubElement(no_ssl, "passive-controller-flag")
    if kwargs.pop('delete_passive_controller_flag', False) is True:
        delete_passive_controller_flag = config.find('.//*passive-controller-flag')
        delete_passive_controller_flag.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_openflow_logical_instance_passive_no_ssl_passive_controller_flag_act(Action):
    def run(self, delete_openflow, rbridge_id, delete_passive, instance_id, delete_passive_controller_flag, delete_rbridge_id, delete_no_ssl, delete_logical_instance, delete_instance_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_openflow_logical_instance_passive_no_ssl_passive_controller_flag(delete_logical_instance=delete_logical_instance, delete_passive_controller_flag=delete_passive_controller_flag, username=username, rbridge_id=rbridge_id, delete_openflow=delete_openflow, delete_no_ssl=delete_no_ssl, delete_passive=delete_passive, host=host, instance_id=instance_id, delete_instance_id=delete_instance_id, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    