from dotenv import load_dotenv
import discord
import os

from app.openai_api import gpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')


class CustomClient(discord.Client):
    async def on_ready(self):
        print("Success, u r logged in as: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

        if message.author == 'Kielon':
            await message.channel.send('jak ty pojebany')

        if message.content.startswith('/ai'):
            user_message = message.content.replace('/ai', '')
            print(user_message)
            bot_response = gpt_response(user_message)
            await message.channel.send(bot_response)


intents = discord.Intents.default()
intents.message_content = True

client = CustomClient(intents=intents)
