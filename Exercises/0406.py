# Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and pay)

def computepay(hours,rate) :
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        xp = reg * otp
    else :
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay:", xp)
