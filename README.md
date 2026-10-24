# 🎮 Glow ESP — Educational Game Hacking Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Project-Educational-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Cyber%20Security-Research-red?style=for-the-badge">
</p>

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de explorar conceitos de **Game Hacking, programação em Python e Cyber Security**.

A aplicação consiste em um experimento educacional que utiliza a biblioteca `pymem` para estudar a interação entre um programa externo e a memória de um processo, utilizando o CS:GO como ambiente de experimentação.

O projeto também possui uma interface gráfica desenvolvida com Dear PyGui, permitindo explorar conceitos de criação de interfaces e integração entre diferentes bibliotecas Python.

**Este projeto foi desenvolvido exclusivamente para fins educacionais, experimentação e aprendizado pessoal.**

Como entusiasta de Cyber Security, meu objetivo foi testar meus conhecimentos, compreender melhor o funcionamento da manipulação de memória e explorar conceitos relacionados à engenharia reversa de aplicações.

## 🎯 Objetivos

Os principais objetivos deste projeto são:

* Estudar conceitos fundamentais de Game Hacking.
* Compreender como programas externos interagem com processos.
* Explorar a leitura e escrita de memória utilizando Python.
* Aprender sobre offsets e estruturas de memória.
* Desenvolver uma interface gráfica utilizando Dear PyGui.
* Praticar a organização de código em Python.
* Aplicar conhecimentos adquiridos durante meus estudos de programação e Cyber Security.

## ⚙️ Funcionalidades

### 🔹 Glow ESP

O projeto possui uma implementação experimental de Glow ESP.

Essa funcionalidade utiliza informações de memória para estudar como determinados dados relacionados às entidades do jogo podem ser acessados e utilizados em uma aplicação externa.

O código trabalha com informações como:

* Lista de entidades.
* Identificação de equipes.
* Índices relacionados ao sistema de Glow.
* Valores de cores RGB.
* Transparência.
* Ativação do efeito visual.

O objetivo dessa implementação é compreender, na prática, como a manipulação de memória pode modificar informações utilizadas por uma aplicação.

### 🔹 Interface Gráfica

A interface foi desenvolvida utilizando a biblioteca Dear PyGui.

Ela possui:

* Uma janela principal.
* Identificação do projeto.
* Botão de ativação.
* Interface simples para interação com a funcionalidade experimental.

A criação dessa interface também permitiu praticar conceitos de desenvolvimento de aplicações gráficas em Python.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização                                                |
| ---------- | --------------------------------------------------------- |
| Python     | Linguagem principal do projeto                            |
| Pymem      | Estudo de interação com memória de processos              |
| Dear PyGui | Desenvolvimento da interface gráfica                      |
| Tkinter    | Exibição de mensagens                                     |
| Offsets    | Referências utilizadas para estudar estruturas de memória |

## 📂 Estrutura do Projeto

```text
Glow-ESP/
│
├── main.py
│
├── offsets.py
│
└── README.md
```

**Observação:** A estrutura acima representa uma organização sugerida para o projeto. Os nomes dos arquivos podem variar conforme a organização utilizada no desenvolvimento.

## 📚 Conceitos Estudados

Durante o desenvolvimento deste projeto, foram explorados conceitos relacionados a:

### Programação em Python

* Importação de bibliotecas.
* Criação de funções.
* Organização de código.
* Estruturas condicionais.
* Loops.
* Manipulação de variáveis.
* Integração entre bibliotecas.

### Manipulação de Memória

* Leitura de informações de processos.
* Escrita de valores em memória.
* Utilização de offsets.
* Identificação de estruturas de dados.
* Interação entre aplicações externas e processos.

### Interfaces Gráficas

* Criação de janelas.
* Botões.
* Textos.
* Organização de elementos gráficos.
* Eventos e callbacks.

## 🚀 Instalação

Para executar o projeto em um ambiente de desenvolvimento Python, instale as bibliotecas utilizadas:

```bash
pip install pymem dearpygui
```

O Tkinter normalmente acompanha as instalações convencionais do Python no Windows.

Também é necessário possuir o arquivo `offsets.py` utilizado pelo projeto.

## ▶️ Execução

Abra o projeto em seu ambiente de desenvolvimento Python.

Execute o arquivo principal:

```bash
python main.py
```

A aplicação apresenta uma interface gráfica experimental desenvolvida para estudar os conceitos abordados no projeto.

## ⚠️ Aviso Legal e Responsabilidade

Este projeto foi desenvolvido **exclusivamente para fins educacionais, experimentação e aprendizado pessoal**.

O código representa um experimento de um entusiasta de Cyber Security interessado em compreender conceitos de programação, engenharia reversa e interação com processos.

O projeto não foi desenvolvido com a intenção de prejudicar outros jogadores, comprometer sistemas ou promover vantagens indevidas em partidas competitivas.

A utilização de ferramentas de manipulação de memória em jogos pode violar os termos de serviço, as regras de servidores ou os mecanismos anticheat.

Por esse motivo, recomenda-se que qualquer experimentação seja realizada exclusivamente em ambientes controlados, offline ou em aplicações próprias, com autorização adequada.

**O autor não se responsabiliza pelo uso indevido, pelas modificações realizadas por terceiros ou pelas consequências decorrentes da utilização deste código em ambientes não autorizados.**

## 👨‍💻 Autor

Projeto desenvolvido por um entusiasta de Python e Cyber Security.

O desenvolvimento teve como principal objetivo testar conhecimentos adquiridos durante os estudos de programação e explorar conceitos relacionados ao funcionamento interno de aplicações.

## 📖 Considerações Finais

Este projeto representa uma experiência prática de aprendizado envolvendo Python, interfaces gráficas e conceitos de manipulação de memória.

A proposta foi transformar conhecimentos teóricos em uma aplicação experimental, permitindo compreender melhor como diferentes componentes de software podem interagir.

O desenvolvimento faz parte da minha jornada de aprendizado em programação e Cyber Security.

**Estudar, experimentar e compreender o funcionamento das tecnologias é o principal objetivo deste projeto.**
