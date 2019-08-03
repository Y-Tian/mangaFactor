# from skimage.measure import structural_similarity as ssim
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2

def import_images(dir_real, dir_machined):
	real = cv2.imread(dir_real)
	machined = cv2.imread(dir_machined)
	tuple_of_images = (convert_to_greyscale(real), convert_to_greyscale(machined))
	# tuple_of_images = (real, machined)
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
		plot_images_generic(imageA, imageB, m, s, "Real vs Artificial")

def plot_images_generic(imageA, imageB, m, s, title):
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
	laplacianA = cv2.Laplacian(imageA,cv2.COLOR_BGR2GRAY)
	laplacianB = cv2.Laplacian(imageB,cv2.COLOR_BGR2GRAY)

	if not without_plot:
		plot_images_laplacien(imageA, imageB, laplacianA, laplacianB)


def get_images_laplacien_transform(imageA, imageB):
	laplacianA = cv2.Laplacian(imageA, cv2.COLOR_BGR2GRAY)
	laplacianB = cv2.Laplacian(imageB, cv2.COLOR_BGR2GRAY)
	tuple_of_images = (laplacianA, laplacianB)

	return tuple_of_images


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

def compare_images_contour(without_plot, imageA, imageB):
	thresh1, bw1 = cv2.threshold(imageA, 127, 255, cv2.THRESH_BINARY)
	contours1, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	thresh2, bw2 = cv2.threshold(imageB, 127, 255, cv2.THRESH_BINARY)
	contours2, _ = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours1:
		cv2.drawContours(imageA, contour, -1, (0, 255, 0), 3)
	cv2.imshow("Frame", imageA)
	cv2.waitKey(0)

def compare_images_black_white(without_plot, imageA, imageB):
	thresh1, bw1 = cv2.threshold(imageA, 20, 255, 0)
	thresh2, bw2 = cv2.threshold(imageB, 20, 255, 0)

	if not without_plot:
		plot_images_generic(bw1, bw2, 0, 0, "")

if __name__== "__main__":
	tuple_of_images = import_images("images/test7_real.jpg", "images/test7_art.jpg")
	tuple_of_laplacian_images = get_images_laplacien_transform(tuple_of_images[0], tuple_of_images[1])

	# compare_images_ssim(False, tuple_of_images[0], tuple_of_images[1])
	# compare_images_laplacien(False, tuple_of_images[0], tuple_of_images[1])

	# compare_images_ssim(False, tuple_of_laplacian_images[0], tuple_of_laplacian_images[1])
	# compare_images_contour(False, tuple_of_laplacian_images[0], tuple_of_laplacian_images[1])
	# compare_images_contour(False, tuple_of_laplacian_images[0], tuple_of_laplacian_images[1])
	compare_images_black_white(False, tuple_of_laplacian_images[0], tuple_of_laplacian_images[1])