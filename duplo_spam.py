from tools.check_input import CheckInput
from tools.text import banner, cursor, clear, replace
from send_requests import send_requests
import os


def clear_screen(): return os.system(
    "cls") if os.sys.platform == "win32" else os.system("clear")


def main():
    clear_screen()
    print(banner, f"{replace}Введите номер телефона:{clear}", sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(f"{replace}Введите колличество циклов:{clear}")
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    print(
        """\033[3;32m*Если вы ввели больше 10 циклов,
        то после 5-го скорость спама уменьшится\033[0m"""
    )
    send_requests(phone, count)
    clear_screen()
    print(
        "\033[1;32mГотово!",
        f"Телефон: \033[35m{phone}\033[1;32m",
        f"Колличество циклов: \033[35m{count}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
