

# qbfile = open("qbdata.txt", "r")

# # for aline in qbfile:

# # 	values = aline.split()
# # 	print('QB ', values[0], values[1], 'had a rating of ', values[10])


# line = qbfile.readline()
# while line:
# 	values = line.split()
# 	print('QB ', values[0], values[1], 'had a rating of ', values[10])
# 	line = qbfile.readline()

# qbfile.close()



with open('qbdata.txt') as md:

	print(md)

	for line in md:
		print(line)

print(md)