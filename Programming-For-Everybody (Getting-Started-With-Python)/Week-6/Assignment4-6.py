def computepay(h,r):
    if(hrs<=40):
        pay=hrs*rate
    else:
        extra_pay=(hrs-40)*rate*1.5
        pay=(rate*40)+extra_pay
    return pay
hrs=int(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
pay= computepay(hrs,rate)

print("Pay",pay)