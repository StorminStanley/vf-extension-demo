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


def rbridge_id_hardware_profile_kap_predefined_kap_profiletype(**kwargs):
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
            
    hardware_profile = ET.SubElement(rbridge_id, "hardware-profile", xmlns="urn:brocade.com:mgmt:brocade-hardware")
    if kwargs.pop('delete_hardware_profile', False) is True:
        delete_hardware_profile = config.find('.//*hardware-profile')
        delete_hardware_profile.set('operation', 'delete')
        
    kap = ET.SubElement(hardware_profile, "kap")
    if kwargs.pop('delete_kap', False) is True:
        delete_kap = config.find('.//*kap')
        delete_kap.set('operation', 'delete')
        
    predefined = ET.SubElement(kap, "predefined")
    if kwargs.pop('delete_predefined', False) is True:
        delete_predefined = config.find('.//*predefined')
        delete_predefined.set('operation', 'delete')
        
    kap_profiletype = ET.SubElement(predefined, "kap_profiletype")
    if kwargs.pop('delete_kap_profiletype', False) is True:
        delete_kap_profiletype = config.find('.//*kap_profiletype')
        delete_kap_profiletype.set('operation', 'delete')
        
    kap_profiletype.text = kwargs.pop('kap_profiletype')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_hardware_profile_kap_predefined_kap_profiletype_act(Action):
    def run(self, delete_kap_profiletype, rbridge_id, delete_predefined, delete_hardware_profile, kap_profiletype, delete_kap, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_hardware_profile_kap_predefined_kap_profiletype(username=username, kap_profiletype=kap_profiletype, delete_kap_profiletype=delete_kap_profiletype, rbridge_id=rbridge_id, delete_kap=delete_kap, delete_hardware_profile=delete_hardware_profile, host=host, delete_rbridge_id=delete_rbridge_id, delete_predefined=delete_predefined, password=password, callback=_callback, mgr=mgr)
        return 0
    