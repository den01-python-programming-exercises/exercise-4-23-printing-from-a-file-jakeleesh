def main():
    #write your code below this line
    try:
        f = open("data.txt", "r")
        print(f.read())
    except:
        print("Error")
    finally:
        f.close()

if __name__ == '__main__':
    main()
