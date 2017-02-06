import numpy as np
import time
from numpy.linalg import eigvals
results = []
def run_experiment(niter=100): 
	K = 100
	for _ in xrange(niter):
		mat = np.random.randn(K, K)
		max_eigenvalue = np.abs(eigvals(mat)).max() 
		results.append(max_eigenvalue)
		return results
some_results = run_experiment()
print 'Largest one we saw: %s' % np.max(some_results)
