from ndn4sid import polynomials


def main():
    # Define 3 variables and one
    nb_var = 3
    x0,x1,x2 = polynomials.Polynomial.get_all_variables(nb_var)
    one = polynomials.Polynomial.get_one(nb_var)

    # Perform arithmetics on a polynomial.
    p1 = (x0+x1-2*x2-3*one)**2
    # Simplify the expression
    p1 = p1.simplify()
    
    # [4,1,1] is a known root of the polynomial, we can check this.
    root = [4,1,1]
    p1_value = p1(root)
    assert p1_value == 0

    # [1,2,3] is not a root of p1 and has a function value of 36
    not_a_root = [1,2,3]
    p1_value = p1(not_a_root)
    assert p1_value == 36

    # Analytic value of the derivative with respect to x0
    p1_der = 2*(x0+x1-2*x2-3*one)
    p1_calculated_der = p1.d(0)
    p_diff = (p1_der-p1_calculated_der).simplify()
    
    # Check if the polynomial is zero.
    assert str(p_diff) == ''







if __name__ == "__main__":
    main()