f0 = 0
f1 = 1
set = False
while True:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    if (fn > 100):
        set = True
    else:
        set = False
    print(fn)
    if (set == True):
        break
    
