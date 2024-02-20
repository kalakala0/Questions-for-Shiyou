from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from datetime import datetime

edge_driver_path = "D:/msedgedriver.exe"
url = "https://www.boc.cn/sourcedb/whpj/"

def search(currency,date):
    driver = webdriver.Edge(executable_path=edge_driver_path)
    driver.get(url)
    #登录网站
    time.sleep(2)
    #停顿使加载完全

    select_element = driver.find_element_by_xpath('//*[@id="pjname"]')
    select = Select(select_element)
    value_to_select = currency
    select.select_by_value(value_to_select)
    #查询对应的货币种类

    driver.find_element_by_xpath('//*[@id="erectDate"]').send_keys(date)
    driver.find_element_by_xpath('//*[@id="nothing"]').send_keys(date)
    #查询对应的日期
    driver.find_element_by_xpath('//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input').click()
    #点击搜索
    try:
        result = driver.find_element_by_xpath('/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text
        return result
    except Exception:
        return False
    #若当日不存在数据则报错

currency_dict = {
    'GBP':'英镑',
    'HKD':'港币',
    'USD':'美元',
    'CHF':'瑞士法郎',
    'DEM':'德国马克',
    'FRF':'法国法郎',
    'SEK':'新加坡元',
    'DKK':'丹麦克朗',
    'SGD':'瑞典克朗',
    'NOK':'挪威克朗',
    'CAD':'加拿大元',
    'JPY':'日元',
    'AUD':'澳大利亚元',
    'EUR':'欧元',
    'MOP':'澳门元',
    'PHP':'菲律宾比索',
    'THP':'泰国铢',
    'NZD':'新西兰元',
    'KPW':'韩元',
    'SUR':'卢布',
    'MYR':'林吉特',
    'TWD':'新台币',
    'ESP':'西班牙比塞塔',
    'ITL':'意大利里拉',
    'NLG':'荷兰盾',
    'BEF':'比利时法郎',
    'FIM':'芬兰马克',
    'INR':'印度卢比',
    'IDR':'印尼卢比',
    'BRC':'巴西里亚尔',
    'AED':'阿联酋迪拉姆',
    'ZAR':'南非兰特',
    'SAR':'沙特里亚尔',
    'TRL':'土耳其里拉',
}
#货币名称对应

def validate_date(date_str):
    try:
        date_object = datetime.strptime(date_str, '%Y%m%d')
        return date_object.year >= 2001
        # 验证日期不得早于2001年
    except ValueError:
        return False
#验证日期是否合理

def validate_currency(currency_str):
    return currency_str in currency_dict
#验证货币简称是否合理

def convert_date_format(date_str):
    date_object = datetime.strptime(date_str, '%Y%m%d')
    return date_object.strftime('%Y-%m-%d')
#日期转换

def convert_currency(currency_str):
    return currency_dict.get(currency_str, 'Unknown Currency')

input_date_currency = input("请输入日期和货币（例如：20211231 USD）: ")
input_list = input_date_currency.split()
#分割字符串

if len(input_list) == 2 and validate_date(input_list[0]) and validate_currency(input_list[1]):
#如果输入合理
    formatted_date = convert_date_format(input_list[0])
    full_currency_name = convert_currency(input_list[1])
    if search(full_currency_name,formatted_date):
        print(search(full_currency_name,formatted_date))
    else:
        print("不存在当日数据")
else:
    print("输入不合法，请重新输入")
