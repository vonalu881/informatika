def month_calendar(start_weekday, days):
    weeks = []
    current_week = []
    
    for _ in range(start_weekday):
        current_week.append("  ")
        
    for day in range(1, days + 1):
        current_week.append(f"{day:2}")
        
        if len(current_week) == 7:
            weeks.append(" ".join(current_week))
            current_week = []
            
    if current_week:
        weeks.append(" ".join(current_week))
        
    final_calendar = "\n".join(week.rstrip() for week in weeks)
    
    return final_calendar

