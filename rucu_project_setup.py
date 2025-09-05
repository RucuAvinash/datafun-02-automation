"""
File: rucu_project_setup.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Rucmani Sethu

"""

###########################
# Import external Python Libraries
###########################

import pathlib
import loguru
import sys
import datetime
import time

###########################
# Import Local modules
###########################
import utils_rucu_1

###########################
# CONFIGURE LOGGER AND VERIFY
###########################

logger = loguru.logger
logger.remove()  
logger.add("project.log", level="INFO", rotation="100 KB")
logger.add(sys.stdout, level="INFO")  # Add this line
logger.info("Logger Loaded.")


#############################
# DECLARE GLOBAL VARIABLES
#############################

base_path = 'C:/Users/rucma/OneDrive/Desktop'
path = pathlib.Path(base_path)

################################
# DEFINE FUNCTION : CHECK IF BASE_PATH IS A DIRECTORY:
# CREATE A FUNCTION TO CREATE FOLDER IF BASE PATH IS A DIRECTORY
# PASS IN STRING AS PARAM TO HOLD FOLDER NAME

def create_folder(folder_name: str)  -> None:
    if path.is_dir():
      new_folder_path = path/folder_name   # Create the Path
      new_folder_path.mkdir(exist_ok= True) #make a directory and if a dir already exists do not display error
      logger.info(f"Folder'{new_folder_path}' created successfully.")
    else:
      loguru.info("Path is not a directory")


#########################################################################################
# DEFINE FUNCTION 2 : ITERATES NUMBER LIST AND CREATES FOLDER IF NUMBER IN LIST IS EVEN
# CREATE A FUNCTION TO CREATE A FOLDER IF BASE PATH IS A DIRECTORY
# PASS IN INTEGER AS A PARAMETER TO HOLD LIST OF NUMBERS
###########################################################################################

def create_even_folder(number:list) -> None:
    for n in number:
        if n%2==0:
            new_folder_path = path/str(n)
            new_folder_path.mkdir(exist_ok=True)
            logger.info(f"Folder{new_folder_path}created successfully")
        else:
            logger.info(f"Folder not created as {n} is an odd number")

###########################################################################
# DEFINE FUNCTION 3. ITERATES NUMBER LIST AND CREATES FOLDER IF FOLDER NAME IS PALINDROME
# CREATE A FUNCTION TO CREATE FOLDER IF BASE PATH IS A DIRECTORY
# PASS IN A STRING AS PARAM TO HOLD FOLDER NAME

def create_folder_if_palindrome(folder_list: list) -> None:
    for name in folder_list:
        clean_name = name.replace(" " ,"").lower()
        if clean_name==clean_name[::-1]:
           logger.info(f"'{folder_list}' is a palindrome.Creating folder.")
           new_folder_path = path/name
           new_folder_path.mkdir(exist_ok=True)
           logger.info(f"Palindrome folder'{new_folder_path}' created successfully.")
        else:
            logger.info(f"'{name} is not a Palindrome.Skipping.")

#################################################################################################
# DEFINE FUNCTION 4 : WHILE LOOP
# WRITE A FUNCTION TO CREATE FOLDERS PERIODICALLY (EVERY 5 SECONDS FOR 5 ITERATIONS FROM (0-4))
################################################################################################


def create_periodic_folder(duration: int)  -> None:
    iteration = 5
    counter = 0 
    while counter < iteration :
        utc_time = datetime.datetime.now(datetime.timezone.utc)
        #FORMAT THE TIME TO HUMAN READING STRING
        #%Y: YEAR WITH CENTURY(eg: 2023)
        #%m: MONTH AS ZERO PADDED NUMBER (eg: 01)
        #%d: DAY OF THE MONTH( eg:27)
        #%H: HOUR (24- HOUR CLOCK)
        #%M: MINUTE
        #%S: SECOND
        #%Z: TIMEZONE NAME

        human_readable_time = utc_time.strftime("%Y-%m-%d-%H-%M-%S-%Z")
        folder_name = f"periodic - {human_readable_time}-{counter}"

        new_folder_path = path/folder_name
        new_folder_path.mkdir(exist_ok=True)
        logger.info(f" Created folder with {folder_name}")

        counter +=1

        if counter < iteration:
                logger.info(f"Sleeping {duration} seconds before next folder...")
                time.sleep(duration)

###########################################
# Define a main() function for this module.
###########################################

def main() -> None:
        "Main function to demonstrate module capabilities."
        logger.info('########################################')
        logger.info("#Starting execution of main")
        logger.info('##########################################')
        logger.info(f"Byline: {utils_rucu_1.get_byline()}")

# Call function to create a new folder if directory is a path
name = "Rucu_new_folder"
create_folder(folder_name = name)

# Call function to create folders if number is an even number
numbers = [1,2,3,4]
create_even_folder(numbers)

# Call function to create folder if name is a Palindrome
name = ["MOM","Rucu","MADAM"]
create_folder_if_palindrome(folder_list= name)

# Call function to create folder periodically
duration = 3
create_periodic_folder(duration = duration)


#####################################
# Conditional Execution
#####################################
  
if __name__ == "__main__":
    main()