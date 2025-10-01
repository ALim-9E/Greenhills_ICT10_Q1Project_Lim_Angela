from pyscript import display

restaurant_name = "Bonchon" # String
owner_name = "Owner: Seo Jin-Duk"     # String     
year_established = 2002 # integer

business_hours = ("10:00 AM", "10:00 PM") # tuple
result = ', '.join(business_hours) # string
display(result, target="div5")

number_of_locations = "350 locations" # string
display(number_of_locations, target="div5")

display(restaurant_name, target="div2")
display(owner_name, target="div3")
display(year_established, target="div3")
