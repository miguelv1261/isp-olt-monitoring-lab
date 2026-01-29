from datetime import datetime


def normalize(raw, level, olt=None, pon=None, ont=None):
    metric = {
    'timestamp': datetime.utcnow(),
    'tags': {},
    'fields': {}
    }


    if level == 'OLT':
        metric['measurement'] = 'olt_metrics'
        metric['tags'] = {'olt_id': olt['id']}
        metric['fields'] = {'cpu': 40, 'memory': 65}


    if level == 'PON':
        metric['measurement'] = 'pon_metrics'
        metric['tags'] = {'olt_id': olt['id'], 'pon': pon}
        metric['fields'] = {'onts_online': 32}


    if level == 'ONT':
        metric['measurement'] = 'ont_metrics'
        metric['tags'] = {'olt_id': olt['id'], 'ont': ont}
        metric['fields'] = {'rx_power': -22.5, 'tx_power': 2.1}


    return metric