import unittest
from project import (dot_product, cross_product, angle_between, magnitude,
                     add_vectors, subtract_vectors, scalar_multiplication,
                     vector_projection, is_orthogonal, unit_vector,
                     area_of_parallelogram, volume_of_parallelepiped)

class TestVectorOperations(unittest.TestCase):

    def test_dot_product(self):
        self.assertEqual(dot_product((1, 2, 3), (4, -5, 6)), 12)

    def test_cross_product(self):
        self.assertEqual(cross_product((1, 2, 3), (4, 5, 6)), (-3, 6, -3))

    def test_angle_between(self):
        self.assertAlmostEqual(angle_between((1, 0, 0), (0, 1, 0)), 90)

    def test_magnitude(self):
        self.assertEqual(magnitude((3, 4, 0)), 5)

    def test_add_vectors(self):
        self.assertEqual(add_vectors((1, 2, 3), (4, 5, 6)), (5, 7, 9))

    def test_subtract_vectors(self):
        self.assertEqual(subtract_vectors((4, 5, 6), (1, 2, 3)), (3, 3, 3))

    def test_scalar_multiplication(self):
        self.assertEqual(scalar_multiplication((1, 2, 3), 3), (3, 6, 9))

    def test_vector_projection(self):
        # Assuming vector_projection returns a vector and not a scalar
        self.assertEqual(vector_projection((1, 0, 0), (2, 0, 0)), (1, 0, 0))

    def test_is_orthogonal(self):
        self.assertTrue(is_orthogonal((1, 0, 0), (0, 1, 0)))

    def test_unit_vector(self):
        self.assertEqual(unit_vector((1, 0, 0)), (1, 0, 0))

    def test_area_of_parallelogram(self):
        self.assertEqual(area_of_parallelogram((1, 0, 0), (0, 1, 0)), 1)

    def test_volume_of_parallelepiped(self):
        self.assertEqual(volume_of_parallelepiped((1, 0, 0), (0, 1, 0), (0, 0, 1)), 1)

if __name__ == '__main__':
    unittest.main()
