from datetime import timedelta

def daterange(start_date: str, end_date: str):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
