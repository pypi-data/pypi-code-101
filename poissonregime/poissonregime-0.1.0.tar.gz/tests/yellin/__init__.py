import numpy as np
from numpy import log, sqrt
#import scipy.stats

def CMaxinf(CL1,If1,x):
	pass
def ConfLev(m, _, x):
	pass
def Cinf(y, f):
	pass
def y_vs_CLf(CMax,f):
	pass
def RZERO(Botmu,Topmu,mu,EPS,MAXF,FUp):
	pass

def Fup(x, I, CL1, If1, N1, muB1, MeanMax, FC1, FB1):
      NMax = 150000
      f = np.empty(NMax)
      fmin1 = np.empty(7)
      # Common/Fupcom/f
      CMax = 0.
      CMxinf = CMaxinf(CL1,If1,x)
      for m in range(N1):
         if muB1 != 0:
            f[m]=0.
            for I1 in range(N1-m):
               f[m]= max(f[m],(1.-(muB1/x))*(FC1[I1+m+1]-FC1[I1])+(muB1/x)*(FB1[I1+m+1]-FB1[I1]))
         if f[m] > fmin1[If1]:
          if x <= MeanMax:
            C = ConfLev(m, x * f[m],x)
          else:
            y = (m - x * f[m]) / sqrt(x * f[m])
            C = Cinf(y, f[m])
          
          if C > CMax:
             CMax = C
             mmax = m
          
          if f[m] >= 1:
              break
      return CMax - CMxinf, mmax


