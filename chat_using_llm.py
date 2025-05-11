import asyncio
from playwright.async_api import async_playwright
from langchain_ollama.llms import OllamaLLM

# Initialize Ollama LLM (Mistral)
llm = OllamaLLM(model="mistral")


sample_chat=(
    "Here is a sample chat\n"
    "ok"
"You: girl or boy"
"Stranger: girl"
"You: cool"
"Stranger: you're alone or just simple talking?"
"You: what do you mean"
"Stranger: means you are ok if you are in a gf's body?"
"You: huh"
"Stranger: hahah"
"You: haven't brushed another girl"
"You: touched her during sleep"
"Stranger: but if I were in a girl's body, would be sick af"
"You: you are sick lol"
"Stranger: why"
"You: haha you're not a real nerd"
"Stranger: what do you mean?"
"You: touching a girl in sleep"
"You: you are not cool bro"
"Stranger: you think so?"
"You: yes"
"Stranger: lol, I am telling you, you must be better than me"
"Stranger: because the mind of men here is severely dry with imagination"
"You: stop jerking man in making relations"
"Stranger: not jerking"
"Stranger: just doing casuals"
"You: casual fun only"
"Stranger: yeah, some mental tweaks"
"You: bro, you need more sessions in anivity"
"Stranger: hahah ok"
"Stranger: I know many sessions"
"You: not functional level"
"Stranger: you too sound sick lol"
"You: I hope you find compassion in situations"
"Stranger: compassion?"
"You: yes"
"Stranger: I am bad at sympathy"
"You: you seem like it"
"Stranger: but still I care"
"You: why are you on here?"
"Stranger: idk"
"You: horny kid?"
"Stranger: nah"
"You: joke"
"Stranger: just Indian kids float over here"
"You: yeah"
"You: Indian kids flood"
"Stranger: you too?"
"You: probably"
"You: everyone is speaking rapidly"
"Stranger: except only those specific freaks that don't want to write long messages"
"You: sounds healthy bro"
"Stranger: ok"
"You: how's the mental space"
"Stranger: fine"
"You: have you ever been in a real one?"
"Stranger: with a real girl?"
"Stranger: probably"
"You: if your parents would ask to get married now"
"You: to a fully filtered someone"
"You: from a good or decent group in relationship"
"You: why not"
"Stranger: why not?"
"You: are you out?"
"Stranger: no"
"You: good to be introvert"
"Stranger: just selectively love people"
"You: valid and fine, shy boys get respect twice before the fall"
"Stranger: hahaha"
"Stranger: true that"
"You: makes more time"
"Stranger: I know"
"You: even nerds are in magic"
"You: even girls bring up character a while"
"You: you been kissed for a guy?"
"Stranger: no"
"Stranger: but I should"
"You: why not by now"
"Stranger: idk"
"You: what is ideal encounter?"
"Stranger: just a learned one"
"Stranger: which has some context & not before even I could judge a second right"
"You: good"
"You: not like"
"You: but rather even some body, sometimes"
"You: true"
"Stranger: I just like sweet internal liking a woman who teaches me something"
"You: same"
"You: so nobody has been into a girl even when I had all things to give back to it"
"You: selfless love not a tool"
"Stranger: exactly"
"Stranger: preach"
"You: too sassy?"
"Stranger: this thought happens in movies only :P"
"You: too kind"
"Stranger: so then what's the deal with the intellectuals"
"You: just challenges"
"Stranger: maybe happens the first must not be love"
"Stranger: that's truth"
"You: needs time even slowfalling"
"Stranger: exactly"
"Stranger: one could love a profile from yesterday"
"You: not good unless it's real"
"You: you must be on side of real"
"You: you done open relationships?"
"Stranger: probably not"
"You: good thing bro"
"Stranger: too weird for marriage"
"You: you thinking abt it"
"You: ever done a life list?"
"You: things you wanna do before marriage"
"Stranger: yes"
"You: like"
"Stranger: be an artist"
"You: good"
"Stranger: you aren't too young for marriage"
"You: I am just 21"
"Stranger: you will marry at 23?"
"You: if I get an internal yes someday"
"Stranger: when"
"Stranger: when she comes"
"You: you'll get married?"
"Stranger: idk"
"You: but traditional ones most Indian women want"
"Stranger: some"

)

# Personality prompt
system_prompt = (
    "use sample chat as a reference "
    "answer taking chat history into account "
    "strictly dont act as ai be as human as possible"
    "You're chatting as a 20-year-old Indian guy. "
    "Be cool, casual "
    "Use simple language "
    "answer in short 5-8 words and dont use emojis and punctuations strictly"
)

