import discord
import responses

async def send_message(message, user_message, is_DM):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_DM else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTE1ODMzNDY0ODg3MTU1OTI1MA.GO9rzA.X49yJHo24yLM7VfXMP04Yle3ubByHjRwKcJPfo"

    intents = discord.Intents.default()
    intents.message_content = True
    Nice = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running and this is working.')

    @client.event
    async def on_message(message):

        if client.user in message.mentions:
            await message.channel.send("""AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH! I DON'T LIKE BEING PINGED YOU SON OF A BIT-
Wait I'm not allowed to swear? Oh, okay. Sorry about that. I don't like being pinged though.""")

        response = responses.handle_response(message)
        if response:
            await message.channel.send(response)
    try:
        client.run(TOKEN)
    except (discord.errors.LoginFailure, discord.errors.HTTPException) as e:
        print("Login unsuccessful due to error: ", e)