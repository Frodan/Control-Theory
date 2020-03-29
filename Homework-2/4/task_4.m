syms s

A=[1 0; 2 1];
B=[2; 2];
C=[-1  4];
D=2;

Phi=inv(s*eye(2)-A);

H=C*Phi*B+D; 

disp(H);