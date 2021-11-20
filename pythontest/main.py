from fast_fractals import fast_mandel
from time import time
from other_implementations import numpy_mandel, python_mandel
from glob import glob
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 



def time_f(f,n,method):
	print("Started ", method)
	times = []
	for i in range(n):
		t1 = time()
		a = f(500, 50)
		time_elapsed = time() - t1
		times.append(time_elapsed)
	print(f"Finished in {sum(times)/len(times)}s ({n} run avg.)\n\n")

#time_f(numpy_mandel, 10, "numpy")
#time_f(python_mandel, 10, "base python")





### Variables
N = 8000 # Image is (N x N) in size
s = 2 # Stripe density. 2 was found to be the best parameter (smoothest)

lx = -2.    #
ly = -1.12  #  Bounds of the
ux = 0.47   #  Mandelbrot set.
uy = 1.12   #

X0 = [lx, ly, ux, uy]

### Text settings

font = ImageFont.truetype("Garamond.ttf", 60)
color = (255, 255, 255)


def compute_one_frame(X, n_iter, name, text = None):
	a,b = np.array(fast_mandel(N, n_iter, X, s))
	a = np.reshape(a, (N,N))
	b = np.reshape(b, (N,N))

	filter = np.argwhere(b == -1).T
	b[filter[0], filter[1]] = np.max(b)

	b = b - np.min(b)
	b = b / np.max(b)

	a = a - np.min(a)
	a = a / np.max(a)
	
	c = matplotlib.cm.twilight(0.1*a + 0.9*b)

	c[filter[0], filter[1], :] = 0

	im = Image.fromarray((c*255).astype(np.uint8)).convert("RGB")

	if text is not None:
		draw = ImageDraw.Draw(im)
		draw.text((20, N-70),text,(255,255,255),font=font)
	

	im.save(f"{name}.jpeg")

def generate_zoom(X_0, x, y, steps, steps_to_center, zoom, start_step = 0):
	
	x0, y0 = (X_0[0]+X_0[2])/2, (X_0[1]+X_0[3])/2
	xr0, yr0 = (X_0[2]-X_0[0])/2, (X_0[3]-X_0[1])/2
	xi = np.linspace(x0, x, steps_to_center)
	yi = np.linspace(y0, y, steps_to_center)
	xri = [xr0 * (1-zoom)**k for k in range(steps)]
	yri = [yr0 * (1-zoom)**k for k in range(steps)]
	print("Step 1: Centering...")
	old_min_a = 0
	old_max_a = 0
	old_min_b = 0
	old_max_b = 0
	for k in tqdm(range(start_step, steps)):
		if k < steps_to_center:
			X = [xi[k] - xri[k], yi[k] - yri[k], xi[k]+ xri[k], yi[k] + yri[k]]
		else:
			X = [x - xri[k], y - yri[k], x + xri[k], y + yri[k]]

		a,b = np.array(fast_mandel(N, iters(k), X, s))
		b = np.reshape(b, (N,N))
		a = np.reshape(a, (N,N))
		new_min_a = np.min(a)

		filter = np.argwhere(b == -1).T
		b[filter[0], filter[1]] = np.max(b)

		new_min_b = np.min(b)
		

		if k==start_step:
			old_min_a = new_min_a
			old_min_b = new_min_b

		min_a = 0.5*new_min_a + 0.5* old_min_a
		min_b = 0.5*new_min_b + 0.5* old_min_b
		

		old_min_a = new_min_a
		old_min_b = new_min_b

		a = a - min_a
		new_max_a = np.max(a)
		if k==start_step:
			old_max_a = new_max_a
		max_a = 0.5*new_max_a + 0.5* old_max_a
		old_max_a = new_max_a

		a = a/max_a
		a[a < 0] = 0
		a[a > 1] = 1

		b = b - min_b
		new_max_b = np.max(b)
		if k==start_step:
			old_max_b = new_max_b
		max_b = 0.5*new_max_b + 0.5* old_max_b
		old_max_b = new_max_b

		b = b/max_b
		b[b < 0] = 0
		b[b > 1] = 1
		c = 0.1*a+0.9*b

		imgRGB = (matplotlib.cm.twilight(0.1*a+0.9*b)*255)
		imgRGB[filter[0], filter[1], :] = 0
		im = Image.fromarray(imgRGB.astype(np.uint8)).convert("RGB")
		im.save(f"zoom2/zoom{str(k).zfill(5)}.jpeg")
	
def iters(k):
	return 1180 + 4*(k-1380)

x1 = (-1.6241199193994318 -1.624119919281773) / 2
y1 = (-0.00013088931048083944 -0.0001308892443058033) /2

#generate_zoom(X0, x1, y1, 2000, 60, 0.02, start_step = 1380)

zoom = 0.02
nice_step = 646
xr0 = (ux-lx) / 2 * (1-zoom)**nice_step
yr0 = (uy-ly) / 2 * (1-zoom)**nice_step
k = nice_step
X = [x1 - xr0, y1 - yr0, x1 + xr0, y1 + yr0]
#for it in tqdm( np.linspace(345,900, 100)):
#	compute_one_frame(X, round(it), "iter_effect/" + str(round(it)).zfill(4), text = "Iteration " + str(round(it)))

#compute_one_frame(X, 1000, "nice_spiral_big", text = "Iteration 1500" )

def create_video():
    img_array = []
    for filename in tqdm(glob("iter_effect/*")):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter(f"iter_effect/video.avi",cv2.VideoWriter_fourcc(*'DIVX'), 50, size)
    for i in tqdm(range(len(img_array))):
        out.write(img_array[i])
    out.release()

#create_video()

print(X)
