import unittest
import pandas as pd
import src.orchestration.iofileservice.io_file_service as iofs
import pandas.testing as pdtest


class IOFileServiceTest(unittest.TestCase):
    def test_get_data(self):
        obtained_data = iofs.IOFileService().get_data('../../../src/orchestration/data/cs-training_Transactional.csv')

        expected_data = pd.read_csv('../../../src/orchestration/data/cs-training_Transactional.csv')
        pdtest.assert_frame_equal(obtained_data, expected_data)


if __name__ == "__main__":
    unittest.main()
