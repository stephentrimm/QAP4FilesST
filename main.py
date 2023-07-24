# Program Description: One Stop Insurance Company claims processing system
# Written By: Stephen Trimm
# Dates Written: July 18th to July 26th, 2023

# Import Required Libraries
import datetime
import time
from tqdm import tqdm

# Open the defaults file and read the values into variables
f = open("OSICDef.dat", "r")
NXT_POL_NUM = int(f.readline())                 # Next policy number
BASIC_PREM = float(f.readline())                # The basic premium
ADD_CAR_DISCOUNT = float(f.readline())          # Discount for additional cars
EXT_LIABILITY = float(f.readline())             # Extra liability costs
GLASS_COVERAGE= float(f.readline())             # Glass Coverage
LOANER_COVERAGE = float(f.readline())           # Loaner coverage
HST_RATE = float(f.readline())                  # HST Rate
PROCESS_FEE = float(f.readline())               # Processing fee for monthly payments
f.close()

# Inputs and Validations
while True:

    while True:
        FirstName = input("Enter the customer's first name (END to quit program): ").title()
        if FirstName == "":
            print("Error - Customer's first name cannot be blank.")
        else:
            break

    if FirstName.upper() == "END":
        print("Thank you for using One Stop Insurance Company. Have a great day!")
        break

    while True:
        LastName = input("Enter the customer's last name: ").title()
        if LastName == "":
            print("Error- Customer's last name cannot be blank. ")
        else:
            break

    FullName = FirstName + " " + LastName

    while True:
        StADD = input("Enter the customer's street address: ").title()
        if StADD == "":
            print("Error- Street address cannot be blank. ")
        else:
            break

    while True:
        City = input("Enter the customer's city: ").title()
        if City == "":
            print("Error - City cannot be blank. ")
        else:
            break

    ProvList = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV", ]
    while True:
        Prov = input("Enter the province (LL): ").upper()

        if Prov =="":
            print("Error - province cannot be blank. ")
        elif len(Prov) != 2:
            print("Error- Province must be 2 letters only.")
        elif Prov not in ProvList:
            print("Error - not a valid province.")
        else:
            break

    while True:
        PostCode = input("Enter the Postal Code: ").upper()

        if PostCode == "":
            print("Error - Postal Code cannot be blank. ")
        else:
            break

    while True:
        PhoneNum = input("Enter the customer's phone number (9999999999): ")

        if PhoneNum == "":
            print("Error - phone number cannot be blank.")
        elif not PhoneNum.isdigit():
            print("Error - phone number must be 10 digits.")
        elif len(PhoneNum) != 10:
            print("Error - phone number must be 10 digits")
        else:
            break
    PhoneNum = "(" + PhoneNum[0:3] + ")" + " " + PhoneNum[3:6] + "-" + PhoneNum[6:]

    while True:
        NumCars = int(input("Enter the number of cars being insured: "))

        if NumCars == "":
            print("Error - number of cars cannot be blank.")
        elif NumCars <1:
            print("Error  - At least one car must be insured.")
        else:
            break

    YNList = ["Y", "N"]

    while True:
        ExtraLiab = input("Would the customer like to purchase extra liability (Enter Y for Yes or N for No): ").upper()

        if ExtraLiab == "":
            print("Error - selection cannot be blank. ")
        elif ExtraLiab not in YNList:
            print("Error - Please enter Y for Yes or N for No.")
        else:
            if ExtraLiab == "Y":
                ExtraLiabDsp = "Yes"
            else:
                ExtraLiabDsp = "No"
            break

    while True:
        GlassCov = input("Would the customer like to purchase extra glass coverage (Enter Y for Yes or N for No)? ").upper()

        if GlassCov == "":
            print("Error - selection cannot be blank. ")
        elif GlassCov not in YNList:
            print("Error - please enter Y for Yes or N for No.")
        else:
            if GlassCov == "Y":
                GlassCovDsp = "Yes"
            else:
                GlassCovDsp = "No"
            break

    while True:
        OptLoaner = input("Would you like to rent a loaner car (Enter Y for Yes or N for No)?  ").upper()

        if OptLoaner == "":
            print("Error - selection cannot be blank.")
        elif OptLoaner not in YNList:
            print("Error - please enter Y for Yes or N for No. ")
        else:
            if OptLoaner == "Y":
                OptLoanerDsp = "Yes"
            else:
                OptLoanerDsp = "No"
            break

    FMList = ["F", "M"]

    while True:
        PayOption = input("Enter F for payment in Full or M for Monthly payments: ").upper()

        if PayOption == "":
            print("Error - selection cannot be blank.")
        elif PayOption not in FMList:
            print("Error - Enter F for full payment or M for monthly payment. ")
        else:
            if PayOption == "F":
                PayOptionDsp = "Paid in Full"
            else:
                PayOptionDsp = "Monthly Payment"
            break

    # Calculations:
    ExtraCostOne = 0                                       # ExtraCostOne calculates the discount per additional car
    if NumCars == 1:
        ExtraCostOne = BASIC_PREM
    else:
        ExtraCostOne = BASIC_PREM + (NumCars - 1) * BASIC_PREM * ADD_CAR_DISCOUNT

    ExtraCostTwo = 0                                       # ExtraCostTwo adds extra liability per car if applicable
    if ExtraLiab == "N":
        ExtraCostTwo = 0
    else:
        ExtraCostTwo = EXT_LIABILITY * NumCars

    ExtraCostThree = 0                                      # BonusThree adds glass coverage per car if applicable
    if GlassCov == "N":
        ExtraCostThree = 0
    else:
        ExtraCostThreeThree = GLASS_COVERAGE * NumCars

    ExtraCostFour = 0                                       # BonusFour adds loaner car coverage if applicable
    if OptLoaner == "N":
        ExtraCostFour = 0
    else:
        ExtraCostFour = LOANER_COVERAGE * NumCars

    TotalExtra = ExtraCostOne + ExtraCostTwo + ExtraCostThree + ExtraCostFour   # Total extra cost
    TotalPrem = BASIC_PREM + TotalExtra                                         # total premium cost
    HstCost = TotalPrem * HST_RATE                                              # Hst on total premium
    TotalCost = TotalPrem + HstCost                                             # Total cost after HST added
    CurrDate = datetime.datetime.now()                                          # the current date
    InvDate = CurrDate.date()                                                   # the invoice date is the current date

    if PayOption == "F":
        Payment = TotalCost
    else:
        Payment = (TotalCost + PROCESS_FEE)/8
        NxtMonth = CurrDate.month % 12 + 1
        NxtYear = CurrDate.year if NxtMonth != 1 else CurrDate.year + 1
        NxtPayDate = CurrDate.replace(month=NxtMonth, year=NxtYear, day=1)

