function acc = Test_Dendrite(x_test, y_test,weights, cases)
    tic;
    true = 0;
    acc = 0;
    
    for i=1:cases
        output = predictDMNN(x_test(i,:),weights);
        yfit = find(output);
    
        if(i <= cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>cases/6 && i<=2*cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>2*cases/6 && i<=3*cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>3*cases/6 && i<=4*cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>4*cases/6 && i<=5*cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        elseif(i>5*cases/6)

            if(yfit == y_test(i,1))
                true = true + 1;
            end
        end
    
    end
    
    acc = round((true/cases)*100,2);
    toc;
    fprintf('Accuracy %f\n',acc)

end