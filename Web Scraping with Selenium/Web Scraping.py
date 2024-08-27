from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import logging
import datetime
import os
import time


def log_file_configuration():
    """This function configures logging to write log messages for our web scraping script."""
    try:
        # Check if there's an existing Logs folder in the working directory, if false, the code automatically create a new folder named "Logs"
        if not ("Logs" in os.listdir()):
            os.mkdir("Logs")

        # Create the file name for the log of the execution (Example: 2024-08-25 10:32 Log file.log)
        file_name = datetime.datetime.today().strftime("%Y-%m-%d %H-%M") + " Log file"

        logger.setLevel(logging.INFO)  # Set the minimum level of messages to log

        # Create handlers
        file_handler = logging.FileHandler("./Logs/" + file_name)
        console_handler = logging.StreamHandler()

        # Set the level for handlers (optional, file_handler level can be different from logger level)
        file_handler.setLevel(logging.INFO)
        console_handler.setLevel(logging.WARNING)

        # Create formatters and set them for handlers
        formatter = logging.Formatter("%(name)s - %(levelname)s : %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.info("Function: log_file_configuration() ---- START")
        logger.info("Configuration of the log file was successful.")
        logger.info("File name : {}".format(str(file_name)))
    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: log_file_configuration() ---- END")


def selenium_chrome_web_config():
    """This function configures and returns a Selenium Chrome WebDriver instance

    Returns:
        webdriver.Chrome: A configured Chrome WebDriver instance.
    """
    try:
        logger.info("Function: selenium_chrome_web_config() ---- START")
        logger.info("Configuration of the selenium web driver will now start")
        # Configuration of the web driver so that it will not automatically close
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--incognito")

        logger.info("Configuration of the selenium web driver was successful")
        
        # This line of code doesn't need a a local web driver file.
        return webdriver.Chrome(options=options)

    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: selenium_chrome_web_config() ---- END")


def grid_data_div_parser(element):
    """Parses and extracts data from a given HTML element representing a grid data cell.

        This function takes an HTML element as input, which is expected to contain data within a grid structure.
    It extracts relevant information from the element's attributes and child elements and returns a structured
    representation of the data.

    Args:
        element (Selenium.find_element.get_attribute()): The HTML element to be parsed, typically representing a grid cell.
            This element is expected to have specific attributes and child elements containing the data to be extracted.

    Returns:
        List: A list containing all the div thath have an attribute of data-grid-cell-position
    """
    try:
        logger.info("Function: grid_data_div_parser() ---- START")
        
        logger.info("Parsing of data in the extracted HTML element will now start.")

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(element, "html.parser")

        # Find all div elements with "data-qa" attributes
        divs_with_data_qa = soup.find_all(
            "div", attrs={"data-grid-cell-position": True}
        )
        
        logger.info("Parsing the <div> element with attributte of 'data-grid-cell-position'")
        logger.info("{}".format(str(divs_with_data_qa)))
        
        return divs_with_data_qa

    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: grid_data_div_parser() ---- END")

    """This function configures and returns a Selenium Chrome WebDriver instance

    Returns:
        webdriver.Chrome: A configured Chrome WebDriver instance.
    """
    try:
        logger.info("Function: selenium_chrome_web_config() ---- START")

        # Configuration of the web driver so that it will not automatically close
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--incognito")

        # This line of code doesn't need a a local web driver file.
        return webdriver.Chrome(options=options)

    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: selenium_chrome_web_config() ---- END")


def value_checking_for_string(value):
    """Checks the provided value and returns it if it is not None; otherwise, returns an empty string.

    This function is used to ensure that a value is returned as a non-null string. If the input value is None,
    the function returns an empty string. If the input value is not None, the function returns the original value.

    Args:
        value (str or None): The value to check. It can be a string or None.

    Returns:
        str: The original value if it is not None; an empty string if the value is None.
    """
    try:
        logger.info("Function: value_checking_for_string() ---- START")
        logger.info("Checking the value is valid : {}".format(value))
        
        # Return a blank value if the value is None, else the actual value
        return (value.text.strip() if value is not None else "")

    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: value_checking_for_string() ---- END")


def value_checking_for_amount(value):
    """Checks the provided value and returns it if it is not None; otherwise, returns a default value of $0.

    This function is used to ensure that a value is returned as a non-null string. If the input value is None,
    the function returns a default value of $0. If the input value is not None, the function returns the original value.

    Args:
        value (str or None): The value to check. It can be a string or None.

    Returns:
        str: The original value if it is not None; an empty string if the value is None.
    """
    try:
        logger.info("Function: value_checking_for_amount() ---- START")
        logger.info("Checking the value is valid : {}".format(value))
        
        # Return a default $0 value if the value is None, else the actual value
        return (value.text.strip() if value is not None else "$0")

    except Exception as error_message:
        logger.error(error_message)

    finally:
        logger.info("Function: value_checking_for_amount() ---- END")


def scraping_main_function():
    """Main function for scraping data from a specified website and saving it to an output file (Excel).
    This function is responsible for initializing the web scraping process, including setting up the web driver,
    navigating to the target URL, extracting data from the web page, and saving the scraped data to the specified output file (Excel).
    """
    try:
        log_file_configuration()

        # Assign the instance of the selenium web driver to the driver variable
        driver = selenium_chrome_web_config()
        logger.info("Function: scraping_main_function() ---- START")

        # Initialize the doamin name and the pathe for the target website
        target_url = "https://www.goat.com"
        param = "/sneakers"

        # Open the target website
        driver.get(target_url + param)
        logger.info("Web data scraping will now start. The target web page is {}".format(target_url + param))

        # Wait for 5 seconds to execute the next process
        time.sleep(5)

        """The try-except construct in this script checks for the presence of a cookie consent prompt on the website. 
        If the script does not encounter an error and proceeds to the subsequent line, it confirms the existence of the prompt. 
        Consequently, the script will automatically interact with the 'Reject All' button to refuse all cookies.
        """
        try:
            # Check if there's a cookie banner
            logger.info("The script is now checking if the cookie banner exists.")
            driver.find_element(By.XPATH, '//*[@id="onetrust-banner-sdk"]')

            # The 'Reject All' button will be click and proceed with the next process.
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
                )
            ).click()
            logger.info("The 'Reject All' button was clicked.")
        except:
            logging.warning(
                "Warning: Unable to find the element associated with the cookie banner. The script will now proceed to the next process."
            )

        logger.info("The script will now execute the scrolling of the page.")
        # The webpage will scroll n times to get more items in the website
        for scroll_number in range(0, 5):
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        logger.info("Extracting the HTML element of the products.")
        # Get the innerHTML attribute of the whole grid data (list of products) after reaching the max number of scroll.
        element_of_products = driver.find_element(
            By.XPATH, '//*[@id="grid-body"]/div'
        ).get_attribute("innerHTML")
        logger.info("Extracted HTML element of the producsts\n. {}".format(str(element_of_products)))

        # Call the grid_data_div_parser function to process the 'innerHTML' attribute of each <div> element.
        # This function will return a list of <div> elements that meet the specified filter criteria.
        extracted_div_list = grid_data_div_parser(element_of_products)

        # Initialize an empty list to store collected data.
        # This list will become a 2D list after further processing.
        list_of_products = []

        # Iterate through the collected list of divs_with_qa
        logger.info("The script will now iterate over the list of products to extract and collect the data contained within each item.")
        for grid_div in extracted_div_list:
            logger.info("\n")
            # Get the <a> child element
            child_a_data = grid_div.find_all("a")

            # Iniailize a list for the product data.
            # The content of the list will be [Url, Product Name, Release Date, Product Price, Retail Price]
            temp_product_data = [
                target_url + child_a_data[0].get("href").strip(),
                value_checking_for_string(
                    child_a_data[0].find("div", {"data-qa": "grid_cell_product_name"})
                ),
                value_checking_for_string(
                    child_a_data[0].find(
                        "div", {"data-qa": "grid_cell_product_release_date"}
                    )
                ),
                value_checking_for_amount(
                    child_a_data[0].find("div", {"data-qa": "grid_cell_product_price"})
                ),
                value_checking_for_amount(
                    child_a_data[0].find("div", {"data-qa": "grid_cell_retail_price"})
                ),
            ]
            
            logger.info("Collected data: {}".format(temp_product_data))

            # Append the collected product data to the list of products.
            list_of_products.append(temp_product_data)
            logger.info("Adding the collected data to the master list".format(temp_product_data))


        # Create a DataFrame based from the list of products
        products_df = pd.DataFrame(
            list_of_products,
            columns=[
                "URL Link",
                "Product Name",
                "Release Date",
                "Product Price",
                "Retail Price",
            ],
        )
        
        # Write the DataFrame to an Excel file
        products_df.to_excel('output.xlsx', index=False, sheet_name='Sneakers')

    except Exception as error_message:
        logger.error(error_message)
    finally:
        logger.info("Function: scraping_main_function() ---- END")


# Change the working directory from the default python folder to the working project folder
os.chdir(
    r"C:\Users\Sabonity\OneDrive\Projects\Python\Web Scraping with Selenium\GOAT Web Scraping"
)
# Initialize the get logger name for our log file content.
logger = logging.getLogger("Goat Web Scraping")

# Invoking the scraping_main_function function to start the web scraping script
scraping_main_function()