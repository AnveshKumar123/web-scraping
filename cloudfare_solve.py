from playwright.sync_api import sync_playwright
import time
import random

def human_like_mouse_movements(page):
    # Random mouse movement around the page
    for _ in range(random.randint(5, 10)):
        x = random.randint(100, 1000)
        y = random.randint(100, 700)
        page.mouse.move(x, y, steps=random.randint(10, 25))
        time.sleep(random.uniform(0.1, 0.5))

def human_scroll(page):
    # Simulate scrolling
    for _ in range(5):
        scroll_by = random.randint(100, 400)
        page.mouse.wheel(0, scroll_by)
        time.sleep(random.uniform(0.2, 0.5))

def random_hover(page):
    # Hover over a few elements
    elements = page.locator("a")
    count = min(elements.count(), 5)
    for i in range(count):
        try:
            el = elements.nth(i)
            el.hover()
            time.sleep(random.uniform(0.3, 0.6))
        except:
            continue

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US"
    )
    page = context.new_page()
    page.goto("https://www.thehindu.com/archive/web/2025/03/28/?page=1")

    # Human-like behavior before solving CAPTCHA
    time.sleep(random.uniform(2, 4))
    human_like_mouse_movements(page)
    human_scroll(page)
    random_hover(page)

    print("👉 Please solve the CAPTCHA manually if it shows up...")
    input("✅ Press Enter *after* you're fully inside and see content...")

    # Save authenticated session
    context.storage_state(path="auth.json")
    browser.close()