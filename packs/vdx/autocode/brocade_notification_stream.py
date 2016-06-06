#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_notification_stream(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def BGPSessionState_BGPPeerIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_BGPSessionState', False) is True:
            delete_BGPSessionState = config.find('.//*BGPSessionState')
            delete_BGPSessionState.set('operation', 'delete')
            
        BGPPeerIpAddress = ET.SubElement(BGPSessionState, "BGPPeerIpAddress")
        if kwargs.pop('delete_BGPPeerIpAddress', False) is True:
            delete_BGPPeerIpAddress = config.find('.//*BGPPeerIpAddress')
            delete_BGPPeerIpAddress.set('operation', 'delete')
            
        BGPPeerIpAddress.text = kwargs.pop('BGPPeerIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_BGPPeerState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_BGPSessionState', False) is True:
            delete_BGPSessionState = config.find('.//*BGPSessionState')
            delete_BGPSessionState.set('operation', 'delete')
            
        BGPPeerState = ET.SubElement(BGPSessionState, "BGPPeerState")
        if kwargs.pop('delete_BGPPeerState', False) is True:
            delete_BGPPeerState = config.find('.//*BGPPeerState')
            delete_BGPPeerState.set('operation', 'delete')
            
        BGPPeerState.text = kwargs.pop('BGPPeerState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_BGPNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_BGPNeighborPrefixExceeded', False) is True:
            delete_BGPNeighborPrefixExceeded = config.find('.//*BGPNeighborPrefixExceeded')
            delete_BGPNeighborPrefixExceeded.set('operation', 'delete')
            
        BGPNeighborIpAddress = ET.SubElement(BGPNeighborPrefixExceeded, "BGPNeighborIpAddress")
        if kwargs.pop('delete_BGPNeighborIpAddress', False) is True:
            delete_BGPNeighborIpAddress = config.find('.//*BGPNeighborIpAddress')
            delete_BGPNeighborIpAddress.set('operation', 'delete')
            
        BGPNeighborIpAddress.text = kwargs.pop('BGPNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_neighborPrefixLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_BGPNeighborPrefixExceeded', False) is True:
            delete_BGPNeighborPrefixExceeded = config.find('.//*BGPNeighborPrefixExceeded')
            delete_BGPNeighborPrefixExceeded.set('operation', 'delete')
            
        neighborPrefixLimit = ET.SubElement(BGPNeighborPrefixExceeded, "neighborPrefixLimit")
        if kwargs.pop('delete_neighborPrefixLimit', False) is True:
            delete_neighborPrefixLimit = config.find('.//*neighborPrefixLimit')
            delete_neighborPrefixLimit.set('operation', 'delete')
            
        neighborPrefixLimit.text = kwargs.pop('neighborPrefixLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_RIBRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_RIBSystemRouteLimitExceeded', False) is True:
            delete_RIBSystemRouteLimitExceeded = config.find('.//*RIBSystemRouteLimitExceeded')
            delete_RIBSystemRouteLimitExceeded.set('operation', 'delete')
            
        RIBRouteLimit = ET.SubElement(RIBSystemRouteLimitExceeded, "RIBRouteLimit")
        if kwargs.pop('delete_RIBRouteLimit', False) is True:
            delete_RIBRouteLimit = config.find('.//*RIBRouteLimit')
            delete_RIBRouteLimit.set('operation', 'delete')
            
        RIBRouteLimit.text = kwargs.pop('RIBRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_RIBNextHopLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_RIBNextHopLimitExceeded', False) is True:
            delete_RIBNextHopLimitExceeded = config.find('.//*RIBNextHopLimitExceeded')
            delete_RIBNextHopLimitExceeded.set('operation', 'delete')
            
        RIBNextHopLimit = ET.SubElement(RIBNextHopLimitExceeded, "RIBNextHopLimit")
        if kwargs.pop('delete_RIBNextHopLimit', False) is True:
            delete_RIBNextHopLimit = config.find('.//*RIBNextHopLimit')
            delete_RIBNextHopLimit.set('operation', 'delete')
            
        RIBNextHopLimit.text = kwargs.pop('RIBNextHopLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelDestinationIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_VxLANTunnelState', False) is True:
            delete_VxLANTunnelState = config.find('.//*VxLANTunnelState')
            delete_VxLANTunnelState.set('operation', 'delete')
            
        TunnelDestinationIpAddress = ET.SubElement(VxLANTunnelState, "TunnelDestinationIpAddress")
        if kwargs.pop('delete_TunnelDestinationIpAddress', False) is True:
            delete_TunnelDestinationIpAddress = config.find('.//*TunnelDestinationIpAddress')
            delete_TunnelDestinationIpAddress.set('operation', 'delete')
            
        TunnelDestinationIpAddress.text = kwargs.pop('TunnelDestinationIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_VxLANTunnelState', False) is True:
            delete_VxLANTunnelState = config.find('.//*VxLANTunnelState')
            delete_VxLANTunnelState.set('operation', 'delete')
            
        TunnelState = ET.SubElement(VxLANTunnelState, "TunnelState")
        if kwargs.pop('delete_TunnelState', False) is True:
            delete_TunnelState = config.find('.//*TunnelState')
            delete_TunnelState.set('operation', 'delete')
            
        TunnelState.text = kwargs.pop('TunnelState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_OSPFNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_OSPFNeighborState', False) is True:
            delete_OSPFNeighborState = config.find('.//*OSPFNeighborState')
            delete_OSPFNeighborState.set('operation', 'delete')
            
        OSPFNeighborIpAddress = ET.SubElement(OSPFNeighborState, "OSPFNeighborIpAddress")
        if kwargs.pop('delete_OSPFNeighborIpAddress', False) is True:
            delete_OSPFNeighborIpAddress = config.find('.//*OSPFNeighborIpAddress')
            delete_OSPFNeighborIpAddress.set('operation', 'delete')
            
        OSPFNeighborIpAddress.text = kwargs.pop('OSPFNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_NeighborState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_OSPFNeighborState', False) is True:
            delete_OSPFNeighborState = config.find('.//*OSPFNeighborState')
            delete_OSPFNeighborState.set('operation', 'delete')
            
        NeighborState = ET.SubElement(OSPFNeighborState, "NeighborState")
        if kwargs.pop('delete_NeighborState', False) is True:
            delete_NeighborState = config.find('.//*NeighborState')
            delete_NeighborState.set('operation', 'delete')
            
        NeighborState.text = kwargs.pop('NeighborState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_NewMasterIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_VRRPNewMaster', False) is True:
            delete_VRRPNewMaster = config.find('.//*VRRPNewMaster')
            delete_VRRPNewMaster.set('operation', 'delete')
            
        NewMasterIpAddress = ET.SubElement(VRRPNewMaster, "NewMasterIpAddress")
        if kwargs.pop('delete_NewMasterIpAddress', False) is True:
            delete_NewMasterIpAddress = config.find('.//*NewMasterIpAddress')
            delete_NewMasterIpAddress.set('operation', 'delete')
            
        NewMasterIpAddress.text = kwargs.pop('NewMasterIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_VRRPSessionId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_VRRPNewMaster', False) is True:
            delete_VRRPNewMaster = config.find('.//*VRRPNewMaster')
            delete_VRRPNewMaster.set('operation', 'delete')
            
        VRRPSessionId = ET.SubElement(VRRPNewMaster, "VRRPSessionId")
        if kwargs.pop('delete_VRRPSessionId', False) is True:
            delete_VRRPSessionId = config.find('.//*VRRPSessionId')
            delete_VRRPSessionId.set('operation', 'delete')
            
        VRRPSessionId.text = kwargs.pop('VRRPSessionId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_VRFName(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_RIBVRFRouteLimitExceeded', False) is True:
            delete_RIBVRFRouteLimitExceeded = config.find('.//*RIBVRFRouteLimitExceeded')
            delete_RIBVRFRouteLimitExceeded.set('operation', 'delete')
            
        VRFName = ET.SubElement(RIBVRFRouteLimitExceeded, "VRFName")
        if kwargs.pop('delete_VRFName', False) is True:
            delete_VRFName = config.find('.//*VRFName')
            delete_VRFName.set('operation', 'delete')
            
        VRFName.text = kwargs.pop('VRFName')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_RIBVRFRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_RIBVRFRouteLimitExceeded', False) is True:
            delete_RIBVRFRouteLimitExceeded = config.find('.//*RIBVRFRouteLimitExceeded')
            delete_RIBVRFRouteLimitExceeded.set('operation', 'delete')
            
        RIBVRFRouteLimit = ET.SubElement(RIBVRFRouteLimitExceeded, "RIBVRFRouteLimit")
        if kwargs.pop('delete_RIBVRFRouteLimit', False) is True:
            delete_RIBVRFRouteLimit = config.find('.//*RIBVRFRouteLimit')
            delete_RIBVRFRouteLimit.set('operation', 'delete')
            
        RIBVRFRouteLimit.text = kwargs.pop('RIBVRFRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_ARPLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_ARPLimitExceeded', False) is True:
            delete_ARPLimitExceeded = config.find('.//*ARPLimitExceeded')
            delete_ARPLimitExceeded.set('operation', 'delete')
            
        ARPLimit = ET.SubElement(ARPLimitExceeded, "ARPLimit")
        if kwargs.pop('delete_ARPLimit', False) is True:
            delete_ARPLimit = config.find('.//*ARPLimit')
            delete_ARPLimit.set('operation', 'delete')
            
        ARPLimit.text = kwargs.pop('ARPLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_NDLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        if kwargs.pop('delete_NDLimitExceeded', False) is True:
            delete_NDLimitExceeded = config.find('.//*NDLimitExceeded')
            delete_NDLimitExceeded.set('operation', 'delete')
            
        NDLimit = ET.SubElement(NDLimitExceeded, "NDLimit")
        if kwargs.pop('delete_NDLimit', False) is True:
            delete_NDLimit = config.find('.//*NDLimit')
            delete_NDLimit.set('operation', 'delete')
            
        NDLimit.text = kwargs.pop('NDLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        