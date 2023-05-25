def check(str, tags):
    for tag in tags:
        if tag in str:
            return True
    return False

str = "sdf: sedf"
tags = {":", "："}
if check(str, {"sd"}) and check(str, tags):
    print("SSSS")
else :
    print("CCC")