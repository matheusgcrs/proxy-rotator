# 🧭 Proxy Rotator - Python

Este projeto é uma ferramenta que busca, valida, enriquece e rotaciona proxies de forma automática e eficiente.  
Ideal para quem precisa trocar de IP constantemente em aplicações como automações, scraping de dados, testes ou navegação segura.

---

## 🤔 O que é um Proxy?

Um **proxy** é como um intermediário entre você e a internet.

### Exemplo simples:
Imagine que você está em uma sala e quer conversar com alguém, mas prefere não mostrar quem é você. Então, você pede para outra pessoa (o proxy) entregar sua mensagem por você. A pessoa do outro lado responde para esse intermediário, que te repassa a resposta.

✅ Resultado: o destinatário nunca sabe que foi você quem enviou a mensagem.

---

## 🧠 Por que usar um Rotador de Proxies?

Sites costumam bloquear IPs que fazem muitas requisições repetidas.  
Com um **rotador**, você alterna automaticamente entre vários IPs, evitando bloqueios e aumentando sua liberdade de navegação/automações.

---

## 🚀 Funcionalidades

- 🔄 Busca proxies de múltiplas fontes públicas
- ✅ Valida proxies rapidamente com múltiplas threads
- 🌍 Enriquecimento de IPs com geolocalização (país, cidade, região)
- 🔁 Rotador de proxies com ciclo automático
- 🧪 Testes unitários incluídos

---

## 🛠️ Como usar

### 1. Instale as dependências
pip install requests

### 2. Na raiz do projeto rode
python -m cli.update