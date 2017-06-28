import pytest
import numpy as np
from polyssifier.polyssifier import exponent_matrix, create_multivariate

@pytest.mark.medium
def test_exponent_matrix():
    matrix = np.matrix('1 2; 3 4')
    matrix_2pow = np.matrix('1 4; 9 16')
    matrix_3pow = np.matrix('1 8; 27 64')
    matrix_4pow = np.matrix('1 16; 81 256')
    assert all(np.array_equal(matrix, exponent_matrix(matrix, 1)))
    assert all(np.array_equal(matrix_2pow == exponent_matrix(matrix, 2)))
    assert all(np.array_equal(matrix_3pow == exponent_matrix(matrix, 3)))
    assert all(np.array_equal(matrix_4pow == exponent_matrix(matrix, 4)))

@pytest.mark.medium
def test_create_multivariate():
    matrix = np.matrix('5 6; 7 8')
    poly1 = np.matrix('5 6; 7 8')
    poly2 = np.matrix('5 6 25 36; 7 8 49 64')
    poly3 = np.matrix('5 6 25 36 125 216; 7 8 49 64 343 512')
    assert all(np.array_equal(poly1, create_multivariate(matrix, 1)))
    assert all(np.array_equal(poly2, create_multivariate(matrix, 2)))
    assert all(np.array_equal(poly3, create_multivariate(matrix, 3)))