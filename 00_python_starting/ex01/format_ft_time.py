import datetime
import time


now = datetime.datetime.now()
microSeconds = now.microsecond

seconds = time.mktime(now.timetuple()) + microSeconds / 1_000_000

msg = "Seconds since January 1, 1970:"
print(f"{msg} {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
