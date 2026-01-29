import time
from collector import collect_olt_metrics, collect_pon_metrics, collect_ont_metrics
from influx_writer import connect_influx


def start_scheduler(config):
    influx = connect_influx(config)
    olts = config['olts']


    olt_tick = 0
    ont_tick = 0


    while True:
        if olt_tick % 30 == 0:
            for olt in olts:
                collect_olt_metrics(olt, influx)
                collect_pon_metrics(olt, influx)


        if ont_tick % 60 == 0:
            for olt in olts:
                collect_ont_metrics(olt, influx)


        time.sleep(1)
        olt_tick += 1
        ont_tick += 1