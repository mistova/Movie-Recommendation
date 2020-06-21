movies = {}                                                 #name, category, ageBottomLimit, quality
adminId = "123321"                                          #Expert to add movies
adminPass = "321123"
dosyas = open("satisfaction.txt", 'r')
satisfaction, t = dosyas.readline().split('\n')
satisfaction = float(satisfaction)
satisfactionCount = dosyas.readline()
satisfactionCount = int(satisfactionCount)
dosyas.close()
class movie:
    name = ""
    category = ""
    age = 0
    quality = 0.0
    def __init__(self, name, category, age, quality):
        self.name = name
        self.category = category
        self.age = age
        self.quality = quality

dosya = open("movies.txt", 'r')
while True:                                                 #get datas in movies.txt.
    temp = dosya.readline()
    if temp == "0":
        break
    temp,       t = temp.split('\n')
    category,   t = dosya.readline().split('\n')             #\n 's out
    age,        t = dosya.readline().split('\n')
    quality,    t = dosya.readline().split('\n')
    movies[temp] = movie(temp, category, int(age), float(quality))
dosya.close()


def showMovies():
    print("\n\nName\t\tCategory\t\tMin Age\t\tQuality\n")
    for i in movies:
        print(movies[i].name, "\t\t", movies[i].category, "\t\t", movies[i].age, "\t\t", movies[i].quality, "\n")

def searchMovie():
    i = input("Name of movie :")
    if i in movies:
        print("\n\nName\t\tCategory\t\tMin Age\t\tQuality\n")
        print(movies[i].name, "\t\t", movies[i].category, "\t\t", movies[i].age, "\t\t", movies[i].quality, "\n")
    else:
        print("\nNo movie found !\n")

def isSuit(age, degree, mov):
    if(age < mov.age):
        return False
    elif(degree * 2 > mov.quality * satisfaction):
        return False
    elif(age > (mov.quality * mov.quality + age/10) * satisfaction):
        return False
    elif(mov.category == "Cartoon" and age > 16 * satisfaction):
        return False
    elif(mov.category == "Horror"  and age * satisfaction < 18):
        return False
    elif(age * degree > (mov.quality * mov.quality * mov.quality +(age * degree)/10) * satisfaction):
        return False
    else:
        return True

def showList(name, age, degree):
    print("\n\nRecommended List of", name)
    print("\nName\t\tCategory\t\tMin Age\t\tQuality\n")
    for i in movies:
        if(isSuit(age, degree, movies[i])):
            print(movies[i].name, "\t\t", movies[i].category, "\t\t", movies[i].age, "\t\t", movies[i].quality, "\n")

def save():
    dosya = open("movies.txt", 'w')
    for i in movies:
        dosya.writelines(movies[i].name + '\n')
        dosya.writelines(movies[i].category + '\n')
        dosya.writelines(str(movies[i].age) + '\n')
        dosya.writelines(str(movies[i].quality) + '\n')
    dosya.writelines("0")
    dosya.close()

def adminLogin():                                           #Admin edits movies.
    id = input("Please enter expert id :")
    password = input("Please enter expert pasword :")
    if id == adminId and password == adminPass:
        while True:
            print("\n\n")
            print("1 - ) Show movies")
            print("2 - ) Add movie")
            print("3 - ) Delete movie")
            print("4 - ) Edit movie")
            print("5 - ) Search movie")
            print("6 - ) Save and Back")
            choice = input("\nPlease choose an operation :")
            if choice == "1":
                showMovies()
            elif choice == "2":
                name = input("Enter a movie name : ")
                category = input("Enter a category : ")
                age = int(input("Enter min age : "))
                quality = float(input("Enter quality point : "))
                movies[name] = movie(name, category, age, quality)
            elif choice == "3":
                temp = input("Name of movie :")
                if temp in movies:
                    movies.pop(temp)
                else:
                    print("\nProduct is not valid !\n")
            elif choice == "4":
                temp = input("Name of movie :")
                if temp in movies:
                    movies.pop(temp)
                    name = input("Rename movie : ")
                    category = input("Enter a category : ")
                    age = int(input("Enter min age : "))
                    quality = float(input("Enter quality point : "))
                    movies[name] = movie(name, category, age, quality)
                else:
                    print("\nProduct is not valid  !\n")
            elif choice == "5":
                searchMovie()
            elif choice == "6":
                save()
                break
            else:
                print("\n\tInvalid Operation !\n")
    else:
        choice = input("Wrong id or password\nSelect '1' for try again :")
        if choice == "1":
            adminGirisi()
        else:
            print("\nTurned Back !\n")


def userLogin():
    global satisfaction
    global satisfactionCount
    while True:
        print("\n\n")
        print("1 - ) Show movies")
        print("2 - ) Search Movies")
        print("3 - ) **Recommended Movies For You**")           #Desired action
        print("4 - ) Main Menu")
        choice = input("\nPlease choose an operation :")
        if choice == "1":
            showMovies()
        elif choice == "2":
            searchMovie()
        elif choice == "3":
            name = input("\nEnter Your Name :")
            age  = int(input("\nEnter Your Age :"))
            print("\n1 - ) Primary School")
            print("2 - ) High School")
            print("3 - ) Undergradute")
            print("4 - ) Graduate")
            degree = int(input("\nSelect Your school degree :"))
            showList(name, age, degree)
            temp = int(input("\nGive a point between 1 - 10 to recommended list :"))
            satisfaction = (temp/10 + satisfaction * satisfactionCount) / (satisfactionCount + 1)
            satisfactionCount += 1
            sat = open("satisfaction.txt", 'w')
            sat.writelines(str(satisfaction) + '\n')
            sat.writelines(str(satisfactionCount))
            sat.close()
        elif choice == "4":
            break
        else:
            print("\n\tInvalid Operation !\n")


while True:                                                     #Main Menu
    choice = input("\n\n1 - ) Admin Login\n2 - ) User Login\n3 - ) Exit\n\nPlease choose an operation :")
    if choice == "1":
        adminLogin()
    elif choice == "2":
        userLogin()
    elif choice == "3":
        break
    else:
        print("\n\tInvalid Operation !\n")