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
        # Just need to append a single value in the default capabilities
        c = super(IosxrDeviceHandler, self).get_capabilities()
        c.append("urn:ietf:params:netconf:base:1.1")
        return c

    def get_xml_base_namespace_dict(self):
        """
        Base namespace needs a None key.

        See 'nsmap' argument for lxml's Element().

        """
        return { None : BASE_NS_1_0 }

    def get_xml_extra_prefix_kwargs(self):
        d = {
            "cdp-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-cdp-cfg",
            "cdp-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-cdp-oper",
            "sam-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-crypto-sam-cfg",
            "sam-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-crypto-sam-oper",
            "ha-eem-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ha-eem-cfg",
            "ha-eem-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ha-eem-oper",
            "if-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
            "if-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper",
            # "if-oper-sub1": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper-sub1",
            # "if-oper-sub2": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper-sub2",
            "infra-infra-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg",
            "ip-domain-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-cfg",
            "ip-domain-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper",
            "ip-iarm-datatypes": "http://cisco.com/ns/yang/Cisco-IOS-XR-ip-iarm-datatypes",
            "ipv4-io-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg",
            "ipv4-io-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-oper",
            "ipv4-ma-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-ma-cfg",
            "ipv4-ma-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-ma-oper",
            "ipv4-ma-subscriber-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-ma-subscriber-cfg",
            "ipv6-ma-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv6-ma-cfg",
            "ipv6-ma-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv6-ma-oper",
            "ipv6-ma-subscriber-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-ipv6-ma-subscriber-cfg",
            "lib-keychain-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-lib-keychain-cfg",
            "lib-keychain-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-lib-keychain-oper",
            "man-netconf-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-man-netconf-cfg",
            "man-xml-ttyagent-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-man-xml-ttyagent-cfg",
            "man-xml-ttyagent-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-man-xml-ttyagent-oper",
            "parser-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-parser-cfg",
            "qos-ma-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-qos-ma-cfg",
            "qos-ma-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-qos-ma-oper",
            "rgmgr-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-rgmgr-cfg",
            "rgmgr-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-rgmgr-oper",
            "shellutil-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg",
            "shellutil-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-oper",
            "subscriber-infra-tmplmgr-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg",
            "tty-management-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-cfg",
            "tty-management-datatypes": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-datatypes",
            "tty-management-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-management-oper",
            "tty-server-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-server-cfg",
            "tty-server-oper": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-server-oper",
            "tty-vty-cfg": "http://cisco.com/ns/yang/Cisco-IOS-XR-tty-vty-cfg",
            "cisco-xr-types": "http://cisco.com/ns/yang/cisco-xr-types",
            }
        d.update(self.get_xml_base_namespace_dict())
        return {"nsmap": d}

    def perform_qualify_check(self):
        return False
