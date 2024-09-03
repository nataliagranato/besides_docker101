# Um Dockerfile tradicional

Este é um exemplo de Dockerfile tradicional, que é um arquivo de texto que contém uma série de instruções para a construção de uma imagem Docker. Nele utilizamos um sistema operacional completo, o que torna a imagem maior e menos segura. Não usamos a abordagem de multi-stage build, que é uma técnica para reduzir o tamanho das imagens Docker. Tampouco um sistema operacional minimalista, como o Alpine Linux.
