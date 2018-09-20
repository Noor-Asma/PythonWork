import proj10_quad as quad

try:
    with open("quad_input.txt","r+") as fh:
        input_data=fh.readlines()
        
except IOError,e :
    raise AssertionError("cannot acces the input file")

valid_para=[]
valid_perimeter=[]
valid_area=[]

line_no=0
valid_parallelogram=0
invalid_parallelogram=0
no=1
print "*"*60
print "Input data"
for i in input_data:
    print "Line %i : %s" %(no,i)
    no+=1
print "*"*60


print "*"*60
for line in input_data:
    line_no+=1
    if line:
        sides=line.split(',')
        quad_ins=quad.Quad(sides[0],sides[1],sides[2])
        if quad_ins.is_valid():
            print "-"*60
            print "Valid paralleogram data"
            print "Paralellogram:",line
            perimeter=quad_ins.perimeter()
            print "Perimeter of parallelogram:" ,perimeter
            area=quad_ins.area()
            print "Area of parallelogram:",area
            valid_para.append(line)
            valid_perimeter.append(perimeter)
            valid_area.append(area)
            valid_parallelogram+=1
            del quad_ins
            print "-"*60

        else:
            print "*"*60
            print"Invalid Paralellogram Data:",line
            invalid_parallelogram+=1
            print "*"*60
    else:
         print "Line is empty"

print "*"*60
         

#length=len(valid_list)
"""
print valid_para
print valid_perimeter
print valid_area
"""


def average_perimeter():
    avg_peri=0
    for i in valid_perimeter:
        avg_peri+=float(i)
    length=len(valid_perimeter)
    return avg_peri/length

def average_area():
    avg_area=0
    for i in valid_area:
        avg_area+=float(i)
    length=len(valid_area)
    return avg_area/length

def find_max_perimeter_parallelogram():
    print "-"*60  
    max_peri=max(valid_perimeter)
    index=valid_perimeter.index(max_peri)
    largest_peri_paralleogram=valid_para[index]
    par_area=valid_area[index]
    print "Largest perimeter Parallelogram:",largest_peri_paralleogram
    print "Largest Perimeter:",max_peri
    print "Area:",par_area
    print "-"*60  

def find_max_area_parallelogram():
    print "-"*60  
    max_area=max(valid_area)
    index=valid_area.index(max_area)
    largest_area_paralleogram=valid_para[index]
    par_peri=valid_perimeter[index]
    print "Largest area Parallelogram:",largest_area_paralleogram
    print "Largest Area:", max_area
    print "Perimeter:",par_peri
    print "-"*60  



print "*"*60  
print "Total Processed lines:",line_no
print "Total Valid Paralleogram processed:",valid_parallelogram
print "Average perimeter of valid Paralleogram:" , average_perimeter()
print "Average area of valid Paralleogram:" , average_area()
find_max_perimeter_parallelogram()
find_max_area_parallelogram()
print "*"*60

