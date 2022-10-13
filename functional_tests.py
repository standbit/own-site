from selenium import webdriver

#test that Django page opens
browser = webdriver.Chrome("/mnt/c/Users/stani/Downloads/chromedriver_win32101022/chromedriver.exe")
browser.get("http://127.0.0.1:8000")
assert "Congratulations" in browser.title