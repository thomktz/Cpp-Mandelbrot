# C++-based Python package for fast computing of the Mandelbrot set

### The Mandelbrot set

A point `c = a + ib` in the complex plane is in the Mandelbrot set if the following series does not diverge as n tends to infinity :

![](http://www.sciweavers.org/download/Tex2Img_1637406052.jpg)

A point that isn't inside the set will always be greater than any radius `R>2` at some point of the iteration.

A point inside will typically be colored black.

![mandel](https://user-images.githubusercontent.com/60552083/142724263-a4d3a02d-4ae3-4775-b8f6-a85816103acd.png)


### The coloring

The typical way to color the rest of the set (the outside points) is to have the color as a function of the number of iterations before escaping the radius (c.f. previous image). 
However, the coloring technique here is called average stripe coloring and works as such :

The 'orbit' is the collection on the points (f_i) mapped by a function. Then, by taking the average of the mapped orbits and mapping that number to a color, you get a coloring that can look like this :

![zoom00000](https://user-images.githubusercontent.com/60552083/142724184-e7d7266a-09ac-4356-967b-30e451808ae2.jpeg)

