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


def protocol_spanning_tree_mstp_error_disable_agtimeout_enable(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    spanning_tree = ET.SubElement(protocol, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    mstp = ET.SubElement(spanning_tree, "mstp")
    if kwargs.pop('delete_mstp', False) is True:
        delete_mstp = config.find('.//*mstp')
        delete_mstp.set('operation', 'delete')
        
    error_disable_agtimeout = ET.SubElement(mstp, "error-disable-agtimeout")
    if kwargs.pop('delete_error_disable_agtimeout', False) is True:
        delete_error_disable_agtimeout = config.find('.//*error-disable-agtimeout')
        delete_error_disable_agtimeout.set('operation', 'delete')
        
    enable = ET.SubElement(error_disable_agtimeout, "enable")
    if kwargs.pop('delete_enable', False) is True:
        delete_enable = config.find('.//*enable')
        delete_enable.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_spanning_tree_mstp_error_disable_agtimeout_enable_act(Action):
    def run(self, delete_error_disable_agtimeout, delete_mstp, delete_enable, delete_spanning_tree, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_spanning_tree_mstp_error_disable_agtimeout_enable(delete_error_disable_agtimeout=delete_error_disable_agtimeout, delete_enable=delete_enable, delete_spanning_tree=delete_spanning_tree, delete_protocol=delete_protocol, delete_mstp=delete_mstp, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    