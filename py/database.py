# -*- coding: UTF-8 -*-
# filename: database.py

import MySQLdb


def score_query():
	# 完成
	conn = MySQLdb.connect("localhost", "root", "", "csdw", charset="utf8")
	cursor = conn.cursor()
	sql = "select a.name, b.score from player_name a, player_info b where a.id=b.id;"
	query_result = ""
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			name = row[0]
			score = str(row[1])
			query_result += u"\u3010" + name + u"\u3011\uFF1A" + score + "\n"
	# print(query_result)
	except:
		print("Error! Unable to fetch data")
		return "fail"
	conn.close()
	return query_result


def write_record(record):
	# record为上传标准格式数据代码，str类型

	# 读取标准格式数据代码，解码为具体数据

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

	# 将数据写入player_gamedetail库
	# 完成

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

	sql1_check_duplicate = "select count(*) from player_gamedetail where id={} and game_time={} and score={}" \
						   " and hu={} and zhuang={} and pao={} and bao={} and lou={}" \
						   " and big_winner={} and big_boomer={}" \
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

	# 完成写入player_gamedetail表，开始更新player_info表

	# 更新积分
	# 完成
	sql1_score = "update player_info set score = score + {} where id = {};".format(player1_score, player1_id)
	sql2_score = "update player_info set score = score + {} where id = {};".format(player2_score, player2_id)
	sql3_score = "update player_info set score = score + {} where id = {};".format(player3_score, player3_id)
	sql4_score = "update player_info set score = score + {} where id = {};".format(player4_score, player4_id)
	sql_score_check = "select sum(score) from player_info"
	try:
		cursor.execute(sql1_score)
		cursor.execute(sql2_score)
		cursor.execute(sql3_score)
		cursor.execute(sql4_score)
		cursor.execute(sql_score_check)
		score_check_result = cursor.fetchone()
		print("score_check_result = " + score_check_result)
		if score_check_result != 0:
			conn.rollback()
			return "fail"
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新参赛场数
	# 完成
	sql1_game_count = "update player_info set game_count = game_count + 1 where id = {}".format(player1_id)
	sql2_game_count = "update player_info set game_count = game_count + 1 where id = {}".format(player2_id)
	sql3_game_count = "update player_info set game_count = game_count + 1 where id = {}".format(player3_id)
	sql4_game_count = "update player_info set game_count = game_count + 1 where id = {}".format(player4_id)

	try:
		cursor.execute(sql1_game_count)
		cursor.execute(sql2_game_count)
		cursor.execute(sql3_game_count)
		cursor.execute(sql4_game_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新大赢家、最佳炮手次数
	# 完成
	sql_big_winner_count = "update player_info set big_winner_count = big_winner_count + 1 where id = {};" \
		.format(big_winner)
	sql_big_boomer_count = "update player_info set big_boomer_count = big_boomer_count + 1 where id = {};" \
		.format(big_boomer)

	try:
		cursor.execute(sql_big_winner_count)
		cursor.execute(sql_big_boomer_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新胜场数、负场数
	# 完成
	if player1_score < 0:
		sql1_win_lose = "update player_info set win_count = win_count + 1 where id = {};".format(player1_id)
	else:
		sql1_win_lose = "update player_info set lose_count = lose_count + 1 where id = {};".format(player1_id)
	if player2_score < 0:
		sql2_win_lose = "update player_info set win_count = win_count + 1 where id = {};".format(player2_id)
	else:
		sql2_win_lose = "update player_info set lose_count = lose_count + 1 where id = {};".format(player2_id)
	if player3_score < 0:
		sql3_win_lose = "update player_info set win_count = win_count + 1 where id = {};".format(player3_id)
	else:
		sql3_win_lose = "update player_info set lose_count = lose_count + 1 where id = {};".format(player3_id)
	if player4_score < 0:
		sql4_win_lose = "update player_info set win_count = win_count + 1 where id = {};".format(player4_id)
	else:
		sql4_win_lose = "update player_info set lose_count = lose_count + 1 where id = {};".format(player4_id)

	try:
		cursor.execute(sql1_win_lose)
		cursor.execute(sql2_win_lose)
		cursor.execute(sql3_win_lose)
		cursor.execute(sql4_win_lose)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新单场赢最多、输最多
	# 完成
	# 可重构
	try:
		if player1_score < 0:
			sql1_win_max = "select win_max from player_info where id = {};".format(player1_id)
			cursor.execute(sql1_win_max)
			result = cursor.fetchone()
			if player1_score * -1 > result:
				sql1_update_win_max = "update player_info set win_max = {} where id = {};" \
					.format(player1_score * -1, player1_id)
				cursor.execute(sql1_update_win_max)
		else:
			sql1_lose_max = "select lose_max from player_info where id = {};".format(player1_id)
			cursor.execute(sql1_lose_max)
			result = cursor.fetchone()
			if player1_score * -1 < result:
				sql1_update_lose_max = "update player_info set lose_max = {} where id = {};" \
					.format(player1_score * -1, player1_id)
				cursor.execute(sql1_update_lose_max)

		if player2_score < 0:
			sql2_win_max = "select win_max from player_info where id = {};".format(player2_id)
			cursor.execute(sql2_win_max)
			result = cursor.fetchone()
			if player2_score * -1 > result:
				sql2_update_win_max = "update player_info set win_max = {} where id = {};" \
					.format(player2_score * -1, player2_id)
				cursor.execute(sql2_update_win_max)
		else:
			sql2_lose_max = "select lose_max from player_info where id = {};".format(player2_id)
			cursor.execute(sql2_lose_max)
			result = cursor.fetchone()
			if player2_score * -1 < result:
				sql2_update_lose_max = "update player_info set lose_max = {} where id = {};" \
					.format(player2_score * -1, player2_id)
				cursor.execute(sql2_update_lose_max)

		if player3_score < 0:
			sql3_win_max = "select win_max from player_info where id = {};".format(player3_id)
			cursor.execute(sql3_win_max)
			result = cursor.fetchone()
			if player3_score * -1 > result:
				sql3_update_win_max = "update player_info set win_max = {} where id = {};" \
					.format(player3_score * -1, player3_id)
				cursor.execute(sql3_update_win_max)
		else:
			sql3_lose_max = "select lose_max from player_info where id = {};".format(player3_id)
			cursor.execute(sql3_lose_max)
			result = cursor.fetchone()
			if player3_score * -1 < result:
				sql3_update_lose_max = "update player_info set lose_max = {} where id = {};" \
					.format(player3_score * -1, player3_id)
				cursor.execute(sql3_update_lose_max)

		if player4_score < 0:
			sql4_win_max = "select win_max from player_info where id = {};".format(player4_id)
			cursor.execute(sql4_win_max)
			result = cursor.fetchone()
			if player4_score * -1 > result:
				sql4_update_win_max = "update player_info set win_max = {} where id = {};" \
					.format(player4_score * -1, player4_id)
				cursor.execute(sql4_update_win_max)
		else:
			sql4_lose_max = "select lose_max from player_info where id = {};".format(player4_id)
			cursor.execute(sql4_lose_max)
			result = cursor.fetchone()
			if player4_score * -1 < result:
				sql4_update_lose_max = "update player_info set lose_max = {} where id = {};" \
					.format(player4_score * -1, player4_id)
				cursor.execute(sql4_update_lose_max)
	except:
		conn.rollback()
		return "fail"

	# 更新连胜连败
	# 完成
	try:
		sql1_get_current_winning_streak_count = "select current_winning_streak_count from player_info where id = {};" \
			.format(player1_id)
		cursor.execute(sql1_get_current_winning_streak_count)
		result1 = cursor.fetchone()

		sql2_get_current_winning_streak_count = "select current_winning_streak_count from player_info where id = {};" \
			.format(player2_id)
		cursor.execute(sql2_get_current_winning_streak_count)
		result2 = cursor.fetchone()

		sql3_get_current_winning_streak_count = "select current_winning_streak_count from player_info where id = {};" \
			.format(player3_id)
		cursor.execute(sql3_get_current_winning_streak_count)
		result3 = cursor.fetchone()

		sql4_get_current_winning_streak_count = "select current_winning_streak_count from player_info where id = {};" \
			.format(player4_id)
		cursor.execute(sql4_get_current_winning_streak_count)
		result4 = cursor.fetchone()

		if player1_score < 0:  # 如果赢了 清空最长连败
			if result1 == 0:  # 连胜为0，说明在连败，需要清空
				sql1_update_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count " \
						"where id = {} and current_losing_streak_count > losing_streak_count;".format(player1_id)
				cursor.execute(sql1_update_losing_streak_count)
				sql1_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 0 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_losing_streak_count)
				sql1_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 1 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_winning_streak_count)
			else:  # 连胜不为0，在连胜，增加连胜次数
				sql1_set_current_winning_streak_count = "update player_info set current_winning_streak_count = current_winning_streak_count + 1 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_winning_streak_count)
				sql1_set_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_winning_streak_count)
		else:  # 如果输了 清空最长连胜
			if result1 != 0:  # 连胜不为0，在连胜，需要清空
				sql1_update_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count " \
					"where id = {} and current_winning_streak_count > winning_streak_count;".format(player1_id)
				cursor.execute(sql1_update_winning_streak_count)
				sql1_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 0 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_winning_streak_count)
				sql1_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 1 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_losing_streak_count)
			else:  # 连胜为0，在连败，增加连败次数
				sql1_set_current_losing_streak_count = "update player_info set current_losing_streak_count = current_losing_streak_count + 1 where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_current_losing_streak_count)
				sql1_set_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count where id = {};" \
					.format(player1_id)
				cursor.execute(sql1_set_losing_streak_count)

		if player2_score < 0:  # 如果赢了 清空最长连败
			if result2 == 0:  # 连胜为0，说明在连败，需要清空
				sql2_update_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count " \
						"where id = {} and current_losing_streak_count > losing_streak_count;".format(player2_id)
				cursor.execute(sql2_update_losing_streak_count)
				sql2_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 0 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_losing_streak_count)
				sql2_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 1 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_winning_streak_count)
			else:  # 连胜不为0，在连胜，增加连胜次数
				sql2_set_current_winning_streak_count = "update player_info set current_winning_streak_count = current_winning_streak_count + 1 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_winning_streak_count)
				sql2_set_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_winning_streak_count)
		else:  # 如果输了 清空最长连胜
			if result2 != 0:  # 连胜不为0，在连胜，需要清空
				sql2_update_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count " \
					"where id = {} and current_winning_streak_count > winning_streak_count;".format(player2_id)
				cursor.execute(sql2_update_winning_streak_count)
				sql2_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 0 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_winning_streak_count)
				sql2_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 1 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_losing_streak_count)
			else:  # 连胜为0，在连败，增加连败次数
				sql2_set_current_losing_streak_count = "update player_info set current_losing_streak_count = current_losing_streak_count + 1 where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_current_losing_streak_count)
				sql2_set_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count where id = {};" \
					.format(player2_id)
				cursor.execute(sql2_set_losing_streak_count)

		if player3_score < 0:  # 如果赢了 清空最长连败
			if result3 == 0:  # 连胜为0，说明在连败，需要清空
				sql3_update_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count " \
						"where id = {} and current_losing_streak_count > losing_streak_count;".format(player3_id)
				cursor.execute(sql3_update_losing_streak_count)
				sql3_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 0 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_losing_streak_count)
				sql3_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 1 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_winning_streak_count)
			else:  # 连胜不为0，在连胜，增加连胜次数
				sql3_set_current_winning_streak_count = "update player_info set current_winning_streak_count = current_winning_streak_count + 1 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_winning_streak_count)
				sql3_set_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_winning_streak_count)
		else:  # 如果输了 清空最长连胜
			if result3 != 0:  # 连胜不为0，在连胜，需要清空
				sql3_update_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count " \
					"where id = {} and current_winning_streak_count > winning_streak_count;".format(player3_id)
				cursor.execute(sql3_update_winning_streak_count)
				sql3_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 0 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_winning_streak_count)
				sql3_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 1 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_losing_streak_count)
			else:  # 连胜为0，在连败，增加连败次数
				sql3_set_current_losing_streak_count = "update player_info set current_losing_streak_count = current_losing_streak_count + 1 where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_current_losing_streak_count)
				sql3_set_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count where id = {};" \
					.format(player3_id)
				cursor.execute(sql3_set_losing_streak_count)

		if player4_score < 0:  # 如果赢了 清空最长连败
			if result4 == 0:  # 连胜为0，说明在连败，需要清空
				sql4_update_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count " \
						"where id = {} and current_losing_streak_count > losing_streak_count;".format(player4_id)
				cursor.execute(sql4_update_losing_streak_count)
				sql4_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 0 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_losing_streak_count)
				sql4_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 1 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_winning_streak_count)
			else:  # 连胜不为0，在连胜，增加连胜次数
				sql4_set_current_winning_streak_count = "update player_info set current_winning_streak_count = current_winning_streak_count + 1 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_winning_streak_count)
				sql4_set_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_winning_streak_count)
		else:  # 如果输了 清空最长连胜
			if result4 != 0:  # 连胜不为0，在连胜，需要清空
				sql4_update_winning_streak_count = "update player_info set winning_streak_count = current_winning_streak_count " \
					"where id = {} and current_winning_streak_count > winning_streak_count;".format(player4_id)
				cursor.execute(sql4_update_winning_streak_count)
				sql4_set_current_winning_streak_count = "update player_info set current_winning_streak_count = 0 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_winning_streak_count)
				sql4_set_current_losing_streak_count = "update player_info set current_losing_streak_count = 1 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_losing_streak_count)
			else:  # 连胜为0，在连败，增加连败次数
				sql4_set_current_losing_streak_count = "update player_info set current_losing_streak_count = current_losing_streak_count + 1 where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_current_losing_streak_count)
				sql4_set_losing_streak_count = "update player_info set losing_streak_count = current_losing_streak_count where id = {};" \
					.format(player4_id)
				cursor.execute(sql4_set_losing_streak_count)
	except:
		conn.rollback()
		return "fail"

	# 更新坐庄数
	# 完成

	sql1_zhuang_count = "update player_info set zhuang_count = zhuang_count + {} where id = {};" \
		.format(player1_zhuang, player1_id)
	sql2_zhuang_count = "update player_info set zhuang_count = zhuang_count + {} where id = {};" \
		.format(player2_zhuang, player2_id)
	sql3_zhuang_count = "update player_info set zhuang_count = zhuang_count + {} where id = {};" \
		.format(player3_zhuang, player3_id)
	sql4_zhuang_count = "update player_info set zhuang_count = zhuang_count + {} where id = {};" \
		.format(player4_zhuang, player4_id)

	try:
		cursor.execute(sql1_zhuang_count)
		cursor.execute(sql2_zhuang_count)
		cursor.execute(sql3_zhuang_count)
		cursor.execute(sql4_zhuang_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新胡牌数
	# 完成

	sql1_hu_count = "update player_info set hu_count = hu_count + {} where id = {};" \
		.format(player1_hu, player1_id)
	sql2_hu_count = "update player_info set hu_count = hu_count + {} where id = {};" \
		.format(player2_hu, player2_id)
	sql3_hu_count = "update player_info set hu_count = hu_count + {} where id = {};" \
		.format(player3_hu, player3_id)
	sql4_hu_count = "update player_info set hu_count = hu_count + {} where id = {};" \
		.format(player4_hu, player4_id)

	try:
		cursor.execute(sql1_hu_count)
		cursor.execute(sql2_hu_count)
		cursor.execute(sql3_hu_count)
		cursor.execute(sql4_hu_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新点炮数
	# 完成

	sql1_pao_count = "update player_info set pao_count = pao_count + {} where id = {};" \
		.format(player1_pao, player1_id)
	sql2_pao_count = "update player_info set pao_count = pao_count + {} where id = {};" \
		.format(player2_pao, player2_id)
	sql3_pao_count = "update player_info set pao_count = pao_count + {} where id = {};" \
		.format(player3_pao, player3_id)
	sql4_pao_count = "update player_info set pao_count = pao_count + {} where id = {};" \
		.format(player4_pao, player4_id)

	try:
		cursor.execute(sql1_pao_count)
		cursor.execute(sql2_pao_count)
		cursor.execute(sql3_pao_count)
		cursor.execute(sql4_pao_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新摸宝数
	# 完成

	sql1_bao_count = "update player_info set bao_count = bao_count + {} where id = {};" \
		.format(player1_bao, player1_id)
	sql2_bao_count = "update player_info set bao_count = bao_count + {} where id = {};" \
		.format(player2_bao, player2_id)
	sql3_bao_count = "update player_info set bao_count = bao_count + {} where id = {};" \
		.format(player3_bao, player3_id)
	sql4_bao_count = "update player_info set bao_count = bao_count + {} where id = {};" \
		.format(player4_bao, player4_id)

	try:
		cursor.execute(sql1_bao_count)
		cursor.execute(sql2_bao_count)
		cursor.execute(sql3_bao_count)
		cursor.execute(sql4_bao_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新漏宝数
	# 完成

	sql1_lou_count = "update player_info set lou_count = lou_count + {} where id = {};" \
		.format(player1_lou, player1_id)
	sql2_lou_count = "update player_info set lou_count = lou_count + {} where id = {};" \
		.format(player2_lou, player2_id)
	sql3_lou_count = "update player_info set lou_count = lou_count + {} where id = {};" \
		.format(player3_lou, player3_id)
	sql4_lou_count = "update player_info set lou_count = lou_count + {} where id = {};" \
		.format(player4_lou, player4_id)

	try:
		cursor.execute(sql1_lou_count)
		cursor.execute(sql2_lou_count)
		cursor.execute(sql3_lou_count)
		cursor.execute(sql4_lou_count)
		conn.commit()
	except:
		conn.rollback()
		return "fail"

	# 更新最多坐庄数
	# *****************  未完成  *********************

	try:

	except:
		conn.rollback()
		return "fail"

	# 更新最多胡牌数
	# *************  未完成  *****************

	conn.close()
	return "success"


if __name__ == "__main__":
	# write_result = write_record("20200316;462160,-230,4,6,4,0,0;231508,-136,2,4,0,0,1;741920,106,10,5,1,0,2;"
	#                             "253786,260,6,7,4,2,3;253786;462160")
	# print(write_result)
	score_query()
