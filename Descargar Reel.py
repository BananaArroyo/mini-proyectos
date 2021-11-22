from instascrape import Reel
import time
  
# session id
SESSIONID = "Paste session Id Here"
  
# Heder with session id
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    "cookie": f'sessionid={SESSIONID};'
}
  
# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(
    'https://www.instagram.com/reel/CV6D76yAL0x/?utm_medium=copy_link')
  
# Using  scrape function and passing the headers
insta_reel.scrape(headers=headers)
  
# Giving path where we want to download reel to the 
# download function
insta_reel.download(fp=f"/Users/puntoambar/Desktop/reel.mp4")
  
# printing success Message
print('Downloaded Successfully.')