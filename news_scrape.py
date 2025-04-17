from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import csv 
import time 
import random
import os

page_counter = 1  # Start from page 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US",
        storage_state="auth.json"  # Load saved session
    )

    page = context.new_page()
    stealth_sync(page)  # Apply stealth settings 

    # Open file and write headers once
    with open("news_data.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["headline", "label", "link"])

        while True:
            print(f"Currently on page {page_counter}")
            page.goto(f"https://www.thehindu.com/archive/web/2025/03/28/?page={page_counter}")
            page.wait_for_load_state("networkidle")

            # Extract news articles
            articles = page.locator("div.element")
            count = articles.count()

            for i in range(count):
                try:
                    element = articles.nth(i)
                    label = element.locator("div.label").inner_text()
                    headline = element.locator("div.title a").inner_text()
                    link = element.locator("div.title a").get_attribute("href")
                    writer.writerow([headline, label, link])
                except Exception as e:
                    print(f"Error extracting article {i} on page {page_counter}: {e}")

            # Check if next page exists
            next_page_number = str(page_counter + 1)
            next_button = page.locator(f'a.page-link:text("{next_page_number}")')

            if next_button.count() > 0:
                time.sleep(random.uniform(1, 2))  # Simulate human-like delay
                next_button.click()
                page.wait_for_load_state("networkidle")
                page_counter += 1
            else:
                print("No more pages.")
                break

    browser.close()
