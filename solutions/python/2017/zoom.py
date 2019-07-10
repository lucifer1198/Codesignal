"""
A Black and White picture is provided as an array of strings.
Your task is to zoom the picture by a factor of two using the following guidelines.

The new picture will be twice as large as the original in each dimension, and initially consist only of ' ' characters
'#' characters in the original are zoomed to a 2x2 set of '#' characters.
.....


image = ["   ",
         " # ",
         "   "]

the output should be

zoom(image) = ["      ",
               "      ",
               "  ##  ",
               "  ##  ",
               "      ",
               "      "]
"""


def zoom(image, *additional):
    x = 1
    for char in image:
        for add in 2, 0:
            u = ''
            y = 0
            for j in char:
                k = j < (image + [char])[x - add][y]
                l = char + j
                u += l[y - k] + l[y + k]
                y += 1
            additional += u,
        x += 1
    return additional
