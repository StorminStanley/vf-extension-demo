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


def interfaceLinkState_ifIndex(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interfaceLinkState = ET.SubElement(config, "interfaceLinkState", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interfaceLinkState', False) is True:
        delete_interfaceLinkState = config.find('.//*interfaceLinkState')
        delete_interfaceLinkState.set('operation', 'delete')
        
    ifIndex = ET.SubElement(interfaceLinkState, "ifIndex")
    if kwargs.pop('delete_ifIndex', False) is True:
        delete_ifIndex = config.find('.//*ifIndex')
        delete_ifIndex.set('operation', 'delete')
        
    ifIndex.text = kwargs.pop('ifIndex')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interfaceLinkState_ifIndex_act(Action):
    def run(self, ifIndex, delete_interfaceLinkState, delete_ifIndex, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interfaceLinkState_ifIndex(ifIndex=ifIndex, delete_ifIndex=delete_ifIndex, host=host, delete_interfaceLinkState=delete_interfaceLinkState, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    