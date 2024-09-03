# A Cadeia de Boas Práticas

Para garantir a segurança e a eficiência em aplicações Cloud Native, devemos considerar os 4C's: Containers, Clusters, Cloud e Código.

Implementação de boas práticas deve ser feita em todas as etapas do desenvolvimento, desde a escrita do código, a implantação em produção e na utilização de clusters de orquestração e containers.

## Containers e DevOps

A relação entre containers e DevOps é fundamental. Containers permitem que as equipes de desenvolvimento e operações trabalhem de forma mais integrada, facilitando a entrega contínua e a automação.

## Cloud Native Trail Map

A Cloud Native Computing Foundation (CNCF) oferece o [Cloud Native Trail Map](https://github.com/Tech-Preta/trailmap), que orienta sobre os componentes essenciais para construir aplicações nativas de nuvem.

## O Docker

Docker revolucionou a forma como desenvolvemos, testamos e implantamos aplicações, estabelecendo um padrão na indústria para a utilização de containers.

## Diferentes Abordagens de Dockerfile

- [Dockerfile Tradicional](./traditional)
- [Multi Stage Build](./multi-stage)
- [Com Alpine](./alpine)
- [Distroless](./distroless)

## Assinando Imagens com Cosign e por que usar

Assinar imagens com [Cosign](https://github.com/sigstore/cosign) garante a integridade e a autenticidade das imagens de container, aumentando a segurança no pipeline de CI/CD.

## Qualidade do Dockerfile com Hadolint

Utilize [Hadolint](https://github.com/hadolint/hadolint) para verificar a qualidade do seu Dockerfile, garantindo que ele siga as melhores práticas e padrões de segurança.

## Scan de Vulnerabilidade com Docker Scout e Trivy

Realize scans de vulnerabilidade em suas imagens de container utilizando ferramentas como [Docker Scout](https://docs.docker.com/scan/) e [Trivy](https://github.com/aquasecurity/trivy) para identificar e corrigir possíveis falhas de segurança.

## Conclusão

A importância de utilizar imagens pequenas e sem vulnerabilidades não pode ser subestimada. Imagens menores reduzem o tempo de download e a superfície de ataque, enquanto a ausência de vulnerabilidades garante um ambiente mais seguro e confiável.
