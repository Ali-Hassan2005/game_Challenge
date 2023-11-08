import random
import cv2

bags=[10,10,10]

def is_over():
    flag = True
    if bags[0]==0 and bags[1] ==0 and bags[2] ==0 :
        flag = False
    return flag
def display_image(status,user):
    if status == "win":
        img = cv2.imread("assets/1.jpeg")
        text = f"{user} won!"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (20, 50), font, 1, (255, 0, 0),5)
        cv2.imshow("Game Result", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else :
        img = cv2.imread("assets/2.png")
        text = f"{user} lose!"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (20, 50), font, 1, (255, 0, 0),5)
        cv2.imshow("Game", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def play_game():
    username = input("Enter your username: ")
    print("Welcome to the game!")

    while True :
        print(f"\nCurrent state of bags: {bags}")
        while True:
            try:
                bag = int(input("Enter the bag number (1, 2, 3): "))
                num_objects = int(input("Enter the number of objects to remove (1-5): "))

                if 1 <= bag <= 3 and 1 <= num_objects <= 5 and bags[bag - 1] >= num_objects :
                    bags[bag - 1] -= num_objects
                    print(f"{username} removed {num_objects} objects from bag {bag}.")
                    break
                else:
                    print("Invalid input. Try again.")
            except:
                print("Invalid input. Please enter valid numbers.")

        if not is_over():
            display_image("win",username)
            break  

        while True:
            comp_bag = random.randint(1, 3)
            comp_num_objects = random.randint(1,5) 
            if 1 <= comp_bag <= 3 and 1 <= comp_num_objects <= 5 and bags[comp_bag - 1] >= comp_num_objects:
                bags[comp_bag - 1] -= comp_num_objects
                print(f"Computer removed {comp_num_objects} objects from bag {comp_bag}.")
                break  

        if not is_over():
            display_image("Lost",username)
            break
            


play_game()                   

