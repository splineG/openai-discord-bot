import openai
import discord

openai.api_key = "your openai api key here"

intents = discord.Intents()
intents.messages = True

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!generate"):
        prompt = message.content[9:]
        response = generate_response(prompt)
        await message.channel.send(response)

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )

    return response["choices"][0]["text"]

client.run("your bot token here") 
