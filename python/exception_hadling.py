# x = 5
# y = "hello"
# try:
# 	z = x + y
# except :
# 	print("Error: cannot add an int and a str")

# try:
# 	k = 5//0
# 	# print(k)

# #except ZeroDivisionError:
# #	print("Can't divide by zero")

# finally:
# 	print('This is always executed')

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise



# def this_fails():
#     x = 1/0

# try :
#     this_fails()
# except Exception as e:
#     print(f"Infinity error {e}")


# try: 
# 	raise NameError("Hi there")
# except TypeError:
# 	print ("An exception")
# 	raise
# except:
# 	print("Unknown error")
# 	raise


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)

