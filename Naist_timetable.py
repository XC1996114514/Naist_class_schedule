import datetime,os

class Event:
    """
    事件对象
    """
    def __init__(self,kwargs):
        self.event_data = kwargs

    def __turn_to_string__(self):
        self.event_text = "BEGIN:VEVENT\n"
        for item,data in self.event_data.items():
            item = str(item).replace("_","-")
            if item not in ["ORGANIZER","DTSTART","DTEND"]:
                self.event_text += "%s:%s\n"%(item,data)
            else:
                self.event_text += "%s;%s\n"%(item,data)
        self.event_text += "END:VEVENT\n"
        return self.event_text

class Calendar:
    """
    日历对象
    """
    def __init__(self,calendar_name="My Calendar"):
        self.__events__ = {}
        self.__event_id__ = 0
        self.calendar_name = calendar_name

    def add_event(self,**kwargs):
        event = Event(kwargs)
        event_id = self.__event_id__
        self.__events__[self.__event_id__] = event
        self.__event_id__ += 1
        return event_id

    def modify_event(self,event_id,**kwargs):
        for item,data in kwargs.items():
            self.__events__[event_id].event_data[item] = data

    def remove_event(self,event_id):
        self.__events__.pop(event_id)

    def get_ics_text(self):
        self.__calendar_text__ = """BEGIN:VCALENDAR\nPRODID:-//ZHONG_BAI_REN//APPGENIX-SOFTWARE//\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:%s\nX-WR-TIMEZONE:null\n"""%self.calendar_name
        for key,value in self.__events__.items():
            self.__calendar_text__ += value.__turn_to_string__()
        self.__calendar_text__ += "END:VCALENDAR"
        return self.__calendar_text__

    def save_as_ics_file(self):
        ics_text = self.get_ics_text()
        open("%s.ics"%self.calendar_name,"w",encoding="utf8").write(ics_text)#使用utf8编码生成ics文件，否则日历软件打开是乱码

    def open_ics_file(self):
        os.system("%s.ics"%self.calendar_name)

def add_event(cal, SUMMARY, DTSTART, DTEND, DESCRIPTION, LOCATION):
    """
    向Calendar日历对象添加事件的方法
    :param cal: calender日历实例
    :param SUMMARY: 事件名
    :param DTSTART: 事件开始时间
    :param DTEND: 时间结束时间
    :param DESCRIPTION: 备注
    :param LOCATION: 时间地点
    :return:
    """
    time_format = "TZID=Asia/Tokyo:{date.year}{date.month:0>2d}{date.day:0>2d}T{date.hour:0>2d}{date.minute:0>2d}00"
    dt_start = time_format.format(date=DTSTART)
    dt_end = time_format.format(date=DTEND)
    create_time = datetime.datetime.today().strftime("%Y%m%dT%H%M%SZ")
    cal.add_event(
        SUMMARY=SUMMARY,
        ORGANIZER="CN=My Calendar:mailto:nobody@gmail.com",
        DTSTART=dt_start,
        DTEND=dt_end,
        DTSTAMP=create_time,
        UID="{}-11@appgenix-software.com".format(create_time),
        SEQUENCE="0",
        CREATED=create_time,
        DESCRIPTION=DESCRIPTION,
        LAST_MODIFIED=create_time,
        LOCATION=LOCATION,
        STATUS="CONFIRMED",
        TRANSP="OPAQUE"
    )

