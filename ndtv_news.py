from playwright.sync_api import sync_playwright
import csv
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=True for silent run
    page = browser.new_page()
    page.goto("https://archives.ndtv.com/articles/2025-03.html", timeout=60000)

    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Headline", "Link"])

        for i in range(1, 10, 2):  # ui-id-1 to ui-id-9 (odd)
            try:
                header_selector = f"#ui-id-{i}"
                content_selector = f"#ui-id-{i + 1}"

                print(f"Clicking {header_selector}...")

                # Click and wait for dropdown to show
                page.click(header_selector)
                page.wait_for_selector(f"{content_selector} li a", timeout=10000)

                # Extract date from header
                date_elem = page.query_selector(f"{header_selector} a")
                if not date_elem:
                    print(f"No date link found in {header_selector}")
                    continue
                date = date_elem.inner_text().strip()
                print(f"Date: {date}")

                # Extract links
                links = page.query_selector_all(f"{content_selector} li a")
                print(f"Found {len(links)} headlines")

                for link in links:
                    headline = link.inner_text().strip()
                    href = link.get_attribute("href")
                    writer.writerow([date, headline, href])
                    print(f"[{date}] {headline} -> {href}")

                time.sleep(0.5)

            except Exception as e:
                print(f"Error processing dropdown #{i}: {e}")

    browser.close()
