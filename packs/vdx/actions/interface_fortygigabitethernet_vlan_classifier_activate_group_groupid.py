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


def interface_fortygigabitethernet_vlan_classifier_activate_group_groupid(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    vlan = ET.SubElement(fortygigabitethernet, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    classifier = ET.SubElement(vlan, "classifier")
    if kwargs.pop('delete_classifier', False) is True:
        delete_classifier = config.find('.//*classifier')
        delete_classifier.set('operation', 'delete')
        
    activate = ET.SubElement(classifier, "activate")
    if kwargs.pop('delete_activate', False) is True:
        delete_activate = config.find('.//*activate')
        delete_activate.set('operation', 'delete')
        
    group = ET.SubElement(activate, "group")
    if kwargs.pop('delete_group', False) is True:
        delete_group = config.find('.//*group')
        delete_group.set('operation', 'delete')
        
    groupid = ET.SubElement(group, "groupid")
    if kwargs.pop('delete_groupid', False) is True:
        delete_groupid = config.find('.//*groupid')
        delete_groupid.set('operation', 'delete')
        
    groupid.text = kwargs.pop('groupid')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_vlan_classifier_activate_group_groupid_act(Action):
    def run(self, delete_vlan, delete_classifier, name, delete_group, delete_fortygigabitethernet, delete_activate, delete_interface, delete_name, delete_groupid, groupid, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_vlan_classifier_activate_group_groupid(delete_activate=delete_activate, name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_vlan=delete_vlan, delete_groupid=delete_groupid, delete_classifier=delete_classifier, groupid=groupid, host=host, delete_group=delete_group, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    