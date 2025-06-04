
class College:

    name = "\nWelcome to SGM College Karad !!!!!!"
    
    def __init__(self, art_dept, com_dept, sce_dept):
        self.art_dept = art_dept
        self.com_dept =  com_dept
        self.sce_dept =  sce_dept


branch = College("\nWelcome in Art Department", "\nWelcome in Commerce Department", "\nWelcome in Science Department")


class Dep_Fees(College):
    
    
    def __init__(self, art_dept, com_dept, sce_dept, art_fees, com_fees, sce_fees):
        
        super().__init__(art_dept, com_dept, sce_dept)
        
        self.art_fees = art_fees
        self.com_fees = com_fees
        self.sce_fees = sce_fees

    
fees = Dep_Fees("Welcome in Art Department", "Welcome in Commerce Department", "Welcome in Science Department", 1800, 5500, 14000)


class ssc_marks(Dep_Fees):
    
    @staticmethod
    def get_marks():
        print("\n--- Applicant, Check Your Marks Eligibility ---")
        
        try:
            M = int(input("Enter Your SSC Marks (out of 100): "))
            if M >= 70:
                print("Congratulations! With marks, you are eligible for admission based on marks.")

                return True
            else:
                print("Sorry, your marks are below 70. Please choose another college or check other criteria.")

                return False
        except:

            print("Invalid input. Please enter a number for marks.")

            return False




if ssc_marks.get_marks():
    print(College.name)
    dep = int(input("\nFOR ART ENTER 1 | FOR COMMERCE ENTER 2 | FOR SCIENCE ENTER 3 :- "))
    
    if dep == 1:
        print(branch.art_dept)
        print("Fees of Art Department- ",fees.art_fees)
    elif dep == 2:
        print(branch.com_dept)
        print("Fees of Commerce Department- ",fees.com_fees)

    elif dep == 3:
        print(branch.sce_dept)
        print("Fees of Science Department- ",fees.sce_fees)

    else:
        print("Invalid department choice. Please enter 1, 2, or 3.")

else:
    pass