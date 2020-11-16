from .colors import RESET_ALL, BOLD, REVERSE, BLINK, FG
import random


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
