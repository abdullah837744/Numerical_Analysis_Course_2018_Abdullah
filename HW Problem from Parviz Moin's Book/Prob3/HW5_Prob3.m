%% Stability Region
% Generating mesh
xm=linspace(-4,2,600);
ym=linspace(-4,4,800);
xo = zeros(1,800); 
yo = zeros(1,600);
[x,y]=meshgrid(xm,ym);
% Define the complex number
z=x+i*y;
% Growth Factor
GF = 1+z+(z.^2)/2+(z.^3)/6 ;
%GF = 1+z ;
zlevel = abs(GF);
% Plot
figure(1)
plot(xm,yo,'k-','LineWidth',2);hold on
plot(xo,ym,'k-','LineWidth',2)
contour(x,y,zlevel,[1 1],'b--','LineWidth',2)
hold off ;grid on ;
ylim([-3 3])
%xlim([-2 1])
title('Stability digram for RK-3')
xlabel('h*alpha_R'); ylabel('h*alpha_I');
h = figure(1);
saveas(h,'Stability digram for RK-3.png');
