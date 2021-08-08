from selenium import webdriver
opts = webdriver.chrome.options.Options()
# opts.headless = True

browser = webdriver.Chrome(options=opts, executable_path='')

with open(".env", "w") as f:
    f.write(f"HOST={browser.command_executor._url}\n")
    f.write(f"SESSION={browser.session_id}")

print("Broser started")
print("Executor", browser.command_executor._url)
print("SessionID", browser.session_id)

browser.get('https://binomo-investment.com/trading')