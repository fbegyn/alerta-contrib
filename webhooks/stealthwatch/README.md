Cisco Stealthwatch Monitor Webhook
==============

Receive [Cisco Stealthwatch](https://www.cisco.com/c/en/us/products/security/stealthwatch/index.html) notifications via webhook callbacks.

For help, join [![Gitter chat](https://badges.gitter.im/alerta/chat.png)](https://gitter.im/alerta/chat)

Installation
------------

Clone the GitHub repo and run:

    $ python setup.py install

Note: If Alerta is installed in a python virtual environment then plugins
need to be installed into the same environment for Alerta to dynamically
discover them.

Configuration
-------------

The custom webhook will be auto-detected and added to the list of available API endpoints.

Add the Alerta API webhook URL in the Stealthwatch web portal.


Example input
--------------

```
{
    "assigned_to": null,
    "assigned_to_username": null,
    "comments": {
        "comments": [
        {
            "comment": "Closed Due To Inactivity",
            "time": "2019-03-14T01:00:02.071891+00:00",
            "user": null
        },
        {
            "comment": "Updated by 18 observations",
            "time": "2019-03-06T16:49:15.126880+00:00",
            "user": null
        }
        ],
        "count": 2,
        "text": "2 comments"
    },
    "created": "2019-03-06T15:00:00Z",
    "description": "This is a test alert of a service.",
    "hostname": null,
    "id": 34,
    "ips_when_created": [],
    "last_modified": "2019-03-06T16:49:14.963758Z",
    "merit": 6,
    "natural_time": "1\u00a0week, 6\u00a0days ago",
    "new_comment": null,
    "obj_created": "2019-03-06T15:15:25.461616Z",
    "observations": [
        2360,
        2370,
        2371,
        2372,
        2373,
        2374,
        2375,
        2390,
        2397,
        2399,
        2438,
        2459,
        2465,
        2468,
        2469,
        2526,
        2533,
        2546,
        2547,
        2548,
        2560,
        2569,
        2613,
        2632,
        2640,
        2702,
        2738,
        2828,
        2912,
        3066,
        3136,
        3168,
        3276,
        3308,
        3341,
        3403,
        3505,
        3523,
        3599,
        3632,
        3700,
        3750,
        3910,
        3923,
        3954,
        3955,
        3961,
        3962,
        3965,
        3970,
        3973,
        3974,
        4000,
        4029,
        4065,
        4148,
        4174,
        4636,
        4652,
        4864,
        4871,
        4957
    ],
    "priority": 20,
    "publish_time": "2019-03-06T15:15:24.980150+00:00",
    "resolved": false,
    "resolved_time": "2019-03-14T01:00:02.065549Z",
    "resolved_user": null,
    "rules_matched": [
        {
        "count": 22,
        "value": "Test 2"
        },
        {
        "count": 18,
        "value": "Test"
        },
        {
        "count": 22,
        "value": "Test 3"
        }
    ],
    "snooze_settings": null,
    "source": 603,
    "source_info": {
        "created": "2019-03-01T23:14:09.788513+00:00",
        "name": "Network"
    },
    "source_name": "Network",
    "source_params": {
        "id": 603,
        "meta": "net-link",
        "name": "Network"
    },
    "tags": [],
    "text": "Test Alert on Network\nhttps://axians.obsrvbl.com/#/alerts/34",
    "time": "2019-03-06T15:40:00Z",
    "type": "Test Alert"
}
```

Example Output
--------------

```
{
    "status": "Activated",
    "context": {
        "timestamp": "2015-08-14T22:26:41.9975398Z",
        "id": "/subscriptions/s1/resourceGroups/useast/providers/microsoft.insights/alertrules/ruleName1",
        "name": "ruleName1",
        "description": "some description",
        "conditionType": "Metric",
        "condition": {
            "metricName": "Requests",
            "metricUnit": "Count",
            "metricValue": "10",
            "threshold": "10",
            "windowSize": "15",
            "timeAggregation": "Average",
            "operator": "GreaterThanOrEqual"
        },
        "subscriptionId": "s1",
        "resourceGroupName": "useast",
        "resourceName": "mysite1",
        "resourceType": "microsoft.foo/sites",
        "resourceId": "/subscriptions/s1/resourceGroups/useast/providers/microsoft.foo/sites/mysite1",
        "resourceRegion": "centralus",
        "portalLink": "https://portal.azure.com/#resource/subscriptions/s1/resourceGroups/useast/providers/microsoft.foo/sites/mysite1"
    },
    "properties": {
        "key1": "value1",
        "key2": "value2"
    }
}
```

References
----------

License
-------

Copyright (c) 2019 Francis Begyn. Available under the MIT License.
