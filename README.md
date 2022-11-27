# EMG_Classification
> Fine hand movements classification and Incremental Learning.

This project retrieved Electromyographic signals or EMG signals from 6 different hand movements.
In order to obtain the best results, 9 different classifier were used to train the model.
To increase the accuracy of the model, Warm Start and Partial Fit are used to readjust the model's performance.

Each classifier uses 5 K-Folds, Cross validation and 36 time-domain features.
These classifiers are: LDA, SVM, MLP and NNET.
Some classifiers have different hyperparameters to obtain the 9 mentioned.

The dataset consists of 30 subjects, and 240 trials.

![](header.png)


## Studies

* Single Subject Independent (SSI)
    * This studie trains the model using just one subject from the 30.
* Leave One Out Participant (LOOP)
    * This studies trains the model using 29 subjects from the dataset and tests with the remaining subject.
* Warm Start and Partial Fit
    * Readjusting the model's performance by using WS and PF
* ANOVA and Tukey's HSD
    * Obtain models performances' statistics.

## Scripts

* main.ipynb
    * This script is the source of the results, it obtains the models of the training phase and tests.
* ANOVA_TUKEY.ipynb
    * This script computes the statistical tests from the classifiers
* PFvsWSInstro.ipynb
    * To comprehend how partial fit and warm start is computed using classifiers
* LOOP_OL_Tables.ipynb, SSI_OL_Tables.ipynb and WSvsPF_OL_Tables.ipynb
    * Create overleaf LATEX tables of the results.
* SSInLOOP.ipynb
    * Test the studies SSI and LOOP 
* Matlab/src/main2.mlx
    * First approach to EMG data analysis and classifiers.


## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)
