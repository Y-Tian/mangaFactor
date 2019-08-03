# from skimage.measure import structural_similarity as ssim
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2

def import_images(dir_real, dir_machined):
	real = cv2.imread(dir_real)
	machined = cv2.imread(dir_machined)
	tuple_of_images = (convert_to_greyscale(real), convert_to_greyscale(machined))
	return tuple_of_images

def convert_to_greyscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def ssim(imageA, imageB):
	return measure.compare_ssim(imageA, imageB)

def compare_images_ssim(without_plot, imageA, imageB):
	# compute the mean squared error and structural similarity index
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	
	if not without_plot:
		plot_images_ssim(imageA, imageB, m, s, "Real vs Artificial")

def plot_images_ssim(imageA, imageB, m, s, title):
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

def compare_images_laplacien(without_plot, imageA, imageB):
	laplacianA = cv2.Laplacian(imageA,cv2.CV_64F)
	laplacianB = cv2.Laplacian(imageB,cv2.CV_64F)

	if not without_plot:
		plot_images_laplacien(imageA, imageB, laplacianA, laplacianB)


def plot_images_laplacien(imageA, imageB, imageC, imageD):
	plt.subplot(2,2,1),plt.imshow(imageA, cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(imageB, cmap = 'gray')
	plt.title('Artificial'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(imageC, cmap = 'gray')
	plt.title('Original_edge'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(imageD, cmap = 'gray')
	plt.title('Artificial_edge'), plt.xticks([]), plt.yticks([])

	# show the images
	plt.show()

if __name__== "__main__":
	tuple_of_images = import_images("images/test7_real.jpg", "images/test7_art.jpg")
	# compare_images_ssim(False, tuple_of_images[0], tuple_of_images[1])
	compare_images_laplacien(False, tuple_of_images[0], tuple_of_images[1])