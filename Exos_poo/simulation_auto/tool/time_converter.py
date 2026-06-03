class TimeConverter:
    @staticmethod
    def sec_to_hour(sec):
        return int(sec // 3600)
    
    @staticmethod
    def sec_to_min(sec):
        return int(sec // 60)
    
    @staticmethod
    def sec_to_day(sec):
        return int(sec // 86400)
    
    @staticmethod
    def convert_to_day_hour_min_sec(sec):
        tc = TimeConverter()
        day = tc.sec_to_day(sec)
        r = sec % 86400
        hour = tc.sec_to_hour(r)
        r = sec % 3600
        min = tc.sec_to_min(r)
        r = sec % 60
        return (day, hour, min, r)
    