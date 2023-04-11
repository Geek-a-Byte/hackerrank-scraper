import requests
from bs4 import BeautifulSoup as bs
import lxml

# Page header
head= { 'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# Login URL
login_url = 'https://www.hackerrank.com/auth/login'

# Open up a session
s = requests.session()

# Open the login page
r = s.get(url)

print(r.status_code)
# Get the csrf-token from meta tag
soup = bs(r.text,'lxml')
csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

# Get the page cookie
cookie = r.cookies

# Set CSRF-Token
head['X-CSRF-Token'] = csrf_token
head['X-Requested-With'] = 'XMLHttpRequest'

# Build the login payload
payload = {
'username': '', #<-- your username
'password': '', #<-- your password
'remember':'1' 
}

# Try to login to the page
r = s.post(login_url, cookies=cookie, data=payload, headers=head)

print(r.status_code)


url2='https://www.hackerrank.com/rest/hackers/geek_a_byte32/badges'


# Try to get a page behind the login page
r = s.get(url2, headers=head)

print(r.status_code)

# # Check if login was successful
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
