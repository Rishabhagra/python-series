def mat(s, d):
    (s_x, s_y), (d_x, d_y) = s, d
    route = set()
    for i in range( s_x , d_x+(1 if s_x<=d_x else -1) , (1 if s_x<=d_x else -1) ):
        if (i,s_y) not in route:
            route.add( (i,s_y) )
            print( (i,s_y) )

    for i in range( s_y , d_y+(1 if s_y<=d_y else -1) , (1 if s_y<=d_y else -1) ):
        if (d_x,i) not in route:
            route.add( (d_x,i) )
            print( (d_x,i) )



print('')
mat((1,2),(1,4))
