from datetime import datetime

def get_time():
    now = datetime.now()
    return f"Agora são {now.strftime('%H:%M')}"