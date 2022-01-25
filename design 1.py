import numpy as np
def A (x):
  return 10**(x/20)

Amin = A(-5)
Amax = A(-36)
R = 10000

R1 = (-R+R*Amax)/(Amax-Amin)-R
print (f"Optimal R1: {R1}")

R2 = (-R*Amax)/(Amax-Amin)
print (f"Optimal R2: {R2}\n")

R=10000
R1=7840
R2=290

Amin2=(R2 + R)/(R1+R2+R)
Amax2=(R2)/(R1+R2+R)

print(f"Teoretisk reell min demping: {20*np.log10(Amin2)}")
print(f"Teoretisk reell max demping: {20*np.log10(Amax2)}\n")

print(f"Teoretisk min dempet v2: {Amin2*5}")
print(f"Teoretisk max dempet v2: {Amax2*5}\n")

v1 = 5.16
v3min = 2.94 
v3max = 0.082

Amin3 = v3min/v1
Amax3 = v3max/v1

print(f"Faktisk reell min demping: {20*np.log10(Amin3)}")
print(f"Faktisk reell max demping: {20*np.log10(Amax3)}")
