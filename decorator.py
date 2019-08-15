

def decor_for_connect(f):
    try:
        f()
    except:
        print("something wrong")
    finally:
       return f

