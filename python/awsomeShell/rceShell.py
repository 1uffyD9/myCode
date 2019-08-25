from cmd import Cmd
from colored import fg, bg, attr, stylize
import sys

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print "Hello, %s" % name

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit



if __name__ == '__main__':
    prompt = MyPrompt()

    ## Colors ############

    starting = fg("green") + attr("bold")
    error = fg("red")
    promptColor = fg(220) + attr(1)
    promptArrow = fg(70) + attr(1)


    prompt.prompt = stylize("luffy-lfi",promptColor) + stylize("> ", promptArrow)
    
    try:
        prompt.cmdloop(stylize("Starting prompt for LFI...", starting))
    except KeyboardInterrupt:
        print(stylize("\nGot keyboard interrupt. Exiting...",error))
        sys.exit(0)
