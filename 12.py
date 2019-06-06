import re
sec_check = re.compile(r'^.*(?=.{8，})(?=.*[A-Za-z])(?=.*[0-9]{1,})')
sec_check.findall('abc23A4jhsopo1442Sd')
