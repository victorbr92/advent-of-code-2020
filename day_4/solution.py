from pydantic import BaseModel, ValidationError, conint, constr, validator
from typing import Literal
from typing import Optional

with open('input.txt', 'r') as f:
    raw_data = [line.split() for line in f.read().split('\n\n')]


class PassportData(BaseModel):
    byr: conint(gt=1919, lt=2003)
    iyr: conint(gt=2009, lt=2021)
    eyr: conint(gt=2019, lt=2031)
    hgt: constr(regex=r'(\d+cm|\d+in)')
    hcl: constr(regex=r'(#[0-9a-f]{6}$)')
    ecl: Literal['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid: constr(regex=r'(\d{9}$)')
    cid: Optional[str] = None

    @validator('hgt')
    def validate_height(cls, v):
        if isinstance(v, str):
            unit = v[-2::]
            height = int(v[0:-2])
            if unit == 'cm':
                if height < 150 or height > 193:
                    raise ValueError(f'Height value {height} incorrect for cm')
                return v
            elif unit == 'in':
                if height < 59 or height > 76:
                    raise ValueError(f'Height value {height} incorrect for in')
                return v
            else:
                raise ValueError(f'Height unit {unit} incorrectly defined')


if __name__ == '__main__':
    clean_data = [{field.split(':')[0]: field.split(':')[1] for field in data} for data in raw_data]
    passport_lists = []
    for data in clean_data:
        try:
            passport = PassportData(**data)
            passport_lists.append(passport)
        except ValidationError as error:
            pass

    print(len(passport_lists))
