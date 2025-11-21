import random

# List of sports trivia facts
trivia_facts = [
    "The Pittsburgh Penguins were founded in 1967 as part of the NHL expansion.",
    "Mario Lemieux saved the Penguins from bankruptcy twice — as a player and later as owner.",
    "Sidney Crosby was drafted first overall by the Penguins in 2005.",
    "The Penguins won back-to-back Stanley Cups in 2016 and 2017.",
    "Evgeni Malkin won the Conn Smythe Trophy in 2009.",
    "The Penguins have won five Stanley Cups: 1991, 1992, 2009, 2016, and 2017.",
    "Marc-André Fleury was the first overall pick in the 2003 NHL Draft.",
    "The Penguins moved to PPG Paints Arena (formerly Consol Energy Center) in 2010.",
    "Kris Letang has spent his entire NHL career with the Penguins.",
    "Mario Lemieux scored 8 points in a single playoff game in 1988, tying an NHL record.",
    "The Pittsburgh Steelers were founded in 1933 and were originally named the Pittsburgh Pirates.",
    "The Steelers have won six Super Bowls, tied for the most in NFL history.",
    "The 'Steel Curtain' defense dominated the NFL in the 1970s.",
    "Terry Bradshaw won four Super Bowls as the Steelers' quarterback.",
    "Franco Harris' 'Immaculate Reception' in 1972 is considered the greatest play in NFL history.",
    "Mike Tomlin has never had a losing season since becoming the Steelers' head coach in 2007.",
    "Ben Roethlisberger holds nearly every major Steelers passing record.",
    "The Steelers' Terrible Towel was created by broadcaster Myron Cope in 1975.",
    "Troy Polamalu was inducted into the Pro Football Hall of Fame in 2020.",
    "Heinz Field opened in 2001 and became Acrisure Stadium in 2022.",
]


def get_random_trivia():
    return random.choice(trivia_facts)


def main():
    print("🏆 Random Sports Trivia Generator 🏆")
    print("-----------------------------------")
    print(f"Trivia of the day:\n{get_random_trivia()}")


if __name__ == "__main__":
    main()
