from flowlogparser import FlowLogParser

if __name__ == '__main__':

    flow_log_parser = FlowLogParser('./TestCases/TestCase1/Input/lookup_table.csv',
                                    './ProtocalTranslator/protocol-numbers.csv')
    flow_log_parser.parse_flowlog('./TestCases/TestCase1/Input/flow_logs.txt')
    flow_log_parser.create_output('./TestCases/TestCase1/Output')

