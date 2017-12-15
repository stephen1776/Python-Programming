'''
6.9 (Conversions between feet and meters) Write a module that contains the following
two functions:

def footToMeter(foot):
# Converts from feet to meters

def meterToFoot(meter):
# Converts from meters to feet

The formulas for the conversion are:
foot = meter / 0.305
meter = 0.305 * foot
Write a test program that invokes these functions to display tables.
'''
# Convert from feet to meters
def footToMeter(foot):
    meters = 0.305 * foot
    return meters

# Convert from meters to feet
def meterToFoot(meter):
    feet = meter / 0.305
    return feet


def main():
    print(format("Feet", "<15s"), format("Meters", "<15s"), "  |    ", format("Meters", "<15s"),
          format("Feet", "<15s"))
    print("---------------------------------------------------------------")

    Feet = 1
    meters = 20
    i = 1

    while i <= 10:
        print(format(Feet, "<15.1f"), format(footToMeter(Feet), "<15.3f"), "  |    ",
              format(meters, "<15.1f"), format(meterToFoot(meters), "<15.3f"))
        Feet += 1
        meters += 6
        i += 1

if __name__ == '__main__':
    main()
