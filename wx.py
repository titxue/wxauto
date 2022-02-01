# coding=utf8
import itchat
import time
import random
from itchat.content import (
    TEXT,
    FRIENDS,
    NOTE,
    PICTURE
)

itchat.auto_login()
itchat.get_friends(update=True)  # 更新好友数据。
itchat.get_chatrooms(update=True)  # 更新群聊数据。

friends = itchat.get_friends(update=True)
# 发送人员列表 可过滤
nickNames = []
for friend in friends:
    # print(friend)
    nickNames.append(friend["NickName"])

    # time.sleep(5)
# print(nickNames)


for nickName in nickNames:
    author = itchat.search_friends(nickName=nickName)[0]
    r = author.send('做任务吗？ 5立 三星号 周不过10的  （做的途中突然联系不到我就加QQ群：6）')
    time.sleep(5)
    print(r["BaseResponse"]["ErrMsg"]+"微信昵称："+nickName)



# 单发信息  nickName -> 微信昵称 不是备注
# author = itchat.search_friends(nickName='wx')[0]
# print(author)
# r = author.send('做任务吗？ 5立 三星号 周不过10的  （做的途中突然联系不到我就加QQ群：675093852）') #这里
# print(r["BaseResponse"]["ErrMsg"])


# 自动回复
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text

# itchat.auto_login()
itchat.run()
