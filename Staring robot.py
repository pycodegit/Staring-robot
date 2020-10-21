from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import time
import datetime

 
# webhook="https://oapi.dingtalk.com/robot/send?access_token=1dc215f41f0b03879258034a39c0b80c465aa135c9ef858ae16693ba6a7788f6"
webhook="https://oapi.dingtalk.com/robot/send?access_token=3c7d625ee6ed62d7a48747dca1c525473af5a0575387313297a5df98465cfe26"
ddrobot= DingtalkChatbot( webhook)
 
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}



def binance():
    symbol="ANTUSDT"
    binance_url='https://api.binance.com/api/v3/depth?symbol={}&limit=5'.format(symbol)
    resp=requests.get(binance_url,headers=headers)
    data=resp.json()
    data=data['bids'][0]
    lirun=(float(data[0])-8.2492)*59.29*usdt_rmb
    # print(lirun)
    msg='我的币安{}买入价，当前买家{}，盈利情况{}'.format(symbol,data,lirun)
    print(msg)
    # ddrobot.send_text(msg=msg,is_at_all=True)
    ddrobot.send_markdown(title='货币监控消息.',text='''# {}:行情 {}\n>{}\n'''.format(n,now,msg),is_at_all=True)



    # symbol="CRVUSDT"
    # binance_url='https://api.binance.com/api/v3/depth?symbol={}&limit=5'.format(symbol)
    # resp=requests.get(binance_url,headers=headers)
    # data=resp.json()
    # data=data['bids'][0]
    # lirun=(float(data[0])-3.467)*190.972*usdt_rmb
    # # print(lirun)
    # msg='我的币安{}买入价，当前买家{}，盈利情况{}'.format(symbol,data,lirun)
    # print(msg)
    # # ddrobot.send_text(msg=msg,is_at_all=True)
    # ddrobot.send_markdown(title='货币监控消息.',text='''# {}:行情 {}\n>{}\n'''.format(n,now,msg),is_at_all=True)


    symbol="MATICUSDT"
    binance_url='https://api.binance.com/api/v3/depth?symbol={}&limit=5'.format(symbol)
    resp=requests.get(binance_url,headers=headers)
    data=resp.json()
    data=data['bids'][0]
    lirun=(float(data[0])-0.02572)*16383.2*usdt_rmb
    # print(lirun)
    msg='我的币安{}买入价，当前买家{}，盈利情况{}'.format(symbol,data,lirun)
    print(msg)
    # ddrobot.send_text(msg=msg,is_at_all=True)
    ddrobot.send_markdown(title='货币监控消息.',text='''# {}:行情 {}\n>{}\n'''.format(n,now,msg),is_at_all=True)
     

def huobi():
    symbol="crvusdt"
    huobi_url="http://api.huobi.br.com/market/detail/merged?symbol={}".format(symbol)  # 聚合行情（Ticker）
    resp=requests.get(huobi_url,headers=headers)
    tick=resp.json()['tick']
    # print(tick)
    ask=tick['ask']
    bid=tick['bid']
    # print('-'*30)
    # print('当前的最低卖价:',ask)
    # print("当前的最高买价:",bid)
    lirun=(float(bid[0])-3.31)*110.851*usdt_rmb+(float(bid[0])-3.31)*105.8439*usdt_rmb+(float(bid[0])-3.23)*133.239*usdt_rmb+(float(bid[0])-3.485)*104.8*usdt_rmb+(float(bid[0])-3.485)*80.4349*usdt_rmb
    # print(lirun)
    msg='我的火币{}买入价，当前买家{}，盈利情况{}'.format(symbol,bid,lirun)
    print(msg)
    # ddrobot.send_text(msg=msg_1,is_at_all=True)
    ddrobot.send_markdown(title='货币监控消息.',text='''# {}:行情 {}\n>{}\n'''.format(n,now,msg),is_at_all=True)
    # print('-'*30)



if __name__ == '__main__':
    global usdt_rmb
    usdt_rmb=6.89
    n=0
    while True:
        ddrobot.send_text(msg="全体注意了!!!!!.",is_at_all=True)
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        n+=1
        try:
            binance()
            # huobi()
            print('-'*30)
        except Exception as e:
            print(e)
            print("访问网址异常")
        time.sleep(5*60)




        