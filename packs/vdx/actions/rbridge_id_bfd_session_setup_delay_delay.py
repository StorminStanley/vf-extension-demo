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


def rbridge_id_bfd_session_setup_delay_delay(**kwargs):
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
            
    bfd_session_setup_delay = ET.SubElement(rbridge_id, "bfd-session-setup-delay", xmlns="urn:brocade.com:mgmt:brocade-bfd")
    if kwargs.pop('delete_bfd_session_setup_delay', False) is True:
        delete_bfd_session_setup_delay = config.find('.//*bfd-session-setup-delay')
        delete_bfd_session_setup_delay.set('operation', 'delete')
        
    delay = ET.SubElement(bfd_session_setup_delay, "delay")
    if kwargs.pop('delete_delay', False) is True:
        delete_delay = config.find('.//*delay')
        delete_delay.set('operation', 'delete')
        
    delay.text = kwargs.pop('delay')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_bfd_session_setup_delay_delay_act(Action):
    def run(self, delay, delete_rbridge_id, delete_delay, rbridge_id, delete_bfd_session_setup_delay, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_bfd_session_setup_delay_delay(username=username, rbridge_id=rbridge_id, delete_bfd_session_setup_delay=delete_bfd_session_setup_delay, host=host, delay=delay, delete_delay=delete_delay, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    