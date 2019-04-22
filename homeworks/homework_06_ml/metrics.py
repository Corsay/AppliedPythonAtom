#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :param derivative: if true return mse derivative regression loss
    :return: loss
    """
    # mse = ( 1 / N ) * sum( (y_true[i] - y_hat[i]) ^ 2 )
    # mse = mean( (y_true[i] - y_hat[i]) ^ 2 )
    # mse_derivative = ( -2 / N ) * sum( y_true[i] - y_hat[i] )
    # mse_derivative = -2 * mean( y_true[i] - y_hat[i] )
    diff = y_true - y_hat

    if derivative:
        return np.mean(diff) * -2

    return np.mean(diff ** 2)


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    # mae = ( 1 / N ) * sum( |y_true[i] - y_hat[i]| )
    # mae = mean( |y_true[i] - y_hat[i]| )
    return np.mean(np.abs(y_true - y_hat))


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    # r2 = 1 - sum( (y_true[i] - y_hat[i]) ^ 2 ) / sum( (y_true[i] - mean) ^ 2 )
    # mean = sum(y_true) / N
    m = np.mean(y_true)
    return 1 - np.sum((y_true - y_hat) ** 2) / np.sum((y_true - m) ** 2)
