function [u1, u2, x1, x3] = laser_plane(u1, u2, x1_t0, x2_t0, x3_t0, x4_t0, final_t, lamda1, lamda2)
% clc;clear all;
syms x1(t) x2(t) x3(t) x4(t) u1(t) u2(t) p1(t) p2(t) p3(t) p4(t);
%digits(4);
% final_t = 1;
% lamda1 = 1;
% lamda2 = 2;
%boundary value 
% u1_t0=0;
% u2_t0=0;

% x1_t0=3.2;
% x2_t0=0;
% x3_t0=0.9;
% x4_t0=0;
% 
% u1 = 0;
% u2 = 0;
for i=1:1:4
    
disp(i);
if i > 1
clear x1 x2 x3 x4 p1 p2 p3 p4 J_1(t) J_2(t) delta_H_u1(t) delta_H_u2(t);
syms x1(t) x2(t) x3(t) x4(t) p1(t) p2(t) p3(t) p4(t) J_1(t) J_2(t) delta_H_u1(t) delta_H_u2(t);
end
eqn_x4 = diff(x4,t) == u1;
cond_x4 = x4(0) == x4_t0;
x4(t) = dsolve(eqn_x4,cond_x4);

eqn_x3 = diff(x3,t) == x4;
cond_x3 = x3(0) == x3_t0;
x3(t) = dsolve(eqn_x3,cond_x3);

eqn_x2 = diff(x2,t) == 10*u2;
cond_x2 = x2(0) == x2_t0;
x2(t) = dsolve(eqn_x2,cond_x2);


eqn_x1 = diff(x1,t) == x2;
cond_x1 = x1(0) == x1_t0;
x1(t) = dsolve(eqn_x1,cond_x1);


eqn_p1 = diff(p1,t) == -2*lamda1*(x3+x1*u2-1)*u2 - 2*lamda2*(x1-3);
cond_p1 = p1(final_t) == 0;
p1(t) = dsolve(eqn_p1,cond_p1);


eqn_p2 = diff(p2,t) == -p1;
cond_p2 = p2(final_t) == 0;
p2(t) = dsolve(eqn_p2,cond_p2);


eqn_p3 = diff(p3,t) == -2*lamda1*(x3+x1*u2-1);
cond_p3 = p3(final_t) == 0;
p3(t) = dsolve(eqn_p3,cond_p3);


eqn_p4 = diff(p4,t) == -p3;
cond_p4 = p4(final_t) == 0;
p4(t) = dsolve(eqn_p4,cond_p4);


J_1(t) = int((x3 + x1*u2 - 1) , t);
J_2(t) = int((x1-3) , t);
delta_H_u1 = p4;
delta_H_u2 = lamda1*( 2*(x3+x1*u2-1)*x1 + p2 );
t = 0.5;
disp(vpa(subs(J_1)));
disp(vpa(subs(J_2)));
disp(vpa(subs(delta_H_u1)));
disp(vpa(subs(delta_H_u2)));

%使用步长为0.05的寻优U_k+1 = U_k - alfa * g , g = delta_H / delta_U
u1 = u1 - 0.02*delta_H_u1;
u2 = u2 - 0.02*delta_H_u2; 
end
%plot
% disp(vpa(J_1(final_t) - J_1(0)));
% disp(vpa(J_2(final_t) - J_2(0)));
% t = 0:0.1:final_t;
% 
% subplot(321);plot(t,u1(t));title('u1');
% 
% subplot(322);plot(t,u2(t));title('u2');
% 
% subplot(323);plot(t,x1(t));title('x1');
% 
% subplot(324);plot(t,x3(t));title('x3');
% 
% subplot(325);plot(t,J_1(t));title('J_1');
% 
% subplot(326);plot(t,J_2(t));title('J_2');
% figure;
% plot(x1(t),x3(t));title('x1-x3');
