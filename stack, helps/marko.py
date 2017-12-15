# //tehtävä 7
size = int(input("Box size (3-10)"))
if size > 10 or size < 3:
    raise Exception("Select between 3 and 10")

for a in range(0, size):
    print("* " * size)

# //tehtävä 8
# älä välitä mistään .format() setistä, ei alkuperäisessä tehtävän annossa.
# Tee pankki datalle mihin säilöt päivien tiedot tässä tapauksessa *List. DATE EI TEHTÄVÄN ANNOSSA, ei tarvi tallentaa.
# pythonissa mikä vaan string riittää määrittämään muuttujan c# muistaakseni "var + datatype + name"
# Listat : http://www.tutorialsteacher.com/csharp/csharp-list
# Range : https://www.dotnetperls.com/enumerable-range
#

data = []
date = 1

# d looppaa niin kauan kun se on välissä 0 - 30, koska d ei ole määritetty se lähtee ekasta määritetystä numerosta 0
# nousevasti kunnes osuu 30, eli tekee 30 looppia.

for d in range(0, 30):
    temp = int(input("Temperature for day{}\n".format(date)))  # variable temp pyytää integer userinputin
    # jos haluat c# tulostamaan kysymyksen on se tulostettava erikseen userinput koodia
    if temp > 30 or temp < -40:  # error säädös, or c#:ssä on kaksi tolppaa ||
        raise Exception("Where do u live in? space?")
    else:  # jos kaikki ok, lisätään lämpötila data pankkiin
        data = data + [temp]
        date += 1

average = 0  # pankki lämpötila laskulle
for n in data:  # looppaa kaikkien data pankissa olevien objectien läpi
    average = average + n  # ja lisää ne yhteen averagen kanssa joka on täten nouseva integer

average = average / 30  # lasketaan oikea keskiarvo, yhteislämpö / päivät.
if average > 11:
    print("T-shirt will be enough, average temperature of the month: {}c".format(
        average))  # Säännöt console tulostuksille
if average in range(0, 10):
    print("Spring is coming, average temperature of the month: {}c".format(average))
if average in range(0, -10):
    print("Nice skiing weather, average temperature of the month: {}c".format(average))
if average < -10:
    print("Cold winter weather, average temperature of the month: {}c".format(average))
