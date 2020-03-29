syms s

A=[2 1; -3 1];
B=[-1 5; 3 1];
C=[-2  0];
D=[2 4];

Phi=inv(s*eye(2)-A);
H=C*Phi*B+D; 

disp(H);