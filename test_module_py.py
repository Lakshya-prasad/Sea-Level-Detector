import unittest
import sea_level_predictor
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


class SeaLevelPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected title: 'Rise in Sea Level'")

    def test_plot_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected xlabel: 'Year'")

    def test_plot_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected ylabel: 'Sea Level (inches)'")

    def test_plot_data_points(self):
        # Check scatter plot has correct number of points
        scatter = self.ax.collections[0]
        actual_len = len(scatter.get_offsets())
        self.assertEqual(actual_len, 134, "Expected 134 data points in scatter plot")

    def test_line1_endpoints(self):
        # First line: full dataset regression extended to 2050
        line = self.ax.lines[0]
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        self.assertEqual(int(x_data[0]), 1880, "First line should start at year 1880")
        self.assertEqual(int(x_data[-1]), 2050, "First line should end at year 2050")
        self.assertAlmostEqual(round(float(y_data[-1]), 1), 21.7, delta=0.5,
                               msg="First line y at 2050 should be ~21.7 inches")

    def test_line2_endpoints(self):
        # Second line: post-2000 regression extended to 2050
        line = self.ax.lines[1]
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        self.assertEqual(int(x_data[0]), 2000, "Second line should start at year 2000")
        self.assertEqual(int(x_data[-1]), 2050, "Second line should end at year 2050")
        self.assertAlmostEqual(round(float(y_data[-1]), 1), 26.0, delta=0.5,
                               msg="Second line y at 2050 should be ~26.0 inches")


if __name__ == '__main__':
    unittest.main()
