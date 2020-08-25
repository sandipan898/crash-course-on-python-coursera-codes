import random

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print()
print("Datetime module\n")
import datetime
now = datetime.datetime.now()
print("Type: " + str(type(now)))

print("Time: " + str(now))

print("Year: " + str(now.year))

print("Future date (after 28 days): " + str(now + datetime.timedelta(days=28)))
