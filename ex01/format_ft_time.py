import time

seconds = time.time()
formatted_seconds = f"{seconds:,.4f}"
scientific_notation = f"{float(seconds):.2e}"

date = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970: " + formatted_seconds +
      " or " + scientific_notation + " in scientific notation")
print(date)
