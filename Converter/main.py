# Pozdrav Uporabniku
print "Hello my name is KiloMile and i convert Kilometers to Miles. Enter value below and watch the magic happen :)"

print "Do you want to do a conversion? Answer yes or no. "

answer = (raw_input())

while answer == "yes":
    # Vnos Kilometrou
    kilometers = int(raw_input("Enter value in kilometers:"))
    # Izracun in Prikaz
    conv_fac = 1.609
    miles = kilometers * conv_fac
    print('%0.4f kilometers is equal to %0.4f miles' % (kilometers, miles))
    # Vprasanje o Nadalnji uporabi
    print "Do you want to do a new conversion? Answer yes or no. "
    answer = (raw_input())
if answer == "no":
    print "Goodbye my name is KiloMile and i'm out DOOOOITZ"
