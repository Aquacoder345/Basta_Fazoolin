class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address 

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#brunc menu
brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
}
early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
Arepas = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
early_brunch_menu = Menu('Early Brunch', early_bird, 1500, 1800)
#print(early_brunch_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
dinner_menu = Menu('Dinner', dinner, 1700, 2300)
kids_menu = Menu('Kids Menu', kids, 1100, 2100)
arepas_menu = Menu("Take a' Arepa", Arepas, 1000, 2000)

menus = [brunch_menu, early_brunch_menu, dinner_menu, kids_menu, arepas_menu]


flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

#print(flagship_store.available_menus(1700))
#print(new_installment.available_menus(1700))

basta = Business('Basta Fazoolin with my Heart', [flagship_store, new_installment])

arepa = Business("Take a' Arepa", [arepas_place])
print(arepa.franchises[0].menus[0])
