import sys

class Calendar:
    """
    カレンダーの日付を表示するクラス
    """
    def __init__(self, daysInYear: int, daysInMonth: int, daysInWeek: int, date: str):
        """
        コンストラクタ
        """
        self.daysInYear = int(daysInYear)
        self.daysInMonth = int(daysInMonth)
        self.daysInWeek = int(daysInWeek)
        self.year, self.month, self.day = map(int, date.split("-"))

    def is_valid_date(self) -> bool:
        """
        入力された値から不正かどうかを判定する
        """
        year_month_ratio = self.daysInYear // self.daysInMonth
        if self.daysInMonth >99:
            return False
        if year_month_ratio > 99:
            return False
        if self.day > self.daysInMonth:
            return False
        if self.month > year_month_ratio:
            return False
        return True
    
    def is_leap_year(self) -> bool:
        """
        うるう年かどうかを判定する
        一年あたりのずれ= daysInYear % daysInMonth
        現在当たりのずれ = 一年あたりのずれ * (year - 1)
        うるう年がくる間隔 = 現在当たりのずれ // daysInMonth
        """
        interval = ((self.daysInYear % self.daysInMonth) *(self.year -1)) // self.daysInMonth
        if interval == 0:
            return True
        elif self.year % interval != 0:
            if self.month > self.daysInMonth:
                return False
        else:
            if self.month + 1 > self.daysInMonth:
                return False
        return True


    def get_dayOfTheWeek(self) -> str:
        """
        曜日を判定する
        """
        dayOfTheWeek = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        sum_of_date = self.daysInYear * (self.year -1) + self.daysInMonth * (self.month -1) + self.day -1
        return dayOfTheWeek[sum_of_date % self.daysInWeek]

def main():
    daysInYear, daysInMonth, daysInWeek, date = sys.stdin.readline().split()
    calendar = Calendar(daysInYear, daysInMonth, daysInWeek, date)
    if calendar.is_valid_date() and calendar.is_leap_year():
        day_of_week = calendar.get_dayOfTheWeek()
        print(day_of_week)
    else:
        print("-1")
        exit()

if __name__ == "__main__":
    main()