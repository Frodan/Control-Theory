num = [1, 3, 8];
denum = [1, 2, 3, 13, 7];
G = tf(num, denum);

z = -0.29628;
k = 80.317;
C = tf(k *[1 z], [1]);
T = feedback(C*G, 1);
step(T);
