from config import *

def starting_log():
    logging.basicConfig(filename="my-logfile.log", 
                        format="%(asctime)s - %(name)s - %(message)s", 
                        filemode="w", level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    
def logger(fun):
    def wrapper(*args, **kwargs):
        starting_log()
        fun(*args, **kwargs)
        logging.shutdown()
    return wrapper






    