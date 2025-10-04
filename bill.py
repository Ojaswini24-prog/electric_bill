def calculate_bill(units):
    if units <= 100:
        return 0
    elif units <= 200:
        return (units - 100) * 5
    elif units <= 300:                                                
        return (100 * 5) + (units - 200) * 10
    else:
        return (100 * 5) + (100 * 10) + (units - 300) * 20
    
print("Total Bill: ₹", calculate_bill(units))    