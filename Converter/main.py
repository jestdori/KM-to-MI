# Pozdrav Uporabniku
print "Hello my name is KiloMile and i convert Kilometers to Miles. Enter value below and watch the magic happen :)"

# Factor iz KM V Miles
conv_fac = 0.621372

# Vnos Kilometrou
kilometers = int(raw_input("Enter value in kilometers:" ) )

# Izracun In Prikaz
miles = kilometers * conv_fac
print('%0.4f kilometers is equal to %0.4f miles' %(kilometers,miles))

# Vprasanje o Nadalnji uporabi
print "Do you want to do a new conversion? Answer yes or no. "
answer = (raw_input())

# Loop
while answer == "yes":
    # Vnos Kilometrou
    kilometers = int(raw_input("Enter value in kilometers:"))
    # Izracun in Prikaz
    miles = kilometers * conv_fac
    print('%0.4f kilometers is equal to %0.4f miles' % (kilometers, miles))
    # Vprasanje o Nadalnji uporabi
    print "Do you want to do a new conversion? Answer yes or no. "
    answer = (raw_input())
if answer == "no":
    print "Goodbye my name is KiloMile and i'm out DOOOOITZ"