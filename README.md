## Assumptions
 * Given the requirement to use minimal python libraries, I have only used the following 2: csv, collections
 * This solution can only parse the default V2 flow logs
 * Given that matches are case-insensitive, I produce the output tags as all lowercase
           
## Protocal Translation
I needed a way to translate protocal numbers to their english name (eg: 6 becomes TCP). I downloaded a CSV file from 
https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xml#protocol-numbers-1 to do so

## Instructions on how to run parser

```python
from flowlogparser import FlowLogParser

flow_log_parser = FlowLogParser('./TestCases/TestCase1/Input/lookup_table.csv',
                                './ProtocalTranslator/protocol-numbers.csv')
flow_log_parser.parse_flowlog('./TestCases/TestCase1/Input/flow_logs.txt')
flow_log_parser.create_output('./TestCases/TestCase1/Output')
```

## Testing
I have created 2 full system test cases under the folder 'TestCases'. These are pretty minimal test cases with one 
being a happy case modelled off the illumio provided inputs. The second test case specifically checks for the case-insensitive 
tagging requirement. 

```commandline
cd IllumioProject
python -m unittest discover
```