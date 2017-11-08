# Just for selenium_test_ep.py
search_result_selectors = "#rso h3 a"
first_link = "#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > h3 > a"
num_of_pages_to_check = 5
search_word = "Automation"
search_domain = "siemens.com"
# valid domain "testautomationday.com"

USERNAME = "John Doe"
ACCESS_KEY = "accesskey"
base_url = "http://www.google.com"

browser_config = {
    'chrome_62_win_10': {
        'browser': 'Chrome',
        'browser_version': '62.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768'
    },
    'ff_44_osx_hs': {
        'browser': 'Firefox',
        'browser_version': '44.0',
        'os': 'OS X',
        'os_version': 'High Sierra',
        'resolution': '1600x1200'
    }
}