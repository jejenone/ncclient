"""
Handler for Cisco IOS-XR device specific information.

Note that for proper import, the classname has to be:

    "<Devicename>DeviceHandler"

...where <Devicename> is something like "Default", "Nexus", etc.

All device-specific handlers derive from the DefaultDeviceHandler, which implements the
generic information needed for interaction with a Netconf server.

"""

from ncclient.xml_ import BASE_NS_1_0

from .default import DefaultDeviceHandler
from ncclient.operations.third_party.iosxr.rpc import GetConfigConfiguration

class IosxrDeviceHandler(DefaultDeviceHandler):
    """
    Cisco IOS-XR handler for device specific information.


    """
    def __init__(self, device_params):
        super(IosxrDeviceHandler, self).__init__(device_params)

    def get_capabilities(self):
        # Just need to replace a single value in the default capabilities
        c = super(IosxrDeviceHandler, self).get_capabilities()
        #c[0] = "urn:ietf:params:xml:ns:netconf:base:1.0"
        #c[0] = "urn:ietf:params:netconf:base:1.0"
        c.append("urn:ietf:params:netconf:base:1.1")
        return c

    def add_additional_operations(self):
        dict = {}
        dict['get_config_configuration'] = GetConfigConfiguration
        return dict

    def get_xml_base_namespace_dict(self):
        """
        Base namespace needs a None key.

        See 'nsmap' argument for lxml's Element().

        """
        return { None : BASE_NS_1_0 }

    def get_xml_extra_prefix_kwargs(self):
        d = { "if": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg" }
        d.update(self.get_xml_base_namespace_dict())
        return {"nsmap": d}

    def perform_qualify_check(self):
        return False
