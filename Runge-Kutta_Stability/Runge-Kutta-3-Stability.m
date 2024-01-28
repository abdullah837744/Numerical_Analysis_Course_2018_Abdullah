%% Stability Region
% Generating mesh
xm=linspace(-2,2,400);
ym=linspace(-2,2,400);
xo = zeros(1,400); 
yo = zeros(1,400);
[x,y]=meshgrid(xm,ym);
% Define the complex number
z=x+i*y;
% Growth Factor
GF = 1+(3*z/2)+(z.^3/6) ;
%GF = 1+z ;
zlevel = abs(GF);
% Plot
figure(1)
plot(xm,yo,'k-','LineWidth',2);hold on
plot(xo,ym,'k-','LineWidth',2)
contour(x,y,zlevel,[1 1],'b--','LineWidth',2)
hold off ;grid on ;
ylim([-1 1])
xlim([-2 1])
title('Stability digram for RK-3')
xlabel('h*alpha_R'); ylabel('h*alpha_I');
h = figure(1);
saveas(h,'Stability digram for RK-3.png');
