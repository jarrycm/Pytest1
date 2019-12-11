#!/usr/bin/python
# coding: UTF-8
#define function for sourcechannelID match in the responding position of match object where pageconversion involving payment page.
import sys
import datetime
import time

#datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
#,orderStatus,BalanceType,serverfrom,isonline,maskedhotelid,custtype,frompackageorder,isfhpkg,Referenceby,UID,ciiquantity,ciireceivable,ciipayable,ciiamount,ordamount
#,'checkInDate',orderStatus,BalanceType,serverfrom,isonline,maskedhotelid,custtype,frompackageorder,isfhpkg,Referenceby,UID,ciiquantity,ciireceivable,ciipayable,ciiamount,ordamount
InsertDate=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
for inputline in sys.stdin:
	try:
		(orderID,Arrival,ETD,checkdateInterval)=inputline.strip().split('\t')
	except:
		print >> sys.stderr ,'CAN NOT split for inputline:'+ inputline
		continue 
	arrival_to_date=time.strptime(Arrival[0:19],'%Y-%m-%d %H:%M:%S')

	for day in range(int(checkdateInterval)):
		checkInDate=time.strftime("%Y-%m-%d",time.localtime(time.mktime(arrival_to_date)+day*24*3600))
		print '\t'.join([orderID,Arrival,ETD,checkInDate])