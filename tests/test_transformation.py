#!/usr/bin/python
from skdb.geom import *
from skdb.gui import *
#test that a shape can be transformed in the same way that a make_vertex object is transformed
#test also gp_Pnt.Transform and BRepBuilderAPI_Transform
#do the points line up? vert2 and obj should be the same.
#now use SetTransformation

#TODO use TopExp to find the point of the arrow, then compare gp_Pnt's

if __name__ == "__main__":
    trsf1 = gp_Trsf()
    my_ax3 = gp_Ax3(gp_Ax2(gp_Pnt(0,2.1,0), gp_Dir(-1,1,1)))
    trsf1.SetTransformation(my_ax3)

    point2 = Point(0,0,0)
    point2.Transform(trsf1)
    vert2 = make_vertex(point2)

    #apply BRepBuilderAPI_Transform to vertex1
    vert1 = make_vertex(Point(0,2.1,0))
    obj = BRepBuilderAPI_Transform(vert1, trsf1, True).Shape()

    my_ax = gp_Ax2(gp_Pnt(0,2.1,0), gp_Dir(-1,1,1))
    my_ax.SetDirection(gp_Dir(-1,0,0))
    my_ax = gp_Ax3(my_ax)
    print my_ax.Direct() #when my_ax is gp_Ax3
    blahr = gp_Trsf(); blahr.SetTransformation(my_ax)
    arrow3 = Arrow().to(dest=blahr) #tests BRepBuilderAPI_Transform

    display.DisplayShape(make_vertex(Point(0,0,0))) #display origin marker
    display.DisplayShape(obj) #vert1 but with BRepBuilderAPI_Transform applied to it
    display.DisplayColoredShape(vert2,'GREEN') #make_vertex(point2)
    display.DisplayColoredShape(arrow3,'RED') #make_arrow_to

    start_display()

    pt1 = gp_Pnt(0,0,-1) #0,0,-1
    trsf1 = gp_Trsf()
    normal_vec = gp_Dir(0,1,0)
    x_vec = gp_Dir(1,0,0)
    trsf1.SetTransformation(gp_Ax3(gp_Ax2(gp_Pnt(0,0,0), gp_Dir(0,1,0), gp_Dir(1,0,0)))) #0,0,-1 --> 0,1,0
    print pt1.Transformed(trsf1).XYZ().X(); pt1.Transformed(trsf1).XYZ().Y(); pt1.Transformed(trsf1).XYZ().Z() #0, 1, 0


def tlater(point=Point(1,0,0), origin=Point(0,0,0), normal=Direction(0,0,1), vx=Direction(1,0,0)):
    '''
    constructs a transformation
    point = Point(point)
    origin = Point(origin)
    normal_vec = Direction(normal)
    x_vec = Direction(vx)
    '''
    point = Point(point)
    origin = Point(origin)
    normal_vec = Direction(normal)
    x_vec = Direction(vx)
    trsf = gp_Trsf()
    trsf.SetTransformation(gp_Ax3(gp_Ax2(origin, normal_vec, x_vec)))
    resulting_point = point.Transformed(trsf)
    print "\t(%s, %s, %s)" % (resulting_point.XYZ().X(), resulting_point.XYZ().Y(), resulting_point.XYZ().Z())
    return resulting_point

def big_test():
    for a in [0, 1, -1]:
        for b in [0, 1, -1]:
            for c in [0, 1, -1]:
                for d in [0, 1, -1]:
                    for e in [0, 1, -1]:
                        for f in [0, 1, -1]:
                            try:
                                normal = Direction(a,b,c)
                                vx = Direction(d,e,f)
                                print "normal=%s, vx=%s" % ([a,b,c], [d,e,f]) #% (normal, vx) <-- doesn't produce the right results
                                tlater(normal=normal, vx=vx)
                            except RuntimeError, v:
                                True #oops?
    return

