from netconf_client import netconf_connect
from parser import parse_xml
from normalizer import normalize
from influx_writer import write_metrics




def collect_olt_metrics(olt, influx):
    session = netconf_connect(olt)
    if not session:
        return
    xml = session.get('<olt-system-metrics/>').data_xml
    data = parse_xml(xml)
    metric = normalize(data, 'OLT', olt=olt)
    write_metrics(metric, influx)
    session.close()




def collect_pon_metrics(olt, influx):
    session = netconf_connect(olt)
    if not session:
        return
    for pon in olt['pon_ports']:
        xml = session.get(f'<pon-metrics port="{pon}"/>').data_xml
        data = parse_xml(xml)
        metric = normalize(data, 'PON', olt=olt, pon=pon)
        write_metrics(metric, influx)
    session.close()




def collect_ont_metrics(olt, influx):
    session = netconf_connect(olt)
    if not session: 
        return
    for ont in olt['sample_onts']:
        xml = session.get(f'<ont-metrics id="{ont}"/>').data_xml
        data = parse_xml(xml)
        metric = normalize(data, 'ONT', olt=olt, ont=ont)
        write_metrics(metric, influx)
    session.close()