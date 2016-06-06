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


def rbridge_id_hardware_profile_kap_customized_kap_profilename(**kwargs):
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
        
    customized = ET.SubElement(kap, "customized")
    if kwargs.pop('delete_customized', False) is True:
        delete_customized = config.find('.//*customized')
        delete_customized.set('operation', 'delete')
        
    kap_profilename = ET.SubElement(customized, "kap_profilename")
    if kwargs.pop('delete_kap_profilename', False) is True:
        delete_kap_profilename = config.find('.//*kap_profilename')
        delete_kap_profilename.set('operation', 'delete')
        
    kap_profilename.text = kwargs.pop('kap_profilename')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_hardware_profile_kap_customized_kap_profilename_act(Action):
    def run(self, rbridge_id, kap_profilename, delete_hardware_profile, delete_kap, delete_rbridge_id, delete_customized, delete_kap_profilename, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_hardware_profile_kap_customized_kap_profilename(delete_kap_profilename=delete_kap_profilename, username=username, rbridge_id=rbridge_id, kap_profilename=kap_profilename, delete_kap=delete_kap, host=host, delete_hardware_profile=delete_hardware_profile, delete_customized=delete_customized, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    