from dataclasses import dataclass
from saa.luga import Luga


@dataclass
class English(Luga):
    time = {
        "to": "{minute} minutes to {hour}",
        "past": "{minute} minutes past {hour}",
        0: "{hour} o'clock",
        15: "quorter past {hour}",
        45: "quorter to {hour}",
        30: "half past {hour}",
    }
    number_connector = "and"
    connect_format = "{0} {2}"
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eightteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str]:
      
      
      is_to = "to" if minute > 30 else "past"

      if hour > 12:
          hour = hour - 12
            
      if is_to == "to":
          hour += 1
          minute = 60 - minute
      
      return hour, minute, is_to 