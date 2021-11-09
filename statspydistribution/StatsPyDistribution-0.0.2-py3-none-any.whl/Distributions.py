class Distributions:

    def __init__(self, x, y, m, v, mo, me, sk, kr, mgf):
        self._x = x
        self._y = y
        self._cdf = []
        self._mgf = mgf
        self._mn = m
        self._var = v
        self._mod = mo
        self._med = me
        self._skw = sk
        self._krt = kr

    def name(self):
        raise NotImplementedError

    def get_data(self):
        return {'x': self._x, 'y': self._y}

    def frequency_density_formula(self):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__

    def notation(self):
        """
        Notation of distribution
        :rtype: string
        """
        raise NotImplementedError

    def parameters(self):
        """
        Parameters of distribution
        :rtype: string
        """
        raise NotImplementedError

    def support(self):
        """
        it is x axis value on which probability mass function is being genereated
        :rtype: list of object
        """
        return self._x

    def probability_mass_function_value(self):
        return self._y

    def cumulative_distribution_function_value(self):
        if len(self._cdf) == 0:
            for idx, val in enumerate(self._y):
                if idx == 0:
                    self._cdf.append(self._y[idx] / 10)
                else:
                    self._cdf.append(self._cdf[idx - 1] + self._y[idx] / 10)
        return self._cdf

    def mean(self):
        return self._mn

    def mode(self):
        return self._mod

    def median(self):
        return self._med

    def variance(self):
        return self._var

    def skewness(self):
        return self._skw

    def kurtosis(self):
        return self._krt

    def movement_generating_function_value(self):
        return self._mgf

    def plot(self):
        raise NotImplementedError
