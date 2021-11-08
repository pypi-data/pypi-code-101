from gwpopulation.conversions import convert_to_beta_parameters
from gwpopulation.hyperpe import HyperparameterLikelihood, xp
from gwpopulation.models.spin import (
    iid_spin,
    iid_spin_magnitude_beta,
    independent_spin_magnitude_beta,
)


def prior_conversion(parameters):
    """Wrapper around conversion for prior constraints"""
    for key in ["amax", "amax_1", "amax_2"]:
        if key not in parameters:
            parameters[key] = 1
    parameters, _ = convert_to_beta_parameters(parameters)
    return parameters


KNOWN_ARGUMENTS = {
    iid_spin: ["mu_chi", "sigma_chi", "xi_spin", "sigma_spin"],
    iid_spin_magnitude_beta: ["mu_chi", "sigma_chi"],
    independent_spin_magnitude_beta: [
        "mu_chi_1",
        "mu_chi_2",
        "sigma_chi_1",
        "sigma_chi_2",
    ],
}


class MinimumEffectiveSamplesLikelihood(HyperparameterLikelihood):
    def _compute_per_event_ln_bayes_factors(self):
        """
        Compute the per event ln Bayes factors.

        This method imposes a condition that the number of effective
        samples per Monte Carlo integral must be at least as much
        as the total number of events. Otherwise the lnBF is set to
        - infinity.

        Returns
        -------
        array-like
            The ln BF per event subject to having a sufficient number
            of independent samples.
        """
        per_event_bfs, n_effectives = self.per_event_bayes_factors_and_n_effective()
        per_event_bfs *= n_effectives > self.n_posteriors
        return xp.log(per_event_bfs)

    def per_event_bayes_factors_and_n_effective(self):
        weights = self.hyper_prior.prob(self.data) / self.sampling_prior
        per_event_bfs = xp.sum(weights, axis=-1)
        n_effectives = xp.nan_to_num(per_event_bfs ** 2 / xp.sum(weights ** 2, axis=-1))
        per_event_bfs /= self.samples_per_posterior
        return per_event_bfs, n_effectives
