#
#  Command for evaluating a math expression. Add `aiohttp`
#  as a dependency. While slower than the version that uses
#  the numexpr package, this is safer with less restrictions.
#

import aiohttp


class Module:
    description = "Evaluates a math expression"
    usage = "<expression>"
    min_args = 1

    @staticmethod
    async def run(bot, namespace, text, args, sender, tripcode, ulevel) -> None:
        url = "http://api.mathjs.org/v4/"
        data = {
            "expr": " ".join(args),
            "precision": 10
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=data) as resp:
                    data = await resp.json()
                    await bot.reply(sender, data["result"] if data["result"] else f"Error: {data['error']}")

            except:
                await bot.reply(sender, "Could not connect to mathjs.org")
