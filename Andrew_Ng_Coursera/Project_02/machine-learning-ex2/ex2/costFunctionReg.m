function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta);

% You need to return the following variables correctly 
J = 0;
reg = 0;
sum_J = 0;
sum_grad = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

% Regularization Parameter
for j = 2:n
  % NOTE: Start at j = 2 because theta(0) (or theta(1) because arrays in 
  % octave start at 1) does NOT get regularized.
  reg += theta(j, 1)^2;
endfor

reg *= (lambda / (2*m));


% Calculate J (Cost function)
for iter = 1:m
  hx = sigmoid(theta' * X(iter, :)');
  p1 = -y(iter) * log(hx);
  p2 = (1 - y(iter)) * log(1 - hx);
  sum_J += p1 - p2;
endfor

J = (1/m) * sum_J + reg;

% sigmoid input
in = theta(1);
for i = 2:length(theta)
  
endfor

% Gradient of theta 0
sum = 0;
for i = 1:m
  hx = sigmoid(theta' * X(i,:)');
  sum += ((hx - y(i))*X(i,1));
endfor
grad(1) = (1/m) * sum;

% Gradient for theta 1, 2, 3, ......
h = sigmoid(X*theta);
grad = (1/m * X' * (h - y)) + (lambda/m * grad);

% =============================================================

end
