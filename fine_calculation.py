# Day 8: Library Management System
# Fine Calculation Feature

FINE_PER_DAY = 5

def calculate_fine():
    print("\n--- Library Fine Calculator ---")

    days_late = int(input("Enter the number of days late: "))

    if days_late < 0:
        print("Invalid number of days!")
    elif days_late == 0:
        print("No fine. Book returned on time!")
    else:
        fine = days_late * FINE_PER_DAY
        print("Days late:", days_late)
        print("Fine per day: Rs.", FINE_PER_DAY)
        print("Total fine: Rs.", fine)

calculate_fine()
