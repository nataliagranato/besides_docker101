# Giropops Senhas

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9384/badge)](https://www.bestpractices.dev/projects/9384)[![Build da imagem de container Redis](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/redis-docker.yml/badge.svg?branch=main)](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/redis-docker.yml) [![Build da imagem de container giropops-senhas](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/giropops-docker.yml/badge.svg)](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/giropops-docker.yml) [![Build e Distribuição de Pacotes com Melange e APKO](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/chainguard.yml/badge.svg)](https://github.com/Tech-Preta/LINUXtips-PICK/actions/workflows/chainguard.yml) [![CodeQL](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/github-code-scanning/codeql) [![Dependabot Updates](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/dependabot/dependabot-updates) [![Image digest update](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/digestabot.yml/badge.svg)](https://github.com/Tech-Preta/giropops-senhas/actions/workflows/digestabot.yml) 

O projeto **Giropops Senhas** é uma aplicação web desenvolvida com Flask que permite a geração e gerenciamento de senhas. A aplicação utiliza Redis para armazenamento de dados e é containerizada usando Docker. Além disso, o projeto inclui integração contínua com GitHub Actions para construção e envio de imagens Docker, bem como verificação de vulnerabilidades.

## Ferramentas e Tecnologias Utilizadas

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515) ![AquaSec](https://img.shields.io/badge/aqua-%231904DA.svg?style=for-the-badge&logo=aqua&logoColor=#0018A8) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)

## Ferramentas e Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web utilizado para construir a aplicação.
- **Redis**: Banco de dados em memória utilizado para armazenamento de dados.
- **Docker**: Utilizado para containerização da aplicação.
- **GitHub Actions**: Utilizado para integração contínua e automação de tarefas.
- **Cosign**: Utilizado para assinatura e verificação de imagens de contêiner.
- **Kyverno**: Utilizado para políticas de segurança no Kubernetes.
- **Kubernetes**: Utilizado para orquestração de contêineres em produção.
- **Prometheus**: Utilizado para monitoramento e alertas.
- **APKO**: Utilizado para construção de imagens de contêiner.
- **Melange**: Utilizado para construção de pacotes.
- **Helm**: Utilizado para gerenciamento de pacotes Kubernetes.

## Utilizando a aplicação localmente

1. Clone o repositório:

```bash
git clone https://github.com/Tech-Preta/giropops-senhas.git
cd giropops-senhas
```

2. Utilize o Compose
```bash
docker-compose up -d
```

4. Acesse a aplicação em seu navegador:

```
http://localhost:5000
```

## Contribuindo

Contribuições são bem-vindas! Por favor, siga as diretrizes abaixo ao contribuir para este projeto.

### Criando uma Issue

Se você encontrar um bug ou tiver uma ideia para uma nova funcionalidade, por favor, crie uma issue usando o template apropriado:

1. Vá para a aba "Issues" do repositório.
2. Clique em "New issue".
3. Selecione o template de bug ou feature request.
4. Preencha as informações necessárias e envie a issue.

### Fazendo um Pull Request

Para contribuir com código, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma nova branch para sua feature ou correção de bug (`git checkout -b minha-feature`).
3. Faça as mudanças necessárias e adicione testes, se aplicável.
4. Commit suas mudanças (`git commit -m 'Adiciona minha nova feature'`).
5. Push para a branch (`git push origin minha-feature`).
6. Abra um pull request usando o template de pull request.

### Templates

- [Template de Pull Request](.github/PULL_REQUEST_TEMPLATE.md)
- [Template de Issue de Bug](.github/ISSUE_TEMPLATE/bug_report.md)
