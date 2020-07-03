import logging
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.transient')

class VmwareTrapTransformer(PluginBase):

    def pre_receive(self, alert):

        LOG.info(alert.attributes['trapvars'])

        return alert

    def post_receive(self, alert):
        return

    def status_change(self, alert):
        return
