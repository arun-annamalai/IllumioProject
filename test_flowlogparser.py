import unittest
import filecmp

from flowlogparser import FlowLogParser

class TestFlowLogParser(unittest.TestCase):
    def test_flowlogparser(self):
        testcase_information = [['TestCase1', 'test_illumio_provided_input']
                          ,['TestCase2', 'test_case_insensitive_tags']]

        for testcase in testcase_information:
            testcase_number = testcase[0]
            with self.subTest(i=testcase[1]):
                flow_log_parser = FlowLogParser(f'./TestCases/{testcase_number}/Input/lookup_table.csv',
                                                './ProtocalTranslator/protocol-numbers.csv')
                flow_log_parser.parse_flowlog(f'./TestCases/{testcase_number}/Input/flow_logs.txt')
                flow_log_parser.create_output(f'./TestCases/{testcase_number}/Output')
                self._compare_output_file_contents(f'./TestCases/{testcase_number}/Output',
                                                   f'./TestCases/{testcase_number}/ExpectedOutput')

    def _compare_output_file_contents(self, actual_output_dir, expected_output_dir):
        assert(filecmp.cmp(actual_output_dir + '/combination_counts.csv', expected_output_dir + '/combination_counts.csv', shallow=False))
        assert (
            filecmp.cmp(actual_output_dir + '/tag_counts.csv', expected_output_dir + '/tag_counts.csv',
                        shallow=False))