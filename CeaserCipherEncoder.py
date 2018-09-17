alphabets="abcdefghijklmnopqrstuvwxyz"
alp_list=list(alphabets)
#print alp_list
inp_string=raw_input("enter string")
shift=input("enter shift")

out=''
for i in inp_string.lower():
    shifted=((alp_list.index(i)+1)+shift)%26
    out=out+alp_list[shifted-1]

print out   
