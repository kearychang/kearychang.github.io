from collections import deque #1.3
import heapq #1.4
from collections import defaultdict #1.6
from collections import OrderedDict #1.7
from collections import Counter #1.12
import random #1.12
from operator import itemgetter #1.13
from operator import attrgetter #1.14
from itertools import groupby #1.15
from collections import namedtuple #1.18
from collections import ChainMap #1.20

# 1.1 Unpack sequence into variables
def unpack(seq):
    a, b, c, d, _ = seq
    return (a,b,c,d)

#print(unpack((1,2,3,4,5)))

# 1.2 Unpack elements from iterables of arbitrary length
def unpack2(seq):
    a, b, c, d, *n = seq
    return (a,b,c,d,*n)

#print(unpack2((1,2,3,4,5,6,7,8,9,10)))

# 1.3 Keep last n item
def keepLastN(seq,n):
    if (n >= 2):
        q = deque(maxlen=n)
        for e in seq:
            q.append(e)
            print(q)
    else:
        raise Exception("n too small")

#keepLastN((1,2,3,4,5),2)

#1.4 Find largest or smallest N items in collection
def largestSmallestN(seq,isLargest,n):
    heap = []
    for e in seq:
        heapq.heappush(heap,e)
    if isLargest == True:
        print(heapq.nlargest(n,heap))
    else:
        print(heapq.nsmallest(n,heap))

#largestSmallestN((23,21,-32,623,-2,0,12,-352,3),False,3)
#largestSmallestN((23,21,-32,623,-2,0,12,-352,3),True,3)

#1.5 Priority Q
class PriorityQ:
    def __init__(self):
        self._index = 0
        self._q = []

    def push(self,item,priority):
        heapq.heappush(self._q, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._q)[-1]

class Item:
    def __init__(self,name):
        self._name = name

    def __repr__(self):
        return 'Item({!r})'.format(self._name)

'''
q = PriorityQ()
q.push(Item("Y"),25)
q.push(Item("D"),4)
q.push(Item("Z"),26)
q.push(Item("H"),8)

for i in range(4):
    print(q.pop())
'''

#1.6 Multidict is a dictionary that maps keys to more than 1 value
def multidict():
    d = defaultdict(list) #automatically initializes first value to empty list
    d['a'].append(2)
    d['a'].append(3)
    d['a'].append(4)
    print(d['a'])

#multidict()

#1.7 Create a dictionary with control of order of items when iterating or serializing
### As of Python 3.5/3.6, dicts are already ordered by insertion. 
### But for older versions, use OrderedDict

#1.8 Calculate with dictionary (min, max, sort, etc.)
def dictMin(dict):
	print(min( zip( dict.values(), dict.keys() ) ))

#dictMin({'a':5, 'b':2, 'c':7, 'd':0, 'e':-2, 'f':1})

#1.9 Find out what 2 dictionaries have in common (keys, values)
def dictDiff(d1,d2):
    print("COMMON KEYS")
    print(d1.keys() & d2.keys())
    print("COMMON ITEMS")
    print(d1.items() & d2.items())
    print("IN d1 NOT IN d2")
    print(d1.keys() - d2.keys())

#d1 = {'a':1, 'b':2, 'c':3}
#d2 = {'a':1, 'b':2}
#dictDiff(d1,d2)

#1.10 Remove Duplicates from Sequence Maintaining Order
def removeDuplicate(seq):
    seen = set()
    for e in seq:
        if e not in seen:
            yield e
            seen.add(e)

#l = list(removeDuplicate([{'a':1, 'b':2, 'c':3}, 2]))
#print(l)
#l = list(removeDuplicate([1,5,2,1,9,1,5,10]))
#print(l)

#1.11 Name a slice
def nameSlice(seq):
    s= slice(2,5)
    return seq[s]

#print(nameSlice([n for n in range(15)]))

#1.12 Find most Frequent items in Sequence
def getMostCommon(seq,n):
    counter = Counter(seq)
    print(counter.most_common(n))

#getMostCommon([random.randint(1,10) for n in range(15)],3)

#1.13 Sort list of dictionaries by key or multiple keys
def sortDict(listDict, key):
    i = itemgetter(key)
    rows_by_key = sorted(listDict,key=i)
    print(rows_by_key)

def randomN(start,end):
    return random.randint(start,end)

#listDict = []
#[listDict.append({1: randomN(1,15), 2:randomN(1,15), 3:randomN(1,15)}) for e in range(5)]
#sortDict(listDict,1)

#1.14 Implement sorting for classes without sorting function

class User:
    def __init__(self,id):
        self.id = id

    def __repr__(self):
        return 'User({})'.format(self.id)

def sortUser(listUser):
    sortedListUser = sorted(listUser, key=attrgetter("id"))
    print(sortedListUser)

#listUser = [User(randomN(1,100)) for e in range(randomN(1,15))]
#sortUser(listUser)

#1.15 group by
def groupListDictBy(listDict,sortKey):
    for letter,items in groupby(listDict, key=itemgetter(sortKey)):
        print(letter)
        for i in items:
            print('!!!',i)

#listDict = [{'a':randomN(1,15),'b':randomN(1,15)} for e in range(randomN(5,10))]
#groupListDictBy(listDict,'b')

#1.16 Reduce or extract values of a sequence by some critiera
def filterSequence(seq,criteriaFunc):
    #return filter(seq,criteriaFunc)
    return [e for e in seq if criteriaFunc(e)]

#f = lambda x: x>12
#print(filterSequence([randomN(1,15) for e in range(randomN(10,15))], f))

#1.17 Make a subset of a dictionary
def subsetDict(dict,criteriaFunc):
    return {key:value for key,value in dict.items() if criteriaFunc(key)}

#criteriaFunc = lambda key : key > 5
#dict = {key:key*2 for key in range(10)}
#print(dict)
#print(subsetDict(dict,criteriaFunc))

#1.18 Access tuple elements by name
def getNamedTupleElement(tuple):
    print(tuple.height)

#Person = namedtuple('Person', ['height','age'])
#t = Person(168,28)
#getNamedTupleElement(t)

#1.20 Present multiple dictionaries as a single logical one
def createLogicalDict(dict1,dict2):
    return ChainMap(dict1,dict2)

d1 = {key:key*2 for key in range(10)}
d2 = {key:key*3 for key in range(5,15)}
c = createLogicalDict(d1,d2)
print(c[7])
print(c[13])
