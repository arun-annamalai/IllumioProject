import csv
from collections import defaultdict

class FlowLogParser:
    def __init__(self, lookup_table_path: str, protocol_translator_table_path: str):
        self.protocol_dict = self._parse_protocol_translator_table(protocol_translator_table_path)
        self.lookup_dict = self._parse_lookup_table(lookup_table_path)
        self.tag_counts = defaultdict(int)
        self.combination_counts = defaultdict(int)

    def parse_flowlog(self, flowlog_filepath: str) -> None:
        """
            This function will parse the flowlog and keep the outputs in memory. You should call create_output after
            this function.

            Args:
                flowlog_filepath (str): The filepath to the flow log text file
        """
        with open(flowlog_filepath, 'r') as flowlog_file:
            for line in flowlog_file:
                fields = line.split()
                dstPort, protocol = fields[6].lower(), self.protocol_dict[int(fields[7])]

                # Perform Tag Matching
                tag = 'untagged' if (dstPort, protocol) not in self.lookup_dict else self.lookup_dict[(dstPort, protocol)]
                self.tag_counts[tag] += 1

                # Perform Combination Matching
                self.combination_counts[(dstPort, protocol)] += 1

    def create_output(self, output_dir_path = './Output') -> None:
        """
            This function will write 2 files (combination_counts.csv and tag_counts.csv) to an output directory of your choice.

            Args:
                output_dir_path (str): The directory path to where you want to store the output files in. Defaults to ./Output
        """
        self._create_combination_counts_output(output_dir_path)
        self._create_tag_counts_output(output_dir_path)

    def _parse_lookup_table(self, filepath: str) -> dict:
        with open(filepath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            # skip header
            next(csvreader)
            lookup_dict = {}
            for row in csvreader:
                dst_port, protocol, tag = row[0].lower(), row[1].lower(), row[2].lower()
                lookup_dict[(dst_port, protocol)] = tag
            return lookup_dict

    def _parse_protocol_translator_table(self, protocol_translator_table_path: str) -> dict:
        with open(protocol_translator_table_path, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            # skip header
            next(csvreader)
            protocol_dict = {}
            for row in csvreader:
                protocol_dict[int(row[0].lower())] = row[1].lower()
            return protocol_dict

    def _create_combination_counts_output(self, output_dir_path: str) -> None:
        with open(output_dir_path + '/combination_counts.csv', 'w') as tag_count_file:
            header = ['Port', 'Protocol', 'Count']
            data = [[k[0], k[1], v] for k, v in self.combination_counts.items()]

            csvwriter = csv.writer(tag_count_file)
            csvwriter.writerow(header)
            csvwriter.writerows(data)

    def _create_tag_counts_output(self, output_dir_path: str) -> None:
        with open(output_dir_path + '/tag_counts.csv', 'w') as tag_count_file:
            header = ['Tag', 'Count']
            data = [[k, v] for k, v in self.tag_counts.items()]

            csvwriter = csv.writer(tag_count_file)
            csvwriter.writerow(header)
            csvwriter.writerows(data)
