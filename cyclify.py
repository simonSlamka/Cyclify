'''
CYCLIFY
A very simple program that calculates the approximate occurance of a menstrual cycle based on the last one.
Will be updated to use more than one of previous occurences and thus give a better estimate.
The current use of this is mainly for scripting purposes where this program would act like a module to quickly calculate some values.
There's no expected direct usage from regular users.
!!! THE OUTPUT OF THIS PROGRAM DOES NOT, IN ANY WAY, SHAPE, OR FORM, CONSTITUTE MEDICAL ADVICE. IT IS NOT MEANT TO BE USED FOR MEDICAL PURPOSES !!!
'''

from datetime import datetime, timedelta

bLoop = 1
while(bLoop == 1):
    try:
        date_last_cycle = datetime.strptime(
            input("\nPlease enter the date of your last period [mm/dd/yyyy]:\n"), "%m/%d/%Y")
        print("\n----------\nTo verify, your last period was on:",
              date_last_cycle.strftime("%A, %m/%d/%Y"), " correct (Y or N)?\n")
        if(input("") == "Y"):
            print("Your next period is expected to begin within 4 days of " + str(datetime.strftime(
                date_last_cycle + timedelta(days=28), "%A, %m/%d/%Y")))  # day not displaying correctly
            bLoop = 0
    except Exception as err:
        print(f"{err}")
