# Furiapp Bot

Este é um bot do Telegram desenvolvido para interagir com os fãs da equipe FURIA Esports. Ele oferece funcionalidades como exibição de últimos jogos, notícias, quiz interativo, informações sobre os integrantes do time e links úteis.

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- Python 3.8 ou superior
- Um token de bot do Telegram (gerado pelo BotFather)
- Uma chave de API do PandaScore (para acessar informações sobre os jogos)
- Biblioteca `pip` para gerenciar dependências

## Configuração

1. **Clone o repositório ou copie os arquivos para o seu ambiente local.**

2. **Instale as dependências do projeto.**

   Execute o seguinte comando no terminal para instalar as bibliotecas necessárias:

   ```bash
   pip install python-telegram-bot python-dotenv requests

3. **Configure as variáveis de ambiente.**

Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
telegram_secret_key=SEU_TOKEN_DO_TELEGRAM 
panda_api_key=SUA_CHAVE_DE_API_DO_PANDASCORE

Substitua `SEU_TOKEN_DO_TELEGRAM` pelo token do seu bot do Telegram e `SUA_CHAVE_DE_API_DO_PANDASCORE` pela sua chave de API do PandaScore.

4. **Verifique as permissões do bot.**

Certifique-se de que o bot foi adicionado ao grupo ou canal desejado e que possui as permissões necessárias para enviar mensagens e interagir com os usuários.

## Como Iniciar o Bot

1. **Execute o script principal.**

No terminal, navegue até o diretório do projeto e execute o seguinte comando:

bash
python furiapp_bot.py

2. **Interaja com o bot no Telegram.**

Abra o Telegram, procure pelo seu bot (usando o nome ou o username configurado no BotFather) e envie o comando /start para começar a interação.

Funcionalidades
📅 Últimos Jogos: Exibe os últimos jogos da equipe FURIA.
📰 Últimas Notícias: Mostra as notícias mais recentes sobre a equipe.
🎲 Quiz: Um quiz interativo com perguntas sobre a FURIA.
👥 Nossas Feras: Lista os integrantes do time de CS:GO com links para seus perfis no Instagram.
🔗 Links Úteis: Links para as redes sociais e canais oficiais da FURIA.
👋 Até a próxima!: Encerra a interação com o bot.

## Estrutura do Projeto

.env                # Arquivo de configuração de variáveis de ambiente
.gitignore          # Arquivo para ignorar arquivos sensíveis no controle de versão
furiapp_bot.py      # Código principal do bot
logo.jpg            # Imagem do logo (opcional)
read.me             # Este arquivo README