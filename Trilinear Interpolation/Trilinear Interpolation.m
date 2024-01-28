%%% Trilinear Interpolation %%%% Abdullah %%%%%
%% Given function
% F = x^2 * sin(y) * exp(z) ;
%% Grid points
xid = [0.0; 0.5; 1.0] ; 
yid = [0.0; 0.5; 1.0] ;
zid = [0.0; 0.5; 1.0] ;
%% Interpolated point
cx = 0.3 ; cy = 0.3 ; cz = 0.3 ; 
%% Computation
F = zeros(3,3,3) ;  
for i = 1:3
    id = (i-1)*0.5 ;
    for j = 1:3
       jd =  (j-1)*0.5 ;
        for k = 1:3
           kd =  (k-1)*0.5 ; 
            F(i,j,k) = id^2 * sin(jd) * exp(kd) ;
        end
    end
end
%% Relative Distance from above and below points 
xd = (cx-xid(1))/(xid(2)-xid(1)) ;
yd = (cy-yid(1))/(yid(2)-yid(1)) ;
zd = (cz-zid(1))/(zid(2)-zid(1)) ;
%% x_shifting
C00 = F(1,1,1)*(1-xd) + F(2,1,1)*xd ;
C01 = F(1,1,2)*(1-xd) + F(2,1,2)*xd ;
C10 = F(1,2,1)*(1-xd) + F(2,2,1)*xd ;
C11 = F(1,2,2)*(1-xd) + F(2,2,2)*xd ; 
%% y_shifting
C0 = C00*(1-yd) + C10*yd ;
C1 = C01*(1-yd) + C11*yd ;
%% z_shifting
C = C0*(1-zd) + C1*zd ;


        
            





