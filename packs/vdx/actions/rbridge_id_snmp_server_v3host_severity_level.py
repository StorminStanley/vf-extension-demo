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


def rbridge_id_snmp_server_v3host_severity_level(**kwargs):
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
            
    snmp_server = ET.SubElement(rbridge_id, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
    if kwargs.pop('delete_snmp_server', False) is True:
        delete_snmp_server = config.find('.//*snmp-server')
        delete_snmp_server.set('operation', 'delete')
        
    v3host = ET.SubElement(snmp_server, "v3host")
    if kwargs.pop('delete_v3host', False) is True:
        delete_v3host = config.find('.//*v3host')
        delete_v3host.set('operation', 'delete')
        
    hostip_key = ET.SubElement(v3host, "hostip")
    hostip_key.text = kwargs.pop('hostip')
    if kwargs.pop('delete_hostip', False) is True:
        delete_hostip = config.find('.//*hostip')
        delete_hostip.set('operation', 'delete')
            
    username_key = ET.SubElement(v3host, "username")
    username_key.text = kwargs.pop('username')
    if kwargs.pop('delete_username', False) is True:
        delete_username = config.find('.//*username')
        delete_username.set('operation', 'delete')
            
    severity_level = ET.SubElement(v3host, "severity-level")
    if kwargs.pop('delete_severity_level', False) is True:
        delete_severity_level = config.find('.//*severity-level')
        delete_severity_level.set('operation', 'delete')
        
    severity_level.text = kwargs.pop('severity_level')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_snmp_server_v3host_severity_level_act(Action):
    def run(self, delete_snmp_server, username, severity_level, rbridge_id, delete_username, hostip, delete_hostip, delete_rbridge_id, delete_severity_level, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_snmp_server_v3host_severity_level(delete_snmp_server=delete_snmp_server, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_hostip=delete_hostip, severity_level=severity_level, host=host, delete_username=delete_username, hostip=hostip, username=username, password=password, delete_severity_level=delete_severity_level, callback=_callback, mgr=mgr)
        return 0
    