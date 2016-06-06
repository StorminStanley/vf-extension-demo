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


def rbridge_id_ssh_server_ssh_vrf_cont_use_vrf_use_vrf_name(**kwargs):
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
            
    ssh = ET.SubElement(rbridge_id, "ssh", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
    if kwargs.pop('delete_ssh', False) is True:
        delete_ssh = config.find('.//*ssh')
        delete_ssh.set('operation', 'delete')
        
    server = ET.SubElement(ssh, "server")
    if kwargs.pop('delete_server', False) is True:
        delete_server = config.find('.//*server')
        delete_server.set('operation', 'delete')
        
    ssh_vrf_cont = ET.SubElement(server, "ssh-vrf-cont")
    if kwargs.pop('delete_ssh_vrf_cont', False) is True:
        delete_ssh_vrf_cont = config.find('.//*ssh-vrf-cont')
        delete_ssh_vrf_cont.set('operation', 'delete')
        
    use_vrf = ET.SubElement(ssh_vrf_cont, "use-vrf")
    if kwargs.pop('delete_use_vrf', False) is True:
        delete_use_vrf = config.find('.//*use-vrf')
        delete_use_vrf.set('operation', 'delete')
        
    use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
    if kwargs.pop('delete_use_vrf_name', False) is True:
        delete_use_vrf_name = config.find('.//*use-vrf-name')
        delete_use_vrf_name.set('operation', 'delete')
        
    use_vrf_name.text = kwargs.pop('use_vrf_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ssh_server_ssh_vrf_cont_use_vrf_use_vrf_name_act(Action):
    def run(self, delete_use_vrf, use_vrf_name, rbridge_id, delete_use_vrf_name, delete_server, delete_ssh_vrf_cont, delete_ssh, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ssh_server_ssh_vrf_cont_use_vrf_use_vrf_name(use_vrf_name=use_vrf_name, username=username, delete_ssh=delete_ssh, rbridge_id=rbridge_id, delete_use_vrf_name=delete_use_vrf_name, delete_ssh_vrf_cont=delete_ssh_vrf_cont, host=host, delete_use_vrf=delete_use_vrf, delete_rbridge_id=delete_rbridge_id, delete_server=delete_server, password=password, callback=_callback, mgr=mgr)
        return 0
    