from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import logging
from telegram.constants import ChatType
import requests
import datetime
from dotenv import load_dotenv
import os

url_pandascore = "https://api.pandascore.co/csgo/matches?filter[opponent_id]=furia&page[size]=3&page[number]=1&begin_at=2025-01-01T00:00:00Z&end_at=2025-04-30T00:00:00Z"
EQUIPE = "FURIA"

payload = {}
# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
panda_api_key = os.getenv("panda_api_key")

headers = {
    'Authorization': f'Bearer {panda_api_key}'
}

response = requests.request("GET", url_pandascore, headers=headers, data=payload)

print(response.text)

# Configurando o log para exibição completa no terminal
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Banco de dados para o quiz com perguntas e respostas
quiz_questions = [
    {
        "pergunta": "Quem é o capitão do time de CS:GO da FURIA?",
        "opcoes": ["Art", "KSCERATO", "yuurih", "saffee", "FalleN"],
        "resposta": "FalleN"
    },
    {
        "pergunta": "Qual é o nome do treinador do time de CS:GO da FURIA?",
        "opcoes": ["zews", "peacemaker","sidde", "bit", "guerri"],
        "resposta": "sidde"
    },
    {
        "pergunta": "Em que ano a organização FURIA foi fundada?",
        "opcoes": ["2015", "2017", "2018", "2019"],
        "resposta": "2017"
    },
    {
        "pergunta": "Qual país a organização FURIA representa?",
        "opcoes": ["Estados Unidos", "Canadá", "Brasil", "Portugal"],
        "resposta": "Brasil"
    },
    {
        "pergunta": "Qual jogador da FURIA tem o apelido 'KSCERATO'?",
        "opcoes": ["Kaike Cerato", "Kevin Santos", "Kauê Cerato", "Kaique Santos"],
        "resposta": "Kaike Cerato"
    },
    {
        "pergunta": "Quantos jogadores compõem o time titular de CS:GO?",
        "opcoes": ["6", "5", "4", "7"],
        "resposta": "5"
    },
    {
        "pergunta": "Qual é o mapa mais jogado pela FURIA em competições?",
        "opcoes": ["Inferno", "Mirage", "Nuke", "Overpass"],
        "resposta": "Mirage"
    },
]

# Lista de integrantes do time de CS:GO da FURIA com links para o Instagram
integrantes_csgo = [
    {"nome": "Gabriel 'FalleN' Toledo", "instagram": "https://www.instagram.com/fallen"},
    {"nome": "Kaike 'KSCERATO' Cerato", "instagram": "https://www.instagram.com/kscerato"},
    {"nome": "Yuri 'yuurih' Santos", "instagram": "https://www.instagram.com/yuurihfps"},
    {"nome": "Mareks 'YEKINDAR' Gaļinskis", "instagram": "https://www.instagram.com/yek1ndar"},
    {"nome": "Danil 'molodoy' Golubenko", "instagram": "https://www.instagram.com/danil.molodoy"},
]

links_uteis = [
    {"Site/Loja oficial FURIA": "https://www.furia.gg/"},
    {"Canal oficial do YouTube": "https://www.youtube.com/channel/UCE4elIT7DqDv545IA71feHg?sub_confirmation=1"},
    {"Twitch": "https://www.twitch.tv/furiatv?lang=pt-br"},
    {"Instagram": "https://www.instagram.com/furiagg"},
    {"Twitter/X": "https://x.com/FURIA"},
    {"TikTok": "https://www.tiktok.com/@furiagg"},
]

# Variável para armazenar o progresso do quiz por usuário
user_quiz_progress = {}

