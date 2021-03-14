# -*- coding: UTF-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import database
# import database_new
import time


class Handle(object):

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)  # 后台打日志
            recMsg = receive.parse_xml(webData)
            query_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                          "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
            auto_reply = "欢迎关注CSDW大赛组委会！\n\n" \
                                  "回复【0】获取 <积分>\n" \
                                  "回复【1】获取 <参赛场数>\n" \
                                  "回复【2】获取 <大赢家数>\n" \
                                  "回复【3】获取 <最佳炮手数>\n" \
                                  "回复【4】获取 <胜场数>\n" \
                                  "回复【5】获取 <负场数>\n" \
                                  "回复【6】获取 <大赢家率>\n" \
                                  "回复【7】获取 <最佳炮手率>\n" \
                                  "回复【8】获取 <胜率>\n" \
                                  "回复【9】获取 <败率>\n" \
                                  "回复【10】获取 <单场赢最多>\n" \
                                  "回复【11】获取 <单场输最多>\n" \
                                  "回复【12】获取 <最长连胜>\n" \
                                  "回复【13】获取 <最长连败>\n" \
                                  "回复【14】获取 <坐庄数>\n" \
                                  "回复【15】获取 <胡牌数>\n" \
                                  "回复【16】获取 <点炮数>\n" \
                                  "回复【17】获取 <摸宝数>\n" \
                                  "回复【18】获取 <漏宝数>\n" \
                                  "回复【19】获取 <单场最多坐庄数>\n" \
                                  "回复【20】获取 <单场最多胡牌数>\n" \
                                  "回复【21】获取 <单场最少胡牌数>\n" \
                                  "回复【22】获取 <单场最多点炮数>\n" \
                                  "回复【23】获取 <单场最多摸宝数>\n" \
                                  "回复【24】获取 <单场最多漏宝数>\n" \
                                  "回复【25】获取 <场均坐庄>\n" \
                                  "回复【26】获取 <场均胡牌>\n" \
                                  "回复【27】获取 <场均点炮>\n" \
                                  "回复【28】获取 <场均摸宝>\n" \
                                  "回复【29】获取 <场均漏宝>\n" \
                                  "回复【30】获取 <当前连胜场数>\n" \
                                  "回复【31】获取 <当前连败场数>\n\n" \
                                  "回复【房号】获取房间号(随用随取，不要乱试)\n\n" \
                                  "更多功能开发中，敬请期待！"
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == "event":
                    if recMsg.Event == "subscribe":
                        content = auto_reply
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == "text":
                    # ####### 查询类
                    # 查询积分
                    if recMsg.Content in query_list:
                        content = database.query_info(recMsg.Content).encode("UTF-8")

                    # 获取房号
                    elif recMsg.Content == "房号":
                        content = database.get_room_id()

                    # 查询对局历史
                    elif recMsg.Content.startswith("his-"):
                        content = database.query_game_his(recMsg.Content[4:])

                    # ####### 上传类
                    # 上传对局信息，写入数据
                    elif recMsg.Content.startswith("upload-"):
                        content = database.write_record(recMsg.Content[7:])

                    # 删除一条对局信息，更新player_info
                    elif recMsg.Content.startswith("remove-"):
                        content = database.remove_record(recMsg.Content[7:])

                    # 上传新房号，写入房号池
                    elif recMsg.Content.startswith("room-"):
                        content = database.add_room(recMsg.Content[5:])

                    # ####### 彩蛋类
                    # 对对子
                    elif recMsg.Content == "东边日出西边雨":
                        content = "红色奥迪治不举"
                    elif recMsg.Content == "癞蛤蟆操青蛙":
                        content = "呱呱呱呱呱呱"

                    # 其余未知关键词
                    else:
                        content = auto_reply
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
        except Exception as e:
            print(e)
            return e
