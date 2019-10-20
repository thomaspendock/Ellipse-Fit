import numpy as np

'''
The best fit method below works as follows:

Use the fact that a 2x2 matrix A transforms a unit circle into an ellipse.

A matrix D (data matrix) has its SVD: D = U*S*transpose(V)

V2 is the first 2 columns of V. Because D, and therefore U and S are rank 2,
the rest of the columns in V2 are irrelevant.

So, D = U*S*transpose(V2)

U*S is 2x2 matrix that transforms the (x,y) coordinates in V2.

The points in V2 roughly lie on a circle, that is not necassarily a unit circle.

So a scale factor, the average length of the norm of the points in V2 is
correct the size difference in V2 and the unit circle.

So the transformation matrix A is U*S*scale, and this acts on the unit circle
to get an ellipse.
'''



def ellipse_fit(data, segments=100):
    '''Returns a set of 100 points that lie on the linear best fit
       ellispe of the data.'''
    size = len(data)
    np_data = np.transpose(np.array(data))

    # Center the data around the origin
    xmean = np_data[0].mean()
    ymean = np_data[1].mean()
    np_data[0] -= xmean
    np_data[1] -= ymean

    # Take the SVD of the data matrix
    U, S, V = np.linalg.svd(np_data)
    # The first 2 columns of V are relevant
    V2 = V[:2]

    # Find the average norm of all the x y points in V2
    scale = sum([np.linalg.norm(V2[:,i]) for i in range(size)])/size

    # Generate a list of angles and a list of points on a unit circle
    thetas = np.linspace(0, 2*np.pi, segments)
    unit_circle = np.stack((np.cos(thetas), np.sin(thetas)))

    # Transform the unit circle using the transformation matrix
    transform = scale * U.dot(np.diag(S))
    fit = transform.dot(unit_circle) + np.array([[xmean], [ymean]])

    return fit[0,:], fit[1,:]
