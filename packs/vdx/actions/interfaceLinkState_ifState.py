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


def interfaceLinkState_ifState(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interfaceLinkState = ET.SubElement(config, "interfaceLinkState", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interfaceLinkState', False) is True:
        delete_interfaceLinkState = config.find('.//*interfaceLinkState')
        delete_interfaceLinkState.set('operation', 'delete')
        
    ifState = ET.SubElement(interfaceLinkState, "ifState")
    if kwargs.pop('delete_ifState', False) is True:
        delete_ifState = config.find('.//*ifState')
        delete_ifState.set('operation', 'delete')
        
    ifState.text = kwargs.pop('ifState')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interfaceLinkState_ifState_act(Action):
    def run(self, delete_ifState, delete_interfaceLinkState, ifState, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interfaceLinkState_ifState(delete_ifState=delete_ifState, delete_interfaceLinkState=delete_interfaceLinkState, host=host, ifState=ifState, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    