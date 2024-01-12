import logging,os,time
from config.config import Config


class Logger:

    def __init__(self,logger:str) -> None:
        if not os.path.exists(Config.logs_dir):
            os.mkdir(Config.logs_dir)

        #Create a logger
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
        self.logger=logging.getLogger(logger)
        #self.logger.propagate = False
        #self.logger.setLevel(logging.DEBUG)

        #Create a file handler to write log file
        wd = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        #log_file=os.path.join(log_path,'%s.log' %wd)
        log_file=Config.logs_dir+'\\'+logger+wd+'.log'
        fh=logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)

        # Create a console handler to write log file
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.INFO)

        #Define the format of log
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        #Add handler to logger
        self.logger.addHandler(fh)
        #self.logger.addHandler(ch)

    def getlog(self) -> logging.Logger:
        return self.logger

    def write_log(self,level:str,message:str) -> None:
        key=level.lower()
        self.logger.__getattribute__(key)(message)

if __name__ == '__main__':

    loger=Logger('mylog').getlog()
    print(type(loger))
    loger.debug("This is a debug log")
    loger.info("This is an info log")
    loger.warning("This is a warning log")
    loger.error("This is an error log")
    loger.critical("This is a critical log")

    l1=Logger('testlog')
    l1.write_log('debug','debug log')
    l1.write_log('INFO', 'info log')









