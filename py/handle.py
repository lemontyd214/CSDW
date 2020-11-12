# -*- coding: UTF-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import database

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == "event":
                    if recMsg.Event == "subscribe":
                        content = "欢迎关注CSDW大赛组委会！\n\n" \
                                  "回复【积分】获取最新积分情况\n\n" \
                                  "更多功能开发中，敬请期待！"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == "text":
                    if recMsg.Content == "积分":
                        content = database.score_query().encode("UTF-8")
                    elif recMsg.Content == "东边日出西边雨":
                        content = "红色奥迪治不举"
                    else:
                        content = "欢迎关注CSDW大赛组委会！\n\n" \
                                  "回复【积分】获取最新积分情况\n\n" \
                                  "更多功能开发中，敬请期待！"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return reply.Msg().send()
        except Exception, Argment:
            return Argment