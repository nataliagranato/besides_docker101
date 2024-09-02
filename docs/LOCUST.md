# Teste de carga com Locust

O Locust é uma ferramenta de teste de carga que permite simular um grande número de usuários acessando um sistema ao mesmo tempo. Ele é muito utilizado para testar a escalabilidade de aplicações web.

No caso da nossa aplicação, o Locust será utilizado para simular o acesso de um grande número de usuários ao sistema, a fim de verificar se o mesmo é capaz de suportar a carga gerada. Para isso, será necessário criar um script que simule o comportamento dos usuários ao acessar o sistema.

Além disso conseguiremos verificar se o nosso cluster irá escalar a aplicação, visto que definimos no `values.yaml` a utilização de um `HorizontalPodAutoscaler`. O bloco que define o `HorizontalPodAutoscaler` é o seguinte:

```yaml

autoscaling:
  enabled: true
  minReplicas: 1
  maxReplicas: 100
  targetCPUUtilizationPercentage: 80
  targetMemoryUtilizationPercentage: 80
```

O `HorizontalPodAutoscaler` irá escalar a aplicação de acordo com a utilização de CPU e memória. O `targetCPUUtilizationPercentage` e `targetMemoryUtilizationPercentage` definem o percentual de utilização de CPU e memória que irá disparar a escala da aplicação. Nesse caso o número máximo de réplicas é 100.

## Instalação

Para instalar o Locust, basta executar o seguinte comando:

```bash
cd locust
kubectl apply -f deployment.yaml -n locust
kubectl apply -f service.yaml -n locust
kubectl apply -f configmap.yaml -n locust
kubectl apply -f ingress.yaml -n locust
```

## Acesso

Para acessar o locust e iniciar os testes de carga, basta acessar o endereço `https://locust.nataliagranato.xyz` no navegador. Ou use o port-forward:

```bash
kubectl port-forward svc/locust 8089:80 -n locust
```

Ao acessar a aplicação, será necessário informar o número de usuários a serem simulados, a taxa de usuários por segundo e o tempo de execução do teste. Após preencher essas informações, basta clicar no botão `Start` para iniciar o teste.

Acompanhe o andamento do teste na aba `Charts`, onde é possível visualizar o número de usuários ativos, a taxa de requisições por segundo, o tempo de resposta e outros dados relevantes.

Para validar se o teste está sendo executado com sucesso, verifique os logs do locust. Você verá algo como:

```bash
[2024-08-20 00:31:03,380] locust-66d9c889d9-s5v5g/INFO/locust.main: Starting web interface at http://0.0.0.0:8089

[2024-08-20 00:31:03,394] locust-66d9c889d9-s5v5g/INFO/locust.main: Starting Locust 2.31.3

[2024-08-20 00:31:11,772] locust-66d9c889d9-s5v5g/INFO/locust.runners: Ramping to 1000 users at a rate of 100.00 per second

[2024-08-20 00:31:20,864] locust-66d9c889d9-s5v5g/INFO/locust.runners: All users spawned: {"Giropops": 1000} (1000 total users)
```

Esses logs indicam que o teste foi iniciado com sucesso na API `https://senhas.nataliagranato.xyz/api/senhas` e que os usuários estão sendo criados conforme o que eu solicitei.

Ao final do teste, é possível visualizar um relatório com os resultados obtidos, incluindo o número total de requisições, o tempo médio de resposta, o tempo total de execução e outros dados importantes.

Para visualizar o meu relatório inicial, acesse o link: [Relatório Inicial](https://locust.nataliagranato.xyz/stats/report?theme=dark)
