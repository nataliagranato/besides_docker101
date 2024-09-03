# O que são imagens distroless?

Imagens distroless são imagens Docker que contêm apenas o aplicativo e suas dependências, sem um sistema operacional. Isso torna a imagem mais segura e menor.

A vantagem de usar imagens distroless é que elas são menores e mais seguras. Como não há um sistema operacional dentro da imagem, não há pacotes desnecessários que possam ser explorados por um invasor.

## O nosso exemplo de imagem distroless

- **Faça o pull da imagem:**

```
docker pull nataliagranato/my-app:v4.0.0
```

- **Execute o contêiner:**

```
docker run --rm nataliagranato/my-app:v4.0.0
```

**Prepare-se para ver a mensagem de saída do nosso aplicativo.**

Você pode ver que a imagem é bem menor que a imagem anterior, pois não temos um sistema operacional dentro dela, apenas o binário do nosso aplicativo.
