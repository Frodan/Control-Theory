syms x(t)
Dx = diff(x);
eqn = diff(x,t,2) - diff(x,t) + 3 == sin(2*t);
cond1 = x(0) == 5;
cond2 = Dx(0) == 2;
conds = [cond1, cond2];
S(t) = dsolve(eqn, conds);
Sol = simplify(S);
%% S