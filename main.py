#Global variables for recipents
food_option = 1
med_option = 2
toiletries_option = 3
clothing_option = 4
fem_hyg_option = 5
child_care_option = 6
misc_option = 7
recip_global_list = [food_option, med_option, toiletries_option, clothing_option, fem_hyg_option, child_care_option, misc_option]

#Global bvariables for donors
donor_food_option = 1
donor_med_option = 2
donor_toiletries_option = 3
donor_clothing_option = 4
donor_fem_hyg_option = 5
donor_child_care_option = 6
donor_misc_option = 7

#Recipent selection
def recipSelection():
  return True

#Donor Selection
def donorSelection():
  return True
  
#When user first opens the website
print("Hello, Welcome to Help Express! Please select a profile.")
option_one = 1
option_two = 2

print(option_one, ". Recipent profile")
print(option_two, ". Donor profile")

#Where the recipent or donor pick their profiles
user_prof_input = int(input("Enter the option number (between 1 & 2) "))

#If user input is 1, then the user is directed to the recipent profile
if (user_prof_input == option_one):
  print("Welcome to the Recipent profile.")

  #Add general info
  user_full_name = input("Full name: ")

  #Checks to make sure the recipen enters the phone number in the right format
  number_of_tries = 0 

  while(number_of_tries < 10):
      user_phone_num = input("Phone Number (###)-###-####: ")
      if len(user_phone_num) != 12:
        print("Please enter phone number in (###)-###-#### format.")
        number_of_tries += 1
      if len(user_phone_num) == 12:
        break
        
  print("What do you need?")
  recip_list = ["Food", "Medicine (Over-The-Counter)", "Toiletries", "Clothing", "Feminine Hygiene Product", "Childcare Supplies", "Miscellaneous"]
  print(food_option, ".", recip_list[0])
  print(med_option, ".", recip_list[1])
  print(toiletries_option, ".", recip_list[2])
  print(clothing_option, ".", recip_list[3])
  print(fem_hyg_option, ".", recip_list[4])
  print(child_care_option, ".", recip_list[5])
  print(misc_option, ".", recip_list[6])

  counter = 0
  user_selection = int(input("Select which category you want to see (1-7) "))
#Recipent selection
  for i in recip_global_list:
      if (recip_global_list[counter] == user_selection):
        print (recip_list[counter])
        break
  
      else:
        counter += 1
  
#If the user input is 2, then the used is directed to the donor profile
if (user_prof_input == option_two):
  #Add general info
  print("Welcome to the Donor profile.")
    #Add general info
  user_full_name = input("Full name: ")

  #Checks to make sure the donor enters the phone number in the right format
  number_of_tries = 0 
  while(number_of_tries < 10):
      user_phone_num = input("Phone Number (###)-###-####: ")
      if len(user_phone_num) != 12:
        print("Please enter phone number in (###)-###-#### format.")
        number_of_tries += 1
      if len(user_phone_num) == 12:
        break
  print("What do you intend to donate?")
  
  donor_list = ["Food", "Medicine (Over-The-Counter)", "Toiletries", "Clothing", "Feminine Hygiene Product", "Childcare Supplies", "Miscellaneous"]
  print(food_option, ".", donor_list[0])
  print(med_option, ".", donor_list[1])
  print(toiletries_option, ".", donor_list[2])
  print(clothing_option, ".", donor_list[3])
  print(fem_hyg_option, ".", donor_list[4])
  print(child_care_option, ".", donor_list[5])
  print(misc_option, ".", donor_list[6])

  counter = 0
  user_selection = int(input("Select which category you want to donate (1-7) "))
#Recipent selection
  for i in recip_global_list:
      if (recip_global_list[counter] == user_selection):
        print (donor_list[counter])
        break
  
      else:
        counter += 1
  
#Comparisons
# if (food_option == donor_food_option)