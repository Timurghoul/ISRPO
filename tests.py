import unittest

from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as tri_area, perimeter as tri_perimeter


class RectangleTestCase(unittest.TestCase):
    def test_rect_area_zero(self):
        self.assertEqual(rect_area(10, 0), 0)
        self.assertEqual(rect_area(0, 0), 0)

    def test_rect_area_positive_integers(self):
        self.assertEqual(rect_area(4, 5), 20)
        self.assertEqual(rect_area(7, 3), 21)

    def test_rect_area_square(self):
        self.assertEqual(rect_area(10, 10), 100)

    def test_rect_area_large_numbers(self):
        self.assertEqual(rect_area(10_000, 20_000), 200_000_000)

    def test_rect_area_floats(self):
        self.assertAlmostEqual(rect_area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rect_area(0.5, 0.5), 0.25)

    def test_rect_perimeter_zero(self):
        self.assertEqual(rect_perimeter(0, 0), 0)
        self.assertEqual(rect_perimeter(5, 0), 10)

    def test_rect_perimeter_positive_integers(self):
        self.assertEqual(rect_perimeter(5, 6), 22)

    def test_rect_perimeter_square(self):
        self.assertEqual(rect_perimeter(4, 4), 16)

    def test_rect_perimeter_symmetry(self):
        self.assertEqual(rect_perimeter(2, 7), rect_perimeter(7, 2))

    def test_rect_perimeter_large_numbers(self):
        self.assertEqual(rect_perimeter(10_000, 20_000), (10_000 + 20_000) * 2)

    def test_rect_perimeter_floats(self):
        self.assertAlmostEqual(rect_perimeter(2.5, 4.0), (2.5 + 4.0) * 2)
        self.assertAlmostEqual(rect_perimeter(0.5, 0.5), 2.0)


class SquareTestCase(unittest.TestCase):

    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_square_area_positive_integers(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(7), 49)

    def test_square_area_large_numbers(self):
        self.assertEqual(square_area(10_000), 100_000_000)

    def test_square_area_floats(self):
        self.assertAlmostEqual(square_area(2.5), 6.25)
        self.assertAlmostEqual(square_area(0.5), 0.25)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_positive_integers(self):
        self.assertEqual(square_perimeter(4), 16)

    def test_square_perimeter_large_numbers(self):
        self.assertEqual(square_perimeter(10_000), 40_000)

    def test_square_perimeter_floats(self):
        self.assertAlmostEqual(square_perimeter(2.5), 10.0)


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area_zero(self):
        self.assertEqual(tri_area(0, 10), 0)
        self.assertEqual(tri_area(0, 0), 0)

    def test_triangle_area_positive_integers(self):
        self.assertEqual(tri_area(10, 4), 20)
        self.assertEqual(tri_area(6, 3), 9)

    def test_triangle_area_floats(self):
        self.assertAlmostEqual(tri_area(2.5, 4.0), 5.0)
        self.assertAlmostEqual(tri_area(3.5, 1.5), 2.625)

    def test_triangle_area_large_numbers(self):
        self.assertEqual(tri_area(10_000, 2_000), 10_000 * 2_000 / 2)

    def test_triangle_perimeter_zero(self):
        self.assertEqual(tri_perimeter(0, 0, 0), 0)
        self.assertEqual(tri_perimeter(0, 3, 4), 7)

    def test_triangle_perimeter_positive_integers(self):
        self.assertEqual(tri_perimeter(3, 4, 5), 12)

    def test_triangle_perimeter_floats(self):
        self.assertAlmostEqual(tri_perimeter(2.5, 3.5, 4.0), 10.0)

    def test_triangle_perimeter_large_numbers(self):
        self.assertEqual(tri_perimeter(10_000, 20_000, 30_000), 60_000)

