# 🤖 Furiapp Bot

**Bot do Telegram desenvolvido para interagir e engajar a comunidade de fãs da equipe FURIA Esports.**

Este bot atende a fãs fervorosos, oferecendo acesso rápido a informações cruciais sobre o time, jogos recentes, notícias e uma experiência de quiz interativo.

## 🎯 Contexto do Projeto (Processo Seletivo FURIA)

Este projeto foi desenvolvido como parte de um **Processo Seletivo para a vaga de Engenheiro(a) de Software na FURIA Esports**.

O objetivo principal foi demonstrar habilidades de **integração de APIs externas (PandaScore)**, desenvolvimento de **lógica de aplicação (Python)** e construção de uma **interface conversacional (Telegram Bot)**, tudo focado na paixão e na marca da organização.

## ✨ Funcionalidades

O bot foi projetado para fornecer as seguintes interações através de comandos no Telegram:

* **📅 Últimos Jogos:** Exibe o placar e detalhes dos últimos confrontos da equipe FURIA (via integração com PandaScore).
* **📰 Últimas Notícias:** Mostra as notícias mais recentes sobre a equipe e seus jogadores.
* **🎲 Quiz:** Um quiz interativo com perguntas sobre a história e os membros da FURIA para testar o conhecimento dos fãs.
* **👥 Nossas Feras:** Lista os integrantes da equipe (presumivelmente CS:GO, conforme o código) com links diretos para seus perfis no Instagram.
* **🔗 Links Úteis:** Fornece acesso rápido às redes sociais e canais oficiais da FURIA.
* **👋 Até a próxima!:** Comando para encerrar a sessão de interação.

---

## 🛠️ Configuração e Instalação

Siga os passos abaixo para configurar e executar o bot em seu ambiente local.

### Pré-requisitos

Certifique-se de ter os seguintes itens prontos antes de começar:

* **Python:** Versão **3.8 ou superior**.
* **Token do Telegram:** Um token de bot válido obtido através do **BotFather**.
* **Chave da PandaScore:** Uma chave de API da **PandaScore** para acessar dados atualizados sobre os jogos.
* **Gerenciador de Pacotes:** `pip` instalado para gerenciar as dependências.

### 1. Instalação de Dependências

Clone o repositório para o seu ambiente local e instale as bibliotecas necessárias:

```bash
# Clone o repositório
git clone [https://www.youtube.com/watch?v=351MZvGXpnY](https://www.youtube.com/watch?v=351MZvGXpnY)
cd furiapp-bot

# Instale as dependências
pip install python-telegram-bot python-dotenv requests
````

### 2\. Variáveis de Ambiente

Para manter suas chaves seguras, crie um arquivo chamado **`.env`** na raiz do projeto e adicione suas credenciais:

```.env
# TOKEN SECRETO DO BOT GERADO PELO BOTFATHER
TELEGRAM_SECRET_KEY=SEU_TOKEN_DO_TELEGRAM

# CHAVE DE API PARA OBTENÇÃO DE DADOS DOS JOGOS
PANDA_API_KEY=SUA_CHAVE_DE_API_DO_PANDASCORE
```

> **Atenção:** Certifique-se de que o arquivo `.env` esteja listado no seu `.gitignore` para não expor suas chaves publicamente.

### 3\. Permissões do Bot

Após a configuração, verifique no Telegram se o bot possui as permissões necessárias para:

  * Enviar mensagens.
  * Interagir com os usuários no chat ou grupo/canal desejado.

## ▶️ Como Iniciar o Bot

Para colocar o bot em funcionamento, execute o script principal via terminal:

```bash
python furiapp_bot.py
```

Com o script rodando, abra o Telegram, procure pelo seu bot e envie o comando `/start` para começar a interagir\!

## 📂 Estrutura do Projeto

A estrutura de arquivos do bot é simples e direta:

```
furiapp-bot/
├── .env                  # Variáveis de ambiente (SECRETO)
├── .gitignore            # Arquivo para ignorar arquivos sensíveis
├── furiapp_bot.py        # Código principal do bot (Lógica e Comandos)
├── logo.jpg              # Imagem do logo (opcional)
└── README.md             # Este arquivo
```

## 🤝 Contribuição

Sua ajuda é bem-vinda\! Se tiver sugestões para novos comandos, melhorias no quiz ou correção de bugs:

1.  Crie um **Fork** do projeto.
2.  Crie uma nova *branch* (`git checkout -b feature/minha-melhoria`).
3.  Faça o **Commit** das suas alterações (`git commit -m 'feat: adiciona comando de estatísticas'`).
4.  Faça o **Push** para a *branch* (`git push origin feature/minha-melhoria`).
5.  Abra um **Pull Request**.
