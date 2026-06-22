from schedule_management import calendar
from datetime import datetime

today = datetime.now()
date = today.strftime("%Y-%m-%d")

event = "회의"

print(calendar.add_event(event, date))
print(calendar.remove_event(event))