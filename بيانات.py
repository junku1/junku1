import datetime
import pyfiglet

Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح.
C = "\033[1;97m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

Lo = pyfiglet.figlet_format('Yousef Ali ')
print(F + Lo)
Lo1 = pyfiglet.figlet_format(' EL.Sultan  ')
print(F + Lo1)


def analyze_national_id(national_id):
    governorates = {
        '01': 'القاهرة',
        '02': 'الإسكندرية',
        '03': 'بورسعيد',
        '04': 'السويس',
        '05': 'الإسماعيلية',
        '06': 'كفر الشيخ',
        '07': 'الغربية',
        '08': 'الدقهلية',
        '09': 'الشرقية',
        '10': 'القليوبية',
        '11': 'دمياط',
        '12': 'الدقهلية',
        '13': 'الشرقية',
        '14': 'القليوبية',
        '15': 'كفر الشيخ',
        '16': 'الغربية',
        '17': 'المنوفية',
        '18': 'البحيرة',
        '19': 'الإسماعيلية',
        '21': 'الجيزة',
        '22': 'بني سويف',
        '23': 'الفيوم',
        '24': 'المنيا',
        '25': 'أسيوط',
        '26': 'سوهاج',
        '27': 'قنا',
        '28': 'أسوان',
        '29': 'الأقصر',
        '31': 'البحر الأحمر',
        '32': 'الوادي الجديد',
        '33': 'مطروح',
        '34': 'شمال سيناء',
        '35': 'جنوب سيناء',
    }

    birth_century = int(national_id[0])
    birth_year_prefix = '19' if birth_century == 2 else '20'
    birth_year = int(birth_year_prefix + national_id[1:3])

    birth_month = int(national_id[3:5])
    birth_day = int(national_id[5:7])

    birth_date = datetime.date(birth_year, birth_month, birth_day)

    governorate_code = national_id[7:9]
    governorate = governorates.get(governorate_code, 'غير معروفة')

    gender_digit = int(national_id[12])
    gender = 'أنثى' if gender_digit % 2 == 0 else 'ذكر'

    birth_century_str = f"{birth_century}1th" if birth_century in [2, 3] else 'غير معروف'

    return governorate, birth_date.strftime('%Y-%m-%d'), gender, birth_century_str


def main():
    national_id = input(F + "Enter the national number : ")

    if len(national_id) == 14 and national_id.isdigit():
        governorate, birth_date, gender, birth_century = analyze_national_id(national_id)
        print(C + "")
        print(f"المحافظة: {governorate}")
        print("")
        print(f"تاريخ الميلاد: {birth_date}")
        print("")
        print(f"الجنس: {gender}")
        print("")

    else:
        print("الرقم القومي غير صحيح.")


if __name__ == "__main__":
    main()
