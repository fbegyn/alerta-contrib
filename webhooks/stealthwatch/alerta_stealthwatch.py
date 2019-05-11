from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

class StealthwatchWebhook(WebhookBase):
    """
    Cisco Stealthwatch alerts webhook
    Good luck finiding any usefull documentation, it's cisco as usual
    """
    def incoming(self, query_string, payload):

        event = payload.get('type', 'No type found')
        resource = payload.get('hostname', 'No resource found')
        text = payload.get('text', 'No text found')
        service = payload.get('source_name', 'No services found')
        resolved = payload.get('resolved', False)

        status = 'undefined'
        severity = 'undefined'
        if resolved:
            status = 'closed'
            severity = 'normal'
        else:
            status = 'opened'
            severity = 'warning'

        return Alert(
            service=[service],
            resource=resource,
            event=event,
            status=status,
            severity=severity,
            environment='Production',
            text=text,
            origin='Cisco Stealthwatch',
            raw_data=payload
        )
