# Grafana

REVISION: 2
2024-08-20T01:32:42.202776820Z NOTES:
2024-08-20T01:32:42.202776820Z 1. Get your 'admin' user password by running:
2024-08-20T01:32:42.202776820Z
2024-08-20T01:32:42.202776820Z    kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
2024-08-20T01:32:42.202776820Z
2024-08-20T01:32:42.202776820Z
2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:
2024-08-20T01:32:42.202776820Z
2024-08-20T01:32:42.202776820Z    grafana.monitoring.svc.cluster.local

2024-08-20T01:32:42.202776820Z    Get the Grafana URL to visit by running these commands in the same shell:
2024-08-20T01:32:42.202776820Z      export POD_NAME=$(kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}")
2024-08-20T01:32:42.202776820Z      kubectl --namespace monitoring port-forward $POD_NAME 3000
2024-08-20T01:32:42.202776820Z

<https://grafana.com/grafana/dashboards/15760-kubernetes-views-pods/>

<https://grafana.com/grafana/dashboards/15758-kubernetes-views-namespaces/>

<https://grafana.com/grafana/dashboards/15761-kubernetes-system-api-server/>

<https://grafana.com/grafana/dashboards/15757-kubernetes-views-global/>

<https://grafana.com/grafana/dashboards/15759-kubernetes-views-nodes/>

Configurar integracao com zabbix, alertmanager, loki e blackbox

<https://grafana.com/grafana/dashboards/15141-kubernetes-service-logs/>
