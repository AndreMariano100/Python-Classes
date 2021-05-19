phonesDocument = """
Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com (724) 900-2986
Rayford Sutton rayfords66@hotmail.com 651-391-3183 / 391-3184
Jerome Gentry jgentry@me.com (604) 720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
Quinton Franks qfranks@comcast.net 209-754-9111
Adam Hubbard cygzfjd61@outlook.com 123-433-6698
Jarred Fox jfox39@live.com 701-528-9851
Arnoldo Parker aparker39@sbcglobal.net (304) 491-9583 / 491-9584
Sid Mcdaniel mcdanie3354@att.net 863-583-8107
"""

# re.VERBOSE mode (lets you add whitespcae and comments to the regex string passed to re.compile()

import re

# 123-456-7890 / (123) 456-7890 / 456-7890

phoneNumRegex = re.compile(r'(((\d\d\d-)|(\(\d\d\d\)\s))?\d\d\d-\d{4})')

phoneList = phoneNumRegex.findall(phonesDocument)
print(phoneList)

for i, phone in enumerate(phoneList):
    print(f'{i+1}.\t{phone[0]}')