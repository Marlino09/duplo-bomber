# -*- coding: utf-8 -*-
import re


class CheckInput:
    def verification_phone(self, phone: str) -> str:
        self.phone = phone
        try:
            phone = re.sub("[^0-9]", "", phone)  # оставляет только цифры
            if phone.startswith("0"):
                phone = "38" + phone
                return phone
            elif phone == "" or phone == " ":
                print("\033[1;31m" + "Номер введён некорректно!\033[0m")
                exit()
            elif phone.startswith("+"):
                return phone[1:]
            else:
                return phone
        except Exception:
            print("\033[1;31m" + "Номер введён некорректно!\033[0m")
            exit()

    def verification_cycles(self, cycles: str) -> int:
        try:
            self.cycles = cycles
            cycles = re.sub("[^0-9]", "", cycles)
            return int(cycles)
        except ValueError:
            print("\033[1;31m" + "Неправильное кол-во циклов!")
            exit()


if __name__ == "__main__":
    phone = input("Введите номер телефона: ")
    cycles = input("Введите колличество циклов: ")
    print(CheckInput().verification_phone(phone))
    print(CheckInput().verification_cycles(cycles))
