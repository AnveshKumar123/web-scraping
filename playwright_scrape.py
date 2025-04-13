from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError
import csv

####### FOR EXTRACTING ALL or TOP K pages QUOTES ( query selector )
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     page.goto("https://quotes.toscrape.com")
#     quote_count=0

    # with open("top3quotes.csv", "w", newline='', encoding="utf-8") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Quote", "Author", "Tags"])
    #     pagecount=0
    #     while True:
    #         quotes = page.query_selector_all(".quote")
    #         for quote in quotes:
    #             text = quote.query_selector(".text").inner_text()
    #             author = quote.query_selector(".author").inner_text()
    #             tags = ", ".join([tag.inner_text() for tag in quote.query_selector_all(".tag")])
    #             writer.writerow([text, author, tags])
    #             quote_count+=1

    #         # Pagination logic
    #         next_btn = page.query_selector(".next > a")
    #         if next_btn and pagecount<3:
    #             next_btn.click()
    #             pagecount+=1
    #             page.wait_for_load_state("networkidle")
    #         else:
    #             break
    # print(quote_count)
    # browser.close()



###### FOR GOING TO LOGIN PAGE AND LOGGING (locator , fill and click )

# def attempt_login(page, username, password):
#     page.goto("http://quotes.toscrape.com/login", wait_until="networkidle")
    
#     username_input=page.locator("text=Username")
#     password_input=page.locator("text=Password")
#     submit_btn = page.locator("input[type='submit']")

#     username_input.fill(username)
#     password_input.fill(password)
#     submit_btn.click()

#     #page.wait_for_load_sta
#     try:
#         page.wait_for_selector("a[href='/logout']", timeout=2000)
#         return True
#     except TimeoutError:
#         return False

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     # Keep trying until successful login
#     while True:
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         success = attempt_login(page, username, password)
#         if success:
#             print("✅ Login successful!")
#             break
#         else:
#             print("❌ Login failed. Please try again.")

#     # After login, print first quote
#     quote = page.locator(".quote .text").first.inner_text()
#     print("First quote:", quote)

#     browser.close()


    