# Formatted Outputs

    TotalExtraDsp = "${:,.2f}".format(TotalExtra)
    TotalPremDsp = "${:,.2f}".format(TotalPrem)
    HstCostDsp = "${:,.2f}".format(HstCost)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    print()
    print("      One Stop Insurance Company")
    print("           Customer Invoice")
    print(" ------------------------------------")
    print()
    print(f" Invoice Date: {InvDate}")
    print(f" Customer Name: {FullName}")
    print(f" Address: {StADD:<20s}")
    print(f"          {City}, {Prov}, {PostCode}")
    print(f" Phone Number: {PhoneNum:<10s}")
    print(f" Number of cars insured: {NumCars}")
    print(f" Extra Liability: {ExtraLiabDsp}")
    print(f" Glass Coverage: {GlassCovDsp}")
    print(f" Optional Loaner: {OptLoanerDsp}")
    print(f" Total Extra Charges: {TotalExtraDsp}")
    print(f" Total Premium Cost: {TotalPremDsp}")
    print(f" HST Cost: {HstCostDsp}")
    print(f" Total Cost: {TotalCostDsp}")
    print(f" Payment: {PayOptionDsp}")

    if PayOption == "M":
        print(f" Monthly Payment: ${Payment:,.2f}")
        print(f" Next Payment Date: {NxtPayDate.strftime('%B %d, %Y')}")
    print()
    print(" ------------------------------------")
    print()
    print(" Thank you for choosing One Stop Insurance Company")
    print(" Have a fantastic day!")
    print()
    print()

    print("Saving insurance claim data....")
    # Add a progress bar or reasonable option here.
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Insurance claim data successfully saved....")
    time.sleep(1)

    # Write the values to a file for future reference
    f = open("Policies.dat", "a")
    f.write(f"{NXT_POL_NUM}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{FullName}, ")
    f.write(f"{StADD}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{ExtraLiab},")
    f.write(f"{GlassCov}, ")
    f.write(f"{OptLoaner}, ")
    f.write(f"{PayOptionDsp}, ")
    f.write(f"{TotalPrem}\n")
    f.close()

    NXT_POL_NUM += 1

    # write the current values back to the default file.
    f = open("OSICDef.dat", "w")
    f.write(f"{NXT_POL_NUM}\n")
    f.write(f"{BASIC_PREM}\n")
    f.write(f"{ADD_CAR_DISCOUNT}\n")
    f.write(f"{EXT_LIABILITY}\n")
    f.write(f"{GLASS_COVERAGE}\n")
    f.write(f"{LOANER_COVERAGE}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")
    f.close()








