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


def interface_hundredgigabitethernet_qos_flowcontrol_pfc_pfc_flowcontrol_tx(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    qos = ET.SubElement(hundredgigabitethernet, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
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
            
    pfc_flowcontrol_tx = ET.SubElement(pfc, "pfc-flowcontrol-tx")
    if kwargs.pop('delete_pfc_flowcontrol_tx', False) is True:
        delete_pfc_flowcontrol_tx = config.find('.//*pfc-flowcontrol-tx')
        delete_pfc_flowcontrol_tx.set('operation', 'delete')
        
    pfc_flowcontrol_tx.text = kwargs.pop('pfc_flowcontrol_tx')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_qos_flowcontrol_pfc_pfc_flowcontrol_tx_act(Action):
    def run(self, delete_qos, name, delete_pfc_flowcontrol_tx, pfc_cos, delete_pfc, pfc_flowcontrol_tx, delete_flowcontrol, delete_interface, delete_name, delete_hundredgigabitethernet, delete_pfc_cos, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_qos_flowcontrol_pfc_pfc_flowcontrol_tx(delete_qos=delete_qos, pfc_cos=pfc_cos, delete_flowcontrol=delete_flowcontrol, delete_pfc_flowcontrol_tx=delete_pfc_flowcontrol_tx, username=username, name=name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, password=password, delete_pfc_cos=delete_pfc_cos, delete_name=delete_name, delete_interface=delete_interface, pfc_flowcontrol_tx=pfc_flowcontrol_tx, delete_pfc=delete_pfc, callback=_callback, mgr=mgr)
        return 0
    