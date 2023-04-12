import requests
from bs4 import BeautifulSoup as bs
import lxml
import json

#header string picked from chrome
headerString='''
{
    "accept": "text/html,application/xhtml+xml,application/xml;q':0.9,image/avif,image/webp,image/apng,*/*;q':0.8,application/signed-exchange;v':b3;q':0.9',text/html,application/xhtml+xml,application/xml;q':0.9,image/avif,image/webp,image/apng,*/*;q':0.8,application/signed-exchange;v':b3;q':0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q':0.9",
    "cache-control": "max-age=0",
    "cookie": "hackerrank_mixpanel_token':7283187c-1f24-4134-a377-af6c994db2a0; hrc_l_i':F; _hrank_session':653fb605c88c81624c6d8f577c9094e4f8657136ca3487f07a3068c25080706db7178cc4deda978006ce9d0937c138b52271e3cd199fda638e8a0b8650e24bb7; _ga':GA1.2.397113208.1599678708; _gid':GA1.2.933726361.1599678708; user_type':hacker; session_id':h3xb3ljp-1599678763378; __utma':74197771.397113208.1599678708.1599678764.1599678764.1; __utmc':74197771; __utmz':74197771.1599678764.1.1.utmcsr':(direct)|utmccn':(direct)|utmcmd':(none); __utmt':1; __utmb':74197771.3.10.1599678764; _biz_uid':5969ac22487d4b0ff8d000621de4a30c; _biz_sid:79bd07; _biz_nA':1; _biz_pendingA':%5B%5D; _biz_flagsA':%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _gat_UA-45092266-28':1; _gat_UA-45092266-26':1; session_referrer':https%3A%2F%2Fwww.google.com%2F; session_referring_domain':www.google.com; session_landing_url':https%3A%2F%2Fwww.hackerrank.com%2Fprefetch_data%3Fcontest_slug%3Dmaster%26get_feature_feedback_list%3Dtrue",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
'''
d = json.loads(headerString)


# Login URL
login_url = 'https://www.hackerrank.com/auth/login'

#creating session
s = requests.Session()
r = s.get(login_url, headers=d)

# Get the csrf-token from meta tag
soup = bs(r.text,'lxml')
# csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

# # Page header
# head = { 
#     'Content-Type':'application/x-www-form-urlencoded',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }

# # Set CSRF-Token
# head['X-CSRF-Token'] = csrf_token
# head['X-Requested-With'] = 'XMLHttpRequest'


# Get the page cookie
cookie = r.cookies


# Build the login payload
payload = {
'username': '', #<-- your username
'password': '', #<-- your password
'remember':'1' 
}

# Try to login to the page
r = s.post(login_url, cookies=cookie, data=payload, headers=d)

print(r.status_code)


url2='https://www.hackerrank.com/rest/hackers/<username>/badges'


# Try to get a page behind the login page
r = s.get(url2, headers=d)

print(r.status_code)

# # Check if login was successful, if so there have to be an element with the id menu_row2
soup = bs(r.text, 'lxml')

# Parse the response JSON
datum = r.json()['models']

total_count=0;
# Print the parsed data
for data in datum:
    print(data['badge_name'],end=' ')
    print(data['solved'])
    total_count+=data['solved']
print(total_count)
