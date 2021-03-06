import random
from typing import Match
from discord import Message
from MoMMI import command, MChannel

@command("pick", r"(?:pick|choose)\s*\((.*?)\)")
async def pick_command(channel: MChannel, match: Match, message: Message) -> None:
    choices = [x.strip() for x in match.group(1).split(",")]
    if len(choices) < 2:
        await channel.send("You need to provide at least 2 options.")
        return

    choice = random.choice(choices)
    await channel.send(f"**{choice}**")

@command("roll", r"(\d+)d(\d+)(?:\+(\d+))?")
async def roll_command(channel: MChannel, match: Match, message: Message) -> None:
    result = "Results: "
    count = int(match.group(1))
    if count > 100:
        await channel.send("Ok look dude. A minute or two after this dice command got implemented bobda ran a god damn 10000000000000000000000000000d10. Now because it has to ITERATE those dice and 10000000000000000000000000000 is a giant fucking number, that locked up MoMMI completely because no amount of asyncio is gonna save this madness. Thank god for SIGKILL. THEN I got pinged by Intigracy telling me MoMMI locked up. *sigh*")
        return
    total = 0
    for i in range(0, count):
        if i > 0:
            result += ", "
        roll = random.randint(1, int(match.group(2)))
        total += roll
        result += str(roll)
    mod = match.group(3)
    if mod is not None:
        result += f" + {mod}"
        total += int(mod)
    result += f" = {total}"
    await channel.send(result)

@command("magic8ball", r"(?:magic|magic8ball)")
async def magic8ball_command(channel: MChannel, match: Match, message: Message) -> None:
    choice = random.choice([
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook: Positive",
        "Yes",
        "Signs point to: Yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better to not tell you right now",
        "Cannot predict now",
        "Concentrate, then ask again",
        "Do not count on it",
        "My reply is: no",
        "My sources say: no",
        "Outlook: Negative",
        "Very doubtful"
    ])
    await channel.send(choice)
