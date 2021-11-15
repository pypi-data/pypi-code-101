from typing import List,Tuple
from dataclasses import dataclass
import numpy as np
import itertools
import copy

@dataclass()
class Monomial:
    '''
    A class to represent multivariate monomials.
    '''
    coef: float
    power: Tuple[int]
    def __post_init__(self):
        """
        Function that is run directly after the initialization.
        """
        self.n = len(self.power)
        
    def get_dimension(self):
        """
        Function to compute the dimension of the monomial.
        """
        return self.n

    def __add__(self, other):
        """
        Function to add two monomials and return a polynomial.
        Parameters:
            self (Monomial): reference to self
            other (Monomial): reference to the other Monomial
        Returns:
            sum_of_self_and_other (Monomial): The sum of self and other
        """
        m1 = copy.copy(self)
        m2 = copy.copy(other)
        sum_of_self_and_other = Polynomial([m1,m2])
        return sum_of_self_and_other
    
    def __sub__(self, other):
        """
        Function to subtract two monomials and return a polynomial.
        Parameters:
            self (Monomial): reference to self
            other (Monomial): reference to the other Monomial
        Returns:
            difference_of_self_and_other (Monomial): The difference of self and other
        """
        m1 = copy.copy(self)
        m2 = copy.copy(other)
        m2.coef = -m2.coef
        difference_of_self_and_other =  Polynomial([m1,m2])
        return difference_of_self_and_other
    
    def __mul__(self,other):
        """
        Function to multiply two monomials and return a polynomial.
        Parameters:
            self (Monomial): reference to self
            other (Monomial): reference to the other Monomial
        Returns:
            product_of_self_and_other (Monomial): The product of self and other
        """
        c = self.coef*other.coef
        p = tuple([p1+p2 for p1,p2 in zip(self.power,other.power)])
        product_of_self_and_other =  Monomial(c,p)
        return product_of_self_and_other

    def __process_power(_,power,marker):
        """
        Private function to process the powers of the terms in the monomial.
        Parameters:
            _ (Monomial): reference to self.
            power: the power
            marker: the marker
        Returns:
            str_of_term (str): A formated string of the term.
        """
        if power==0:
            return ''
        if power==1:
            return marker
        str_of_term = f'{marker}^{{{power}}}'
        return str_of_term

    def __append_coef(self,str_of_term):
        """
        Private function to process the powers of the terms in the monomial.
        Parameters:
            _ (Monomial): reference to self.
            str_of_term (str): A formated string of the term.
        Returns:
            str_of_monomial (str): A formated string of the entire monomial.
        """
        c = self.coef
        if c==0:
            str_of_monomial = ''
            return ''
        if str_of_term == '':
            if c>0:
                str_of_monomial = '+' + str(c)
            else:
                str_of_monomial = str(c)
            return str_of_monomial
        if c == 1:
            str_of_monomial =  '+'+str_of_term
            return str_of_monomial
        if c == -1:
            str_of_monomial =  '-'+str_of_term
            return str_of_monomial
        if c>0:
            str_of_monomial = '+' + str(c) + str_of_term
            return str_of_monomial
        str_of_monomial = str(c) + str_of_term
        return str_of_monomial
    
    def __repr__(self):
        """
        A function to return the string representation of this monomial.
        Parameters:
            self (Monomial): A reference to this.
        Returns:
            str_of_monomial: A formated string of the entire monomial.
        """
        markers = [f'x_{{{k}}}' for k in range(self.n)]
        str_of_term = ''.join([self.__process_power(p,m) for p,m in zip(self.power,markers)])
        str_of_monomial = self.__append_coef(str_of_term)
        return str_of_monomial

    @classmethod
    def get_one(cls,n):
        """
        A method that returns the constant monomial.
        Parameters:
            n (int): The order of the monomial
        Returns:
            one_monomial: The constant monomial
        """
        new_power = (0,)*n
        new_coef = 1
        one_monomial = Monomial(new_coef,new_power)
        return one_monomial
    
    @classmethod
    def get_variable(cls,idx,n):
        """
        A method that returns a single variable..
        Parameters:
            idx (int): The index of the variable
            n (int): The total number of variables
        Returns:
            monomial_n: the first order n-th variable
        """
        assert idx<n
        assert idx>=0
        assert n>=0
        new_power = tuple([int(k==idx) for k in range(n)])
        new_coef = 1
        monomial_n = Monomial(new_coef,new_power)
        return monomial_n
    
    def __call__(self,x):
        """
        A methode to evaluate the monomial expresisons at point x.
        Parameters:
            self (Polynomial): reference to self
            x (List[float]): the point at which the function is evaluated
        Returns:
            function_value (float): The function value at point x
        """
        function_value = self.coef * np.product([x[i]**self.power[i] for i in range(len(x))])
        return function_value

    
