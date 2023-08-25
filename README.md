# Plataforma de Testes para Iniciação Científica
Autor: Roberto Santana Santos

Desenvolvimento de plataforma para realização dos testes referentes ao estudo do aprendizado em seres humanos. 

## Introdução ao Projeto

Plataforma de testes utilizada para obtenção de dados para o projeto de iniciação científica **"Comparação do desempenho entre aprendizado humano e aprendizado de máquina na classificação de imagens de peças industriais: um estudo de caso aplicado"**. 

## Sobre a Plataforma
A plataforma é constituída por um formulário inicial para o levatamento de dados iniciais dos entrevistados e sua relação inicial com elementos de máquina. Em seguida, teremos três etapas consecutivas de teste de identificação de elementos de máquina(fácil, médio e difícil), formadas por três estágios (treinamento, dispersão e validação). Por fim, finalizamos as atividades com um formulário de satisfação e sobre as sensações experienciadas pelos entrevistados.

## Desenvolvimento da Plataforma

Stack
- Python
- Flet framework
- Firebase Realtime Database

A plataforma será desenvolvida inteiramente em python, utilizando frameworks como flet para o frontend e o Firebase Realtime Database como banco de dados, os dados armazenados no firebase serão extraídos para um arquivo csv e tratados para melhor visualização.

estrutura de modelos:
* InitialFormModel -> contendo os dados do formulario inicial
 * EasyTesteModel -> contendo os dados do teste facil
* MediumTesteModel -> contendo os dados do teste medio
* HardTesteModel -> contendo os dados do teste dificil
* FinalFormModel -> contendo os dados do formulario final
* ResultsModel -> contendo todos os dados obtidos
