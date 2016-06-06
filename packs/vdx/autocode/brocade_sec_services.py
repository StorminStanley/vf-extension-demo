#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_sec_services(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def telnet_sa_telnet_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_telnet_sa', False) is True:
            delete_telnet_sa = config.find('.//*telnet-sa')
            delete_telnet_sa.set('operation', 'delete')
            
        telnet = ET.SubElement(telnet_sa, "telnet")
        if kwargs.pop('delete_telnet', False) is True:
            delete_telnet = config.find('.//*telnet')
            delete_telnet.set('operation', 'delete')
            
        server = ET.SubElement(telnet, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        shutdown = ET.SubElement(server, "shutdown")
        if kwargs.pop('delete_shutdown', False) is True:
            delete_shutdown = config.find('.//*shutdown')
            delete_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_telnet_sa', False) is True:
            delete_telnet_sa = config.find('.//*telnet-sa')
            delete_telnet_sa.set('operation', 'delete')
            
        telnet = ET.SubElement(telnet_sa, "telnet")
        if kwargs.pop('delete_telnet', False) is True:
            delete_telnet = config.find('.//*telnet')
            delete_telnet.set('operation', 'delete')
            
        server = ET.SubElement(telnet, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        standby = ET.SubElement(server, "standby")
        if kwargs.pop('delete_standby', False) is True:
            delete_standby = config.find('.//*standby')
            delete_standby.set('operation', 'delete')
            
        enable = ET.SubElement(standby, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_telnet_vrf_cont_use_vrf_use_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_telnet_sa', False) is True:
            delete_telnet_sa = config.find('.//*telnet-sa')
            delete_telnet_sa.set('operation', 'delete')
            
        telnet = ET.SubElement(telnet_sa, "telnet")
        if kwargs.pop('delete_telnet', False) is True:
            delete_telnet = config.find('.//*telnet')
            delete_telnet.set('operation', 'delete')
            
        server = ET.SubElement(telnet, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        telnet_vrf_cont = ET.SubElement(server, "telnet-vrf-cont")
        if kwargs.pop('delete_telnet_vrf_cont', False) is True:
            delete_telnet_vrf_cont = config.find('.//*telnet-vrf-cont')
            delete_telnet_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(telnet_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
            
        use_vrf_name.text = kwargs.pop('use_vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_telnet_vrf_cont_use_vrf_telnet_vrf_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_telnet_sa', False) is True:
            delete_telnet_sa = config.find('.//*telnet-sa')
            delete_telnet_sa.set('operation', 'delete')
            
        telnet = ET.SubElement(telnet_sa, "telnet")
        if kwargs.pop('delete_telnet', False) is True:
            delete_telnet = config.find('.//*telnet')
            delete_telnet.set('operation', 'delete')
            
        server = ET.SubElement(telnet, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        telnet_vrf_cont = ET.SubElement(server, "telnet-vrf-cont")
        if kwargs.pop('delete_telnet_vrf_cont', False) is True:
            delete_telnet_vrf_cont = config.find('.//*telnet-vrf-cont')
            delete_telnet_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(telnet_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name_key.text = kwargs.pop('use_vrf_name')
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
                
        telnet_vrf_shutdown = ET.SubElement(use_vrf, "telnet-vrf-shutdown")
        if kwargs.pop('delete_telnet_vrf_shutdown', False) is True:
            delete_telnet_vrf_shutdown = config.find('.//*telnet-vrf-shutdown')
            delete_telnet_vrf_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        shutdown = ET.SubElement(server, "shutdown")
        if kwargs.pop('delete_shutdown', False) is True:
            delete_shutdown = config.find('.//*shutdown')
            delete_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_exchange(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        key_exchange = ET.SubElement(server, "key-exchange")
        if kwargs.pop('delete_key_exchange', False) is True:
            delete_key_exchange = config.find('.//*key-exchange')
            delete_key_exchange.set('operation', 'delete')
            
        key_exchange.text = kwargs.pop('key_exchange')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_rekey_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        rekey_interval = ET.SubElement(server, "rekey-interval")
        if kwargs.pop('delete_rekey_interval', False) is True:
            delete_rekey_interval = config.find('.//*rekey-interval')
            delete_rekey_interval.set('operation', 'delete')
            
        rekey_interval.text = kwargs.pop('rekey_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        cipher = ET.SubElement(server, "cipher")
        if kwargs.pop('delete_cipher', False) is True:
            delete_cipher = config.find('.//*cipher')
            delete_cipher.set('operation', 'delete')
            
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        mac = ET.SubElement(server, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        standby = ET.SubElement(server, "standby")
        if kwargs.pop('delete_standby', False) is True:
            delete_standby = config.find('.//*standby')
            delete_standby.set('operation', 'delete')
            
        enable = ET.SubElement(standby, "enable")
        if kwargs.pop('delete_enable', False) is True:
            delete_enable = config.find('.//*enable')
            delete_enable.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_rsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        key = ET.SubElement(server, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        rsa = ET.SubElement(key, "rsa")
        if kwargs.pop('delete_rsa', False) is True:
            delete_rsa = config.find('.//*rsa')
            delete_rsa.set('operation', 'delete')
            
        rsa.text = kwargs.pop('rsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_ecdsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        key = ET.SubElement(server, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        ecdsa = ET.SubElement(key, "ecdsa")
        if kwargs.pop('delete_ecdsa', False) is True:
            delete_ecdsa = config.find('.//*ecdsa')
            delete_ecdsa.set('operation', 'delete')
            
        ecdsa.text = kwargs.pop('ecdsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_dsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        key = ET.SubElement(server, "key")
        if kwargs.pop('delete_key', False) is True:
            delete_key = config.find('.//*key')
            delete_key.set('operation', 'delete')
            
        dsa = ET.SubElement(key, "dsa")
        if kwargs.pop('delete_dsa', False) is True:
            delete_dsa = config.find('.//*dsa')
            delete_dsa.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_ssh_vrf_cont_use_vrf_use_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        ssh_vrf_cont = ET.SubElement(server, "ssh-vrf-cont")
        if kwargs.pop('delete_ssh_vrf_cont', False) is True:
            delete_ssh_vrf_cont = config.find('.//*ssh-vrf-cont')
            delete_ssh_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(ssh_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
            
        use_vrf_name.text = kwargs.pop('use_vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_ssh_vrf_cont_use_vrf_ssh_vrf_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        server = ET.SubElement(ssh, "server")
        if kwargs.pop('delete_server', False) is True:
            delete_server = config.find('.//*server')
            delete_server.set('operation', 'delete')
            
        ssh_vrf_cont = ET.SubElement(server, "ssh-vrf-cont")
        if kwargs.pop('delete_ssh_vrf_cont', False) is True:
            delete_ssh_vrf_cont = config.find('.//*ssh-vrf-cont')
            delete_ssh_vrf_cont.set('operation', 'delete')
            
        use_vrf = ET.SubElement(ssh_vrf_cont, "use-vrf")
        if kwargs.pop('delete_use_vrf', False) is True:
            delete_use_vrf = config.find('.//*use-vrf')
            delete_use_vrf.set('operation', 'delete')
            
        use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name_key.text = kwargs.pop('use_vrf_name')
        if kwargs.pop('delete_use_vrf_name', False) is True:
            delete_use_vrf_name = config.find('.//*use-vrf-name')
            delete_use_vrf_name.set('operation', 'delete')
                
        ssh_vrf_shutdown = ET.SubElement(use_vrf, "ssh-vrf-shutdown")
        if kwargs.pop('delete_ssh_vrf_shutdown', False) is True:
            delete_ssh_vrf_shutdown = config.find('.//*ssh-vrf-shutdown')
            delete_ssh_vrf_shutdown.set('operation', 'delete')
            

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_client_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        client = ET.SubElement(ssh, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        cipher = ET.SubElement(client, "cipher")
        if kwargs.pop('delete_cipher', False) is True:
            delete_cipher = config.find('.//*cipher')
            delete_cipher.set('operation', 'delete')
            
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_client_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        client = ET.SubElement(ssh, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        mac = ET.SubElement(client, "mac")
        if kwargs.pop('delete_mac', False) is True:
            delete_mac = config.find('.//*mac')
            delete_mac.set('operation', 'delete')
            
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_client_key_exchange(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        if kwargs.pop('delete_ssh_sa', False) is True:
            delete_ssh_sa = config.find('.//*ssh-sa')
            delete_ssh_sa.set('operation', 'delete')
            
        ssh = ET.SubElement(ssh_sa, "ssh")
        if kwargs.pop('delete_ssh', False) is True:
            delete_ssh = config.find('.//*ssh')
            delete_ssh.set('operation', 'delete')
            
        client = ET.SubElement(ssh, "client")
        if kwargs.pop('delete_client', False) is True:
            delete_client = config.find('.//*client')
            delete_client.set('operation', 'delete')
            
        key_exchange = ET.SubElement(client, "key-exchange")
        if kwargs.pop('delete_key_exchange', False) is True:
            delete_key_exchange = config.find('.//*key-exchange')
            delete_key_exchange.set('operation', 'delete')
            
        key_exchange.text = kwargs.pop('key_exchange')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        