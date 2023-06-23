anna_charge = (sum(bill) - bill[k]) / 2
    
    if b == anna_charge:
        print("Bon Appetit")
    else:
        # bill.remove(bill[k])
        # actual_charge = sum(bill)/2
        diff = b - anna_charge
        print(int(diff)) 
