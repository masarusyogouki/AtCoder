import sys

class Calendar:
    def __init__(self, daysInYear, daysInMonth, daysInWeek, date):
        self.daysInYear = int(daysInYear)
        self.daysInMonth = int(daysInMonth)
        self.daysInWeek = int(daysInWeek)
        self.year, self.month, self.day = map(int, date.split("-"))
    
    def is_valid_date(self) -> bool:
        # 不正かどうかを判断する
        monthInYear = self.daysInYear // self.daysInMonth
        """
        1. 月と日が3桁以上だと不正
        2. dayがdaysInMonthより大きいと不正
        """
        if self.daysInMonth > 99:
            return False
        if monthInYear > 99:
            return False
        if self.day > self.daysInMonth:
            return False
        return True
    
    def leap_year(self) -> bool:
        # うるう年かどうか判断する
        return True
    
    def get_dayOfTheWeek(self) -> str:
        """_summary_
        dayOfTheWeek_candidatesの中から選ばれた曜日を返す

        dayOfTheWeek_candidatesは26文字のアルファベットで構成されている
        sum_of_datesはdateまでの合計日数(indexは0から始まるので-1をする)

        Returns:
            str: dayOfTheWeek_candidatesの中から選ばれた文字
        """
        dayOfTheWeek_candidates = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        sum_of_dates = (self.year - 1) * self.daysInYear + (self.month - 1) * self.daysInMonth + self.day -1
        return dayOfTheWeek_candidates[sum_of_dates % self.daysInWeek]

def main():
    daysInYear, daysInMonth, daysInWeek, date = sys.stdin.readline().split()
    calendar = Calendar(daysInYear, daysInMonth, daysInWeek, date)
    if calendar.is_valid_date():
        print(calendar.get_dayOfTheWeek())
    else:
        print("-1")

if __name__ == '__main__':
    main()