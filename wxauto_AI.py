from zhipuai import ZhipuAI
from wxauto import WeChat
def SendMessageText_Ai(text=None):
    # print("ai开始运行")
    str_text=""
    client = ZhipuAI(api_key="4315ba1abb70113e91584d21015fe749.75qPEFnHOBxbVGAd")  # hongyan-ai-sk
    response = client.chat.completions.create(
        # model="glm-4-0520",
        model="glm-4-flash",
        messages=[
            {"role": "user", "content":text},
        ],
        stream=True,
        )
    for chunk in response:
        str_text+=chunk.choices[0].delta.model_dump()['content']
    return "Ai_AutoMessage:" + str(str_text.strip())  

def main(wx, msgs): 
    for u in msgs.keys():   
        for list_v in msgs[u]:  
            # print(list_v) 
            if list_v[0] == u:  
                # if u == ""
                s1 = SendMessageText_Ai(list_v[1])  
                wx.SendMsg(msg=s1, who=u)   

if __name__ == '__main__':  
    from alive_progress import alive_bar        
    import time     
    items = range(100)  
    with alive_bar(len(items), bar='blocks', spinner='dots_waves',spinner_length=15,title = "Mr.孙") as bar:   
        for item in items:  
            time.sleep(0.02)    
            bar()   
    print() 
    print("Start Run ---> "+"-*-"*30)       
    
    wx = WeChat()   
    user = "文件传输助手"   
    while 1:    
        # msgs = wx.GetAllNewMessage()
        msgs = wx.GetAllNewMessage()    
        if msgs:    
            print(msgs)
            main(wx, msgs)
            # print(msgs[-1].type)
        try:
            time.sleep(2)
            wx.ChatWith(user)
        except KeyboardInterrupt as e:
            wx.ChatWith(user)
            quit("崩溃...退出...")

# wx = WeChat()
# sessions = wx.GetSession()
# for session in sessions:
#     print(f"聊天对象名称: {session.name}")
#     print(f"最后一条消息时间: {session.time}")
#     print(f"最后一条消息内容: {session.content}")
#     print(f"是否有新消息: {session.isnew}", end='\n\n')
#     print(f"当前聊天对象名: {wx.CurrentChat()}") 

