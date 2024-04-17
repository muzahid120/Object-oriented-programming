import logging
from datetime import datetime 
import os 

log_file =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"
log_path=os.path.join(os.getcwd(),'Logs',log_file)




os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,log_file)
format='%(asctime)s***%(lineno)d ***%(name)s***%(lavelname)s***%(message)s'

logging.basicConfig(format=format,level=logging.INFO,filename=log_file_path)