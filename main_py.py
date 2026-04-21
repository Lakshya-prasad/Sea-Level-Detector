import sea_level_predictor
import unittest
import test_module

# Run the plot function during development
sea_level_predictor.draw_plot()

# Run unit tests
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_module)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
