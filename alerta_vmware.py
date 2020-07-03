import logging
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.transient')

class VmwareTrapTransformer(PluginBase):

    def pre_receive(self, alert):

        if "SNMPv1" not in alert.tags:
            return alert
        alert.resource = alert.attributes['trapvars']['_5']
        alert.event = alert.attributes['trapvars']['_4'].split('-')[0].strip()
        alert.text = alert.attributes['trapvars']['_4']
        alert.origin = alert.attributes['trapvars']['_A']
        if alert.attributes['trapvars']['_3'] == "Yellow":
            severity =  "minor"
        elif alert.attributes['trapvars']['_3'] == "Red":
            severity = "major"
        elif alert.attributes['trapvars']['_3'] == "Green":
            severity = "cleared"
        alert.severity = severity
        return alert

    def post_receive(self, alert):
        return

    def status_change(self, alert, status, text):
        return
