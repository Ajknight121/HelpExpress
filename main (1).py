#Global variables for recipents
food_option = 1
med_option = 2
toiletries_option = 3
clothing_option = 4
fem_hyg_option = 5
child_care_option = 6
misc_option = 7
recip_global_list = [food_option, med_option, toiletries_option, clothing_option, fem_hyg_option, child_care_option, misc_option]

#Global recipient profile examples for option 6
recip_one_req = ["Diapers", "Baby Bottle", "Formula", "Baby Clothes", "Baby Wipes"]

recip_two_req = ["Toys", "Diapers", "Formula", "Stuffed Animal", "Blanket"]

#Global variables for donors
donor_food_option = 1
donor_med_option = 2
donor_toiletries_option = 3
donor_clothing_option = 4
donor_fem_hyg_option = 5
donor_child_care_option = 6
donor_misc_option = 7
  
#When user first opens the website
print("Hello, Welcome to Help Express! Please select a profile.")
option_one = 1
option_two = 2

print(option_one, ". Recipent profile")
print(option_two, ". Donor profile\n")

#Where the recipent or donor pick their profiles
user_prof_input = int(input("Enter the option number (between 1 & 2) "))
  
#If the user input is 2, then the used is directed to the donor profile
if (user_prof_input == option_two):
  #Add general info
  print("\nWelcome to the Donor profile.")
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
  print("\nWhat do you intend to donate?")
  
  donor_list = ["Food", "Medicine (Over-The-Counter)", "Toiletries", "Clothing", "Feminine Hygiene Product", "Childcare Supplies", "Miscellaneous"]
  print(food_option, ".", donor_list[0])
  print(med_option, ".", donor_list[1])
  print(toiletries_option, ".", donor_list[2])
  print(clothing_option, ".", donor_list[3])
  print(fem_hyg_option, ".", donor_list[4])
  print(child_care_option, ".", donor_list[5])
  print(misc_option, ".", donor_list[6])

  counter = 0
  user_selection = int(input("\nSelect which category you want to donate (1-7) "))
  
  #Donor selection
  for i in recip_global_list:
      if (recip_global_list[counter] == user_selection):
        print ("You picked:", donor_list[counter])
        break
  
      else:
        counter += 1
  
#Comparisons
  n = int(input("\nHow many items would you like to donate? "))
  print("\nWhich items from the list below do you have to donate?")
  print(" - Diapers")
  print(" - Baby Bottle")
  print(" - Formula")
  print(" - Blankets")
  print(" - Baby Clothes")
  print(" - Toys")
  print(" - School Supplies\n")
  list = []

  for i in range (n):
  
    user_input = input()
    list.append(user_input)

  print("\nHere is a list of potential matches: ")

  list.sort()
  recip_one_req.sort()
  recip_two_req.sort()

  recip_one_match_counter = 0
  recip_two_match_counter = 0
  print(len(list))
  for i in range(len(list)):
    if (list[i] == recip_one_req[0]):
     recip_one_match_counter += 1
    if (list[i] == recip_one_req[1]):
     recip_one_match_counter += 1
    if (list[i] == recip_one_req[2]):
     recip_one_match_counter += 1
    if (list[i] == recip_one_req[3]):
     recip_one_match_counter += 1
    if (list[i] == recip_one_req[4]):
     recip_one_match_counter += 1

    if (list[i] == recip_two_req[0]):
     recip_two_match_counter += 1
    if (list[i] == recip_two_req[1]):
     recip_two_match_counter += 1
    if (list[i] == recip_two_req[2]):
     recip_two_match_counter += 1
    if (list[i] == recip_two_req[3]):
     recip_two_match_counter += 1
    if (list[i] == recip_two_req[4]):
     recip_two_match_counter += 1
    else:
      i += 1
      
  recip_one_percentages = float(recip_one_match_counter/5) * 100
  recip_two_percentages = float(recip_two_match_counter/len(recip_two_req)) * 100

print("You matched with recipient #1 by: ", recip_one_percentages, "%" , "\n")
print("You matched with recipent #2 by: ", recip_two_percentages, "%", "\n")
print ("Which recipent would you like to donate to?")
recip_don_selection = input("Recipent 1 or Recipent 2? ")
print("Thank you for your contribution! Drop off the donations to their selected location.")