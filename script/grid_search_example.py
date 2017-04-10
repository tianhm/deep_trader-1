#!/usr/bin/env python
# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
from modules.neuralnet import NeuralNet
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

# Function to create model, required for KerasClassifier


def create_model(optimizer='rmsprop', init='glorot_uniform'):
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, kernel_initializer=init, activation='relu'))
    model.add(Dense(8, kernel_initializer=init, activation='relu'))
    model.add(Dense(1, kernel_initializer=init, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])
    return model

if __name__ == "__main__":
    factroy = NeuralNet()

    # create model
    model = KerasClassifier(build_fn=create_model, verbose=0)

    optimizers = ['rmsprop', 'adam']
    init = ['glorot_uniform', 'normal', 'uniform']
    epochs = [50, 100, 150]
    batches = [5, 10, 20]
    param_grid = dict(optimizer=optimizers, epochs=epochs,
                      batch_size=batches, init=init)
    grid = GridSearchCV(estimator=model, param_grid=param_grid)
    grid_result = grid.fit(X, Y)


# summarize results
    print("Best: %f using %s" %
          (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))
