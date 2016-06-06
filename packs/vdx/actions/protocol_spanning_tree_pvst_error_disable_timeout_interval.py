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


def protocol_spanning_tree_pvst_error_disable_agtimeout_interval(**kwargs):
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
        
    pvst = ET.SubElement(spanning_tree, "pvst")
    if kwargs.pop('delete_pvst', False) is True:
        delete_pvst = config.find('.//*pvst')
        delete_pvst.set('operation', 'delete')
        
    error_disable_agtimeout = ET.SubElement(pvst, "error-disable-agtimeout")
    if kwargs.pop('delete_error_disable_agtimeout', False) is True:
        delete_error_disable_agtimeout = config.find('.//*error-disable-agtimeout')
        delete_error_disable_agtimeout.set('operation', 'delete')
        
    interval = ET.SubElement(error_disable_agtimeout, "interval")
    if kwargs.pop('delete_interval', False) is True:
        delete_interval = config.find('.//*interval')
        delete_interval.set('operation', 'delete')
        
    interval.text = kwargs.pop('interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_spanning_tree_pvst_error_disable_agtimeout_interval_act(Action):
    def run(self, delete_interval, delete_error_disable_agtimeout, delete_protocol, interval, delete_pvst, delete_spanning_tree, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_spanning_tree_pvst_error_disable_agtimeout_interval(delete_interval=delete_interval, delete_pvst=delete_pvst, delete_error_disable_agtimeout=delete_error_disable_agtimeout, delete_spanning_tree=delete_spanning_tree, delete_protocol=delete_protocol, interval=interval, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    