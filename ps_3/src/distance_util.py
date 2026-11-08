# Write your code in this .py file for Q4 parts 1 and 2. Please ensure that
# you only have the following in this file:
# - the module docstring
# - function definitions
# In other words, do not put your answers for other parts of Q4 in this file.
def get_distance(image1, image2):
    """
    Compute the distance between two images.
    
    Args:
        image1 (list of list of int): The first image represented as a 2D list of pixel values.
        image2 (list of list of int): The second image represented as a 2D list of pixel values.

    Returns:
        float: The computed distance between the two images.
    """
    # Ensure images have same dimensions
    if len(image1) != len(image2) or len(image1[0]) != len(image2[0]):
        raise ValueError("Images must have the same dimensions")


    sum_squared_diff = 0

    for i in range(len(image1)):
        for j in range(len(image1[0])):
            sum_squared_diff += (image1[i][j] - image2[i][j]) ** 2

    distance = sum_squared_diff ** 0.5
    return distance

def get_average_group_distance(image, group):
    """
    Compute the average distance between a given image and a group of images.
    
    Args:
        image (list of list of int): The image represented as a 2D list of pixel values.
        group (list of list of list of int): A list of images, each represented as a 2D list of pixel values.

    Returns:
        float: The average distance between the given image and the group of images.
    """

    total_distance = 0
    num_images = len(group)

    for img in group:
        total_distance += get_distance(image, img)

    average_distance = total_distance / num_images if num_images > 0 else 0
    return average_distance