def UpperLim(CL,If,N,FC,muB,FB,Iflag):
    """
    C Calls y_vs_CLf, which calls DGAUSN, and ConfLev, which calls GAMDIS,
    C both of CERNLIB (libmathlib and libkernlib).
    C
    C Suppose you have a set of N events distributed in some 1-d variable
    C and want to know the CL confidence level upper limit on the mean of
    C the expected number of events.  Assume there's expected distribution
    C characterized by some cumulative probability function, on top of
    C which is an unknown background.  UpperLim is the optimum interval
    C upper limit, taking into account deviation between the observed
    C distribution and the predicted one.
    C
    C CL is the confidence level desired
    C If says which minimum fraction of the cumulative probability
    C   is allowed for seeking the optimum interval.  If=1,2,3,4,5,6,7
    C   corresponds to minimum cumulative probability interval =
    C   .00, .01, .02, .05, .10, .20, .50.
    C N is the number of events
    C FC: Given the foreground distribution whose shape is known, but whose
    C    normalization is to have its upper limit total expected number of
    C    events determined, FC(0) to FC(N+1), with FC(0)=0, FC(N+1)=1, and with 
    C    FC(i) the increasing ordered set of cumulative probabilities for the
    C    foreground distribution for event i, i=1 to N.
    C muB is the total expected number of events from known background.
    C FB is like FC but assuming the distribution shape from known background.
    C Iflag is the return code flag.:
    C   0: Normal return
    C  The flag bits correspond to:
    C   1: More than 5 iterations required.  Unusual, but should be ok.
    C   2: More than 10 iterations needed, but not obtained.  This may be serious.
    C    Other bits in Iflag refer to what happened in the last iteration
    C   4: y_vs_CLf returned status 1 at some time (extrapolated from f0=0.01)
    C   8: y_vs_CLf returned status 2 at some time (extrapolated from f0=1)
    C  16: The optimum interval had status 1.
    C  32: The optimum interval had status 2.
    C  64: Failure to solve CMax = CMaxbar.
    C 128: Couldn't solve CMax=CMaxbar because upperlim wants to be <0.
    C If something goes wrong which prevents return of correct results, the
    C program prints an error message and stops.
    """
    # Integer N,If,Iflag,NMax,I,m,Niter,mdebug,Istat,IflagOpt,MaxF,
    # NMax1,N1,If1,NCalls,I1
    Nmax = 150000
    # The number of iteration, Niter, can be 5 and it only occasionally needs
    # more for low mu and with lots of background.  Even then, 5 is enough to
    # almost always get almost exactly the same answer.
    Niter = 10
    f = np.arange(Nmax)
    fmin = np.array([0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5])
    eps = 0.001
    FB = np.arange(N + 1)
    fmin1 = fmin.copy()
    FC1 = np.arange(Nmax)
    FB1 = np.arange(Nmax)
    #Common/Fupcom/f,
    debug = False
    assert N < Nmax, 'number of events larger than Nmax-1'
    MeanMax=54.5
    FC[0] = 0.
    FC[-1] = 1.
    muB1 = muB
    
    fmin1[1:7] = fmin[1:7]
    if muB <= 0:
        FB[0] = 0
        FB[-1] = 1
        FC1 = FC.copy()
        FB1 = FB.copy()
    # For each m=0 to N find f(m), the maximum over all I from 0 to N-m of
    # FC(I+m+1)-FC(I).  Start out with mu0=float(N) and evaluate
    # CMax=CMaxinf(CL,If,mu).  For each m, y=y_vs_CLf(CMax,f(m)), and x from
    # y=(m-x)/sqrt(x).  Find the smallest value of x/f(m) and call
    # it the new mu.  Iterate until the fractional change of mu < eps, at which
    # time take UpperLim=mu.
    assert 0.8 < CL < 0.995
    assert 1 < If < 7
    if N == 0:
        UpperLim = log(1./(1.-CL))
        return UpperLim, 0
    if muB == 0:
        for m in range(N):
            f[m] = 0
            for i in range(N-m):
                f[m] = max(f[m], FC[i+m+1] - FC[i])
    # For some reason, the quick method of convergence sometimes fails
    # with muB>0.
    converged = False
    if muB == 0:
      mu0 = N * 1.
      for i in range(1,Niter):
         if mu0 < MeanMax:
             break
         CMax = CMaxinf(CL, If, mu0)
         mu = 1.e10
         for m in range(N):
            if muB != 0:
               f[m] = 0.
               for I1 in range(N-m):
                  f[m]=max(
                      f[m], 
                      (1. - (muB / mu0)) * (FC[I1 + m +1] - FC[I1]) + (muB / mu0) * (FB[I1 + m + 1] - FB[I1])
                  )
            if f[m] > fmin[If]:
               y = y_vs_CLf(CMax,f[m])
               #If(Istat.gt.2) Then
               #   Write(6,*) "y_vs_CLf returned with status",Istat
               #   Go to 50
               #EndIf
               #Iflag=Or(Iflag,4*Istat)
               y2 = y**2
               x = m + 0.5 * (y2 + sqrt(y2 * (4. * m + y2)))
               mutmp = x / f[m]
               if mutmp < mu:
                  mu = mutmp
                  # C IflagOpt will have the status of the optimum interval
                  if debug:
                     mdebug = m
                     fdebug = f[m]
                     ydebug = y
         
         if abs(mu0 - mu) / mu < eps and i > 1:
             # TODO: Go to 100
             converged = True
             break

         mu0 = max(muB, mu)
         if mu0 < muB:
             break
         if i == 5:
             # it looks like it won't converge (often with muB>0)
             Iflag = Iflag+1
             break
      else: # yes, this is a for/else statement
          Iflag=Iflag+2
          print("UpperLim did the maximum number of iterations, %d" % Niter)
    # end of muB if

    if not converged:
      # Come here if it's starting to look like mu<54.5, or if convergence
      # fails for mu>54.5.
      IflagOpt = 0
      MAXF = 500
      N1 = N
      CL1 = CL
      If1 = If
      Topmu = N + 4. * sqrt(N) + 5.
      Botmu = max(muB, log(1. / (1. - CL)))
      if muB > 0. and Fup(Botmu,1, CL1, If1, N1, muB1, MeanMax, FC1, FB1) > 0.:
          # It looks like UpperLim wants to be negative
         UpperLim=0.
         Iflag = Iflag + 192
         return UpperLim, Iflag
      R = RZERO(Botmu, Topmu, mu, eps, MAXF, Fup)
      assert not R < 0, "RZERO problem"
    
    UpperLim=mu-muB
    Iflag = Iflag | 16 * IflagOpt
    if debug:
        print(N,mdebug,fdebug,ydebug)
    return UpperLim, Iflag
