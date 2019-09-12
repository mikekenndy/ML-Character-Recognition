function disp = displayPixel(x)
  
  iter = 1;
  
  for i = 1:20
    for j = 1:20
      disp(i,j) = x(iter);
      iter++;
    endfor       
  endfor
   
end