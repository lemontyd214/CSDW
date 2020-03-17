# -*- coding: UTF-8 -*-
# filename: database.py
import MySQLdb


def score_query():
    conn = MySQLdb.connect("localhost", "root", "", "csdw", charset="utf8")
    cursor = conn.cursor()
    sql = "select id, score from player_info;"
    query_result = ""
    '''
    未完成
    '''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            score = row[1]
            # print("id = {}, score = {}".format(id, score))
    except:
        print("Error! Unable to fetch data")
        return False
    conn.close()


def write_record(record):
    # record为上传标准格式数据代码，str类型
    data = record.split(";")

    game_time = int(data[0])

    player1 = data[1].split(",")
    player1_id = int(player1[0])
    player1_score = int(player1[1]) * -1
    player1_hu = int(player1[2])
    player1_zhuang = int(player1[3])
    player1_pao = int(player1[4])
    player1_bao = int(player1[5])
    player1_lou = int(player1[6])

    player2 = data[2].split(",")
    player2_id = int(player2[0])
    player2_score = int(player2[1]) * -1
    player2_hu = int(player2[2])
    player2_zhuang = int(player2[3])
    player2_pao = int(player2[4])
    player2_bao = int(player2[5])
    player2_lou = int(player2[6])

    player3 = data[3].split(",")
    player3_id = int(player3[0])
    player3_score = int(player3[1]) * -1
    player3_hu = int(player3[2])
    player3_zhuang = int(player3[3])
    player3_pao = int(player3[4])
    player3_bao = int(player3[5])
    player3_lou = int(player3[6])

    player4 = data[4].split(",")
    player4_id = int(player4[0])
    player4_score = int(player4[1]) * -1
    player4_hu = int(player4[2])
    player4_zhuang = int(player4[3])
    player4_pao = int(player4[4])
    player4_bao = int(player4[5])
    player4_lou = int(player4[6])

    big_winner = int(data[5])
    big_boomer = int(data[6])

    # 大赢家
    if big_winner == player1_id:
        player1_big_winner = 1
    else:
        player1_big_winner = 0
    if big_winner == player2_id:
        player2_big_winner = 1
    else:
        player2_big_winner = 0
    if big_winner == player3_id:
        player3_big_winner = 1
    else:
        player3_big_winner = 0
    if big_winner == player4_id:
        player4_big_winner = 1
    else:
        player4_big_winner = 0
    # 最佳炮手
    if big_boomer == player1_id:
        player1_big_boomer = 1
    else:
        player1_big_boomer = 0
    if big_boomer == player2_id:
        player2_big_boomer = 1
    else:
        player2_big_boomer = 0
    if big_boomer == player3_id:
        player3_big_boomer = 1
    else:
        player3_big_boomer = 0
    if big_boomer == player4_id:
        player4_big_boomer = 1
    else:
        player4_big_boomer = 0

    conn = MySQLdb.connect("localhost", "root", "", "csdw", charset="utf8")
    cursor = conn.cursor()
    sql1_write = "insert into player_gamedetail values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})" \
        .format(player1_id, game_time, player1_score,
                player1_hu, player1_zhuang, player1_pao, player1_bao, player1_lou,
                player1_big_winner, player1_big_boomer)
    sql2_write = "insert into player_gamedetail values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})" \
        .format(player2_id, game_time, player2_score,
                player2_hu, player2_zhuang, player2_pao, player2_bao, player2_lou,
                player2_big_winner, player2_big_boomer)
    sql3_write = "insert into player_gamedetail values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})" \
        .format(player3_id, game_time, player3_score,
                player3_hu, player3_zhuang, player3_pao, player3_bao, player3_lou,
                player3_big_winner, player3_big_boomer)
    sql4_write = "insert into player_gamedetail values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})" \
        .format(player4_id, game_time, player4_score,
                player4_hu, player4_zhuang, player4_pao, player4_bao, player4_lou,
                player4_big_winner, player4_big_boomer)

    sql1_check_duplicate = "select count(*) from player_gamedetail where id={} and game_time={} and score={}"\
                          " and hu={} and zhuang={} and pao={} and bao={} and lou={}"\
                          " and big_winner={} and big_boomer={}"\
        .format(player1_id, game_time, player1_score,
                player1_hu, player1_zhuang, player1_pao, player1_bao, player1_lou,
                player1_big_winner, player1_big_boomer)
    sql2_check_duplicate = "select count(*) from player_gamedetail where id={} and game_time={} and score={}" \
                           " and hu={} and zhuang={} and pao={} and bao={} and lou={}" \
                           " and big_winner={} and big_boomer={}" \
        .format(player2_id, game_time, player2_score,
                player2_hu, player2_zhuang, player2_pao, player2_bao, player2_lou,
                player2_big_winner, player2_big_boomer)
    sql3_check_duplicate = "select count(*) from player_gamedetail where id={} and game_time={} and score={}" \
                           " and hu={} and zhuang={} and pao={} and bao={} and lou={}" \
                           " and big_winner={} and big_boomer={}" \
        .format(player3_id, game_time, player3_score,
                player3_hu, player3_zhuang, player3_pao, player3_bao, player3_lou,
                player3_big_winner, player3_big_boomer)
    sql4_check_duplicate = "select count(*) from player_gamedetail where id={} and game_time={} and score={}" \
                           " and hu={} and zhuang={} and pao={} and bao={} and lou={}" \
                           " and big_winner={} and big_boomer={}" \
        .format(player4_id, game_time, player4_score,
                player4_hu, player4_zhuang, player4_pao, player4_bao, player4_lou,
                player4_big_winner, player4_big_boomer)
    try:
        cursor.execute(sql1_check_duplicate)
        result1 = cursor.fetchone()
        cursor.execute(sql2_check_duplicate)
        result2 = cursor.fetchone()
        cursor.execute(sql3_check_duplicate)
        result3 = cursor.fetchone()
        cursor.execute(sql4_check_duplicate)
        result4 = cursor.fetchone()
        print(result1[0])
        print(result2[0])
        print(result3[0])
        print(result4[0])
        if result1[0] != 0 or result2[0] != 0 or result3[0] != 0 or result4[0] != 0:
            return "fail"
    except:
        return "fail"
    try:
        cursor.execute(sql1_write)
        cursor.execute(sql2_write)
        cursor.execute(sql3_write)
        cursor.execute(sql4_write)
        conn.commit()
    except:
        conn.rollback()
        return "fail"
    '''
    待完善写入数据后更新player_info内容
    '''
    conn.close()
    return "success"


if __name__ == "__main__":
    write_result = write_record("20200316;462160,-230,4,6,4,0,0;231508,-136,2,4,0,0,1;741920,106,10,5,1,0,2;"
                                "253786,260,6,7,4,2,3;253786;462160")
    print(write_result)
    # score_query()
