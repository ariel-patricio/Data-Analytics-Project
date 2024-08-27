# Web Scraping using Selenium - Goat Online Shop

## Objectives: 

  - Data Extraction: Retrieve key product details such as link, product name, release date, price and retail price from various categories within the Goat Online Shop.
  - Data Organization: Structure the scraped data into a clean and organized format, suitable for analysis or integration with other systems.
  - Automation: Implement an automated scraping process to regularly update the product data, ensuring the information remains current.
  - Logging: Maintain logs to track the execution of the scraping process, capture any errors, and record the status of data collection.

<br/>

## Methodology: 

  1. Setup: Configure the web scraping environment using Python and relevant libraries, such as Selenium for dynamic content interaction and BeautifulSoup for HTML parsing.
  2. Scraping Process:
     1. Navigate through product pages and categories.
     2. Extract product attributes and details.
     3. Handle pagination and dynamic content loading.
  4. Data Storage: Save the collected data in a structured format (Excel) for easy access and further processing.
  5. Logging:
     1. Log Creation: Implement logging functionality to record the execution flow of the script, including start and end times, and the status of data collection.
     2. Error Logging: Capture and log any errors or exceptions encountered during the scraping process, such as network issues, element not found errors, or changes in page structure.
     3. Progress Tracking: Log the progress of data extraction, including the number of products scraped and any encountered issues.
  6. Error Handling: Implement robust error handling to manage issues such as missing elements, changes in page structure, or connectivity problems.


## Scope: 

This project aims to provide valuable insights and data-driven decisions by automating the extraction of key product information from the Goat Online Shop and ensuring the process is well-documented and monitored through detailed logging.

## Technology Used
Python, Selenium, Beautiful Soup, Pandas, and Openpyxl

