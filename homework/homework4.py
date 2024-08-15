cap= int(input("Скільки людей може вмістити автобус:"))
on= int(input("Скільки людей сидить в автобусі:"))
wait= int(input("Скільки людей чекають автобус:"))
if on + wait < cap:
    print("cap=" + str(cap) + "," + "on=" + str(on) + "," + "wait=" + str(wait) + "->" + str(0))



if on + wait > cap:
    print("cap=" + str(cap) + "," + "on=" + str(on) + "," + "wait=" + str(wait) + "->" + str(on + wait - cap))