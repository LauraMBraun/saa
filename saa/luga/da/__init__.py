from dataclasses import dataclass


@dataclass
class Danish:
    time = {
        "to": "{minute} minutter i {hour}",
        "past": "{minute} minutter over {hour}",
        0: "klokken {hour}",
        15: "kvart over {hour}",
        45: "kvart i {hour}",
        30: "halv {hour}",
    }

    number_connector = "og"
    connect_format = "{2}{1}{0}"
    numbers = {
        0: "nul",
        1: "en",
        2: "to",
        3: "tre",
        4: "fire",
        5: "fem",
        6: "seks",
        7: "syv",
        8: "otte",
        9: "ni",
        10: "ti",
        11: "elleve",
        12: "tolv",
        13: "tretten",
        14: "fjorten",
        15: "femten",
        16: "seksten",
        17: "sytten",
        18: "atten",
        19: "nitten",
        20: "tyve",
        30: "tredive",
        40: "fyrre",
        50: "halvtreds",
    }

  

