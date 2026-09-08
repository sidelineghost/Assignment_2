
#to complete this, I used the textbook instructions, though I read ahead a little.
#I also disabled inline text suggestions bc I didn't like them

print("let's do some investment")
#starting out with an empty list to add final values to, and the repeat variable
Lfinal = []
Linit = []
Lrate = []
Ltime = []
Lcomp = []
repeat = "y"

while repeat == "y" or repeat == "Y":
#queries for the values (initial, percentage-rate, total time, and compound division)
    init = float(input("How much do you want to initially invest? "))
    prate = float(input("What is the interest rate in %? (eg. 3 for 3%) "))
    time = float(input("How many years are you investing it? "))
    comp = float(input("How often per year is it compounded? "))

#to translate the rate from percent to decimal
    rate = prate/100

#The Math (tm)
    final = init*(1+rate/comp)**(time*comp)
    diff = final-init


    Lfinal.append(final)
    Linit.append(init)
    Lrate.append(prate)
    Ltime.append(time)
    Lcomp.append(comp)
#every value is stored for the comparisons. A user can make a few and the code will pull
#the details of the best investment option. Note that prate was captured, not rate, for
#display purposes.

    print(f'''
Initially investing ${init:.2f}
will give you ${final:.2f} 
with a difference of ${diff:.2f} 
''')
    
    if len(Lfinal) > 1:
        best = max(Lfinal)
        num = Lfinal.index(best)
        print(f"The best investment so far is attempt #{num} at {best:.2f}")
        print(f'''With an initial value of ${Linit[num]:.2f}
An interest rate of {Lrate[num]}%
Over {Ltime[num]} years
Compounded {Lcomp[num]} times per year

''')



    repeat = input("Do you want to compare with other numbers? y/N ")
    #even though it is already y, if the user just hits enter then repeat becomes
    #a blank string, which ends the script. I added capital Y too, just in case.


print()
print("May your fortunes flow!")