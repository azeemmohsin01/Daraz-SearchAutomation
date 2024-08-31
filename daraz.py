# Required imports form selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Type what you want to search on Daraz.pk
query = input('Enter what you want to search: ')

# filter product page with respect to price
user_choice = int(input('Type 1 if you want to search price low to high or 2 for vice versa: '))

# Daraz url
url = 'https://www.daraz.pk/#?'

# Open a new chrome empty tab
driver = webdriver.Chrome()

# Redirect to daraz website
driver.get(url)

# Navigate to search bar using xpath
search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]')

# Sending user query to search bar
search_bar.send_keys(query)

# Pressing search button
search_bar.send_keys(Keys.RETURN)

# Selecting dropdown to filter the search according to the prices
drop_down = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/span[2]/div')

# Clicking the dropdown to select the available price options
drop_down.click()

# Navigating to low to high price and storing it to low_to_high variable
low_to_high = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/div/div/div/div[2]/div/div')

# Navigating to high to low price and storing it to hight_to_low variable
hight_to_low = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div[2]/div/div/div/div[3]/div/div')

# Checking if user wants low_to_high price                                            
if user_choice == 1:

    # Clicking on the user choice
    low_to_high.click()

# Checking if user wants high_to_low price     
elif user_choice == 2:

    # Clicking on the user choice
    hight_to_low.click()

# Showing invalid number if user didn't type the correct number 
else:
    print('Invalid Number')
