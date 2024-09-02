Local

Operator

   helm install trivy-operator aqua/trivy-operator \
     --namespace trivy-system \
     --create-namespace \
     --version 0.21.4

You have installed Trivy Operator in the trivy-system namespace.
It is configured to discover Kubernetes workloads and resources in
all namespace(s).

Inspect created VulnerabilityReports by:

    kubectl get vulnerabilityreports --all-namespaces -o wide

Inspect created ConfigAuditReports by:

    kubectl get configauditreports --all-namespaces -o wide

Inspect the work log of trivy-operator by:

    kubectl logs -n trivy-system deployment/trivy-operator

Dashboard
<https://grafana.com/grafana/dashboards/16337-trivy-operator-vulnerabilities/>

<https://github.com/aquasecurity/kube-bench>

<https://github.com/aquasecurity/tracee>

<https://github.com/aquasecurity/trivy>
