"""
    >>> Fundamentals

    > id(num) : returns address,
      type(num) : returns type of data that num contains.

    > any integer value is store in class <int>
      there is no concept like long, big int.

    > if it contains same value then the variable
      points to same address because there is 2 stages
      init + decl but in python that happens in one step
      Python has smart memory management.

    > arthematic (+, -, /, *, %, **, //)
      assignment (=, +=, /=, *=, %=, **=, //=)
      comparision (==, !=, >, <, >=, <=)
      logical (and, or, not)
      identity (is, is not) : checks same memory or not
      memebership (in, not in) : checks in sequence
      bitwise (&, |, ^, >>, <<, ~)

    > a number is converts into binary
      and if it finds single '1' it returns true

    > python never care about increment value in loop.
      It cares about the value mentioned in range
      if not then it 1 (start, end - 1, increment/decrement)

    > l = [1, 2, 3, 4, 5]
      l.append(num) : adds at end
      l.pop() : removes last element
      l[index] index -> (-inf, inf) : returns element
      l.sort() : sorts the list

    """


a = [1, 2, 3]
b = [1, 2, 3]

c = 1000
d = 1000

print(id(a), id(b))
print(a is b, c is d)