# Função para criar o menu inicial
def gerar_menu_inicial():
    keyboard = [
        [InlineKeyboardButton("📅 Últimos Jogos", callback_data="jogos")],
        [InlineKeyboardButton("📰 Últimas Notícias", callback_data="noticias")],
        [InlineKeyboardButton("🎲 Quiz", callback_data="quiz")],
        [InlineKeyboardButton("👥 Nossas feras", callback_data="integrantes")],
        [InlineKeyboardButton("🔗 Links Úteis", callback_data="links")],
        [InlineKeyboardButton("👋 Até a próxima!", callback_data="encerrar")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Função para criar o botão de retorno ao menu
def gerar_botao_retorno():
    keyboard = [[InlineKeyboardButton("🔙 Retornar ao Menu", callback_data="menu")]]
    return InlineKeyboardMarkup(keyboard)

# Função para criar botões para opções do quiz
def gerar_opcoes_quiz(opcoes, pergunta_index):
    keyboard = [[InlineKeyboardButton(opcao, callback_data=f"quiz_{pergunta_index}_{opcao}")] for opcao in opcoes]
    return InlineKeyboardMarkup(keyboard)

# Função /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Comando /start recebido de {update.effective_user.first_name}")

    # Enviando mensagem com o menu inicial
    await update.message.reply_text(
        f"👋 Olá, {update.effective_user.first_name}! Bem-vindo ao Furiapp. Aqui você pode acompanhar as novidades e interagir com o time! 🎮\n\n"
        "Escolha uma das opções abaixo:",
        reply_markup=gerar_menu_inicial()
    )

# Função para capturar novas conversas privadas
async def welcome_private_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == ChatType.PRIVATE:  # Verifica se é uma conversa privada
        logger.info(f"Nova conversa privada iniciada por {update.effective_user.first_name}")
        await update.message.reply_text(
            f"👋 Olá, {update.effective_user.first_name}! Bem-vindo ao Furiapp. Aqui você pode acompanhar as novidades e interagir com o time! 🎮\n\n"
            "Escolha uma das opções abaixo para começar:",
            reply_markup=gerar_menu_inicial()
        )

# Função para lidar com os botões interativos
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "jogos":
        string_resultado_formatado = ""
        separador = "*" * 40

        jogos = await buscar_ultimos_3_jogos()
        for jogo in jogos:
            data_partida = jogo.get('data_partida', 'Unknown date')
            vs_text = jogo.get('vs_text', 'TBD')
            resultado = jogo.get('resultado', 'TBD')
            string_resultado_formatado += f"🗓️ {data_partida} \n {vs_text} \n {resultado}\n {separador} \n"

        await query.message.reply_text(
                f"🕹️ Últimos Jogos da FURIA:\n {string_resultado_formatado}",
                reply_markup=gerar_botao_retorno()
            )    

    elif query.data == "links":
        mensagem = "🔗 Links úteis da FURIA:\n"
        for link in links_uteis:
            for nome, url in link.items():
                mensagem += f"• [{nome}]({url})\n"
        await query.edit_message_text(
            mensagem,
            reply_markup=gerar_botao_retorno(),
            disable_web_page_preview=True
        )

    elif query.data == "noticias":
        await query.edit_message_text(
            "📰 Últimas notícias da FURIA:\n"
            "1. [Mais nova assistente de engenharia de software contratada pela FURIA é do interior do estado de São Paulo e conta sua experiência no processo seletivo para a vaga](https://girlsintech.com.br/siteficticio/relato-ana-carolina/).\n"
            "2. [FURIA Esports choca cenário do CS:GO: skullz fora e YEKINDAR é o novo reforço internacional](https://www.vaganerd.com.br/furia-choca-cenario-do-csgo-skullz-fora-e-yekindar-e-o-novo-reforco-internacional/).\n"
            "\nClique nos links para saber mais! 🐾",
            reply_markup=gerar_botao_retorno(),
            disable_web_page_preview=True
        )
    elif query.data == "integrantes":
        mensagem = "👥 Integrantes do Time de CS:GO da FURIA:\n"
        for integrante in integrantes_csgo:
            mensagem += f"• [{integrante['nome']}]({integrante['instagram']})\n"
        await query.edit_message_text(
            mensagem,
            reply_markup=gerar_botao_retorno(),
            disable_web_page_preview=True
        )
    elif query.data == "quiz":
        user_id = query.from_user.id
        user_quiz_progress[user_id] = 0  # Inicializa o progresso do quiz para o usuário
        pergunta_index = user_quiz_progress[user_id]
        pergunta = quiz_questions[pergunta_index]  # Obtém a primeira pergunta
        await query.edit_message_text(
            f"🎲 {pergunta['pergunta']}",
            reply_markup=gerar_opcoes_quiz(pergunta['opcoes'], pergunta_index)
        )
    elif query.data.startswith("quiz_"):
        user_id = query.from_user.id
        _, pergunta_index, resposta = query.data.split("_")
        pergunta_index = int(pergunta_index)

        if resposta == quiz_questions[pergunta_index]["resposta"]:
            await query.edit_message_text("✅ Resposta correta!")
        else:
            await query.edit_message_text(
                f"❌ Resposta errada! A resposta correta era: {quiz_questions[pergunta_index]['resposta']}"
            )

        # Avança para a próxima pergunta
        user_quiz_progress[user_id] += 1
        next_pergunta_index = user_quiz_progress[user_id]

        if next_pergunta_index < len(quiz_questions):
            next_pergunta = quiz_questions[next_pergunta_index]
            await query.message.reply_text(
                f"🎲 {next_pergunta['pergunta']}",
                reply_markup=gerar_opcoes_quiz(next_pergunta['opcoes'], next_pergunta_index)
            )
        else:
            await query.message.reply_text(
                "🎉 Parabéns! Você concluiu o quiz. Obrigado por participar!",
                reply_markup=gerar_botao_retorno()
            )
    elif query.data == "menu":
        await query.edit_message_text(
            "Escolha uma das opções abaixo:",
            reply_markup=gerar_menu_inicial()
        )
    elif query.data == "encerrar":
        await query.edit_message_text(
            "👋 Obrigado por usar o Furiapp! Até a próxima! 🐾🖤"
        )
        logger.info(f"Usuário {query.from_user.first_name} encerrou a interação.")

# Função para buscar os últimos jogos da FURIA na API
async def buscar_ultimos_3_jogos():
    jogos = []
    try:
        # Faz a requisição para a API
        resposta_api = requests.get(url_pandascore, headers=headers)
        
        # Verifica se a resposta foi bem-sucedida
        if resposta_api.status_code != 200:
            print(f"Erro: Código de status recebido {resposta_api.status_code}")
            print(resposta_api.json())
            return
        
        # Analisa a resposta
        jogos = resposta_api.json()
        
        # Verifica se foram encontrados jogos
        if not jogos:
            print("Nenhum jogo encontrado para o time especificado.")
            return
        
        # Processa e exibe os jogos
        print(f"Últimos 3 jogos da {EQUIPE}:")
        for jogo in jogos:
            # Extrai os detalhes do jogo
            data_partida = jogo.get('begin_at', 'Data desconhecida')
            if data_partida:
                data_partida = datetime.datetime.fromisoformat(data_partida.replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M')
            
            # Obtém os nomes dos oponentes
            oponentes = []
            for time in jogo.get('opponents', []):
                oponente = time.get('opponent', {})
                oponentes.append(oponente.get('name', 'TBD'))
            vs_text = " vs ".join(oponentes) if len(oponentes) == 2 else "TBD"
            
            # Obtém o resultado ou status do jogo
            status = jogo.get('status', 'desconhecido')
            vencedor = jogo.get('winner', {}).get('name', 'Nenhum') if jogo.get('winner') else "Nenhum"
            
            resultado = f"Status: {status}, Vencedor: {vencedor}"
            jogos.append({
                "data_partida" : data_partida,
                "vs_text" : vs_text,
                "resultado": resultado
            })
        return jogos         
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")


# Função principal para iniciar o bot
def main():
    # Substitua pelo token do seu bot gerado pelo BotFather
    TOKEN = os.getenv("telegram_secret_key")

    # Configura o bot com o Application
    application = Application.builder().token(TOKEN).build()

    # Adiciona os comandos ao bot
    application.add_handler(MessageHandler(
        filters.ChatType.PRIVATE, welcome_private_chat))  # Usando ChatType.PRIVATE
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))  # Handler para botões interativos

    # Log indicando que o bot foi iniciado
    logger.info("Bot iniciado. Aguardando comandos...")

    # Inicia o bot
    application.run_polling()

# Executa a função principal
if __name__ == "__main__":
    main()