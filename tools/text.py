import random

from .colors import BLINK, BOLD, FG, RESET_ALL, REVERSE

colors = random.choice(
    [FG.green, FG.orange, FG.blue, FG.purple, FG.cyan, FG.yellow, FG.pink]
)
replace = REVERSE + colors
banner = (
    BLINK
    + f"""{colors}
 █▀▄ █░█ █▀▄ █░░ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█
 █░█ █░█ █░█ █░▄ █░█ ░▀▄ █░█ █▀█ █░█░█
 ▀▀░ ░▀░ █▀░ ▀▀▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀
{RESET_ALL}"""
)

cursor = BOLD + f"{colors}d.hack >> "
