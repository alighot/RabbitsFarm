import os


class View:
    def show(self, map, date, rabbit_location, carrot_location, rabbits_number, carrots_number, exception=''):
        for y in map:
            for x in y:
                print(x, end="")
            print("")
        print(f"""Stats:
                  date: {date}
                  number of rabbits: {rabbits_number}       number of carrots: {carrots_number}
                  last rabbit: {rabbit_location}      last carrot: {carrot_location}
                  exceptions: {exception}""")

    def show_preview(self, date, rabbits_number, carrots_number):
        print(f"""Stats:
            date: {date}
            number of rabbits: {rabbits_number}     number of carrots: {carrots_number}""")

    @staticmethod
    def clear():
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')
