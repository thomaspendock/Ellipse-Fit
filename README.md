Python version: 3.5.2
To run the answer for part 1, run part1.py.
To run the answer for part 2, run part2.py.

Note: The graphics window may appear behind all the other windows or may be minimized at first.

Both part1.py and part2.py use the GUI class, which is implemented in the graphics folder. 

GUI class:
The GUI class uses a tkinter window and canvas, along with a simple button at the bottom. Upon initialization, the GUI draws the grid of 20x20 points. The GUI uses arrays to keep track of the IDs of the grid points, all circles drawn by the user, and the best fit ellipse. The points are kept in a 2D array which maps index of the point to ID of the point. This allows O(1) complexity when trying to find the closest point given x,y coordinates, as x,y can easily be converted to i,j indexes, and then the id of a point can be looked up in the array.

part1.py and part2.py use an instance of the GUI and send it different commands bounded by user mouse movements and clicks.

PART1:
The mouse press event is bound to tell the GUI that the mouse is being held down.

The mouse motion event is bound to expand or close the circle drawn on the canvas if the mouse button is down.

Once the mouse is released, the user's circle is drawn on the canvas. A parametric equation is found for this circle, and a set of angles ranging from 0 to 2pi are generated. Each angle, is plugged into the circle's equation, and the closest point on the grid is colored at each iteration. The number of angles to sample is circumference of the circle divided by the size of a point on the grid. Also, during each iteration, the minimum and maximum distance from the middle of the drawn circle to the colored points is tracked. The smallest and largest circles are drawn with the same center as the drawn circle.

PART2:
Mouse press event is bound to tell the GUI that the mouse is being held down, and color a point if the mouse coords are inside the circumference of the circle.

Mouse motion is bound to color points that are hit while the mouse is being dragged around. The user can just drag their cursor around and color points faster than clicking each individual one.

The release of the mouse simply tells the GUI that the mouse is up.

A "Generate" button is also placed under the clear button on the canvas. This generates the best fit ellipse based on the coordinates of all the colored points. The fit function is implemented in fitting/best_fit.py.

The function uses the fact that a 2x2 matrix can act on a unit circle to transform it into an ellipse, since a linear transformation is a rotation and stretch. If a 2x2 matrix is applied to a 2xn unit circle matrix, where each vector is a x,y sample of the unit circle, then the result is an ellipse.

The data matrix is a 2xn matrix where each vector is the x,y coordinate of a colored point on the grid. First, the function centers the data around the origin by subtracting the centroid coordinate. The SVD of the data produces U,S,V where U*S is a rotation (U) and a stretch (S), and is a 2x2 transformation matrix. U*S is applied to V (the function only considers the first 2 columns of V, since there are only 2 singular values and the last n-2 columns are irrelevant). I thought of each column vector in transpose(V) as an x,y coordinate on a rough circle, that is being transformed by U*S to form a rough ellipse. If U*S is used to transform the unit circle, the ellipse would be the wrong size because the rough circle of transpose(V) is not a unit circle. So U*S needs to be scaled by the average column vector norm of transpose(V). 
So U*S*scale, is the transformation matrix that can be applied to the unit circle. After this transform, the centroid of the data needs to be added, because we subtracted in the beginning.

This approach minimizes the sum of the distances of each colored point to the ellipse.

The list of transformed points can be vertices on a polygon, and drawn on the canvas as an approximated ellipse.

