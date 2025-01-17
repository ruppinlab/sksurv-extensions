"""
sksurv_extensions is a library of custom extensions and changes to sksurv
"""

from sklearn.utils.metaestimators import if_delegate_has_method
from sklearn_extensions.pipeline import ExtendedPipeline


@if_delegate_has_method(delegate='_final_estimator')
def predict_cumulative_hazard_function(self, X, **predict_params):
    """Predict cumulative hazard function.

    The cumulative hazard function for an individual
    with feature vector :math:`x` is defined as

    .. math::

        H(t \\mid x) = \\exp(x^\\top \\beta) H_0(t) ,

    where :math:`H_0(t)` is the baseline hazard function,
    estimated by Breslow's estimator.

    Parameters
    ----------
    X : array-like, shape = (n_samples, n_features)
        Data matrix.

    Returns
    -------
    cum_hazard : ndarray, shape = (n_samples,)
        Predicted cumulative hazard functions.
    """
    Xt, predict_params = self._transform_pipeline('predict',
                                                  X, predict_params)
    return self.steps[-1][-1].predict_cumulative_hazard_function(
        Xt, **predict_params)


@if_delegate_has_method(delegate='_final_estimator')
def predict_survival_function(self, X, **predict_params):
    """Predict survival function.

    The survival function for an individual
    with feature vector :math:`x` is defined as

    .. math::

        S(t \\mid x) = S_0(t)^{\\exp(x^\\top \\beta)} ,

    where :math:`S_0(t)` is the baseline survival function,
    estimated by Breslow's estimator.

    Parameters
    ----------
    X : array-like, shape = (n_samples, n_features)
        Data matrix.

    Returns
    -------
    survival : ndarray, shape = (n_samples,)
        Predicted survival functions.
    """
    Xt, predict_params = self._transform_pipeline('predict',
                                                  X, predict_params)
    return self.steps[-1][-1].predict_survival_function(Xt, **predict_params)


ExtendedPipeline.predict_cumulative_hazard_function = (
    predict_cumulative_hazard_function)
ExtendedPipeline.predict_survival_function = (
    predict_survival_function)