if __name__ == '__main__':
    calendar = Calendar(calendar_name="Naist")
    classTime = [
        (9, 20),
        (11, 00),
        (13, 30),
        (15, 10),
        (16, 50),
        (18, 30)
    ]  # 每节课的开始时间

    classTime2 = [
        (10, 50),
        (12, 30),
        (15, 00),
        (16, 40),
        (18, 20),
        (20, 00)
    ]  # 每节课的结束时间

    second = 00
    class1 =['データマイニング',[[2022,11,7],[2022,11,14],[2022,11,14],[2022,11,21],[2022,12,5],[2022,12,12],[2022,12,19],[2022,12,26],[2023,1,11]],1,"エーアイ大講義室[L1]", "金谷　重彦"]
    # print(len(class1[1]))
    for i in range(len(class1[1])):
        class1_name = class1[0]
        class1_year = class1[1][i][0]
        class1_month = class1[1][i][1]
        class1_day = class1[1][i][2]
        class1_start_hour = classTime[class1[2]-1][0]
        class1_start_minute = classTime[class1[2]-1][1]

        class1_end_hour = classTime2[class1[2]-1][0]
        class1_end_minute = classTime2[class1[2]-1][1]

        class1_location = class1[3]
        class1_description = class1[4]



        add_event(calendar,
                  SUMMARY=class1_name,
                  DTSTART=datetime.datetime(year=class1_year,month=class1_month,day=class1_day,hour=class1_start_hour,minute=class1_start_minute,second=00),
                  DTEND=datetime.datetime(year=class1_year,month=class1_month,day=class1_day,hour=class1_end_hour ,minute=class1_end_minute,second=00),
                  DESCRIPTION=class1_description,
                  LOCATION=class1_location)
        
    class2 =['ソフトウェアシステム構築論',[[2022,11,7],[2022,11,14],[2022,11,21],[2022,12,5],[2022,12,12],[2022,12,19],[2022,12,26],[2023,1,11]],2,"エーアイ大講義室[L1]", "飯田　元"]
    for i in range(len(class2[1])):
        class2_name = class2[0]
        class2_year = class2[1][i][0]
        class2_month = class2[1][i][1]
        class2_day = class2[1][i][2]
        class2_start_hour = classTime[class2[2]-1][0]
        class2_start_minute = classTime[class2[2]-1][1]

        class2_end_hour = classTime2[class2[2]-1][0]
        class2_end_minute = classTime2[class2[2]-1][1]

        class2_location = class2[3]
        class2_description = class2[4]
        add_event(calendar,
                  SUMMARY=class2_name,
                  DTSTART=datetime.datetime(year=class2_year,month=class2_month,day=class2_day,hour=class2_start_hour,minute=class2_start_minute,second=00),
                  DTEND=datetime.datetime(year=class2_year,month=class2_month,day=class2_day,hour=class2_end_hour ,minute=class2_end_minute,second=00),
                  DESCRIPTION=class2_description,
                  LOCATION=class2_location)
        
    
    class3 =['自然言語処理',[[2022,11,9],[2022,11,16],[2022,11,30],[2022,12,7],[2022,12,14],[2022,12,21],[2022,12,28],[2023,1,4]],1,"エーアイ大講義室[L1]", "渡辺 太郎"]
    for i in range(len(class3[1])):
        class3_name = class3[0]
        class3_year = class3[1][i][0]
        class3_month = class3[1][i][1]
        class3_day = class3[1][i][2]
        class3_start_hour = classTime[class3[2]-1][0]
        class3_start_minute = classTime[class3[2]-1][1]

        class3_end_hour = classTime2[class3[2]-1][0]
        class3_end_minute = classTime2[class3[2]-1][1]

        class3_location = class3[3]
        class3_description = class3[4]
        add_event(calendar,
                    SUMMARY=class3_name,
                    DTSTART=datetime.datetime(year=class3_year,month=class3_month,day=class3_day,hour=class3_start_hour,minute=class3_start_minute,second=00),
                    DTEND=datetime.datetime(year=class3_year,month=class3_month,day=class3_day,hour=class3_end_hour ,minute=class3_end_minute,second=00),
                    DESCRIPTION=class3_description,
                    LOCATION=class3_location)

    class4 =['アドバンスドリサーチライティング B',[[2022,11,9],[2022,11,16],[2022,11,30],[2022,12,7]],[3,4],'E318（MS）','中山　裕木子']
    for i in range(len(class4[0][1])):
        class4_name = class4[0][0]
        class4_year = class4[1][i][0]
        class4_month = class4[1][i][1]
        class4_day = class4[1][i][2]
        for j in range(len(class4[2])):
            class4_start_hour = classTime[class4[2][j]-1][0]
            class4_start_minute = classTime[class4[2][j]-1][1]

            class4_end_hour = classTime2[class4[2][j]-1][0]
            class4_end_minute = classTime2[class4[2][j]-1][1]

            class4_location = class4[3]
            class4_description = class4[4]
            add_event(calendar,
                        SUMMARY=class4_name,
                        DTSTART=datetime.datetime(year=class4_year,month=class4_month,day=class4_day,hour=class4_start_hour,minute=class4_start_minute,second=00),
                        DTEND=datetime.datetime(year=class4_year,month=class4_month,day=class4_day,hour=class4_end_hour ,minute=class4_end_minute,second=00),
                        DESCRIPTION=class4_description,
                        LOCATION=class4_location)


    class5 =["視覚メディア処理Ⅱ",[[2022,11,10],[2022,11,17],[2022,11,24],[2022,12,1],[2022,12,8],[2022,12,15],[2022,12,22],[2023,1,5]], 1, "エーアイ大講義室[L1]", "向川　康博"]
    for i in range(len(class5[1])):
        class5_name = class5[0]
        class5_year = class5[1][i][0]
        class5_month = class5[1][i][1]
        class5_day = class5[1][i][2]
        class5_start_hour = classTime[class5[2]-1][0]
        class5_start_minute = classTime[class5[2]-1][1]

        class5_end_hour = classTime2[class5[2]-1][0]
        class5_end_minute = classTime2[class5[2]-1][1]

        class5_location = class5[3]
        class5_description = class5[4]
        add_event(calendar,
                    SUMMARY=class5_name,
                    DTSTART=datetime.datetime(year=class5_year,month=class5_month,day=class5_day,hour=class5_start_hour,minute=class5_start_minute,second=00),
                    DTEND=datetime.datetime(year=class5_year,month=class5_month,day=class5_day,hour=class5_end_hour ,minute=class5_end_minute,second=00),
                    DESCRIPTION=class5_description,
                    LOCATION=class5_location)
    
    
    
    print(calendar.get_ics_text())
    calendar.save_as_ics_file()