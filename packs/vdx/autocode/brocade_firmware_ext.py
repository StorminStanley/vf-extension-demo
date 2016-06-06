#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_firmware_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_firmware_version_input_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        input = ET.SubElement(show_firmware_version, "input")
        if kwargs.pop('delete_input', False) is True:
            delete_input = config.find('.//*input')
            delete_input.set('operation', 'delete')
            
        switchid = ET.SubElement(input, "switchid")
        if kwargs.pop('delete_switchid', False) is True:
            delete_switchid = config.find('.//*switchid')
            delete_switchid.set('operation', 'delete')
            
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        switchid = ET.SubElement(show_firmware_version, "switchid")
        if kwargs.pop('delete_switchid', False) is True:
            delete_switchid = config.find('.//*switchid')
            delete_switchid.set('operation', 'delete')
            
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        os_name = ET.SubElement(show_firmware_version, "os-name")
        if kwargs.pop('delete_os_name', False) is True:
            delete_os_name = config.find('.//*os-name')
            delete_os_name.set('operation', 'delete')
            
        os_name.text = kwargs.pop('os_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        os_version = ET.SubElement(show_firmware_version, "os-version")
        if kwargs.pop('delete_os_version', False) is True:
            delete_os_version = config.find('.//*os-version')
            delete_os_version.set('operation', 'delete')
            
        os_version.text = kwargs.pop('os_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_copy_right_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        copy_right_info = ET.SubElement(show_firmware_version, "copy-right-info")
        if kwargs.pop('delete_copy_right_info', False) is True:
            delete_copy_right_info = config.find('.//*copy-right-info')
            delete_copy_right_info.set('operation', 'delete')
            
        copy_right_info.text = kwargs.pop('copy_right_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_build_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        build_time = ET.SubElement(show_firmware_version, "build-time")
        if kwargs.pop('delete_build_time', False) is True:
            delete_build_time = config.find('.//*build-time')
            delete_build_time.set('operation', 'delete')
            
        build_time.text = kwargs.pop('build_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_firmware_full_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        firmware_full_version = ET.SubElement(show_firmware_version, "firmware-full-version")
        if kwargs.pop('delete_firmware_full_version', False) is True:
            delete_firmware_full_version = config.find('.//*firmware-full-version')
            delete_firmware_full_version.set('operation', 'delete')
            
        firmware_full_version.text = kwargs.pop('firmware_full_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        control_processor_vendor = ET.SubElement(show_firmware_version, "control-processor-vendor")
        if kwargs.pop('delete_control_processor_vendor', False) is True:
            delete_control_processor_vendor = config.find('.//*control-processor-vendor')
            delete_control_processor_vendor.set('operation', 'delete')
            
        control_processor_vendor.text = kwargs.pop('control_processor_vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_chipset(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        control_processor_chipset = ET.SubElement(show_firmware_version, "control-processor-chipset")
        if kwargs.pop('delete_control_processor_chipset', False) is True:
            delete_control_processor_chipset = config.find('.//*control-processor-chipset')
            delete_control_processor_chipset.set('operation', 'delete')
            
        control_processor_chipset.text = kwargs.pop('control_processor_chipset')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_memory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        control_processor_memory = ET.SubElement(show_firmware_version, "control-processor-memory")
        if kwargs.pop('delete_control_processor_memory', False) is True:
            delete_control_processor_memory = config.find('.//*control-processor-memory')
            delete_control_processor_memory.set('operation', 'delete')
            
        control_processor_memory.text = kwargs.pop('control_processor_memory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_slot_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        slot_no = ET.SubElement(node_info, "slot-no")
        if kwargs.pop('delete_slot_no', False) is True:
            delete_slot_no = config.find('.//*slot-no')
            delete_slot_no.set('operation', 'delete')
            
        slot_no.text = kwargs.pop('slot_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_instance_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        node_instance_no = ET.SubElement(node_info, "node-instance-no")
        if kwargs.pop('delete_node_instance_no', False) is True:
            delete_node_instance_no = config.find('.//*node-instance-no')
            delete_node_instance_no.set('operation', 'delete')
            
        node_instance_no.text = kwargs.pop('node_instance_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        node_type = ET.SubElement(node_info, "node-type")
        if kwargs.pop('delete_node_type', False) is True:
            delete_node_type = config.find('.//*node-type')
            delete_node_type.set('operation', 'delete')
            
        node_type.text = kwargs.pop('node_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_is_active_cp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        is_active_cp = ET.SubElement(node_info, "is-active-cp")
        if kwargs.pop('delete_is_active_cp', False) is True:
            delete_is_active_cp = config.find('.//*is-active-cp')
            delete_is_active_cp.set('operation', 'delete')
            
        is_active_cp.text = kwargs.pop('is_active_cp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_application_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        if kwargs.pop('delete_firmware_version_info', False) is True:
            delete_firmware_version_info = config.find('.//*firmware-version-info')
            delete_firmware_version_info.set('operation', 'delete')
            
        application_name = ET.SubElement(firmware_version_info, "application-name")
        if kwargs.pop('delete_application_name', False) is True:
            delete_application_name = config.find('.//*application-name')
            delete_application_name.set('operation', 'delete')
            
        application_name.text = kwargs.pop('application_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_primary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        if kwargs.pop('delete_firmware_version_info', False) is True:
            delete_firmware_version_info = config.find('.//*firmware-version-info')
            delete_firmware_version_info.set('operation', 'delete')
            
        primary_version = ET.SubElement(firmware_version_info, "primary-version")
        if kwargs.pop('delete_primary_version', False) is True:
            delete_primary_version = config.find('.//*primary-version')
            delete_primary_version.set('operation', 'delete')
            
        primary_version.text = kwargs.pop('primary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_secondary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        output = ET.SubElement(show_firmware_version, "output")
        if kwargs.pop('delete_output', False) is True:
            delete_output = config.find('.//*output')
            delete_output.set('operation', 'delete')
            
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        if kwargs.pop('delete_show_firmware_version', False) is True:
            delete_show_firmware_version = config.find('.//*show-firmware-version')
            delete_show_firmware_version.set('operation', 'delete')
            
        node_info = ET.SubElement(show_firmware_version, "node-info")
        if kwargs.pop('delete_node_info', False) is True:
            delete_node_info = config.find('.//*node-info')
            delete_node_info.set('operation', 'delete')
            
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        if kwargs.pop('delete_firmware_version_info', False) is True:
            delete_firmware_version_info = config.find('.//*firmware-version-info')
            delete_firmware_version_info.set('operation', 'delete')
            
        secondary_version = ET.SubElement(firmware_version_info, "secondary-version")
        if kwargs.pop('delete_secondary_version', False) is True:
            delete_secondary_version = config.find('.//*secondary-version')
            delete_secondary_version.set('operation', 'delete')
            
        secondary_version.text = kwargs.pop('secondary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        