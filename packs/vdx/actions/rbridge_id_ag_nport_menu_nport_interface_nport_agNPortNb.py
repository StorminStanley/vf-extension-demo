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


def rbridge_id_ag_nport_menu_nport_interface_nport_agNPortNb(**kwargs):
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
            
    ag = ET.SubElement(rbridge_id, "ag", xmlns="urn:brocade.com:mgmt:brocade-ag")
    if kwargs.pop('delete_ag', False) is True:
        delete_ag = config.find('.//*ag')
        delete_ag.set('operation', 'delete')
        
    nport_menu = ET.SubElement(ag, "nport-menu")
    if kwargs.pop('delete_nport_menu', False) is True:
        delete_nport_menu = config.find('.//*nport-menu')
        delete_nport_menu.set('operation', 'delete')
        
    nport_interface = ET.SubElement(nport_menu, "nport-interface")
    if kwargs.pop('delete_nport_interface', False) is True:
        delete_nport_interface = config.find('.//*nport-interface')
        delete_nport_interface.set('operation', 'delete')
        
    nport = ET.SubElement(nport_interface, "nport")
    if kwargs.pop('delete_nport', False) is True:
        delete_nport = config.find('.//*nport')
        delete_nport.set('operation', 'delete')
        
    agNPortNb = ET.SubElement(nport, "agNPortNb")
    if kwargs.pop('delete_agNPortNb', False) is True:
        delete_agNPortNb = config.find('.//*agNPortNb')
        delete_agNPortNb.set('operation', 'delete')
        
    agNPortNb.text = kwargs.pop('agNPortNb')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ag_nport_menu_nport_interface_nport_agNPortNb_act(Action):
    def run(self, rbridge_id, agNPortNb, delete_agNPortNb, delete_nport, delete_ag, delete_rbridge_id, delete_nport_interface, delete_nport_menu, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ag_nport_menu_nport_interface_nport_agNPortNb(delete_ag=delete_ag, delete_agNPortNb=delete_agNPortNb, username=username, delete_nport_menu=delete_nport_menu, rbridge_id=rbridge_id, agNPortNb=agNPortNb, host=host, password=password, delete_rbridge_id=delete_rbridge_id, delete_nport_interface=delete_nport_interface, delete_nport=delete_nport, callback=_callback, mgr=mgr)
        return 0
    