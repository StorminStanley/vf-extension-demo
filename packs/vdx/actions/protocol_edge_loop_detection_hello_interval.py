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


def protocol_edge_loop_detection_hello_interval(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    edge_loop_detection = ET.SubElement(protocol, "edge-loop-detection", xmlns="urn:brocade.com:mgmt:brocade-eld")
    if kwargs.pop('delete_edge_loop_detection', False) is True:
        delete_edge_loop_detection = config.find('.//*edge-loop-detection')
        delete_edge_loop_detection.set('operation', 'delete')
        
    hello_interval = ET.SubElement(edge_loop_detection, "hello-interval")
    if kwargs.pop('delete_hello_interval', False) is True:
        delete_hello_interval = config.find('.//*hello-interval')
        delete_hello_interval.set('operation', 'delete')
        
    hello_interval.text = kwargs.pop('hello_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_edge_loop_detection_hello_interval_act(Action):
    def run(self, delete_hello_interval, hello_interval, delete_edge_loop_detection, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_edge_loop_detection_hello_interval(delete_protocol=delete_protocol, delete_edge_loop_detection=delete_edge_loop_detection, hello_interval=hello_interval, host=host, delete_hello_interval=delete_hello_interval, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    