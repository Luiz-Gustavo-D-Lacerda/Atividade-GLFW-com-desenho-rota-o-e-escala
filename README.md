# Atividade - GLFW com Desenho, Rotação e Escala

Este projeto é uma atividade em Python utilizando **OpenGL** e **GLFW** para exibir um cubo 3D (formato retangular) com **animação de escala pulsante** e **rotação contínua**.

## 🖼️ Visual

- O cubo é desenhado apenas com **arestas brancas**
- Ele gira suavemente em torno dos eixos X e Y
- A escala do cubo aumenta e diminui com base no tempo (efeito "pulsar")

---

## 📦 Requisitos

Certifique-se de ter o Python 3.7 ou superior instalado.

Instale os pacotes necessários com:

```bash
pip install PyOpenGL PyOpenGL_accelerate glfw

```
🧠 O que o código faz

Inicializa uma janela usando glfw

Configura o contexto OpenGL 3.3 (compatível)

Cria uma projeção em perspectiva 3D

Define os vértices e arestas de um cubo retangular

Aplica transformação de:

Translação para afastar o cubo da câmera

Escala animada com math.sin(t)

Rotação contínua no tempo

Desenha as linhas do cubo com glBegin(GL_LINES)
