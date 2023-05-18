# Machine Learning Algorithms for Fake News Prediction

### This repository contains a collection of machine learning algorithms for detecting fake news. The algorithms included in this repository have been evaluated and tested for their effectiveness in identifying false information.

The following table shows the hyperparameters we adjusted for each algorithm to control the learning process: 

| Algorithm |                                       Hyperparameters                                           |
|:---------:|:-------------------------------------------------------------------------------------------:    |
|    SGD        |        loss=’hinge’, penalty=’l2’, alpha=0.0001, random_state=0, max_iter=5, tol=None       |
|     LR        |               random_state=0, solver=’saga’, multi_class=’ovr’, max_iter=10000              |
|    MLP        |            solver=’adam’, alpha=1e-4, hidden_layer_size=(100), random_state=None            |
|    SVM        |                      kernal=’linear’, probability=True, random_state=0                      |
|    ADA        | base_estimator=None, n_estimators=50, learning_rate=1, algorithm=SAMME.R, random_state=None |
|     NB        |                          alpha=1, fit_prior=True, class_prior=None                          |
|    BERT       |      ’bert’, ’neuralmind/bert-base-portuguese-cased’, args=model_args, use_cuda=device      |
|    BERTimbau  |      ’bert-base-uncased’, num_labels=2, output_attentions=False, output_hidden_states=False)|
