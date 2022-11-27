function PBperChMethod( ...
    thumb_arr, ...
    index_arr, ...
    middle_arr, ...
    ring_arr, ...
    pinky_arr, ...
    hand_arr, ...
    method_name, ...
    abr, ...
    sujeto)

    h = figure(1);
    subplot(2,2,1)
    boxplot([thumb_arr(:,1),index_arr(:,1),middle_arr(:,1),ring_arr(:,1),pinky_arr(:,1),hand_arr(:,1)],...
        {'M1','M2','M3','M4','M5','M6'})
    ch_title = strcat(abr,' Box Plot Ch2');
    title(ch_title)
    ylabel(method_name)
    xlabel('Movements')
    
    subplot(2,2,2)
    boxplot([thumb_arr(:,2),index_arr(:,2),middle_arr(:,2),ring_arr(:,2),pinky_arr(:,2),hand_arr(:,2)],...
        {'M1','M2','M3','M4','M5','M6'})
    ch_title = strcat(abr,' Box Plot Ch4');
    title(ch_title)
    ylabel(method_name)
    xlabel('Movements')
    
    subplot(2,2,3)
    boxplot([thumb_arr(:,3),index_arr(:,3),middle_arr(:,3),ring_arr(:,3),pinky_arr(:,3),hand_arr(:,3)],...
        {'M1','M2','M3','M4','M5','M6'})
    ch_title = strcat(abr,' Box Plot Ch6');
    title(ch_title)
    ylabel(method_name)
    xlabel('Movements')
    
    subplot(2,2,4)
    boxplot([thumb_arr(:,4),index_arr(:,4),middle_arr(:,4),ring_arr(:,4),pinky_arr(:,4),hand_arr(:,4)],...
        {'M1','M2','M3','M4','M5','M6'})
    ch_title = strcat(abr,' Box Plot Ch8');
    title(ch_title)
    ylabel(method_name)
    xlabel('Movements')

    savelocation = strcat(sujeto,'/',abr,'.png');
    exportgraphics(h,savelocation)
end