function PlotMENVperMov(Mov, whichmov)
    figure;
    color = ['b', 'r', 'g', 'c'];
    for i=1:4
        subplot(2,2,i)
        plot(Mov(:,i), color(i))
        xlabel('Time')
        ylabel('Peak Envelope Mean Value')
        title(strcat('Movement:',num2str(whichmov), ', Channel:', num2str(i)))
    end
end