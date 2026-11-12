# loop control statement

print ("range of 1 to 6 skip 3 and stop when reach at 5 :-")

for num in range(1, 6):
    if num == 3:
        continue  # Skips printing 3
    if num == 5:
        break     # Stops the loop entirely when reaching 5
    print(num)    # Output will be: 1, 2, 4