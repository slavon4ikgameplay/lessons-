while True:
    total_seconds = int(input("Enter the number of seconds: "))
    if 0 <= total_seconds < 8640000:
        break
    else:
        print("Wrong number.")
        continue

days = total_seconds // 86400
hours = (total_seconds - (days * 86400)) // 3600
minutes = (total_seconds - (days * 86400) - (hours * 3600)) // 60
seconds = (total_seconds - (days * 86400) - (hours * 3600)) - (minutes * 60)


if days % 10 == 1 and days % 100 != 11:
    print(f"{days} день, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    print(f"{days} дні, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
