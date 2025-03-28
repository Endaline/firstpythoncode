import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range (0, my_time)):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(2) #it will take 2 seconds to count for the next number

#  after 3 seconds print time's up
print("Time's up") # type: ignore 