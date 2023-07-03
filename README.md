# Machine Learning Algorithms for Fake News Prediction


![GraphicalAbstract](https://github.com/larasouto/machine-learning-fake-news-prediction/assets/81490646/75cdf424-a0f3-4e6e-8ef3-1c5a7a274dd4)






#### This repository contains a collection of machine learning algorithms for detecting fake news. The algorithms included in this repository have been evaluated and tested for their effectiveness in identifying false information.



The following table shows the hyperparameters we adjusted for each algorithm to control the learning process. 

| Algorithm |                                       Hyperparameters                                           |
|:---------:|:-------------------------------------------------------------------------------------------:    |
|    SGD        |        loss=’hinge’, penalty=’l2’, alpha=0.0001, random_state=0, max_iter=5, tol=None       |
|     LR        |               random_state=0, solver=’saga’, multi_class=’ovr’, max_iter=10000              |
|    MLP        |            solver=’adam’, alpha=1e-4, hidden_layer_size=(100), random_state=None            |
|    SVM        |                      kernal=’linear’, probability=True, random_state=0                      |
|    ADA        | base_estimator=None, n_estimators=50, learning_rate=1, algorithm=SAMME.R, random_state=None |
|     NB        |                          alpha=1, fit_prior=True, class_prior=None                          |
|    BERT       |          'bert', 'bert-base-uncased', args=model_args, use_cuda=device                      |
|    BERTimbau  |      ’bert’, ’neuralmind/bert-base-portuguese-cased’, args=model_args, use_cuda=device      |

## How to run the models

To run the Jupyter Notebooks on your computer, you’ll need to install all the requirements.

```
pip install -r requirements.txt
```

Once you have all the requirements installed, you can open a command prompt or terminal window, navigate to the directory where the Jupyter Notebooks are located, and then run the command

```
jupyter notebook
```





