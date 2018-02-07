import json;
# -*- coding: UTF-8 -*-

jsonstr = '{"id":"16815599ed644840be2f0f2dc216afbb","funName":"receiveMessage","uid":"1851617789","funType":"reqest","page":0,"param":{"target":"Jerry","msgType":"txt","msg":" 就觉得","msgImgUrl":""}}';

def main():
    jsonobj = json.loads(jsonstr);
    print "funName->" + jsonobj['funName']
    print "target ->" + jsonobj['param']['target']
    print "msg ->" + jsonobj['param']['msg']
    method = jsonobj['funName']
    if method == "receiveMessage" :
        print "please deal with receive the message"

    print "resave json(format) -> \n" + json.dumps(jsonobj,indent=4)

if __name__ == "__main__":
    main()