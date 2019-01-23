import requests
import json
from pprint import pprint
import datetime
from slacker import Slacker

y = datetime.date.today() - datetime.timedelta(1)


params = (
    ('api_key', 'WczJQ0wegACAAHJGmQADaAESBSUKWe4iI1OZurfwKU2dusQk9Ke3OVK5PcYK'),
    ('from', y),
    ('to', y),
    ('metrics[]', ['installs', 'new_users', 'daily_active_users', 'revenue', 'daily_paying_users']),
)

r = requests.get('https://rpc.tapjoy.com/api/v1/exports', params=params)

# print(r.json())

data = json.loads(r.text)
install = data['installs'][str(y)]
nru = data['new_users'][str(y)]
dau = data['daily_active_users'][str(y)]
rev = data['revenue'][str(y)]
pu = data['daily_paying_users'][str(y)]



databoy = "인스톨= %s / NRU= %s / DAU= %s / 매출= %s / PU= %s"%(install,nru,dau,int(rev),pu)

token = 'xoxb-342261706786-530496299956-oGj5Hti8Fp16jcTnJwm3H6v6'
slack = Slacker(token)

dic = {"title":"전일 %s 탭조이 지표 입니다!"%str(y), "text": str(databoy)}
attachments = [dic]

slack.chat.post_message('#글로벌-파트', attachments=attachments)

# 테스트 xoxb-337262206096-531724855911-wHrnaH68F1JdN36kNoblpwa5
# xoxb-342261706786-530496299956-oGj5Hti8Fp16jcTnJwm3H6v6

# pprint(data)
# print("어제(",y,")의 현황입니다. 인스톨=",install,"/ NRU=",nru,"/ DAU=",dau,"/ 매출=",rev,"/ PU=",pu)
