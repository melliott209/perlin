import math
import numpy as np

# ----------------- Permutation Table and Possible Gradients ----------------- #

p = [151, 160, 137, 91, 90, 15, 131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 
        103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23, 190, 6, 148, 247, 120, 234, 75, 0, 
        26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33, 88, 237, 149, 56, 
        87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166, 
        77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 
        46, 245, 40, 244, 102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 
        187, 208, 89, 18, 169, 200, 196, 135, 130, 116, 188, 159, 86, 164, 100, 109, 
        198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123, 5, 202, 38, 147, 118, 126, 
        255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42, 223, 183, 
        170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 
        172, 9, 129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 
        104, 218, 246, 97, 228, 251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 
        241, 81, 51, 145, 235, 249, 14, 239, 107, 49, 192, 214, 31, 181, 199, 106, 
        157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254, 138, 236, 205, 
        93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180 ]

# The eight possible gradient vectors
gradients = [   [   1,  1], 
                [   1,  0], 
                [   1, -1], 
                [   0,  1], 
                [   0, -1], 
                [  -1,  1], 
                [  -1,  0], 
                [  -1, -1]      ]

# ============================================================================ #
#                                Noise Functions                               #
# ============================================================================ #
"""Generate noise value between 0 and 1, with the given number of frequency octaves"""
def noise2D(x: float, y: float, octaves: int) -> float:
    total = 0
    maxVal = 0
    freq = 0.005
    ampl = 1
    persistence = 0.5
    for i in range(octaves):
        total += perlin(x * freq, y * freq) * ampl
        maxVal += ampl
        ampl *= persistence
        freq *= 2
    return total / maxVal

"""Generate noise value between 0 and 1 for any given coordinate"""
def perlin(x: float, y: float) -> float:

    # Get base grid integer coordinate
    i = math.floor(x)
    j = math.floor(y)

    # Get offset from base grid integer coordinate
    u = x - i
    v = y - j

    a = i & 255
    b = (i + 1) & 255
    c = j & 255
    d = (j + 1) & 255

    # Get pseudorandom gradients for each of the four surrounding
    # grid integer coordinates
    g1 = grad(p[(p[a] + j   ) & 255])
    g2 = grad(p[(p[b] + j   ) & 255])
    g3 = grad(p[(p[a] + j+1 ) & 255])
    g4 = grad(p[(p[b] + j+1 ) & 255])

    # Compute dot products of gradient vectors and offset vectors
    d1 = dot(g1[0], g1[1], u,   v   )
    d2 = dot(g2[0], g2[1], u-1, v   )
    d3 = dot(g3[0], g3[1], u,   v-1 )
    d4 = dot(g4[0], g4[1], u-1, v-1 )

    # Average the values using linear interpolation to produce noise value
    x1 = interpolate(d1, d2, u)
    x2 = interpolate(d3, d4, u)
    return (interpolate(x1, x2, v) + 1) / 2     # Add 1, and divide result by 2
                                                # to normalize value between
                                                # 0.0 and 1.0

# ============================================================================ #
#                               Helper Functions                               #
# ============================================================================ #

"""Dot product of two vectors"""
def dot(x1: float, y1: float, x2: float, y2: float) -> float:
    return x1 * x2 + y1 * y2

"""The point on a smooth curve ("Smootherstep" Equation)"""
def smooth(t: float) -> float:
    return t*t*t*(t*(t*6.0-15.0)+10.0)

"""Linear interpolate two values using weight w"""
def interpolate(a: float, b: float, w: float) -> float:
    return a + smooth(w) * (b - a)

"""Grab a pseudorandom gradient value for any given integer coordinate"""
def grad(x: int) -> int:
    gIndex = x % 8
    return gradients[gIndex]
