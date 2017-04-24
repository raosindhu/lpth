states = {
    "Oregon": 'OR',
    "Florida": 'FL',
    "California": 'CA',
    "New York": 'NY',
    "Michigan": 'MI'
}

print type(states)
print states
print len(states)

cities = {
    'CA': 'San Francisco',
    'FL': 'Miami',
    'OR': 'Portland'
}

print type(cities)
print cities
print len(cities)

# add some more cities

cities['NY'] = 'New York'
cities['MI'] = 'Detroit'

print cities

print '-'*10
print 'NY state has:', cities['NY']
print 'Oregon state has:', cities[states['Oregon']]
print "Michigan's abbreviation is:", states["Michigan"]

print '-'*10

for state, abbrev in states.items():
    print cities[abbrev]
   # print state
   # print abbrev

print '-'*10

for abbrev, city in cities.items():
    print  abbrev, city

state_name = states.get('Texas', None)

if not state_name:
    print "\nSorry, No Texas"

