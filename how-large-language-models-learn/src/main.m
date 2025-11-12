% Loss function and its derivative
f = @(x) (x - 3).^2 + 2;
df = @(x) 2 * (x - 3);

% Gradient descent
x = 0;
eta = 0.1;
history = x;

for i = 1:20
    x = x - eta * df(x);
    history(end+1) = x;
end

% Plot
x_vals = linspace(-1, 7, 100);
plot(x_vals, f(x_vals), 'b-', 'LineWidth', 2);
hold on;
plot(history, f(history), 'ro-', 'MarkerSize', 8, 'LineWidth', 1.5);
xlabel('Parameter Value');
ylabel('Loss');
legend('Loss Function', 'Learning Path');