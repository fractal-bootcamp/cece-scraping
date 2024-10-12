from playwright.sync_api import sync_playwright

def scraper(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://colorhunt.co/")

    # Wait for the content to load
    page.wait_for_selector('div.feed.global')

    # Extract color palette information
    palettes = page.query_selector_all('.item:not(.hide)')
    
    for palette in palettes[:5]:  # Let's look at the first 5 palettes
        color_spans = palette.query_selector_all('.place span[data-copy]')
        color_codes = [span.get_attribute('data-copy') for span in color_spans]
        
        # Get palette code (unique identifier)
        palette_code = palette.get_attribute('data-code')
        
        print(f"Palette Code: {palette_code}")
        print(f"Colors: {', '.join(color_codes)}")
        print("---")

    browser.close()

with sync_playwright() as playwright:
    scraper(playwright)