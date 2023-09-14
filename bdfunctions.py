from parameters_for_figures import *
"""
    This code contains the rate functions calculations
    sigma_plot calculates: sigma*(P - H)
    hill_plot calculates: kappa*(P - H)*H**n/(H**n + K**n)
    reset_plot calculates: rho*P
    zero reference adds a zero reference line to all plots, it is: 0*H
"""


def sigma_plot(Hl, s, P=P):
    """
    :param Hl: list of H values to calculate the function
    :param s: sigma rate for calculation
    :return: list of sigma*(P - H) values
    """
    to_return = []
    for h in Hl:
        value = s * (P - h)
        to_return.append(value)

    return to_return


def hill_plot(Hl, k=k, n=n, K=K, P=P):
    """
    :param Hl: list of H values to calculate the function
    :param k: kappa parameter from Hill rate
    :param n: hill function exponent
    :return: list of k*(P - h)*h**n/(h**n + K**n) values
    """
    to_return = []
    for h in Hl:
        value = k*(P - h)*h**n/(h**n + K**n)
        to_return.append(value)

    return to_return


def reset_plot(Hl, p=p):
    """
    :param Hl: list of H values to calculate the function
    :param p: rho parameter for reset rate
    :return: returns -\rho*P for all H values
    """
    to_return = []
    for h in Hl:
        value = -p*h
        to_return.append(value)

    return to_return


def zero_reference(Hl):
    """
    :param Hl: list of H values to calculate the function
    :return: returns 0*H for every H value
    """
    to_return = []
    for _ in Hl:
        value = 0
        to_return.append(value)

    return to_return


def sum_lists(L1, L2):
    """
        Sum two lists values term by term
    """
    L3 = []
    for e1, e2 in zip(L1, L2):
        L3.append(e1 + e2)

    return L3
