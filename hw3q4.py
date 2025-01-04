import numpy as np 
import scipy.stats as stat
import matplotlib.pyplot as plt 



means = [3, 5]
s_1 = np.sqrt(10)
s_2 = 2
p = 0.9

sigma = [[(s_1)^2 , p*s_1*s_2], [p*s_1*s_2, (s_2)^2]]
cov = [[10, (0.9*2*np.sqrt(10))], [(0.9*2*np.sqrt(10)), 4]]


# # numpy's multivariate normal function, just generates 100 random samples from mean and covariance matrix 
samples = np.random.multivariate_normal(mean=means, cov=cov, size=100)

x = samples[:,0]
y = samples[:,1]

plt.scatter(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bivariate Normal Scatterplot')

plt.show()


x_mean = sum(x)/100
y_mean = sum(y)/100



s = np.array([x -x_mean,y-y_mean])
s_bar = np.transpose(s)

# # sample covariance: 1/n sum(x-x_bar)(x-x_bar)'

sample_cov = 1/100 * np.dot(s, s_bar)