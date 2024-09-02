# Criando um cluster Kubernetes com `kind`

Para criar um cluster Kubernetes usando `kind` (Kubernetes IN Docker) a partir de um arquivo de configuração, siga os passos abaixo:

## Passos para Criar um Cluster Kubernetes com `kind`

1. **Certifique-se de ter o Docker instalado e em seguida instale o `kind`, você pode instalá-lo usando o comando abaixo:

    ```bash
    curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
    chmod +x ./kind
    sudo mv ./kind /usr/local/bin/kind
    ```

2. **Crie um Arquivo de Configuração do Cluster**:
    - Crie um arquivo de configuração YAML para o cluster. Por exemplo, `kind-config.yaml`:

    ```yaml
    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: worker
    - role: worker
    - role: worker
    - role: control-plane
    kubeadmConfigPatches:
    - |
        kind: InitConfiguration
        nodeRegistration:
        kubeletExtraArgs:
            node-labels: "ingress-ready=true"
    extraPortMappings:
    - containerPort: 80
        hostPort: 80
        protocol: TCP
    - containerPort: 443
        hostPort: 443
        protocol: TCP
    ```

3. **Crie o Cluster Usando o Arquivo de Configuração**:
    - Use o comando `kind create cluster` especificando o arquivo de configuração:

    ```bash
    kind create cluster --config kind-config.yaml
    ```

### Verificação

Após a criação do cluster, você pode verificar se ele está funcionando corretamente usando o comando `kubectl`:

```bash
kubectl get nodes
```

Isso deve listar os nós do cluster que você acabou de criar.
