#
#  Command for evaluating a math expression. Add `numexpr`
#  as a dependency. This is faster than the version that uses
#  mathjs.org's API, but it's less safe and more restricted.
#

import numexpr


class Module:
    description = "Evaluates a math expression"
    usage = "<expression>"
    min_args = 1

    @staticmethod
    async def run(bot, namespace, text, args, sender, trip, ulevel):
        try:
            result = numexpr.evaluate(" ".join(args))
            await bot.reply(sender, result)

        except Exception as e:
            await bot.reply(sender, f"Error: {str(e).rstrip('.')}")
