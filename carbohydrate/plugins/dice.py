import random

import crescent
import hikari

plugin = crescent.Plugin[hikari.GatewayBot, None]()


@plugin.include
@crescent.command(name="roll", description="Rolls some dice")
class Dice:
    number = crescent.option(
        int,
        "The number of dice to roll.",
        min_value=1,
        max_value=25,
    )
    sides = crescent.option(
        int,
        "The number of sides each die will have.",
        default=6,
        min_value=0,
        max_value=100,
    )
    bonus = crescent.option(
        int,
        "A fixed number to add to the total roll.",
        default=0,
        min_value=0,
        max_value=100,
    )

    async def callback(self, ctx: crescent.Context) -> None:
        rolls = [random.randint(1, self.sides) for _ in range(self.number)]
        await ctx.respond(
            " + ".join(f"{r}" for r in rolls)
            + (f" + {self.bonus} (bonus)" if self.bonus else "")
            + f" = **{sum(rolls) + self.bonus:,}**"
        )
