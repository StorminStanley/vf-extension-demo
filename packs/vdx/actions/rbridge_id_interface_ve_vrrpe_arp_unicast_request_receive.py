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


def rbridge_id_interface_ve_vrrpe_arp_unicast_request_receive(**kwargs):
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
            
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    vrrpe = ET.SubElement(ve, "vrrpe", xmlns="urn:brocade.com:mgmt:brocade-vrrp")
    if kwargs.pop('delete_vrrpe', False) is True:
        delete_vrrpe = config.find('.//*vrrpe')
        delete_vrrpe.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrpe, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    arp = ET.SubElement(vrrpe, "arp")
    if kwargs.pop('delete_arp', False) is True:
        delete_arp = config.find('.//*arp')
        delete_arp.set('operation', 'delete')
        
    unicast_request = ET.SubElement(arp, "unicast-request")
    if kwargs.pop('delete_unicast_request', False) is True:
        delete_unicast_request = config.find('.//*unicast-request')
        delete_unicast_request.set('operation', 'delete')
        
    receive = ET.SubElement(unicast_request, "receive")
    if kwargs.pop('delete_receive', False) is True:
        delete_receive = config.find('.//*receive')
        delete_receive.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_vrrpe_arp_unicast_request_receive_act(Action):
    def run(self, delete_unicast_request, name, delete_vrid, delete_receive, vrid, delete_ve, delete_arp, delete_interface, delete_name, delete_rbridge_id, delete_vrrpe, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_vrrpe_arp_unicast_request_receive(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_vrrpe=delete_vrrpe, username=username, delete_arp=delete_arp, delete_receive=delete_receive, delete_ve=delete_ve, password=password, vrid=vrid, host=host, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_unicast_request=delete_unicast_request, callback=_callback, mgr=mgr)
        return 0
    