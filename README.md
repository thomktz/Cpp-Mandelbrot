# C++-based Python package for fast computing of the Mandelbrot set

### The Mandelbrot set

A point `c = a + ib` in the complex plane is in the Mandelbrot set if the following series does not diverge as n tends to infinity :

![](http://www.sciweavers.org/download/Tex2Img_1637406052.jpg)

A point that isn't inside the set will always be greater than any radius `R > 2` at some point of the iteration.

A point inside will typically be colored black.

![mandel](https://user-images.githubusercontent.com/60552083/142724263-a4d3a02d-4ae3-4775-b8f6-a85816103acd.png)


### The coloring

The typical way to color the rest of the set (the outside points) is to have the color as a function of the number of iterations before escaping the radius (c.f. previous image). 
However, the coloring technique here is called average stripe coloring and works as such :

The 'orbit' is the collection of the points (f_i) which are then mapped by a function. By taking the average of the mapped orbits and mapping that number to a color, you get a coloring that can look like this :

![zoom00000](https://user-images.githubusercontent.com/60552083/142724184-e7d7266a-09ac-4356-967b-30e451808ae2.jpeg)


To have an output between 0 and 1, the function is chosen as such :  

![gif](https://user-images.githubusercontent.com/60552083/142729011-5d14ad29-b610-4523-9eb9-3b7d93ef5b08.gif)  

with the stripe density, s_d visually chosen to be 2.   
This output is then put into a matplotlib colormap to have RGB values.


### Number of iterations

The number `n` of maximum iterations is a very important parameter, since it determines both the quality and precision of the image but also the speed at which it renders.  
A typical image is 1000 by 1000 pixels, and each of the pixels will be iterated through the process of z²+c `n` times, and then be taken through the average stripe coloring prcess.

Here is the effect of the parameter on a certain zoomed point of the complex plane :

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/60552083/142724790-60e06e98-ce19-4f34-8813-45e6e55b57f2.gif)

Click [here](https://user-images.githubusercontent.com/60552083/142724864-6af6c98b-1e82-4703-807f-cbebb0f2969d.jpeg) to see a 8000x8000 image at 1500 iterations of the same part of the complex plane


### Speed
For a benchmark image (1000x1000, 500it)

Basic python implementation : 72s  
Parallelized numpy : 0.512s  
My package (1 core CPU): 0.492s  
My package (8 logical cores, CPU) : 0.129s  

### Results

All found in one sontinuous zoom to the point -1.62411991934 + i * (-0.00013088927)

![zoom00000](https://user-images.githubusercontent.com/60552083/142725446-b9f339e6-66f1-47b6-a9aa-d77af46fed24.jpeg)
![zoom00266](https://user-images.githubusercontent.com/60552083/142725462-61a7fdbe-9233-478f-9629-618bbf320a5b.jpeg)
![zoom00613](https://user-images.githubusercontent.com/60552083/142725481-075ea0f8-4bc4-43e3-8687-79d8da7e8d7a.jpeg)
![zoom00925](https://user-images.githubusercontent.com/60552083/142725498-6d25b859-e8a0-4be3-b3ba-5ea794e03aa6.jpeg)
![zoom01337](https://user-images.githubusercontent.com/60552083/142725519-6f07533f-d718-45a4-9d19-754d4d5b2ce3.jpeg)



