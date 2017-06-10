import json
import utils
import sys

class Cli:
    def __init__(self, config_json):
        self.config = json.loads(utils.readLines(config_json))
        if len(sys.argv) <= 1:
            print self.__header_message(self.config["description"])
            print "Commands:\n"+self.__print_arguments()
        for i in range(1,len(sys.argv)):
            arg = sys.argv[i]
            if arg in self.config["args"]:
                self.config = self.config["args"][arg]
                if i+1 == len(sys.argv):
                    if "description" in self.config:
                        print self.__header_message(self.config["description"])
                if not self.config:
                    if len(sys.argv[1:]) > i:
                        print "Too much arguments!!"
                        sys.exit()
                    return
                else:
                    if i == len(sys.argv[1:]):
                        self.__insufficent_argument()
            else:
                self.__wrong_argument()

    def bcolor(self, color):
        colors = {
        "HEADER": '\033[95m',
        "OKBLUE": '\033[94m',
        "OKGREEN": '\033[92m',
        "WARNING": '\033[93m',
        "FAIL": '\033[91m',
        "ENDC": '\033[0m',
        "BOLD": '\033[1m',
        "UNDERLINE": '\033[4m'
        }
        return colors[color]

    def __print_arguments(self):
        msg = ""
        for arg in self.config["args"]:
            msg += "\t"+self.__warning_message(arg)+"\n"
        return msg

    def __header_message(self, message):
        return self.bcolor("HEADER") + message + self.bcolor("ENDC")

    def __fatal_message(self, message):
        return self.bcolor("FAIL") + self.bcolor("BOLD") + self.bcolor("UNDERLINE") + message + self.bcolor("ENDC") + self.bcolor("ENDC") + self.bcolor("ENDC")

    def __warning_message(self, message):
        return self.bcolor("WARNING") + message + self.bcolor("ENDC")

    def __ok_message(self, message):
        return self.bcolor("OKBLUE") + message + self.bcolor("ENDC")

    def __wrong_argument(self):
        print self.__fatal_message("Wrong argument!!")+"\n"+self.__warning_message("Permitted arguments:")
        print self.__print_arguments()
        sys.exit()

    def __insufficent_argument(self):
        print self.__fatal_message("Insufficent Arguments:")
        print self.__print_arguments()
        sys.exit()

Cli("cli.json")
