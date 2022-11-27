function acc = TestPercentages(x_test,y_test,trials,model,sujeto,whichmodel)
    tic;
    true = 0;
    g1 = zeros(1,trials);
    g2 = zeros(1,trials);
    acc = 0;
    for i=1:trials
        yfit = model.predictFcn((x_test(i,:)));
        if(i <= trials/6)
            g1(i) = 1;
            g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>trials/6 && i<=2*trials/6)
            g1(i) = 2;
            g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>2*trials/6 && i<=3*trials/6)
            g1(i) = 3;
            g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>3*trials/6 && i<=4*trials/6)
            g1(i) = 4;
            g2(i) = yfit;g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>4*trials/6 && i<=5*trials/6)
            g1(i) = 5;
            g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>5*trials/6)
            g1(i) = 6;
            g2(i) = yfit;
            if(yfit == y_test(i,1))
                true = true + 1;
            end
        end    
    end
    acc = true/trials;
    fprintf('Test accuracy %2f\n',acc)   
    h = figure(2);
    C = confusionchart(fliplr(g1),fliplr(g2), ... %C = confusionchart(g1,g2, ...
        'Title',strcat('All vs',sujeto), ...
        'RowSummary','row-normalized');

    savelocation = strcat(sujeto,'/','CM_',whichmodel,'_',num2str(acc),'.png');
    exportgraphics(h,savelocation)
    
    toc;
end