import hmac, hashlib
from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase


def verify_message(msg, signature, key):
    """
    Verify the HMAC send from Cisco Stealthwatch
    """
    digest = hmac.new(key, msg=msg, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(digest, signature)


class StealthwatchWebhook(WebhookBase):
    """
    Cisco Stealthwatch alerts webhook
    Good luck finiding any usefull documentation, it's cisco as usual
    """
    def incoming(self, query_string, payload):
        event = payload.get('type', 'No type found')
        resource = payload['source_info']['name'] or payload.get('source', 'No resource found')
        text = payload.get('text', 'No text found')
        service = payload.get('source_name', 'No services found')
        resolved = payload.get('resolved', False)

        status = 'undefined'
        severity = 'undefined'
        if resolved:
            status = 'closed'
            severity = 'normal'
        else:
            status = 'open'
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
