function visualize_attention_decay()
    figure('Position', [100 100 1200 400]);
    context_lengths = [1000, 10000, 100000];
    for i = 1:length(context_lengths)
        ctx_len = context_lengths(i);
        query_pos = ctx_len;
        positions = 1:ctx_len;
        recency = exp(-0.001 * (query_pos - positions));
        distance_penalty = 1 ./ (1 + 0.00001 * (query_pos - positions).^2);
        weights = recency .* distance_penalty;
        weights = weights / sum(weights);
        subplot(1,3,i);
        semilogy(positions, weights, 'LineWidth', 1.5);
        title(['Context Length: ', num2str(ctx_len)]);
        xlabel('Token Position');
        ylabel('Attention Weight (log scale)');
        grid on;
    end
end