@dataclass()
class Polynomial:
    '''
    A class to represent multivariate polynomials
    Parameters:
        monomials(List[np.array]): A list of the monomials
    '''
    monomials: List[Monomial]
        
    def simplify(self):
        '''
        A function that returns a simplified version of self.
        The monomials with the same powers are added together and monomials with a
        coefficient of zero are eliminated.
        '''
        powers = [monomial.power for monomial in self.monomials]
        coefs = [monomial.coef for monomial in self.monomials]
        # Find the set of all unique powers.
        unique_powers = set(powers)
        all_monomials = []
        for p in unique_powers:
            # Find the occurances of power p in the list of all powers.
            indices = [i for i, x in enumerate(powers) if x == p]
            # Take the sum of the coefficients associated to a power p.
            sum_of_coef = np.sum([coefs[i] for i in indices])
            # Check if the coefficient is not zero, otherwise discard the monomial.
            if not sum_of_coef==0:
                new_monomial = Monomial(sum_of_coef,p)
                all_monomials += [new_monomial]
        return Polynomial(all_monomials)
    
    def get_dimension(self):
        """
        Function to get the dimension
        """
        return self.monomials[0].get_dimension()

    
    def __add__(self,other):
        '''
        A function to add two Polynomials together.
        The function creates a new list of monomials by copying the monomials of the arguments.
        and appending them to a new list.
        Parameters:
            self (Polynomial): left part of the sum
            other (Polynomial): right part of the sum
        Returns:
            sum_of_self_and_other (Polynomial): The sum of the two arguments 
        '''
        m_new = []
        if not(hasattr(other, 'monomials')):
            num = other
            one = Polynomial.get_one(self.get_dimension())
            other = other*one

        for m in itertools.chain(self.monomials,other.monomials):
            m_new += [copy.copy(m)]
        sum_of_self_and_other = Polynomial(m_new)
        return sum_of_self_and_other
    
    def __sub__(self, other):
        '''
        A function to subtract two Polynomials together.
        The function multiplies the right polynomial by -1 and adds the result.
        Parameters:
            self (Polynomial): left part of the subtraction
            other (Polynomial): right part of the subtraction
        Returns:
            difference_of_self_and_other (Polynomial): The difference of the two arguments 
        '''
        difference_of_self_and_other = self + (-1)*other
        return difference_of_self_and_other
    
    def __mul__(self,other):
        '''
        A function to multiply two Polynomials together.
        The function multiplies self and other by using the rules of pylonomial multiplication.
        Parameters:
            self (Polynomial): left part of the product
            other (Polynomial): right part of the product
        Returns:
            product_of_self_and_other (Polynomial): The product of the two arguments 
        '''
        new_monomials = []
        for m1 in self.monomials:
            for m2 in other.monomials:
                new_monomials += [m1 * m2]
        product_of_self_and_other = Polynomial(new_monomials)
        return product_of_self_and_other
        
    def __rmul__(self,scalar):
        '''
        A function that implements scalar multiplication. 
        
        Parameters:
            self (Polynomial): left part of the product
            scalar (Polynomial): a scalar to be multiplied by the self.
        Returns:
            scalar_product (Polynomial): The product of the two arguments 
        '''
        monomials_new = []
        for m in self.monomials:
            monomials_new += [Monomial(scalar*m.coef,m.power)]
        scalar_product = Polynomial(monomials_new)
        return scalar_product
    
    def __repr__(self):
        """
        Implementation of the representation function as a string.
        Parameters:
            self (Polynomial): reference to self.
        Returns:
            representation (str): String to represent self
        """
        poly = ''.join([str(m) for m in self.monomials])
        representation = poly.lstrip('+')
        return representation
    
    def __pow__(self,power):
        """
        Implementation of powers of a polynomial.
        Parameters:
            self (Polynomial): reference to self.
            power (int): The power to which we raise self
        Returns:
            power_of_polynomial (Polynomial): String to represent self
        """
        if power==0:
            nb_of_var = len(self.monomials[0].power)
            power_of_polynomial = Polynomial.get_one(nb_of_var)
            return power_of_polynomial
        
        power_of_polynomial = self
        for _ in range(power-1):
            power_of_polynomial = power_of_polynomial * self
        return power_of_polynomial
    
    def __first_order_derivative(self,var):
        """
        Private function that implements the first order derivation of self.
        Parameters:
            self (Polynomial): reference to self.
            var (int): The variable for which we calculate the derivative.
        Returns:
            first_order_differentiation (Polynomial): The first order derivative.
        """
        new_monomials = []
        for m in self.monomials:
            if m.power[var]>0:
                new_coef = m.coef * m.power[var]
                new_power = [p for p in m.power]
                new_power[var] -=1
                new_power = tuple(new_power)
                new_monomials += [Monomial(new_coef,new_power)]
        first_order_differentiation = Polynomial(new_monomials)
        return first_order_differentiation
    
    def d(self,var,order=1):
        """
        Function that calculates the n-th order derivation of self.
        Parameters:
            self (Polynomial): reference to self.
            var (int): The variable for which we calculate the derivative.
            order (int): The order of the differentiation.
        Returns:
            nth_order_differentiation (Polynomial): The first order derivative.
        """
        nth_order_differentiation = self
        for k in range(order):
            nth_order_differentiation = nth_order_differentiation.__first_order_derivative(var)
        return nth_order_differentiation

    @classmethod
    def get_one(cls,n):
        """
        A method that returns the constant Polynomial.
        Parameters:
            n (int): The order of the monomial
        Returns:
            one_polynomial: The constant monomial
        """
        one_monomial = Monomial.get_one(n)
        one_polynomial = Polynomial([one_monomial])
        return one_polynomial
    
    @classmethod
    def get_variable(cls,idx,n):
        """
        A method that returns a single variable..
        Parameters:
            idx (int): The index of the variable
            n (int): The total number of variables
        Returns:
            polynomial_n (Polynomial): the first order n-th variable
        """
        assert idx < n
        assert idx >= 0
        assert n >= 0
        monomial_n = Monomial.get_variable(idx,n)
        polynomial_n = Polynomial([monomial_n])
        return polynomial_n
    
    @classmethod
    def get_all_variables(cls,n):
        """
        A methode that returns all n variables without the constant term.
        Parameters:
            n (int): The total number of variables
        Returns:
            all_variables (tuple[Polynomial]): the first order n-th variable
        """
        assert n >= 0
        all_variables = tuple([Polynomial.get_variable(k,n) for k in range(n)])
        return all_variables
    
    def __call__(self,x):
        """
        A methode to evaluate the polynomial expresisons at point x.
        Parameters:
            self (Polynomial): reference to self
            x (List[float]): the point at which the function is evaluated
        Returns:
            function_value (float): The function value at point x
        """
        function_value = np.sum([m(x) for m in self.monomials])
        return function_value
