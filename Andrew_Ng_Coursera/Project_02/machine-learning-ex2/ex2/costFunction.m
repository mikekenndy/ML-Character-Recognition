function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y);  % number of training examples
n = length(theta);
sum_j = 0;
sum_grad = 0;

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));
grad = theta;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

h = sigmoid(X*theta);

% Vectorized implementation
%J = (1/m) * (-y' * log(h) - (1 - y)' * log(1 - h));

% Non-vectorized implementation
s = 0;
for iter = 1:m
  hx = sigmoid(theta' * X(iter, :)');
  p1 = -y(iter) * log(hx);
  p2 = (1 - y(iter)) * log(1 - hx);
  s += (p1 - p2);
endfor

J = (1/m) * s;

% Vectorized implementation
grad = 1/m * X' * (h - y);

%grad = theta;
%Non-vectorized implementation - DOES NOT WORK, NOT SURE WHY
%for k = 1:10
%  for j = 1:n
%    h = sigmoid(theta' * X');
%    grad(j) = grad(j) - (1/m) * sum((h-y) * X(:,n));
%  endfor
%endfor

% =============================================================

end