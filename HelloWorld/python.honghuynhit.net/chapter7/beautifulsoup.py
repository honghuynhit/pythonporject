from bs4 import BeautifulSoup as Soup
note = '''
<?xml version="1.0" encoding="UTF-8"?>
<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>Two of our famous Belgian Waff
les with plenty of real maple syrup</description>
<calories>650</calories>
</food>
<food>
<name>Strawberry Belgian Waffles</name>
<name>Strawberry Belgian Waffles</name>
<price>$7.95</price>
<description>Light Belgian waffles covered
with strawberries and whipped cream</description>
<calories>900</calories>
</food>
</breakfast_menu>
'''
soup = Soup(note,'xml')
foods = soup.findAll('food')
for x in foods:
    # print(x.find('name').string,': ', x.price.string, x.description.string)
    print(x.findAll())
