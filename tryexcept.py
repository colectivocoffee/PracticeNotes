# def division_from_user():
# 	dividend = int(input("Please enter the dividend: "))
# 	divisor = int(input("Please enter the divisor: "))
# 	print("%d / %d = %f" % (dividend, divisor, dividend/divisor))



# try:
# 	division_from_user()
# # except(ValueError, ZeroDivisionError) as e:
# #     print("Oops, something went wrong!", e)
# except ValueError as ve:
# 	print('value error', ve)
# except ZeroDivisionError as ze:
# 	print('zero division error', ze)
# finally:
# 	print('time to go back to sleep now!')
# 	#division_from_user()


try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("%s is not a valid age. Age must be positive or zero." % age)
except ValueError as err:
    print("You entered incorrect age input: %s" % err)
else:
    print("I see that you are %d years old." % age)