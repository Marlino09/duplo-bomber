from tools.colors import RESET_ALL
from tools.check_input import CheckInput
from tools.text import banner, cursor, replace
from send_requests import send_requests
import os


def clear_screen():
    return (
        os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    )


def main():
    clear_screen()
    print(banner, replace + "Введите номер телефона:" + RESET_ALL, sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(replace + "Введите колличество циклов:" + RESET_ALL)
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    if count >= 10:
        print(
            "\033[3;32m*Вы ввели больше 10 циклов, "
            "после 5-го скорость спама уменьшится" + RESET_ALL
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
