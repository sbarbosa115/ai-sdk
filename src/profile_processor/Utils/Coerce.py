import re
from datetime import datetime

parse_date = lambda date: datetime.strptime(date, '%Y-%m-%d') if date else None

lowercase = lambda text: text.lower

clean_html = lambda text: re.compile(r'<[^>]+>').sub('', text)

clean_spaces = lambda text: text.replace(" ", "")

remove_non_numeric = lambda text: re.compile('[^0-9]').sub('', text)

sanitize_numeric = lambda string: clean_spaces(remove_non_numeric(string))

sanitize_names = lambda string: clean_html(string).strip().lower()