# Conversation history
conversation_history = []
MAX_TURNS = 6

# Format prompt
def build_prompt(new_message: str) -> str:
    history_text = "\n".join(
        [f"Stranger: {u}\nYou: {b}" for u, b in conversation_history]
    )
    return f"{sample_chat}\n{system_prompt}\n{history_text}\nStranger: {new_message}\nYou:"

# Get response from LLM
async def get_llm_response(message: str) -> str:
    full_prompt = build_prompt(message)
    try:
        response = llm.invoke(full_prompt).strip()
        conversation_history.append((message, response))
        if len(conversation_history) > MAX_TURNS:
            conversation_history.pop(0)
        return response
    except Exception as e:
        print("LLM Error:", e)
        return "Oops, something broke 😅"

# Start new chat
# async def start_new_chat(page):
#     global conversation_history
#     conversation_history = []
#     print("Starting new chat...")
#     await page.click("button.inputBox_btn.success")  # Start button
#     await page.wait_for_selector(".chatmsg")

async def start_new_chat(page):
    global conversation_history
    conversation_history = []
    print("Waiting for Start button...")

    buttons = await page.locator("button").all()
    for i, button in enumerate(buttons):
     text = await button.inner_text()
     print(f"Button {i}: '{text}'")


    try:
        # Wait for the Start button using button text
        await page.wait_for_selector("button:has-text('START')", timeout=15000)
        start_button = page.locator("button:has-text('START')")

        # Ensure it's visible and clickable
        if await start_button.is_visible() and await start_button.is_enabled():
            await start_button.scroll_into_view_if_needed()
           # await start_button.click()
            await start_button.click(force=True)
            print("Clicked Start button.")
        else:
            print("Start button not visible or not enabled.")

        # Confirm chat has started by checking for input box
        await page.wait_for_selector(".chatmsg", timeout=10000)
        print("Chat started!")

    except Exception as e:
        print("Failed to start chat:", e)




# Check if chat is disconnected
async def chat_ended(page):
    try:
        input_box = page.locator(".inputContainer input.input")
        send_button = page.locator("button.send")

        if await page.locator("text='Stranger has disconnected'").is_visible():
            return True
        if not await input_box.is_enabled() and not await send_button.is_enabled():
            return True

        return False
    except Exception as e:
        print("Error checking chat ended:", e)
        return True



# Main logic
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("Going to page...")
        await page.goto("https://omegleapp.me/chat/", timeout=60000, wait_until="domcontentloaded")
        print("Page loaded!")
        await page.screenshot(path="after_goto.png")

      
        await start_new_chat(page)

        async def send_message(msg):
            # Ensure input box is not disabled
            input_box = page.locator(".inputContainer input.input")
            send_button = page.locator("button.inputBox_btn.send")

            input_enabled = await input_box.is_enabled()
            send_enabled = await send_button.is_enabled()

            if  await chat_ended(page):
                print("Send blocked: Input disabled or chat ended.")
                return

            try:
                await input_box.fill(msg)
                print("Simulating typing...")
                await asyncio.sleep(8)          # Wait to simulate typing
                await send_button.click()         # Then click to send
                print("Message sent!")
            except Exception as e:
                print("Failed to send message:", e)


        seen_messages = set()

        while True:
            try:
                
                # Check if chat has ended
                if await chat_ended(page):
                    print("Chat ended, restarting...")
                    await start_new_chat(page)
                    seen_messages.clear()
                    continue

                # Get incoming messages
                message_blocks = await page.query_selector_all(".chatBox_messages .text")

                for block in message_blocks:
                    author_span = await block.query_selector(".text_auther")
                    author = await author_span.inner_text() if author_span else ""

                    if "Stranger" in author:
                        msg_div = await block.query_selector(".text_msg")
                        if msg_div:
                            msg_text = await msg_div.inner_text()
                            cleaned_text = msg_text.replace(":", "").strip()

                            if cleaned_text not in seen_messages:
                                seen_messages.add(cleaned_text)
                                print("Stranger:", cleaned_text)
                                response = await get_llm_response(cleaned_text)
                                print("You:", response)
                                await send_message(response)


                await asyncio.sleep(0.2)

            except Exception as e:
                print("Unexpected error:", e)
                await asyncio.sleep(1)

        await browser.close()

# Run bot
asyncio.run(main())
