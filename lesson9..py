from datetime import datetime, timedelta

current_time = datetime.now()

print(current_time)

hour_ago = current_time - timedelta(hours=1)
print("Hour ago was", hour_ago)
