%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%Author: Abdullah Al Mamun
%Title: Lagrange Polynomial and its Derivative
%Course: MAE 5093
%Date: 09-13-2018
%-------------------------------------------------------------------------%
clear; close; clc;
%-------------------------------------------------------------------------%

%Number of Data points
N=9;

%Start point
x0=-1;
%End point
xn=1;
%Exact Function (to generate data points)
f=@(x) cos(10*x).*sin(x);
df=@(x) cos(10*x).*cos(x)-10*sin(10*x).*sin(x);

%Generating Data points
x=linspace(x0,xn,N);
y=f(x);

%Defining comparing points
Nc=100;
xc=linspace(x0,xn,Nc);
ye=f(xc); %Exact Values for the comparing points
yl=zeros(1,Nc);

%-------------------------------------------------------------------------%
%Calculating Lagrange approximation for the xc points
for c=1:Nc
    sum=0;
   for i=1:N
       prod=1;
       for j=1:N
           if(i~=j)
               prod = prod * (xc(c)-x(j))/(x(i)-x(j));
           end
       end
       sum = sum + y(i)*prod;
   end
   yl(c)=sum;
end

%-------------------------------------------------------------------------%
figure(1);
plot(x,y,'k*',xc,yl,xc,ye,'--','Linewidth',2); grid on; grid minor;
xlabel('x');
ylabel('y');
title(['Comparison with Exact Function using '...
       , num2str(N) , ' Data Points']);
legend('Data Points','Lagrange Polynomial','Exact Function');

%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
%Calculating Lagrange derivative approximation for the xc points
dye=df(xc); %Exact Values for the comparing points
dyl=zeros(1,Nc);

for c=1:Nc
    sumi=0;
   for i=1:N
       sumj=0;
       for j=1:N
           if(j~=i)
               prod=1;
               for k =1 :N
                   if(k~=i && k~=j)
                       prod = prod * (xc(c)-x(k))/(x(i)-x(k));
                   end
               end
               sumj = sumj + prod/(x(i)-x(j));
           end
       end
       sumi = sumi + y(i) * sumj;
   end
   dyl(c)=sumi;
end

%-------------------------------------------------------------------------%
figure(2);
plot(xc,dyl,xc,dye,'--','Linewidth',2); grid on; grid minor;
xlabel('x');
ylabel('y^''');
title(['Comparison with Exact Derivative using '...
       , num2str(N) , ' Data Points']);
legend('Lagrange Derivative','Exact Derivative');
%-------------------------------------------------------------------------%
%-------------------------------------------------------------------------%
