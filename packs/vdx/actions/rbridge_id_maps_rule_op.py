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


def rbridge_id_maps_rule_op(**kwargs):
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
            
    maps = ET.SubElement(rbridge_id, "maps", xmlns="urn:brocade.com:mgmt:brocade-maps")
    if kwargs.pop('delete_maps', False) is True:
        delete_maps = config.find('.//*maps')
        delete_maps.set('operation', 'delete')
        
    rule = ET.SubElement(maps, "rule")
    if kwargs.pop('delete_rule', False) is True:
        delete_rule = config.find('.//*rule')
        delete_rule.set('operation', 'delete')
        
    rulename_key = ET.SubElement(rule, "rulename")
    rulename_key.text = kwargs.pop('rulename')
    if kwargs.pop('delete_rulename', False) is True:
        delete_rulename = config.find('.//*rulename')
        delete_rulename.set('operation', 'delete')
            
    op = ET.SubElement(rule, "op")
    if kwargs.pop('delete_op', False) is True:
        delete_op = config.find('.//*op')
        delete_op.set('operation', 'delete')
        
    op.text = kwargs.pop('op')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_maps_rule_op_act(Action):
    def run(self, delete_op, rbridge_id, delete_maps, delete_rulename, rulename, delete_rbridge_id, delete_rule, op, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_maps_rule_op(op=op, username=username, rbridge_id=rbridge_id, delete_maps=delete_maps, rulename=rulename, delete_rulename=delete_rulename, delete_rule=delete_rule, delete_op=delete_op, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    