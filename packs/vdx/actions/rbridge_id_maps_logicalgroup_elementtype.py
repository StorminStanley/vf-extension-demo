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


def rbridge_id_maps_logicalgroup_elementtype(**kwargs):
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
        
    logicalgroup = ET.SubElement(maps, "logicalgroup")
    if kwargs.pop('delete_logicalgroup', False) is True:
        delete_logicalgroup = config.find('.//*logicalgroup')
        delete_logicalgroup.set('operation', 'delete')
        
    logicalgroupname_key = ET.SubElement(logicalgroup, "logicalgroupname")
    logicalgroupname_key.text = kwargs.pop('logicalgroupname')
    if kwargs.pop('delete_logicalgroupname', False) is True:
        delete_logicalgroupname = config.find('.//*logicalgroupname')
        delete_logicalgroupname.set('operation', 'delete')
            
    elementtype = ET.SubElement(logicalgroup, "elementtype")
    if kwargs.pop('delete_elementtype', False) is True:
        delete_elementtype = config.find('.//*elementtype')
        delete_elementtype.set('operation', 'delete')
        
    elementtype.text = kwargs.pop('elementtype')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_maps_logicalgroup_elementtype_act(Action):
    def run(self, delete_logicalgroupname, rbridge_id, delete_elementtype, delete_maps, delete_logicalgroup, logicalgroupname, delete_rbridge_id, elementtype, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_maps_logicalgroup_elementtype(delete_logicalgroupname=delete_logicalgroupname, username=username, delete_elementtype=delete_elementtype, elementtype=elementtype, rbridge_id=rbridge_id, delete_maps=delete_maps, delete_logicalgroup=delete_logicalgroup, host=host, logicalgroupname=logicalgroupname, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    