from datetime import datetime

parse_date = lambda s: datetime.strptime(s, '%Y-%m-%d')
