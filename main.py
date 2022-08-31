from venv import create
# from etl import web_scraping_booklist
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
from settings.toml_config import config
from sql.create_tables import create_tables

# driver = webdriver.Chrome(ChromeDriverManager().install())

# web_scraping_booklist(driver)

create_tables(config)