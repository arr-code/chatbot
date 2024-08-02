from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# URL API server Flask
CHAT_API_URL = 'http://localhost:5000/api/chat'  # Sesuaikan dengan URL Flask Anda
TELEGRAM_API_TOKEN = '7326976152:AAE90E7rFW_dfCx8GJ8XwSafVY2vO9uW-aE'  # Ganti dengan token Telegram Anda

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalamualaikum. Perkenalkan saya Hafsah AI, saya akan membantu anda dalam menjawab pertanyaan seputar pendaftaran siswa baru Pesantren Darul Quran.')

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        response = requests.post(CHAT_API_URL, json={'input': user_message})
        response.raise_for_status()  # Menangani error HTTP
        response_data = response.json()
        chatbot_response = response_data.get('response', 'Sorry, I did not get a valid response.')
    except (requests.exceptions.RequestException, ValueError) as e:
        chatbot_response = 'Error: Unable to process your request.'
        print(f"Error: {e}")  # Print error untuk debugging

    update.message.reply_text(chatbot_response)

def main():
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler untuk perintah /start
    dp.add_handler(CommandHandler('start', start))
    # Menambahkan handler untuk pesan yang bukan perintah
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Memulai polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
