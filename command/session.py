#
#  Admin only command to start sessions on other channels.
#  Logs from individual sessions are not split, so it will
#  get messy. Clean up of sessions is not done when usv3
#  exits, which will make logs even messier.
#

import usv3.bot
import asyncio
import uvloop
import random
import string


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Module:
    description = "Start a session on another channel, randomized if not specified"
    usage = "<start/stop/list> [channel]"
    min_args = 1
    max_args = 2
    groups = ["admins"]

    @staticmethod
    def on_load(bot, namespace):
        namespace.sessions = {}

    @staticmethod
    async def run(bot, namespace, text, args, sender, trip, ulevel):
        channel = args[1] if len(args) == 2 else "".join(random.choices(string.ascii_lowercase, k=8))
        match args[0]:
            case "start":
                if channel in namespace.sessions:
                    await bot.reply(sender, f"Session already running in ?{channel}")
                    return

                config = bot.config.copy()
                config["channel"] = channel
                namespace.sessions[channel] = {}
                namespace.sessions[channel]["instance"] = usv3.bot.Bot(config)
                namespace.sessions[channel]["task"] = asyncio.create_task(namespace.sessions[channel]["instance"].main())
                bot.reply(sender, f"Session started in ?{channel}")

            case "stop":
                if channel not in namespace.sessions:
                    await bot.reply(sender, f"Session not running in ?{channel}")
                    return

                namespace.sessions[channel]["task"].cancel()
                del namespace.sessions[channel]
                await bot.reply(sender, f"Session stopped in ?{channel}")

            case "list":
                await bot.reply(sender, f"Running sessions: ?{' ?'.join(namespace.sessions)}")
