from sys import argv

script, filename = argv

print "I'm going to write these to %r file." % filename

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

txt = open(filename, 'w')

print "Writing......"

txt.write(line1 + "\n")
txt.write(line2 + "\n")
txt.write(line3 + "\n")

print "DONE! Closed file."
txt.close()

#If wanna empty file
#txt.truncate()
