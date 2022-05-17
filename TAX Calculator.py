#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i=0
while (i==0):
    salary= float(input("Enter your income from salary: \n")) #asked for the salary input of the user
    other= float(input("Enter your income from Other sources: \n")) #asked for other incomes of the user
    interest= float(input("Enter your income from Interest in savings: \n")) #asked for the interest getting paid 
    investment= float(input("Enter your Investment Amount: \n")) #asked for the investment amount to the user because Investments for tax savings help save tax. A total of 20% of the investments are subtracted from the total income for computation of tax
    income= salary+ other +interest #income is the sum of all the individual incomes of the user
    Total_income = income-(investment*(20/100)) #Total_income is the income after substracting the investment amount
    print("Your total income after reducing 20% of Investment amount from income is ",Total_income, " from your Investments")
    tax= 0.0 #defining tax as 0.0 as the initial value
    if Total_income <= 500000: #put conditions inorder to find the tax of amount less than 500000
        tax= 0
        print("tax is: ", tax) 
    elif Total_income > 500000 and Total_income <1000000:  #put conditions inorder to find the tax of amount less than 1000000
        tax = Total_income* .20
        print(tax)
    elif Total_income > 1000001: #put conditions inorder to find the tax of amount more than 1000000
        tax = Total_income *.30
        print("Your Taxable amount is: \n", tax)
    i= int(input("Do You Want to Continue?: press 0 to continue ")) #for continue again
 
    print("**THANK YOU**\n")


# In[ ]:




