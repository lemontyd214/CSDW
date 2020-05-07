# -*- coding: UTF-8 -*-
import os


if __name__ == "__main__":
    while 1:
        game_time = input("请输入8位比赛时间（如20200316）：")
        while len(game_time) != 8:
            game_time = input("输入有误，请输入8位比赛时间（如20200316）：")

        id_list = []

        print("请输入第1位选手数据：")
        player1_id = input("ID：")
        while len(player1_id) != 6 or player1_id in id_list:
            player1_id = input("输入有误，请输入第1位选手ID：")
        id_list.append(player1_id)
        player1_score = input("积分：")
        while player1_score == "":
            player1_score = input("输入不能为空！积分：")
        player1_hu = input("胡牌次数：")
        while player1_hu == "":
            player1_hu = input("输入不能为空！胡牌次数：")
        player1_zhuang = input("坐庄次数：")
        while player1_zhuang == "":
            player1_zhuang = input("输入不能为空！坐庄次数：")
        player1_pao = input("点炮次数：")
        while player1_pao == "":
            player1_pao = input("输入不能为空！点炮次数：")
        player1_bao = input("摸宝次数：")
        while player1_bao == "":
            player1_bao = input("输入不能为空！摸宝次数：")
        player1_lou = input("漏宝次数：")
        while player1_lou == "":
            player1_lou = input("输入不能为空！漏宝次数：")

        print("请输入第2位选手数据：")
        player2_id = input("ID：")
        while len(player2_id) != 6 or player2_id in id_list:
            player2_id = input("输入有误，请输入第2位选手ID：")
        id_list.append(player2_id)
        player2_score = input("积分：")
        while player2_score == "":
            player2_score = input("输入不能为空！积分：")
        player2_hu = input("胡牌次数：")
        while player2_hu == "":
            player2_hu = input("输入不能为空！胡牌次数：")
        player2_zhuang = input("坐庄次数：")
        while player2_zhuang == "":
            player2_zhuang = input("输入不能为空！坐庄次数：")
        player2_pao = input("点炮次数：")
        while player2_pao == "":
            player2_pao = input("输入不能为空！点炮次数：")
        player2_bao = input("摸宝次数：")
        while player2_bao == "":
            player2_bao = input("输入不能为空！摸宝次数：")
        player2_lou = input("漏宝次数：")
        while player2_lou == "":
            player2_lou = input("输入不能为空！漏宝次数：")

        print("请输入第3位选手数据：")
        player3_id = input("ID：")
        while len(player3_id) != 6 or player3_id in id_list:
            player3_id = input("输入有误，请输入第3位选手ID：")
        id_list.append(player3_id)
        player3_score = input("积分：")
        while player3_score == "":
            player3_score = input("输入不能为空！积分：")
        player3_hu = input("胡牌次数：")
        while player3_hu == "":
            player3_hu = input("输入不能为空！胡牌次数：")
        player3_zhuang = input("坐庄次数：")
        while player3_zhuang == "":
            player3_zhuang = input("输入不能为空！坐庄次数：")
        player3_pao = input("点炮次数：")
        while player3_pao == "":
            player3_pao = input("输入不能为空！点炮次数：")
        player3_bao = input("摸宝次数：")
        while player3_bao == "":
            player3_bao = input("输入不能为空！摸宝次数：")
        player3_lou = input("漏宝次数：")
        while player3_lou == "":
            player3_lou = input("输入不能为空！漏宝次数：")

        print("请输入第4位选手数据：")
        player4_id = input("ID：")
        while len(player4_id) != 6 or player4_id in id_list:
            player4_id = input("输入有误，请输入第4位选手ID：")
        id_list.append(player4_id)
        player4_score = input("积分：")
        while player4_score == "":
            player4_score = input("输入不能为空！积分：")
        player4_hu = input("胡牌次数：")
        while player4_hu == "":
            player4_hu = input("输入不能为空！胡牌次数：")
        player4_zhuang = input("坐庄次数：")
        while player4_zhuang == "":
            player4_zhuang = input("输入不能为空！坐庄次数：")
        player4_pao = input("点炮次数：")
        while player4_pao == "":
            player4_pao = input("输入不能为空！点炮次数：")
        player4_bao = input("摸宝次数：")
        while player4_bao == "":
            player4_bao = input("输入不能为空！摸宝次数：")
        player4_lou = input("漏宝次数：")
        while player4_lou == "":
            player4_lou = input("输入不能为空！漏宝次数：")

        big_winner = input("请输入大赢家ID：")
        while len(big_winner) != 6 or big_winner not in id_list:
            big_winner = input("输入有误，请输入大赢家ID：")
        big_boomer = input("请输入最佳炮手ID：")
        while len(big_boomer) != 6 or big_boomer not in id_list:
            big_boomer = input("输入有误，请输入最佳炮手ID：")

        if int(player1_score) + int(player2_score) + int(player3_score) + int(player4_score) != 0:
            print("积分总和不为0，请检查并重新输入！")
            continue
        print("请检查输入数据：")
        print("比赛时间为：{}".format(game_time))
        print("第1位选手ID：{}，积分：{}，胡牌次数：{}，坐庄次数：{}，点炮次数：{}，摸宝次数：{}，漏宝次数：{}"
              .format(player1_id, player1_score, player1_hu, player1_zhuang, player1_pao, player1_bao, player1_lou))
        print("第2位选手ID：{}，积分：{}，胡牌次数：{}，坐庄次数：{}，点炮次数：{}，摸宝次数：{}，漏宝次数：{}"
              .format(player2_id, player2_score, player2_hu, player2_zhuang, player2_pao, player2_bao, player2_lou))
        print("第3位选手ID：{}，积分：{}，胡牌次数：{}，坐庄次数：{}，点炮次数：{}，摸宝次数：{}，漏宝次数：{}"
              .format(player3_id, player3_score, player3_hu, player3_zhuang, player3_pao, player3_bao, player3_lou))
        print("第4位选手ID：{}，积分：{}，胡牌次数：{}，坐庄次数：{}，点炮次数：{}，摸宝次数：{}，漏宝次数：{}"
              .format(player4_id, player4_score, player4_hu, player4_zhuang, player4_pao, player4_bao, player4_lou))
        print("大赢家：{}".format(big_winner))
        print("最佳炮手：{}".format(big_boomer))

        input_check = input("请检查数据是否准确，若准确输入y生成上传代码，若有误输入n重新输入：y/n")
        if input_check == "y" or input_check == "Y":
            print("代码如下，请复制并发送至公众号！")
            print("{};{},{},{},{},{},{},{};{},{},{},{},{},{},{};{},{},{},{},{},{},{};{},{},{},{},{},{},{};{};{}"
                  .format(game_time,
                          player1_id, player1_score, player1_hu, player1_zhuang, player1_pao, player1_bao, player1_lou,
                          player2_id, player2_score, player2_hu, player2_zhuang, player2_pao, player2_bao, player2_lou,
                          player3_id, player3_score, player3_hu, player3_zhuang, player3_pao, player3_bao, player3_lou,
                          player4_id, player4_score, player4_hu, player4_zhuang, player4_pao, player4_bao, player4_lou,
                          big_winner,
                          big_boomer))
        elif input_check == "n" or input_check == "N":
            print("放弃当前输入，请重新输入！")
            continue
        exit_check = input("是否退出？y/n")
        if exit_check == "y" or exit_check == "Y":
            break
