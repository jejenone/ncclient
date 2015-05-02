from lxml import etree

from ncclient.operations import util
from ncclient.xml_ import *
from ncclient.operations.rpc import RPC

class GetConfigConfiguration(RPC):
    def request(self, source):
        node = new_ele('get-config')
        node.append(util.datastore_or_url("source", source, self._assert))
#        filter = etree.SubElement(node, 'filter')
#        etree.SubElement(filter, qualify('Configuration', IOSXR_IFMGR))
        return self._request(node)
        #etree.SubElement(filter, qualify('Configuration', IOSXR_IFMGR))
        #return self._request(node)
