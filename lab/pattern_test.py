import re

name_pattern = r'((?:[A-Z][a-z]+[\s-]?)+)([A-Z][a-z]+)?'  # 姓名可能包含連字符或首字母大寫
date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
hospital_pattern = r'(在|就診於)(?:\s+the)?\s+([A-Za-z\s]+)醫院'
medical_record_pattern = r'病例號[：:]?\s?([A-Z0-9]+)'


# 定義規則用於識別不同實體類別
name_pattern = r'((?:[A-Z][a-z]+[\s-]?)+)([A-Z][a-z]+)?'  # 姓名可能包含連字符或首字母大寫
date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
hospital_pattern = r'(在|就診於)(?:\s+the)?\s+([A-Za-z\s]+)醫院'
medical_record_pattern = r'病例號[：:]?\s?([A-Z0-9]+)'

def extract_entities(text):
    entities = {
        'NAME': [],
        'DATE': [],
        'HOSPITAL': [],
        'MEDICALRECORD': []
    }
    
    for match in re.finditer(name_pattern, text):
        full_name = match.group(1)
        last_name = match.group(2)
        if last_name:
            entities['NAME'].append(full_name)
        else:
            entities['NAME'].append(match.group())
    
    entities['DATE'] = re.findall(date_pattern, text)
    
    for match in re.finditer(hospital_pattern, text):
        entities['HOSPITAL'].append(match.group(2))
    
    entities['MEDICALRECORD'] = re.findall(medical_record_pattern, text)
    
    return entities

text = "患者名為 John Doe-Smith，於 03/15/2023 就診於 ABC醫院，病例號:MRC789012。"
entities = extract_entities(text)

print("姓名:", entities['NAME'])
print("日期:", entities['DATE'])
print("醫院:", entities['HOSPITAL'])
print("病例號:", entities['MEDICALRECORD'])
