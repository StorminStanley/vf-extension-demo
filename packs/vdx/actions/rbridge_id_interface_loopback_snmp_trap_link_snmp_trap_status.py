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


def rbridge_id_interface_loopback_snmp_trap_link_snmp_trap_status(**kwargs):
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
        
    loopback = ET.SubElement(interface, "loopback", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
    if kwargs.pop('delete_loopback', False) is True:
        delete_loopback = config.find('.//*loopback')
        delete_loopback.set('operation', 'delete')
        
    id_key = ET.SubElement(loopback, "id")
    id_key.text = kwargs.pop('id')
    if kwargs.pop('delete_id', False) is True:
        delete_id = config.find('.//*id')
        delete_id.set('operation', 'delete')
            
    snmp = ET.SubElement(loopback, "snmp")
    if kwargs.pop('delete_snmp', False) is True:
        delete_snmp = config.find('.//*snmp')
        delete_snmp.set('operation', 'delete')
        
    trap = ET.SubElement(snmp, "trap")
    if kwargs.pop('delete_trap', False) is True:
        delete_trap = config.find('.//*trap')
        delete_trap.set('operation', 'delete')
        
    link_snmp_trap_status = ET.SubElement(trap, "link-snmp-trap-status")
    if kwargs.pop('delete_link_snmp_trap_status', False) is True:
        delete_link_snmp_trap_status = config.find('.//*link-snmp-trap-status')
        delete_link_snmp_trap_status.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_loopback_snmp_trap_link_snmp_trap_status_act(Action):
    def run(self, rbridge_id, delete_trap, delete_id, delete_loopback, delete_interface, delete_snmp, delete_link_snmp_trap_status, delete_rbridge_id, id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_loopback_snmp_trap_link_snmp_trap_status(username=username, delete_link_snmp_trap_status=delete_link_snmp_trap_status, delete_snmp=delete_snmp, rbridge_id=rbridge_id, delete_id=delete_id, delete_loopback=delete_loopback, delete_trap=delete_trap, host=host, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, id=id, password=password, callback=_callback, mgr=mgr)
        return 0
    