<div align="center">

# 🎮 PyQuest Arcade
### Aprenda Python e Análise de Dados com Pandas no ritmo de um jogo Arcade!

[![Status](https://img.shields.io/badge/Status-Pronto_para_Jogar-10b981?style=for-the-badge)]()
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript_ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)]()

[**🕹️ Jogar Agora (GitHub Pages)**](https://rodrigocezartech.github.io/pyquest-arcade/) • [**📂 Explorar Código**](#-estrutura-do-projeto) • [**🚀 Como Rodar**](#-como-executar)

</div>

---

## 🎯 Sobre o Projeto

O **PyQuest Arcade** transforma o aprendizado de programação em uma experiência gamificada e visual. Em vez de listas exaustivas de exercícios teóricos, o jogador assume o controle de **25 missões práticas** baseadas em cenários reais — desde emergências médicas e telemetria orbital até limpeza e agrupamento de DataFrames com **pandas**.

O projeto conta com **duas versões completas**:
1. **Aplicação Web (`index.html`):** Interface responsiva em tela cheia, com criador de avatar, ilustrações SVG dinâmicas por caso, efeitos sonoros sintetizados via Web Audio API e atalhos de teclado.
2. **Versão CLI (`pyquest_arcade.py`):** Jogo interativo em linha de comando feito em Python puro para treinar direto no terminal.

---

## ✨ Principais Funcionalidades

- **🧠 25 Missões Contextualizadas:**
  - **Lógica & Controle:** `if`, `elif`, `else`, `and`, `for / range()`, `while`, `in`.
  - **Estruturas & Funções:** `list.append()`, `dict`, `def`, `return`, `try / except`, `len()`, `sum()`, `str.upper()`, `print()`.
  - **Análise de Dados com Pandas:** `pd.read_csv()`, `pd.read_json()`, `.head()`, `.dropna()`, `.groupby()`, `.describe()`, `.shape`, `.sort_values()`, `.columns`.
- **👾 Criador de Avatar Personalizado:** Customize o estilo do personagem, paleta neon e acessório com salvamento automático no navegador (`localStorage`).
- **🎨 Ilustrações & Prévia de Dados:** Cada missão exibe uma cena SVG temática e, nos desafios de pandas, uma tabela com amostra real dos dados antes da execução.
- **⚡ Mecânica Arcade & Feedback Imediato:**
  - Cronômetro regressivo por questão e bônus de velocidade.
  - Multiplicador de **Combo** por sequência de acertos.
  - Sistema de **Dicas Estratégicas** e explicação técnica detalhada após cada resposta.
  - Placar local (*Leaderboard*) persistente no navegador.
- **🔊 Motor de Áudio Nativo:** Trilha dinâmica por caso e efeitos sonoros gerados em tempo real via **Web Audio API** (sem depender de arquivos externos pesados).
- **⌨️ Atalhos de Teclado:** Jogue sem tirar as mãos do teclado usando `[1]` a `[4]` para responder, `[H]` para pedir dica e `[Enter]` ou `[Espaço]` para avançar.

---

## 📁 Estrutura do Projeto

```text
pyquest-arcade/
├── index.html          # Versão Web completa (renomeie pyquest.html para index.html no GitHub)
├── pyquest_arcade.py   # Versão interativa para rodar no terminal Python
└── README.md           # Documentação do projeto
```

---

## 🚀 Como Executar

### 1. Na Web (Local ou via GitHub Pages)
- **Localmente:** Basta dar um duplo clique no arquivo `index.html` para abrir em qualquer navegador moderno (Chrome, Edge, Firefox, Safari ou celular).
- **Online:** Acesse diretamente pelo link do GitHub Pages: `https://rodrigocezartech.github.io/pyquest-arcade/`

### 2. No Terminal (Python CLI)
Certifique-se de ter o **Python 3** instalado e execute:
```bash
python pyquest_arcade.py
```

---

## 🌐 Sobre o Modo Online e Salas por PIN

- **Acesso Online via Link:** Publicado no **GitHub Pages**, qualquer pessoa no computador ou celular pode abrir o link e jogar online instantaneamente no navegador.
- **Como funciona a Sala por PIN:** O sistema atual gera e valida o PIN localmente no navegador para partidas e placar no dispositivo. Como evolução futura, o frontend pode ser conectado a um backend leve (Firebase, Supabase ou FastAPI com WebSockets) para salas multiplayer sincronizadas em tempo real.

---

## 👨‍💻 Autor

Desenvolvido por **Rodrigo Cezar** ([@RodrigoCezarTech](https://github.com/RodrigoCezarTech)) — conecte-se comigo no [LinkedIn](https://www.linkedin.com/)!