from flask import Flask, jsonify,request
import requests
import random
import json
app = Flask(__name__)
user_agent_list=[


'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/42.0 Safari/537.31'

]



    

@app.route("/fetchbill/api",methods=['POST'])
def fetchbill():
    if request.method=="POST":
      
        opint=request.form['op']
       
        cnint=request.form['cn']
        a={"adParams":{},"op":opint,"cn":cnint}
       
        user_agent = random.choice(user_agent_list)
        url = 'https://rapi.mobikwik.com/recharge/v1/viewpayment'
        payload = json.dumps(a)
        
        headers = {'content-type': 'application/json','Accept':'application/json, text/plain, */*','Refer':'https://www.mobikwik.com/','User-Agent':user_agent,'X-MClient':"0"}
        r = requests.post(url, data=payload, headers=headers)
       
        return jsonify(r.json())
if __name__ == '__main__':
    app.run()
