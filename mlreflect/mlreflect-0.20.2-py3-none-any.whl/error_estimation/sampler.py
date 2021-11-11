import emcee as e

class ParameterSampler:
    def __init__(self,
                 number_of_walkers: int = 32,
                 ):
        sampler = e.EnsembleSampler(number_of_walkers, 4, log_probability, args=[limits, corrected_intensity_log_interp,
                                                                         np.ones_like(
                                                                             corrected_intensity_log_interp) * 0.1,
                                                                         make_log_refl])

state = sampler.run_mcmc(start_labels_walkers, 100)
sampler.reset()

sampler.run_mcmc(state, 1000, progress=True)

samples = sampler.get_chain()