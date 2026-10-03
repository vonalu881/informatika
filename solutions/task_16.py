def month_calendar(start_weekday, days):
    lines = []
    current_line = []
    for _ in range(start_weekday):
        current_line.append("  ")
    for day in range(1, days + 1):
        current_line.append(f"{day:2}")
        if len(current_line) == 7 or day == days:
            lines.append(" ".join(current_line).rstrip())
            current_line = []
    return "\n".join(lines)


