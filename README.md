# ISP OLT Monitoring Lab

Laboratorio de pruebas para un sistema inteligente de monitoreo de red para ISPs,
basado en una OLT GPON simulada, microservicios, InfluxDB y Grafana.

## Tecnologías
- Docker & Docker Compose
- Python (Flask)
- InfluxDB
- Grafana

## Arquitectura
OLT Simulada → Microservicio de Monitoreo → InfluxDB → Dashboard Grafana

## Ejecución
```bash
docker-compose up -d
