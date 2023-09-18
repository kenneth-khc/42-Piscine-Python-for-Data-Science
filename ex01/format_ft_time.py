import time

seconds = time.time()
formatted_seconds = "{:,.4f}".format(seconds)
scientific_notation = "{:.2e}".format(float(seconds))

date = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970: " + formatted_seconds +
      " or " + scientific_notation + " in scientific notation")
print(date)
