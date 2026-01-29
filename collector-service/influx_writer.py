from influxdb_client import InfluxDBClient, Point


def connect_influx(cfg):
    return InfluxDBClient(
    url=cfg['influx']['url'],
    token=cfg['influx']['token'],
    org=cfg['influx']['org']
    )




def write_metrics(metric, client):
    p = Point(metric['measurement'])
    for k, v in metric['tags'].items(): p.tag(k, v)
    for k, v in metric['fields'].items(): p.field(k, v)
    client.write_api().write(bucket='isp_network_metrics', record=p)