# Examples of different ways to print/format different types of values/variables
year = 2025
name = "Ngee Ann Polytechnic"
pi = 22/7

print (f"Eg1 Poly :  {name}, {year}, {pi}")
print (f"Eg2 Poly :  {name:30}, {year:8}, {pi:8.4f}")
print (f"Eg3 Poly :  {name:>30}, {year:<8}, {pi:<8.4f}")
print()     # print a blank line
print ("Eg4 {0}, {1}, {2}".format(name, year, pi))
print ("Eg5 {0}, {2}, {1}\n".format(name, year, pi)) #\n prints a blank line at the end
print ("Eg6 {:30s}, {:8d}, {:8.2f} ".format(name, year, pi))
print ("Eg7 %30s, %8d, %8.3f" % (name, year, pi)) 
print ("Eg8 %-30s, %-8d, %-8.3f" % (name, year, pi)) 