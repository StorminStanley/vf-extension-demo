#!/usr/bin/env python
import xml.etree.ElementTree as ET


class tailf_webui(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def webui_schematics_panels_panel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name = ET.SubElement(panel, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_title(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        properties = ET.SubElement(panel, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        title = ET.SubElement(properties, "title")
        if kwargs.pop('delete_title', False) is True:
            delete_title = config.find('.//*title')
            delete_title.set('operation', 'delete')
            
        title.text = kwargs.pop('title')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        properties = ET.SubElement(panel, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        description = ET.SubElement(properties, "description")
        if kwargs.pop('delete_description', False) is True:
            delete_description = config.find('.//*description')
            delete_description.set('operation', 'delete')
            
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        properties = ET.SubElement(panel, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        width = ET.SubElement(properties, "width")
        if kwargs.pop('delete_width', False) is True:
            delete_width = config.find('.//*width')
            delete_width.set('operation', 'delete')
            
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        properties = ET.SubElement(panel, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        height = ET.SubElement(properties, "height")
        if kwargs.pop('delete_height', False) is True:
            delete_height = config.find('.//*height')
            delete_height.set('operation', 'delete')
            
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id = ET.SubElement(component, "id")
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
            
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_top(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        top = ET.SubElement(properties, "top")
        if kwargs.pop('delete_top', False) is True:
            delete_top = config.find('.//*top')
            delete_top.set('operation', 'delete')
            
        top.text = kwargs.pop('top')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_left(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        left = ET.SubElement(properties, "left")
        if kwargs.pop('delete_left', False) is True:
            delete_left = config.find('.//*left')
            delete_left.set('operation', 'delete')
            
        left.text = kwargs.pop('left')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        width = ET.SubElement(properties, "width")
        if kwargs.pop('delete_width', False) is True:
            delete_width = config.find('.//*width')
            delete_width.set('operation', 'delete')
            
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        height = ET.SubElement(properties, "height")
        if kwargs.pop('delete_height', False) is True:
            delete_height = config.find('.//*height')
            delete_height.set('operation', 'delete')
            
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_z_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        z_index = ET.SubElement(properties, "z-index")
        if kwargs.pop('delete_z_index', False) is True:
            delete_z_index = config.find('.//*z-index')
            delete_z_index.set('operation', 'delete')
            
        z_index.text = kwargs.pop('z_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_image_image_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        component_type = ET.SubElement(properties, "component-type")
        if kwargs.pop('delete_component_type', False) is True:
            delete_component_type = config.find('.//*component-type')
            delete_component_type.set('operation', 'delete')
            
        image = ET.SubElement(component_type, "image")
        if kwargs.pop('delete_image', False) is True:
            delete_image = config.find('.//*image')
            delete_image.set('operation', 'delete')
            
        image = ET.SubElement(image, "image")
        if kwargs.pop('delete_image', False) is True:
            delete_image = config.find('.//*image')
            delete_image.set('operation', 'delete')
            
        image = ET.SubElement(image, "image")
        if kwargs.pop('delete_image', False) is True:
            delete_image = config.find('.//*image')
            delete_image.set('operation', 'delete')
            
        image.text = kwargs.pop('image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_text(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        component_type = ET.SubElement(properties, "component-type")
        if kwargs.pop('delete_component_type', False) is True:
            delete_component_type = config.find('.//*component-type')
            delete_component_type.set('operation', 'delete')
            
        link = ET.SubElement(component_type, "link")
        if kwargs.pop('delete_link', False) is True:
            delete_link = config.find('.//*link')
            delete_link.set('operation', 'delete')
            
        link = ET.SubElement(link, "link")
        if kwargs.pop('delete_link', False) is True:
            delete_link = config.find('.//*link')
            delete_link.set('operation', 'delete')
            
        text = ET.SubElement(link, "text")
        if kwargs.pop('delete_text', False) is True:
            delete_text = config.find('.//*text')
            delete_text.set('operation', 'delete')
            
        text.text = kwargs.pop('text')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_link(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        panels = ET.SubElement(schematics, "panels")
        if kwargs.pop('delete_panels', False) is True:
            delete_panels = config.find('.//*panels')
            delete_panels.set('operation', 'delete')
            
        panel = ET.SubElement(panels, "panel")
        if kwargs.pop('delete_panel', False) is True:
            delete_panel = config.find('.//*panel')
            delete_panel.set('operation', 'delete')
            
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        components = ET.SubElement(panel, "components")
        if kwargs.pop('delete_components', False) is True:
            delete_components = config.find('.//*components')
            delete_components.set('operation', 'delete')
            
        component = ET.SubElement(components, "component")
        if kwargs.pop('delete_component', False) is True:
            delete_component = config.find('.//*component')
            delete_component.set('operation', 'delete')
            
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        if kwargs.pop('delete_id', False) is True:
            delete_id = config.find('.//*id')
            delete_id.set('operation', 'delete')
                
        properties = ET.SubElement(component, "properties")
        if kwargs.pop('delete_properties', False) is True:
            delete_properties = config.find('.//*properties')
            delete_properties.set('operation', 'delete')
            
        component_type = ET.SubElement(properties, "component-type")
        if kwargs.pop('delete_component_type', False) is True:
            delete_component_type = config.find('.//*component-type')
            delete_component_type.set('operation', 'delete')
            
        link = ET.SubElement(component_type, "link")
        if kwargs.pop('delete_link', False) is True:
            delete_link = config.find('.//*link')
            delete_link.set('operation', 'delete')
            
        link = ET.SubElement(link, "link")
        if kwargs.pop('delete_link', False) is True:
            delete_link = config.find('.//*link')
            delete_link.set('operation', 'delete')
            
        link = ET.SubElement(link, "link")
        if kwargs.pop('delete_link', False) is True:
            delete_link = config.find('.//*link')
            delete_link.set('operation', 'delete')
            
        link.text = kwargs.pop('link')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        assets = ET.SubElement(schematics, "assets")
        if kwargs.pop('delete_assets', False) is True:
            delete_assets = config.find('.//*assets')
            delete_assets.set('operation', 'delete')
            
        asset = ET.SubElement(assets, "asset")
        if kwargs.pop('delete_asset', False) is True:
            delete_asset = config.find('.//*asset')
            delete_asset.set('operation', 'delete')
            
        name = ET.SubElement(asset, "name")
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
            
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_base_64_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        assets = ET.SubElement(schematics, "assets")
        if kwargs.pop('delete_assets', False) is True:
            delete_assets = config.find('.//*assets')
            delete_assets.set('operation', 'delete')
            
        asset = ET.SubElement(assets, "asset")
        if kwargs.pop('delete_asset', False) is True:
            delete_asset = config.find('.//*asset')
            delete_asset.set('operation', 'delete')
            
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        asset_type = ET.SubElement(asset, "asset-type")
        if kwargs.pop('delete_asset_type', False) is True:
            delete_asset_type = config.find('.//*asset-type')
            delete_asset_type.set('operation', 'delete')
            
        image = ET.SubElement(asset_type, "image")
        if kwargs.pop('delete_image', False) is True:
            delete_image = config.find('.//*image')
            delete_image.set('operation', 'delete')
            
        base_64_image = ET.SubElement(image, "base-64-image")
        if kwargs.pop('delete_base_64_image', False) is True:
            delete_base_64_image = config.find('.//*base-64-image')
            delete_base_64_image.set('operation', 'delete')
            
        base_64_image.text = kwargs.pop('base_64_image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        schematics = ET.SubElement(webui, "schematics")
        if kwargs.pop('delete_schematics', False) is True:
            delete_schematics = config.find('.//*schematics')
            delete_schematics.set('operation', 'delete')
            
        assets = ET.SubElement(schematics, "assets")
        if kwargs.pop('delete_assets', False) is True:
            delete_assets = config.find('.//*assets')
            delete_assets.set('operation', 'delete')
            
        asset = ET.SubElement(assets, "asset")
        if kwargs.pop('delete_asset', False) is True:
            delete_asset = config.find('.//*asset')
            delete_asset.set('operation', 'delete')
            
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        if kwargs.pop('delete_name', False) is True:
            delete_name = config.find('.//*name')
            delete_name.set('operation', 'delete')
                
        asset_type = ET.SubElement(asset, "asset-type")
        if kwargs.pop('delete_asset_type', False) is True:
            delete_asset_type = config.find('.//*asset-type')
            delete_asset_type.set('operation', 'delete')
            
        image = ET.SubElement(asset_type, "image")
        if kwargs.pop('delete_image', False) is True:
            delete_image = config.find('.//*image')
            delete_image.set('operation', 'delete')
            
        type = ET.SubElement(image, "type")
        if kwargs.pop('delete_type', False) is True:
            delete_type = config.find('.//*type')
            delete_type.set('operation', 'delete')
            
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        user_profile = ET.SubElement(data_stores, "user-profile")
        if kwargs.pop('delete_user_profile', False) is True:
            delete_user_profile = config.find('.//*user-profile')
            delete_user_profile.set('operation', 'delete')
            
        username = ET.SubElement(user_profile, "username")
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
            
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        user_profile = ET.SubElement(data_stores, "user-profile")
        if kwargs.pop('delete_user_profile', False) is True:
            delete_user_profile = config.find('.//*user-profile')
            delete_user_profile.set('operation', 'delete')
            
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        profile = ET.SubElement(user_profile, "profile")
        if kwargs.pop('delete_profile', False) is True:
            delete_profile = config.find('.//*profile')
            delete_profile.set('operation', 'delete')
            
        key = ET.SubElement(profile, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        user_profile = ET.SubElement(data_stores, "user-profile")
        if kwargs.pop('delete_user_profile', False) is True:
            delete_user_profile = config.find('.//*user-profile')
            delete_user_profile.set('operation', 'delete')
            
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        profile = ET.SubElement(user_profile, "profile")
        if kwargs.pop('delete_profile', False) is True:
            delete_profile = config.find('.//*profile')
            delete_profile.set('operation', 'delete')
            
        key_key = ET.SubElement(profile, "key")
        key_key.text = kwargs.pop('key')
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
                
        value = ET.SubElement(profile, "value")
        if kwargs.pop('delete_value', False) is True:
            delete_value = config.find('.//*value')
            delete_value.set('operation', 'delete')
            
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        user_profile = ET.SubElement(data_stores, "user-profile")
        if kwargs.pop('delete_user_profile', False) is True:
            delete_user_profile = config.find('.//*user-profile')
            delete_user_profile.set('operation', 'delete')
            
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        saved_query = ET.SubElement(user_profile, "saved-query")
        if kwargs.pop('delete_saved_query', False) is True:
            delete_saved_query = config.find('.//*saved-query')
            delete_saved_query.set('operation', 'delete')
            
        key = ET.SubElement(saved_query, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        user_profile = ET.SubElement(data_stores, "user-profile")
        if kwargs.pop('delete_user_profile', False) is True:
            delete_user_profile = config.find('.//*user-profile')
            delete_user_profile.set('operation', 'delete')
            
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        if kwargs.pop('delete_username', False) is True:
            delete_username = config.find('.//*username')
            delete_username.set('operation', 'delete')
                
        saved_query = ET.SubElement(user_profile, "saved-query")
        if kwargs.pop('delete_saved_query', False) is True:
            delete_saved_query = config.find('.//*saved-query')
            delete_saved_query.set('operation', 'delete')
            
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
                
        value = ET.SubElement(saved_query, "value")
        if kwargs.pop('delete_value', False) is True:
            delete_value = config.find('.//*value')
            delete_value.set('operation', 'delete')
            
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        data_store = ET.SubElement(data_stores, "data-store")
        if kwargs.pop('delete_data_store', False) is True:
            delete_data_store = config.find('.//*data-store')
            delete_data_store.set('operation', 'delete')
            
        key = ET.SubElement(data_store, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        data_store = ET.SubElement(data_stores, "data-store")
        if kwargs.pop('delete_data_store', False) is True:
            delete_data_store = config.find('.//*data-store')
            delete_data_store.set('operation', 'delete')
            
        key_key = ET.SubElement(data_store, "key")
        key_key.text = kwargs.pop('key')
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
                
        value = ET.SubElement(data_store, "value")
        if kwargs.pop('delete_value', False) is True:
            delete_value = config.find('.//*value')
            delete_value.set('operation', 'delete')
            
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        saved_query = ET.SubElement(data_stores, "saved-query")
        if kwargs.pop('delete_saved_query', False) is True:
            delete_saved_query = config.find('.//*saved-query')
            delete_saved_query.set('operation', 'delete')
            
        key = ET.SubElement(saved_query, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        if kwargs.pop('delete_webui', False) is True:
            delete_webui = config.find('.//*webui')
            delete_webui.set('operation', 'delete')
            
        data_stores = ET.SubElement(webui, "data-stores")
        if kwargs.pop('delete_data_stores', False) is True:
            delete_data_stores = config.find('.//*data-stores')
            delete_data_stores.set('operation', 'delete')
            
        saved_query = ET.SubElement(data_stores, "saved-query")
        if kwargs.pop('delete_saved_query', False) is True:
            delete_saved_query = config.find('.//*saved-query')
            delete_saved_query.set('operation', 'delete')
            
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
                
        value = ET.SubElement(saved_query, "value")
        if kwargs.pop('delete_value', False) is True:
            delete_value = config.find('.//*value')
            delete_value.set('operation', 'delete')
            
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        