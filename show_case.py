import logging as lg


if __name__ == "__main__":

    from log_style import *
    set_up_parser()

    lg.debug("Hi, this is a bug!")
    lg.error("Hi, there is an error!")
    lg.info("Hi, some info!")
