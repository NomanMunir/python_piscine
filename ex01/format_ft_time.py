from datetime import datetime
from time import mktime


now = datetime.now()
microSeconds = now.microsecond

seconds = mktime(now.timetuple()) + microSeconds / 1_000_000


# timeNow = time.time()

print(
    f"Seconds since January 1, 1970: {seconds:.4f} or {seconds:.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
