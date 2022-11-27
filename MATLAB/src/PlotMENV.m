function PlotMENV(M1_mean, ...
    M2_mean, ...
    M3_mean, ...
    M4_mean, ...
    M5_mean, ...
    M6_mean ...
    ,sujeto)

    h = figure(1);
    subplot(2,3,1)
    hold on
    plot(M1_mean(:,1))
    plot(M1_mean(:,2))
    plot(M1_mean(:,3))
    plot(M1_mean(:,4))
    title('M1 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    subplot(2,3,2)
    hold on
    plot(M2_mean(:,1))
    plot(M2_mean(:,2))
    plot(M2_mean(:,3))
    plot(M2_mean(:,4))
    title('M2 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    subplot(2,3,3)
    hold on
    plot(M3_mean(:,1))
    plot(M3_mean(:,2))
    plot(M3_mean(:,3))
    plot(M3_mean(:,4))
    title('M3 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    subplot(2,3,4)
    hold on
    plot(M4_mean(:,1))
    plot(M4_mean(:,2))
    plot(M4_mean(:,3))
    plot(M4_mean(:,4))
    title('M4 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    subplot(2,3,5)
    hold on
    plot(M5_mean(:,1))
    plot(M5_mean(:,2))
    plot(M5_mean(:,3))
    plot(M5_mean(:,4))
    title('M5 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    subplot(2,3,6)
    hold on
    plot(M6_mean(:,1))
    plot(M6_mean(:,2))
    plot(M6_mean(:,3))
    plot(M6_mean(:,4))
    title('M6 peaks envelope mean of channels')
    xlabel('Time'); ylabel('Amplitude');
    legend('ch1','ch2','ch3','ch4')
    hold off
    
    savelocation = strcat(sujeto,'/MENV.png');
    exportgraphics(h,savelocation)
end