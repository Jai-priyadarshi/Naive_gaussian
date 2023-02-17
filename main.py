def gaussian(a1,a2,a3,b1,b2,b3,c1,c2,c3,z1,z2,z3):
    #update 1
    b2-=a2*b1/a1
    b3-=a3*b1/a1
    z2-=z1*b1/a1
    b1=0

    #update 2
    c2-=a2*c1/a1
    c3-=a3*c1/a1
    z3-=z1*c1/a1
    c1=0

    #update 3
    c3-=b3*c2/b2
    z3-=z2*c2/b2
    c2=0

    #back substitution
    x3=z3/c3
    x2=(z2-b3*x3)/b2
    x1=(z1-a2*x2-a3*x3)/a1

    print(x1)
    print(x2)
    print(x3)

gaussian(1,1,1,6,-7,8,2,5,-6,4,2,2)