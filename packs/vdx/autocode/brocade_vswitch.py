#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_vswitch(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_vnetwork_hosts_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_hosts, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_hosts, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_hosts, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_hosts, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_hosts, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_vmnic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        vmnic = ET.SubElement(vnetwork_hosts, "vmnic")
        if kwargs.pop('delete_vmnic', False) is True:
            delete_vmnic = config.find('.//*vmnic')
            delete_vmnic.set('operation', 'delete')
            
        vmnic.text = kwargs.pop('vmnic')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_hosts, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        mac = ET.SubElement(vnetwork_hosts, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_vswitch(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        vswitch = ET.SubElement(vnetwork_hosts, "vswitch")
        if kwargs.pop('delete_vswitch', False) is True:
            delete_vswitch = config.find('.//*vswitch')
            delete_vswitch.set('operation', 'delete')
            
        vswitch.text = kwargs.pop('vswitch')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        interface_type = ET.SubElement(vnetwork_hosts, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_vnetwork_hosts_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_hosts = ET.SubElement(output, "vnetwork-hosts")
        if kwargs.pop('delete_vnetwork_hosts', False) is True:
            delete_vnetwork_hosts = config.find('.//*vnetwork-hosts')
            delete_vnetwork_hosts.set('operation', 'delete')
            
        interface_name = ET.SubElement(vnetwork_hosts, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_hosts_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_hosts = ET.Element("get_vnetwork_hosts")
        config = get_vnetwork_hosts
        if kwargs.pop('delete_get_vnetwork_hosts', False) is True:
            delete_get_vnetwork_hosts = config.find('.//*get-vnetwork-hosts')
            delete_get_vnetwork_hosts.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_hosts, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vms, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vms, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vms, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vms, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_vnetwork_vms_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vms = ET.SubElement(output, "vnetwork-vms")
        if kwargs.pop('delete_vnetwork_vms', False) is True:
            delete_vnetwork_vms = config.find('.//*vnetwork-vms')
            delete_vnetwork_vms.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_vms, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_vnetwork_vms_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vms = ET.SubElement(output, "vnetwork-vms")
        if kwargs.pop('delete_vnetwork_vms', False) is True:
            delete_vnetwork_vms = config.find('.//*vnetwork-vms')
            delete_vnetwork_vms.set('operation', 'delete')
            
        mac = ET.SubElement(vnetwork_vms, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_vnetwork_vms_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vms = ET.SubElement(output, "vnetwork-vms")
        if kwargs.pop('delete_vnetwork_vms', False) is True:
            delete_vnetwork_vms = config.find('.//*vnetwork-vms')
            delete_vnetwork_vms.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_vms, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_vnetwork_vms_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vms = ET.SubElement(output, "vnetwork-vms")
        if kwargs.pop('delete_vnetwork_vms', False) is True:
            delete_vnetwork_vms = config.find('.//*vnetwork-vms')
            delete_vnetwork_vms.set('operation', 'delete')
            
        ip = ET.SubElement(vnetwork_vms, "ip")
        if kwargs.pop('delete_ip', False) is True:
            delete_ip = config.find('.//*ip')
            delete_ip.set('operation', 'delete')
            
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_vnetwork_vms_host_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vms = ET.SubElement(output, "vnetwork-vms")
        if kwargs.pop('delete_vnetwork_vms', False) is True:
            delete_vnetwork_vms = config.find('.//*vnetwork-vms')
            delete_vnetwork_vms.set('operation', 'delete')
            
        host_nn = ET.SubElement(vnetwork_vms, "host-nn")
        if kwargs.pop('delete_host_nn', False) is True:
            delete_host_nn = config.find('.//*host-nn')
            delete_host_nn.set('operation', 'delete')
            
        host_nn.text = kwargs.pop('host_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vms_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vms = ET.Element("get_vnetwork_vms")
        config = get_vnetwork_vms
        if kwargs.pop('delete_get_vnetwork_vms', False) is True:
            delete_get_vnetwork_vms = config.find('.//*get-vnetwork-vms')
            delete_get_vnetwork_vms.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vms, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvpgs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvpgs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvpgs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvpgs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_vnetwork_dvpgs_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvpgs = ET.SubElement(output, "vnetwork-dvpgs")
        if kwargs.pop('delete_vnetwork_dvpgs', False) is True:
            delete_vnetwork_dvpgs = config.find('.//*vnetwork-dvpgs')
            delete_vnetwork_dvpgs.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_dvpgs, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_vnetwork_dvpgs_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvpgs = ET.SubElement(output, "vnetwork-dvpgs")
        if kwargs.pop('delete_vnetwork_dvpgs', False) is True:
            delete_vnetwork_dvpgs = config.find('.//*vnetwork-dvpgs')
            delete_vnetwork_dvpgs.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_dvpgs, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_vnetwork_dvpgs_dvs_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvpgs = ET.SubElement(output, "vnetwork-dvpgs")
        if kwargs.pop('delete_vnetwork_dvpgs', False) is True:
            delete_vnetwork_dvpgs = config.find('.//*vnetwork-dvpgs')
            delete_vnetwork_dvpgs.set('operation', 'delete')
            
        dvs_nn = ET.SubElement(vnetwork_dvpgs, "dvs-nn")
        if kwargs.pop('delete_dvs_nn', False) is True:
            delete_dvs_nn = config.find('.//*dvs-nn')
            delete_dvs_nn.set('operation', 'delete')
            
        dvs_nn.text = kwargs.pop('dvs_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_vnetwork_dvpgs_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvpgs = ET.SubElement(output, "vnetwork-dvpgs")
        if kwargs.pop('delete_vnetwork_dvpgs', False) is True:
            delete_vnetwork_dvpgs = config.find('.//*vnetwork-dvpgs')
            delete_vnetwork_dvpgs.set('operation', 'delete')
            
        vlan = ET.SubElement(vnetwork_dvpgs, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvpgs_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvpgs = ET.Element("get_vnetwork_dvpgs")
        config = get_vnetwork_dvpgs
        if kwargs.pop('delete_get_vnetwork_dvpgs', False) is True:
            delete_get_vnetwork_dvpgs = config.find('.//*get-vnetwork-dvpgs')
            delete_get_vnetwork_dvpgs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvpgs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_dvs, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_dvs, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        host = ET.SubElement(vnetwork_dvs, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_dvs, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_pnic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        pnic = ET.SubElement(vnetwork_dvs, "pnic")
        if kwargs.pop('delete_pnic', False) is True:
            delete_pnic = config.find('.//*pnic')
            delete_pnic.set('operation', 'delete')
            
        pnic.text = kwargs.pop('pnic')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        interface_type = ET.SubElement(vnetwork_dvs, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_vnetwork_dvs_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_dvs = ET.SubElement(output, "vnetwork-dvs")
        if kwargs.pop('delete_vnetwork_dvs', False) is True:
            delete_vnetwork_dvs = config.find('.//*vnetwork-dvs')
            delete_vnetwork_dvs.set('operation', 'delete')
            
        interface_name = ET.SubElement(vnetwork_dvs, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_dvs_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_dvs = ET.Element("get_vnetwork_dvs")
        config = get_vnetwork_dvs
        if kwargs.pop('delete_get_vnetwork_dvs', False) is True:
            delete_get_vnetwork_dvs = config.find('.//*get-vnetwork-dvs')
            delete_get_vnetwork_dvs.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_dvs, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vswitches, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vswitches, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vswitches, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_vswitches, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_vswitches, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        host = ET.SubElement(vnetwork_vswitches, "host")
        if kwargs.pop('delete_host', False) is True:
            delete_host = config.find('.//*host')
            delete_host.set('operation', 'delete')
            
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_vswitches, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_pnic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        pnic = ET.SubElement(vnetwork_vswitches, "pnic")
        if kwargs.pop('delete_pnic', False) is True:
            delete_pnic = config.find('.//*pnic')
            delete_pnic.set('operation', 'delete')
            
        pnic.text = kwargs.pop('pnic')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        interface_type = ET.SubElement(vnetwork_vswitches, "interface-type")
        if kwargs.pop('delete_interface_type', False) is True:
            delete_interface_type = config.find('.//*interface-type')
            delete_interface_type.set('operation', 'delete')
            
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_vnetwork_vswitches_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_vswitches = ET.SubElement(output, "vnetwork-vswitches")
        if kwargs.pop('delete_vnetwork_vswitches', False) is True:
            delete_vnetwork_vswitches = config.find('.//*vnetwork-vswitches')
            delete_vnetwork_vswitches.set('operation', 'delete')
            
        interface_name = ET.SubElement(vnetwork_vswitches, "interface-name")
        if kwargs.pop('delete_interface_name', False) is True:
            delete_interface_name = config.find('.//*interface-name')
            delete_interface_name.set('operation', 'delete')
            
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_vswitches_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_vswitches = ET.Element("get_vnetwork_vswitches")
        config = get_vnetwork_vswitches
        if kwargs.pop('delete_get_vnetwork_vswitches', False) is True:
            delete_get_vnetwork_vswitches = config.find('.//*get-vnetwork-vswitches')
            delete_get_vnetwork_vswitches.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_vswitches, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_input_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_portgroups, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        name = ET.SubElement(input, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_portgroups, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_portgroups, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        input = ET.SubElement(get_vnetwork_portgroups, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_vnetwork_pgs_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_pgs = ET.SubElement(output, "vnetwork-pgs")
        if kwargs.pop('delete_vnetwork_pgs', False) is True:
            delete_vnetwork_pgs = config.find('.//*vnetwork-pgs')
            delete_vnetwork_pgs.set('operation', 'delete')
            
        name = ET.SubElement(vnetwork_pgs, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_vnetwork_pgs_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_pgs = ET.SubElement(output, "vnetwork-pgs")
        if kwargs.pop('delete_vnetwork_pgs', False) is True:
            delete_vnetwork_pgs = config.find('.//*vnetwork-pgs')
            delete_vnetwork_pgs.set('operation', 'delete')
            
        datacenter = ET.SubElement(vnetwork_pgs, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_vnetwork_pgs_vs_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_pgs = ET.SubElement(output, "vnetwork-pgs")
        if kwargs.pop('delete_vnetwork_pgs', False) is True:
            delete_vnetwork_pgs = config.find('.//*vnetwork-pgs')
            delete_vnetwork_pgs.set('operation', 'delete')
            
        vs_nn = ET.SubElement(vnetwork_pgs, "vs-nn")
        if kwargs.pop('delete_vs_nn', False) is True:
            delete_vs_nn = config.find('.//*vs-nn')
            delete_vs_nn.set('operation', 'delete')
            
        vs_nn.text = kwargs.pop('vs_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_vnetwork_pgs_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_pgs = ET.SubElement(output, "vnetwork-pgs")
        if kwargs.pop('delete_vnetwork_pgs', False) is True:
            delete_vnetwork_pgs = config.find('.//*vnetwork-pgs')
            delete_vnetwork_pgs.set('operation', 'delete')
            
        vlan = ET.SubElement(vnetwork_pgs, "vlan")
        if kwargs.pop('delete_vlan', False) is True:
            delete_vlan = config.find('.//*vlan')
            delete_vlan.set('operation', 'delete')
            
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_vnetwork_pgs_host_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vnetwork_pgs = ET.SubElement(output, "vnetwork-pgs")
        if kwargs.pop('delete_vnetwork_pgs', False) is True:
            delete_vnetwork_pgs = config.find('.//*vnetwork-pgs')
            delete_vnetwork_pgs.set('operation', 'delete')
            
        host_nn = ET.SubElement(vnetwork_pgs, "host-nn")
        if kwargs.pop('delete_host_nn', False) is True:
            delete_host_nn = config.find('.//*host-nn')
            delete_host_nn.set('operation', 'delete')
            
        host_nn.text = kwargs.pop('host_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vnetwork_portgroups_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vnetwork_portgroups = ET.Element("get_vnetwork_portgroups")
        config = get_vnetwork_portgroups
        if kwargs.pop('delete_get_vnetwork_portgroups', False) is True:
            delete_get_vnetwork_portgroups = config.find('.//*get-vnetwork-portgroups')
            delete_get_vnetwork_portgroups.set('operation', 'delete')
            
        output = ET.SubElement(get_vnetwork_portgroups, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_input_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        input = ET.SubElement(get_vmpolicy_macaddr, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        mac = ET.SubElement(input, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_input_vcenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        input = ET.SubElement(get_vmpolicy_macaddr, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        vcenter = ET.SubElement(input, "vcenter")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        vcenter.text = kwargs.pop('vcenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_input_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        input = ET.SubElement(get_vmpolicy_macaddr, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        datacenter = ET.SubElement(input, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_input_last_rcvd_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        input = ET.SubElement(get_vmpolicy_macaddr, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        last_rcvd_instance = ET.SubElement(input, "last-rcvd-instance")
        if kwargs.pop('delete_last_rcvd_instance', False) is True:
            delete_last_rcvd_instance = config.find('.//*last-rcvd-instance')
            delete_last_rcvd_instance.set('operation', 'delete')
            
        last_rcvd_instance.text = kwargs.pop('last_rcvd_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        mac = ET.SubElement(vmpolicy_macaddr, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        name = ET.SubElement(vmpolicy_macaddr, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_datacenter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        datacenter = ET.SubElement(vmpolicy_macaddr, "datacenter")
        if kwargs.pop('delete_datacenter', False) is True:
            delete_datacenter = config.find('.//*datacenter')
            delete_datacenter.set('operation', 'delete')
            
        datacenter.text = kwargs.pop('datacenter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_dvpg_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        dvpg_nn = ET.SubElement(vmpolicy_macaddr, "dvpg-nn")
        if kwargs.pop('delete_dvpg_nn', False) is True:
            delete_dvpg_nn = config.find('.//*dvpg-nn')
            delete_dvpg_nn.set('operation', 'delete')
            
        dvpg_nn.text = kwargs.pop('dvpg_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_port_nn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        port_nn = ET.SubElement(vmpolicy_macaddr, "port-nn")
        if kwargs.pop('delete_port_nn', False) is True:
            delete_port_nn = config.find('.//*port-nn')
            delete_port_nn.set('operation', 'delete')
            
        port_nn.text = kwargs.pop('port_nn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_vmpolicy_macaddr_port_prof(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        vmpolicy_macaddr = ET.SubElement(output, "vmpolicy-macaddr")
        if kwargs.pop('delete_vmpolicy_macaddr', False) is True:
            delete_vmpolicy_macaddr = config.find('.//*vmpolicy-macaddr')
            delete_vmpolicy_macaddr.set('operation', 'delete')
            
        port_prof = ET.SubElement(vmpolicy_macaddr, "port-prof")
        if kwargs.pop('delete_port_prof', False) is True:
            delete_port_prof = config.find('.//*port-prof')
            delete_port_prof.set('operation', 'delete')
            
        port_prof.text = kwargs.pop('port_prof')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        has_more = ET.SubElement(output, "has-more")
        if kwargs.pop('delete_has_more', False) is True:
            delete_has_more = config.find('.//*has-more')
            delete_has_more.set('operation', 'delete')
            
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vmpolicy_macaddr_output_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vmpolicy_macaddr = ET.Element("get_vmpolicy_macaddr")
        config = get_vmpolicy_macaddr
        if kwargs.pop('delete_get_vmpolicy_macaddr', False) is True:
            delete_get_vmpolicy_macaddr = config.find('.//*get-vmpolicy-macaddr')
            delete_get_vmpolicy_macaddr.set('operation', 'delete')
            
        output = ET.SubElement(get_vmpolicy_macaddr, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        instance_id = ET.SubElement(output, "instance-id")
        if kwargs.pop('delete_instance_id', False) is True:
            delete_instance_id = config.find('.//*instance-id')
            delete_instance_id.set('operation', 'delete')
            
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id = ET.SubElement(vcenter, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_credentials_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        credentials = ET.SubElement(vcenter, "credentials")
        if kwargs.pop('delete_credentials', False) is True:
            delete_credentials = config.find('.//*credentials')
            delete_credentials.set('operation', 'delete')
            
        url = ET.SubElement(credentials, "url")
        if kwargs.pop('delete_url', False) is True:
            delete_url = config.find('.//*url')
            delete_url.set('operation', 'delete')
            
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_credentials_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        credentials = ET.SubElement(vcenter, "credentials")
        if kwargs.pop('delete_credentials', False) is True:
            delete_credentials = config.find('.//*credentials')
            delete_credentials.set('operation', 'delete')
            
        username = ET.SubElement(credentials, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_credentials_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        credentials = ET.SubElement(vcenter, "credentials")
        if kwargs.pop('delete_credentials', False) is True:
            delete_credentials = config.find('.//*credentials')
            delete_credentials.set('operation', 'delete')
            
        password = ET.SubElement(credentials, "password")
        if kwargs.pop('delete_password', False) is True:
            delete_password = config.find('.//*password')
            delete_password.set('operation', 'delete')
            
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_credentials_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        credentials = ET.SubElement(vcenter, "credentials")
        if kwargs.pop('delete_credentials', False) is True:
            delete_credentials = config.find('.//*credentials')
            delete_credentials.set('operation', 'delete')
            
        vrf_name = ET.SubElement(credentials, "vrf-name")
        if kwargs.pop('delete_vrf_name', False) is True:
            delete_vrf_name = config.find('.//*vrf-name')
            delete_vrf_name.set('operation', 'delete')
            
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        activate = ET.SubElement(vcenter, "activate")
        if kwargs.pop('delete_activate', False) is True:
            delete_activate = config.find('.//*activate')
            delete_activate.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        interval = ET.SubElement(vcenter, "interval")
        if kwargs.pop('delete_interval', False) is True:
            delete_interval = config.find('.//*interval')
            delete_interval.set('operation', 'delete')
            
        interval.text = kwargs.pop('interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_discovery_ignore_delete_all_response_ignore_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        discovery = ET.SubElement(vcenter, "discovery")
        if kwargs.pop('delete_discovery', False) is True:
            delete_discovery = config.find('.//*discovery')
            delete_discovery.set('operation', 'delete')
            
        ignore_delete_all_response = ET.SubElement(discovery, "ignore-delete-all-response")
        if kwargs.pop('delete_ignore_delete_all_response', False) is True:
            delete_ignore_delete_all_response = config.find('.//*ignore-delete-all-response')
            delete_ignore_delete_all_response.set('operation', 'delete')
            
        ignore_value = ET.SubElement(ignore_delete_all_response, "ignore-value")
        if kwargs.pop('delete_ignore_value', False) is True:
            delete_ignore_value = config.find('.//*ignore-value')
            delete_ignore_value.set('operation', 'delete')
            
        ignore_value.text = kwargs.pop('ignore_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcenter_discovery_ignore_delete_all_response_always(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        if kwargs.pop('delete_vcenter', False) is True:
            delete_vcenter = config.find('.//*vcenter')
            delete_vcenter.set('operation', 'delete')
            
        id_key = ET.SubElement(vcenter, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        discovery = ET.SubElement(vcenter, "discovery")
        if kwargs.pop('delete_discovery', False) is True:
            delete_discovery = config.find('.//*discovery')
            delete_discovery.set('operation', 'delete')
            
        ignore_delete_all_response = ET.SubElement(discovery, "ignore-delete-all-response")
        if kwargs.pop('delete_ignore_delete_all_response', False) is True:
            delete_ignore_delete_all_response = config.find('.//*ignore-delete-all-response')
            delete_ignore_delete_all_response.set('operation', 'delete')
            
        always = ET.SubElement(ignore_delete_all_response, "always")
        if kwargs.pop('delete_always', False) is True:
            delete_always = config.find('.//*always')
            delete_always.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        