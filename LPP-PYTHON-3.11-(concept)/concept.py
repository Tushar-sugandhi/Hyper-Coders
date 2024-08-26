from gekko import GEKKO
import subprocess

m = GEKKO()
x1 = m.Var(lb=0, ub=5) 
x2 = m.Var(lb=0, ub=4) 
m.Maximize(100*x1+125*x2) 
m.Equation(3*x1+6*x2<=30) 
m.Equation(8*x1+4*x2<=44)
m.solve(disp=False)
p1 = x1.value[0]; p2 = x2.value[0]
print ('Product 1 (x1): ' + str(p1))
print ('Product 2 (x2): ' + str(p2))
print ('Profit        : ' + str(100*p1+125*p2))

subprocess.run("eog -w solutions/Lin-Prog-Optimal-Sol.png", shell=True, executable="/bin/bash")
