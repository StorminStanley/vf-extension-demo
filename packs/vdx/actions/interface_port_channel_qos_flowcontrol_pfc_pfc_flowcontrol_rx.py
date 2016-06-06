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


def interface_port_channel_qos_flowcontrol_pfc_pfc_flowcontrol_rx(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    qos = ET.SubElement(port_channel, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
    if kwargs.pop('delete_qos', False) is True:
        delete_qos = config.find('.//*qos')
        delete_qos.set('operation', 'delete')
        
    flowcontrol = ET.SubElement(qos, "flowcontrol")
    if kwargs.pop('delete_flowcontrol', False) is True:
        delete_flowcontrol = config.find('.//*flowcontrol')
        delete_flowcontrol.set('operation', 'delete')
        
    pfc = ET.SubElement(flowcontrol, "pfc")
    if kwargs.pop('delete_pfc', False) is True:
        delete_pfc = config.find('.//*pfc')
        delete_pfc.set('operation', 'delete')
        
    pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
    pfc_cos_key.text = kwargs.pop('pfc_cos')
    if kwargs.pop('delete_pfc_cos', False) is True:
        delete_pfc_cos = config.find('.//*pfc-cos')
        delete_pfc_cos.set('operation', 'delete')
            
    pfc_flowcontrol_rx = ET.SubElement(pfc, "pfc-flowcontrol-rx")
    if kwargs.pop('delete_pfc_flowcontrol_rx', False) is True:
        delete_pfc_flowcontrol_rx = config.find('.//*pfc-flowcontrol-rx')
        delete_pfc_flowcontrol_rx.set('operation', 'delete')
        
    pfc_flowcontrol_rx.text = kwargs.pop('pfc_flowcontrol_rx')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_qos_flowcontrol_pfc_pfc_flowcontrol_rx_act(Action):
    def run(self, delete_qos, pfc_flowcontrol_rx, name, pfc_cos, delete_pfc_flowcontrol_rx, delete_pfc, delete_flowcontrol, delete_port_channel, delete_interface, delete_name, delete_pfc_cos, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_qos_flowcontrol_pfc_pfc_flowcontrol_rx(delete_pfc_flowcontrol_rx=delete_pfc_flowcontrol_rx, delete_qos=delete_qos, pfc_cos=pfc_cos, delete_flowcontrol=delete_flowcontrol, delete_port_channel=delete_port_channel, name=name, pfc_flowcontrol_rx=pfc_flowcontrol_rx, host=host, password=password, delete_pfc_cos=delete_pfc_cos, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_pfc=delete_pfc, callback=_callback, mgr=mgr)
        return 0
    