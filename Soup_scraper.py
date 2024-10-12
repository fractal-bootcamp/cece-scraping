import requests
from bs4 import BeautifulSoup

# setup basic structure to fetch color hunt website -- 
def scraper_color():
    url= "https://colorhunt.co/"
    response = requests.get(url)

# create a BeautifulSoup object to parse through the site 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

    
        # find all the color palette elements 
        palette_elements = soup.find_all('div', class_='item')
       
        for palette in palette_elements[:5]: # loop through first five palettes
            print(palette)
        # extract color codes 
            color_divs = palette.find_all('div', class_='palette') # within each palette find each individual color 
        # loop through color_divs and create list of color codes for the palette 
        #     color_codes = [div[''] for div in color_divs] # extract the color codes from attribute of each color div 
        # # need to inspect elements of the dev tools to get exact name of HEX variable 

        # # extract likes count 
        # # find <span> extract its contents 
        #     likes = palette.find('div', class_='flex').text.strip()

        # find and extract color data - print 
            print("successfully fetched colors")
            # print(f"Colors: {', '.join(color_codes)}")
            # print(f"Likes: {likes}")

    else:
            print(f"no color soup for you status: {response.status_code}")

if __name__ == "__main__":
    scraper_color()
