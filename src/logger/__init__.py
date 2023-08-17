import logging
import os, sys
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
#getcwd find the current working directory
#created the directory and joined it

os.makedirs(LOG_DIR,exist_ok=True)

#the extension should be .log
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%y_%m_%d_%H_%M_%S')}"
file_name=f"log_{CURRENT_TIME_STAMP}.log"
# created the file with the current time stamp

log_file_path=os.path.join(LOG_DIR,file_name)
#saving the the log file in the created path

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

