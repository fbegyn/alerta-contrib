import json
import unittest

import alerta_stealthwatch

from alerta.app import create_app, custom_webhooks

class StealthwatchWebhookTestCase(unittest.TestCase):
    def setUp(self):
        test_config = {
            'TESTING': True,
            'AUTH_REQUIRED': False,
        }
        self.app = create_app(test_config)
        self.client = self.app.test_client()

        custom_webhooks.webhooks['stealthwatch'] = alerta_stealthwatch.StealthwatchWebhook()

    def test_stealthwatch_alert_firing_hostname(self):
        stealthwatch_alert = r"""
{
  "assigned_to": null,
  "assigned_to_username": null,
  "comments": {
    "comments": [],
    "count": 0,
    "text": "0 comments"
  },
  "created": "2019-04-17T13:09:45Z",
  "description": "A new device has appeared on a restricted subnet range after not being seen in the lookback period.",
  "hostname": "support.fitit.be",
  "id": 463,
  "ips_when_created": [
    "198.19.0.3"
  ],
  "last_modified": "2019-04-17T14:22:58.928537Z",
  "merit": 0,
  "natural_time": "an hour ago",
  "new_comment": null,
  "obj_created": "2019-04-17T14:22:59.008825Z",
  "observations": [
    14844
  ],
  "priority": 20,
  "publish_time": "2019-04-17T14:22:58.926213+00:00",
  "resolved": false,
  "resolved_time": null,
  "resolved_user": null,
  "rules_matched": null,
  "snooze_settings": null,
  "source": 1826,
  "source_info": {
    "created": "2019-04-17T12:19:32.985658+00:00",
    "hostnames": [
      "support.fitit.be"
    ],
    "ips": [
      "198.19.0.3"
    ],
    "name": "support.fitit.be",
    "namespace": "default"
  },
  "source_name": "support.fitit.be",
  "source_params": {
    "id": 1826,
    "meta": "net-link",
    "name": "support.fitit.be"
  },
  "tags": [],
  "text": "New Internal Device on support.fitit.be\nhttps://axians.obsrvbl.com/#/alerts/463",
  "time": "2019-04-17T13:09:45Z",
  "type": "New Internal Device"
}
"""
        response = self.client.post('/webhooks/stealthwatch',
                                    data=stealthwatch_alert,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('UTF-8'))

    def test_stealthwatch_alert_firing_nohostname(self):
        stealthwatch_alert = r"""
{
  "assigned_to": null,
  "assigned_to_username": null,
  "comments": {
    "comments": [],
    "count": 0,
    "text": "0 comments"
  },
  "created": "2019-05-07T06:38:06Z",
  "description": "A new device has appeared on a restricted subnet range after not being seen in the lookback period.",
  "hostname": "",
  "id": 695,
  "ips_when_created": [],
  "last_modified": "2019-05-07T07:12:45.085574Z",
  "merit": 0,
  "natural_time": "34\u00a0minutes ago",
  "new_comment": null,
  "obj_created": "2019-05-07T07:12:45.209881Z",
  "observations": [
    18781
  ],
  "priority": 20,
  "publish_time": "2019-05-07T07:12:45.081584+00:00",
  "resolved": false,
  "resolved_time": null,
  "resolved_user": null,
  "rules_matched": null,
  "snooze_settings": null,
  "source": 2078,
  "source_info": {
    "created": "2019-05-07T06:40:25.108622+00:00",
    "hostnames": [
      "9.116.183.185.static.ipv4.fitit.be"
    ],
    "ips": [
      "198.19.0.8"
    ],
    "name": "9.116.183.185.static.ipv4.fitit.be",
    "namespace": "default"
  },
  "source_name": "9.116.183.185.static.ipv4.fitit.be",
  "source_params": {
    "id": 2078,
    "meta": "net-link",
    "name": "9.116.183.185.static.ipv4.fitit.be"
  },
  "tags": [],
  "text": "New Internal Device on 9.116.183.185.static.ipv4.fitit.be\nhttps://axians.obsrvbl.com/#/alerts/695",
  "time": "2019-05-07T06:38:06Z",
  "type": "New Internal Device"
}
                    """
        response = self.client.post('/webhooks/stealthwatch',
                                    data=stealthwatch_alert,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('UTF-8'))


    def test_stealthwatch_alert_resolved(self):
        stealthwatch_alert = r"""
{
  "assigned_to": null,
  "assigned_to_username": null,
  "comments": {
    "comments": [
      {
        "comment": "Closed Due To Inactivity",
        "time": "2019-03-16T01:01:45.499033+00:00",
        "user": null
      },
      {
        "comment": "Updated by 4 observations",
        "time": "2019-03-08T09:01:39.978316+00:00",
        "user": null
      },
      {
        "comment": "Updated by 4 observations",
        "time": "2019-03-08T09:01:38.932995+00:00",
        "user": null
      },
      {
        "comment": "Updated by 6 observations",
        "time": "2019-03-08T08:51:46.923999+00:00",
        "user": null
      }
    ],
    "count": 4,
    "text": "4 comments"
  },
  "created": "2019-03-08T08:48:12Z",
  "description": "This is a test alert of a service.",
  "hostname": "se-elk-01",
  "id": 67,
  "ips_when_created": [],
  "last_modified": "2019-03-08T09:01:39.327279Z",
  "merit": 6,
  "natural_time": "2\u00a0weeks, 3\u00a0days ago",
  "new_comment": null,
  "obj_created": "2019-03-08T08:51:46.129877Z",
  "observations": [
    5433,
    5434,
    5435,
    5436,
    5437,
    5438,
    5427,
    5428,
    5429,
    5430,
    5431,
    5432,
    5480,
    5481,
    5482,
    5479,
    5475,
    5476,
    5477,
    5478
  ],
  "priority": 20,
  "publish_time": "2019-03-08T08:51:45.998537+00:00",
  "resolved": true,
  "resolved_time": "2019-03-16T01:01:45.466866Z",
  "resolved_user": null,
  "rules_matched": null,
  "snooze_settings": null,
  "source": 765,
  "source_info": {
    "created": "2019-03-08T08:50:58.502305+00:00",
    "hostnames": [],
    "ips": [
      "10.75.193.112"
    ],
    "name": "10.75.193.112",
    "namespace": "default"
  },
  "source_name": "10.75.193.112",
  "source_params": {
    "id": 765,
    "meta": "net-link",
    "name": "10.75.193.112"
  },
  "tags": [],
  "text": "Test Alert on 10.75.193.112\nhttps://axians.obsrvbl.com/#/alerts/67",
  "time": "2019-03-08T08:56:33Z",
  "type": "Test Alert"
}
                    """
        response = self.client.post('/webhooks/stealthwatch',
                                    data=stealthwatch_alert,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('UTF-8'))

if __name__ == "__main__":
    unittest.main()
