#python requests

import requests

url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.vox-cdn.com%2Fthumbor%2FOus3VQj1sn4tvb3H13rIu8eGoZs%3D%2F0x0%3A2012x1341%2F1400x788%2Ffilters%3Afocal(0x0%3A2012x1341)%3Aformat(jpeg)%2Fcdn.vox-cdn.com%2Fuploads%2Fchorus_image%2Fimage%2F47070706%2Fgoogle2.0.0.jpg&imgrefurl=https%3A%2F%2Fwww.theverge.com%2F2015%2F9%2F1%2F9239769%2Fnew-google-logo-announced&tbnid=acTTLzzqMzW0NM&vet=12ahUKEwjGmIz1_ZL1AhUYkdgFHVNjDHcQMygAegUIARDJAQ..i&docid=JWw0c9TecYe1RM&w=1400&h=788&q=google%20images&ved=2ahUKEwjGmIz1_ZL1AhUYkdgFHVNjDHcQMygAegUIARDJAQ"
res =  requests.get(url).text
print(res)