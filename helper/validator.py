import datetime


class Validator:
    @staticmethod
    def validate(data: dict, rules: dict, name: dict) -> str:
        for key, rule_list in rules.items():
            value = data.get(key, None)
            for rule in rule_list:
                error_message = rule(value)
                if error_message:
                    return f"{name[key]}: {error_message}"
        return None

    @staticmethod
    def max_length(max_length: int):
        def validate(value: str) -> str:
            is_valid = len(value) <= max_length
            if not is_valid:
                return f"Panjang karakter maksimal {max_length}"

        return validate

    @staticmethod
    def min_length(min_length: int):
        def validate(value: str) -> str:
            is_valid = len(value) >= min_length
            if not is_valid:
                return f"Panjang karakter minimal {min_length}"

        return validate

    @staticmethod
    def length(length: int):
        def validate(value: str) -> str:
            is_valid = len(value) == length
            if not is_valid:
                return f"Panjang karakter harus {length}"

        return validate

    @staticmethod
    def required(value: str) -> str:
        is_valid = value != ""
        if not is_valid:
            return "tidak boleh kosong!"

    @staticmethod
    def positive_integer(value: str) -> str:
        try:
            is_valid = int(value) > 0
            if not is_valid:
                return "harus bilangan bulat positif!"
        except ValueError:
            return "harus berupa angka!"

    @staticmethod
    def numeric(value: str) -> str:
        try:
            int(value)
            return None
        except ValueError:
            return "harus berupa angka!"

    @staticmethod
    def decimal(value: str) -> str:
        try:
            float(value)
            return None
        except ValueError:
            return "harus berupa angka desimal!"
