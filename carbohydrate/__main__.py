import os

import crescent
import hikari

bot = hikari.GatewayBot(os.environ["TOKEN"], intents=hikari.Intents.ALL)
client = crescent.Client(bot)
client.plugins.load_folder("carbohydrate.plugins")


@client.include
@crescent.command(description="Pong!")
async def ping(ctx: crescent.Context):
    await ctx.respond("Pong!")


if __name__ == "__main__":
    if os.name != "nt":
        import asyncio

        import uvloop

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    bot.run(
        activity=hikari.Activity(
            name="bread dry",
            type=hikari.ActivityType.WATCHING,
        )
    )
