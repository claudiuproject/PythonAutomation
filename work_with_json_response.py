import json
import requests


# Global Variable

valueFalse = "False"
valueTrue = "True"


#Api Call ...
url = "https://Test2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

 

data_response = response.json()

#Response
"""
api response:

response1 ="{
    "name":"john",
    "ok":"true"

}

response2 = "{
    "name":"Mike",
    "ok": "false"
}
"""

 

def statusBool():
    data_response = response.json()
    data = data_response["ok"]

    if json.dumps(data) == "true":
        data = valueTrue

    elif json.dumps(data) == "false":
        data = valueFalse

def main() : 
    if statusBool() == valueTrue:
        print("Do Something ")
    else:
        print("Do else")

if __name__=="__main__":
    main()



