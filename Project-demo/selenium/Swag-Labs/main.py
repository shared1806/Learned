# File run all TCs
import unittest
from HTMLTestRunner import HTMLTestRunner  

# Auto Find & load all TCs from 'test_scripts' Folder
loader = unittest.TestLoader()
suite = loader.discover('test_scripts')

if __name__ == "__main__":
    # Setup test run with HTML report
    runner = HTMLTestRunner(
        output='results',                    # Create Folder 'results'
        report_name='My Test Report',        # File Name
        descriptions='This is a test report for my unit tests.', # Descriptions report
        report_title='Test Suite',         # Title 
        combine_reports=True,                # Export 1 file
        verbosity=2                          # Mức độ chi tiết của kết quả
    )
    
    # Run test suite and export HTML report
    runner.run(suite)