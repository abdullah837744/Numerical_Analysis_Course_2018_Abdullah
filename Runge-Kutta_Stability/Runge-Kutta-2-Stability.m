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
GF = 1+z+(z.^2/2) ;
%GF = 1+z ;
zlevel = abs(GF);
% Plot
figure(1)
plot(xm,yo,'k-','LineWidth',2);hold on
plot(xo,ym,'k-','LineWidth',2)
contour(x,y,zlevel,[1 1],'b--','LineWidth',2)
hold off ;grid on ;
title('Stability digram for RK-2')
xlabel('h*Lambda_R'); ylabel('h*Lambda_I');
h = figure(1);
saveas(h,'Stability digram for RK-2.png');
