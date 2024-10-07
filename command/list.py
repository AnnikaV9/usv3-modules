#
#  Command for listing users in the current or specified
#  channel.
#

import json
import random
import websockets.asyncio.client


class Module:
    description = "Lists users in a channel. Lists current channel if optional [channel] is not provided."
    usage = "[channel]"
    max_args = 1
    alias = "ls"

    @staticmethod
    async def run(bot, namespace, text, args, sender, tripcode, ulevel):
        if len(args) == 0:
            pretty_list = ", ".join(bot.online_users).replace("_", "\\_")
            await bot.reply(sender, f"?{bot.config['channel']} - {pretty_list}")
            return

        channel = " ".join(args).removeprefix("?")
        nick = f"list{random.randint(1000, 9999)}"
        async with websockets.asyncio.client.connect(bot.config["server"]) as ws:
            await ws.send(json.dumps({"cmd": "join", "nick": f"{nick}#{bot.config['password']}", "channel": channel}))
            recv = json.loads(await ws.recv())

        if recv["cmd"] == "onlineSet":
            users = recv["nicks"]
            users.remove(nick)
            if len(users) == 0:
                await bot.reply(sender, f"?{channel} is empty.")
                return

            pretty_list = ", ".join(users).replace("_", "\\_")
            await bot.reply(sender, f"?{channel} - {pretty_list}")
