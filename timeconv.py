#!/usr/bin/python
# _*_ coding: utf-8 _*_

from datetime import datetime
import time
import pytz

class TimeConv:
	def __init__(self):
		pass

	def epoch2jst(self, epoch_timestamp):
		"""
		Convert epoch timestamp to JST timestamp string
		"""
		_dt = datetime.fromtimestamp(float(epoch_timestamp))
		_jst = pytz.timezone('Asia/Tokyo').localize(_dt)
		return "{0:%Y-%m-%d %H:%M:%S}".format(_jst)

	def epoch2utc(self, epoch_timestamp):
		"""
		Convert epoch timestamp to UTC timestamp string
		"""
		_dt = datetime.utcfromtimestamp(float(epoch_timestamp))
		return "{0:%Y-%m-%d %H:%M:%S}".format(_dt)

	def epoch2jstwithmilisec(self, epoch_timestamp):
		"""
		Convert epoch timestamp to JST timestamp with miliseconds
		"""
		_dt = datetime.fromtimestamp(float(epoch_timestamp))
		_jst = pytz.timezone('Asia/Tokyo').localize(_dt)
		return "{0:%Y-%m-%d %H:%M:%S.}".format(_jst) + "%06d" % (_jst.microsecond // 1000)

	def epoch2utcwithmilisec(self, epoch_timestamp):
		"""
		Convert epoch timestamp to UTC timestamp with miliseconds
		"""
		_dt = datetime.utcfromtimestamp(float(epoch_timestamp))
		return "{0:%Y-%m-%d %H:%M:%S.}".format(_dt) + "%06d" % (_dt.microsecond // 1000)


	def str2epoch(self, time_str):
		"""
		Convert JST string (YYYY-MM-DD HH:mm:ss) to epoch timestamp (int)
		"""
		return int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S")))


if __name__=='__main__':
	epoch_timestamp = "1398416400"
	print "timestamp:\t%s" % epoch_timestamp

	tc = TimeConv()
	print "JST:\t%s" % tc.epoch2jst(epoch_timestamp)
	print "UTC:\t%s" % tc.epoch2utc(epoch_timestamp)
	print "JSTwithMili\t:%s" % tc.epoch2jstwithmilisec(epoch_timestamp)
	print "UTCwithMili\t:%s" % tc.epoch2utcwithmilisec(epoch_timestamp)
	print "*" * 60

	time_str = "2014-04-26 22:00:00"
	print "epoch:\t%s" % tc.str2epoch(time_str)

