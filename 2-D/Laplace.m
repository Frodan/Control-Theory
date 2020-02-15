syms s t X
f = sin(2 * t) - 3;
F = laplace(f, t, s);
Sol = solve(s*s*X - 5*s - 2 - s*X + 5 - 2*X + 1/s, X);
sol = ilaplace(Sol, s, t);
disp(sol);
ezplot(sol, [0, 11]);