class Date:
    def __init__(self, day, month, year):
        if month < 1 or month > 12:
            raise ValueError()
            
        if day < 1 or day > self._get_days_in_month(month, year):
            raise ValueError()
            
        self.day = day
        self.month = month
        self.year = year

    def _is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def _get_days_in_month(self, month, year):
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self._is_leap_year(year):
            return 29
        return days[month]

    def __add__(self, n):
        day = self.day
        month = self.month
        year = self.year
        
        if n >= 0:
            day += n
            while day > self._get_days_in_month(month, year):
                day -= self._get_days_in_month(month, year)
                month += 1
                if month > 12:
                    month = 1
                    year += 1
        else:
            day += n
            while day < 1:
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
                day += self._get_days_in_month(month, year)
                
        return Date(day, month, year)

    def __sub__(self, other):
        if not isinstance(other, Date):
            return 0
            
        if self == other:
            return 0
            
        days_count = 0
        if self < other:
            current = self
            while current < other:
                current = current + 1
                days_count += 1
            return -days_count
        else:
            current = other
            while current < self:
                current = current + 1
                days_count += 1
            return days_count

    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if not isinstance(other, Date):
            return False
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def __repr__(self):
        return "Date(" + str(self.day) + ", " + str(self.month) + ", " + str(self.year) + ")"

    def __str__(self):
        d_str = str(self.day) if self.day >= 10 else "0" + str(self.day)
        m_str = str(self.month) if self.month >= 10 else "0" + str(self.month)
        return d_str + "." + m_str + "." + str(self.year)
