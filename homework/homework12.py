my_list=["   arteM","ivan  ","vasYl "," Petro"," Petro   ","vasYl "]
def space (name):
    rep=name.replace(" ", "")
    cap=rep.capitalize()
    return cap
space_out=list(map(space,my_list))
print(set(space_out))