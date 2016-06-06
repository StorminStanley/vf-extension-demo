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


def interfaceLinkState_ifName(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interfaceLinkState = ET.SubElement(config, "interfaceLinkState", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interfaceLinkState', False) is True:
        delete_interfaceLinkState = config.find('.//*interfaceLinkState')
        delete_interfaceLinkState.set('operation', 'delete')
        
    ifName = ET.SubElement(interfaceLinkState, "ifName")
    if kwargs.pop('delete_ifName', False) is True:
        delete_ifName = config.find('.//*ifName')
        delete_ifName.set('operation', 'delete')
        
    ifName.text = kwargs.pop('ifName')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interfaceLinkState_ifName_act(Action):
    def run(self, ifName, delete_interfaceLinkState, delete_ifName, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interfaceLinkState_ifName(delete_ifName=delete_ifName, username=username, delete_interfaceLinkState=delete_interfaceLinkState, host=host, ifName=ifName, password=password, callback=_callback, mgr=mgr)
        return 0
    