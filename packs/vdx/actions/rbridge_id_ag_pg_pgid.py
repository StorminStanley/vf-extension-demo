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


def rbridge_id_ag_pg_pgid(**kwargs):
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
            
    ag = ET.SubElement(rbridge_id, "ag", xmlns="urn:brocade.com:mgmt:brocade-ag")
    if kwargs.pop('delete_ag', False) is True:
        delete_ag = config.find('.//*ag')
        delete_ag.set('operation', 'delete')
        
    pg = ET.SubElement(ag, "pg")
    if kwargs.pop('delete_pg', False) is True:
        delete_pg = config.find('.//*pg')
        delete_pg.set('operation', 'delete')
        
    pgid = ET.SubElement(pg, "pgid")
    if kwargs.pop('delete_pgid', False) is True:
        delete_pgid = config.find('.//*pgid')
        delete_pgid.set('operation', 'delete')
        
    pgid.text = kwargs.pop('pgid')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ag_pg_pgid_act(Action):
    def run(self, pgid, rbridge_id, delete_pg, delete_pgid, delete_ag, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ag_pg_pgid(delete_ag=delete_ag, username=username, delete_pgid=delete_pgid, delete_pg=delete_pg, rbridge_id=rbridge_id, pgid=pgid, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    