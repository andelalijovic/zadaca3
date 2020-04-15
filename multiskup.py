class MultiSkup(object):
  def __init__(self, kolekcija):
    self.dict = {}
    for i in kolekcija:
      if str(i) not in self.dict:
        self.dict[str(i)] = 1
      else:
        self.dict[str(i)] += 1
  def __str__(self):
    cnt = 1
    s = "{{"
    for i in self.dict:
      s = s + str(i) + "*" + str(self.dict[i])
      if cnt != len(self.dict):
        s += ", "
      cnt += 1
    s = s + "}}"
    return(s)
  def __iter__(self):
    iterable = []
    for i in self.dict:
      for j in range(0, self.dict[i]):
        iterable.append(i)
    return iter(iterable)
  def __repr__(self):
    represent = []
    for i in self.dict:
      for j in range(0, self.dict[i]):
        represent.append(int(i))
    return "MultiSkup(" + str(represent) + ")"
  def add(self, el, numT = 1):
    if str(el) not in self.dict:
      self.dict[str(el)] = numT
    else: 
      self.dict[str(el)] += numT
  def remove (self, el, numT = 1):
    if str(el) in self.dict:
      if self.dict[str(el)] <= numT:
        del self.dict[str(el)]
      else:
        self.dict[str(el)] -= numT

print("*** test 1 ***")
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)
print("\n")
print("*** test 2 ***")
for el in a:
  print(el)
print(repr(a))
print("\n")
print("*** test 3 ***")
a.add(4)
print(a)
a.add(2, 3)
print(a)
a.remove(4, 2)
print(a)