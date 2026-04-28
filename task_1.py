time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

parts = time_string.replace(',', ' ').split()

for item in parts:
    if 'h' in item:
        total_minutes += int(item.replace('h', '')) * 60
    elif 'm' in item:
        total_minutes += int(item.replace('m', ''))
    elif 's' in item:
        total_minutes += int(item.replace('s', '')) // 60

print(total_minutes)