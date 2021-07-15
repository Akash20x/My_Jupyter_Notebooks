Kernel Density Estimation to calculate the estimated probability density function.

KDEs are generally considered better than histograms to examine the distribution of the data since histograms can change drastically based on the number of bins and location of cuts. KDEs are much are robust in this regard and are calculated by fitting a kernel function at each point in the distribution, then summing up the contributions at each point and normalizing it. This gives us a probability estimate for each point in the distribution.
