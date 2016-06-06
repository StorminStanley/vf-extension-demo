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


def rbridge_id_hardware_profile_vlan_classification_predefined_vlan_profiletype(**kwargs):
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
        
    vlan_classification = ET.SubElement(hardware_profile, "vlan-classification")
    if kwargs.pop('delete_vlan_classification', False) is True:
        delete_vlan_classification = config.find('.//*vlan-classification')
        delete_vlan_classification.set('operation', 'delete')
        
    predefined = ET.SubElement(vlan_classification, "predefined")
    if kwargs.pop('delete_predefined', False) is True:
        delete_predefined = config.find('.//*predefined')
        delete_predefined.set('operation', 'delete')
        
    vlan_profiletype = ET.SubElement(predefined, "vlan_profiletype")
    if kwargs.pop('delete_vlan_profiletype', False) is True:
        delete_vlan_profiletype = config.find('.//*vlan_profiletype')
        delete_vlan_profiletype.set('operation', 'delete')
        
    vlan_profiletype.text = kwargs.pop('vlan_profiletype')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_hardware_profile_vlan_classification_predefined_vlan_profiletype_act(Action):
    def run(self, vlan_profiletype, delete_vlan_profiletype, rbridge_id, delete_predefined, delete_vlan_classification, delete_hardware_profile, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_hardware_profile_vlan_classification_predefined_vlan_profiletype(delete_vlan_classification=delete_vlan_classification, username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vlan_profiletype=delete_vlan_profiletype, host=host, password=password, delete_hardware_profile=delete_hardware_profile, delete_predefined=delete_predefined, vlan_profiletype=vlan_profiletype, callback=_callback, mgr=mgr)
        return 0
    