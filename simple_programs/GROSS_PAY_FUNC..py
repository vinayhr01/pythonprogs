def computepay(h, r):
    if float(h) <= 40:
        p1 = h * r
    else:
        p1 = 40 * r
        p =(float(h)-40)*r*1.5
        p1 = p1 + p
    return p1


h = input("Enter Hours:")
float(h)
r = input("Enter rate:")
float(r)
p1 = computepay(float(h),float(r))
print("Pay", p1)