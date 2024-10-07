### A collection of useful modules for [usv3-framework](https://github.com/AnnikaV9/usv3-framework)

Lone modules:
|Module|Description|
|--|--|
|[command.coin](./command/coin.py)|Simple coin flip command.|
|[command.dice](./command/dice.py)|Simple dice roll command.|
|[command.session](./command/session.py)|Admin only command to manage sessions in other channels.|
|[command.list](./command/list.py)|Command for listing users in channels.|
|[command.math](./command/math.py)|Command for evaluating math expressions with [numexpr](https://github.com/pydata/numexpr).|
|[command.mathjs](./command/mathjs.py)|Command for evaluating math expressions with [mathjs.org](https://mathjs.org).|

Module groups:
|Modules|Description|
|--|--|
|[command.afk](./command/afk.py)<br/>[whisper.afk](./whisper/afk.py)<br/>[message.afk_check](./message/afk_check.py)|Modules that manage AFK statuses of users.|
|[command.scramble](./command/scramble.py)<br/>[message.scramble_check](./message/scramble_check.py)|Modules that manage a word scramble game.|
