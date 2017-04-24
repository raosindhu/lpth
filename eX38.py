
ten_things = "Apple Orange Banana Grape Corn Kiwi"

print "There are less than 10 items in ten_things. Let's check"

items = ten_things.split(' ')

print items

new_items = ['Mango', 'Potato', 'Tomato', 'Dublin', 'California']

while len(items) < 10:
    add_item = new_items.pop(0)
    items.append(add_item)
    print "Now ten_things has", len(items)



print items

print ' '.join(items)

print ' '.join(items[3:5])
