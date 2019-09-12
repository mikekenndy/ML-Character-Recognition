function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));
[row, col] = size(z);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

iter = 1;
for i = 1:col
  for j = 1:row
    g(iter) = 1 / (1 + e.^(-z(j,i)));
    iter += 1;
  endfor
endfor


% =============================================================

end
