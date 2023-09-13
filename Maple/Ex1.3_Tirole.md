# Ex1.3 Tirole

A monopolist's marginal cost of supplying a good to consumers is 
 $` \bar{c} = c+t `$
 (where $` t `$ is a unit commodity tax).
 
Let $` p^{m}(\bar{c}) `$ denote the corresponding monopoly price.

(i) Compute $` dp^{m}/d\bar{c} `$ for the following demand functions:

$` p = q^{-\frac{1}{\varepsilon}} `$

$` p = \alpha - \beta q^{\delta} `$

$` p = \alpha -\beta ln{q} `$

----------------------------------
### Solution by using Maple software

p1:=q -> q^-1/epsilon;

p2:=q -> alpha - beta*q^delta;

p3:=q -> alpha - beta*ln(q);

p_1:=p1(q_1);

p_2:=p2(q_2);

p_3:=p3(q_3);

-------

for i from 1 to 3 do

pi[i]:=(p[i]-c)q[i];

end do;

--------

for j from 1 to 3 do

foc[j]:=diff(pi[j],q_j);

qm[j]:=solve(foc[j],q_j);

qqm[j]:=simplify(qm[j]);

end do;

-------

pm_1:=p1(qqm_1);

pm_2:=p2(qqm_2);

pm_3:=p3(qqm_3);

-------

for k from 1 to 3 do

ans[k]:=diff(pm[k],c);

end do

------
[Result File](Maple/Ex1.3_Tirole.pdf)
