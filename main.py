# Program for finding percentage
obtained_number = input("Obtained Number: ")
total_number = input("Total number: ")

# kyun ke mazkura variables batour string mehfooz hue hain toh humein inhe int mein tabdeel karna hoga. 

obtained_number = float(obtained_number)
total_number = float(total_number)

ratio = obtained_number / total_number
percent = ratio * 100
print(f"percentage: {percent}%")