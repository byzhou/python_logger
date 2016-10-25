import logging as lg
import sys
import argparse

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# Custom formatter
class MyFormatter(lg.Formatter):

    err_fmt  = bcolors.HEADER   + " %(asctime)s"        + bcolors.ENDC +\
                bcolors.FAIL    + " [%(levelname)s] "   + bcolors.ENDC +\
                bcolors.WARNING + " %(message)s "       + bcolors.ENDC +\
                bcolors.OKBLUE  + "(%(filename)s"       + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(funcName)s"    + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(lineno)s)"     + bcolors.ENDC 
    dbg_fmt  = bcolors.HEADER   + " %(asctime)s"        + bcolors.ENDC +\
                bcolors.OKGREEN + " [%(levelname)s] "   + bcolors.ENDC +\
                bcolors.WARNING + " %(message)s "       + bcolors.ENDC +\
                bcolors.OKBLUE  + "(%(filename)s"       + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(funcName)s"    + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(lineno)s)"     + bcolors.ENDC
    info_fmt = bcolors.HEADER   + " %(asctime)s"        + bcolors.ENDC +\
                bcolors.HEADER  + " [%(levelname)s] "   + bcolors.ENDC +\
                bcolors.WARNING + " %(message)s "       + bcolors.ENDC +\
                bcolors.OKBLUE  + " (%(filename)s"      + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(funcName)s"    + bcolors.ENDC +\
                bcolors.OKBLUE  + " :: %(lineno)s)"     + bcolors.ENDC 


    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        lg.Formatter.__init__(self, fmt)


    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == lg.DEBUG:
            self._fmt = MyFormatter.dbg_fmt

        elif record.levelno == lg.INFO:
            self._fmt = MyFormatter.info_fmt

        elif record.levelno == lg.ERROR:
            self._fmt = MyFormatter.err_fmt

        # Call the original formatter class to do the grunt work
        result = lg.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._fmt = format_orig

        return result

def set_up_formatter(log_level=lg.INFO):
    fmt = MyFormatter()
    hdlr = lg.StreamHandler(sys.stdout)

    hdlr.setFormatter(fmt)
    lg.root.addHandler(hdlr)
    lg.root.setLevel(log_level)

def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug",
        help="Print all the Debugging, info, error logs",
        action="store_const", dest="loglevel", const=lg.DEBUG,
        default=lg.WARNING,
    )
    parser.add_argument(
        "-i", "--info",
        help="Print all the info, error logs",
        action="store_const", dest="loglevel", const=lg.INFO,
        default=lg.WARNING,
    )
    parser.add_argument(
        "-e", "--error",
        help="Print all the error logs",
        action="store_const", dest="loglevel", const=lg.ERROR,
        default=lg.WARNING,
    )
    parser.add_argument(
        "-v", "--verbose",
        help="Be verbose",
        action="store_const", dest="loglevel", const=lg.INFO,
    )
    args = parser.parse_args()    
    set_up_formatter(args.loglevel)

if __name__ == "__main__":
    set_up_parser()
