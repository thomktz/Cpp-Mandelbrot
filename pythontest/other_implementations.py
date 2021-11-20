import numpy as np


def python_mandel(N, n_iter):
	lx = -2.
	ly = -2.
	ux = 2.
	uy = 2.

	iters = np.zeros(N*N)
	re = np.zeros(N)
	im = np.zeros(N)
	C = np.zeros(N*N*2)
	values = np.zeros(N*N*2)
	for k in range(N):
		re[k] = lx + (ux - lx) / N * (k + 0.5)
		im[k] = ly + (uy - ly) / N * (k + 0.5)
	for k in range(N):
		for j in range(N):
			C[N * k + 2 * j] = re[k]
			C[N * k + 2 * j + 1] = im[k]
	for i in tqdm(range(n_iter)):
		for k in range(N):
			for j in range(N):
				if (C[N * k + 2 * j] != 0) or (C[N * k + 2 * j + 1] != 0):
					values[N * k + 2 * j] = values[N * k + 2 * j] * values[N * k + 2 * j] - values[N * k + 2 * j + 1] * values[N * k + 2 * j + 1] + C[N * k + 2 * j]
					values[N * k + 2 * j + 1] = 2 * values[N * k + 2 * j + 1] * values[N * k + 2 * j] + C[N * k + 2 * j + 1]
					if (values[N * k + 2 * j] * values[N * k + 2 * j] + values[N * k + 2 * j + 1] * values[N * k + 2 * j + 1] > 10):
						iters[N * k + j] = i
						C[N * k + 2 * j] = 0
						C[N * k + 2 * j + 1] = 0
	return iters


def numpy_mandel(N, n_iter):
	lx = -2.
	ly = -2.
	ux = 2.
	uy = 2.

	xstep = np.linspace(lx, ux, N)
	ystep = np.linspace(ly, uy, N)
	C = xstep[:, None] + 1j*ystep.T
	Z = np.zeros((N, N))
	iter = np.zeros((N, N))
	for i in range(n_iter):
		Z = (np.square(Z) + C).copy()
		filter = np.argwhere(np.absolute(Z)>10).T
		iter[filter[0], filter[1]] = i
		Z[filter[0], filter[1]] = 0
		C[filter[0], filter[1]] = 0
	return iter