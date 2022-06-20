def no_teen_sum(a, b, c):
  fini = fix_teen(a) + fix_teen(b) + fix_teen(c)
  return fini
  
def fix_teen(n):
    if 12<n<20:
        if n==15 or n==16:
            return int(n)
        else:
          return int(0)
    return int(n)

print(no_teen_sum(5,15,10))
