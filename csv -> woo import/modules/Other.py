import csv
import os


class Other:
    def __init__(self, sifra, naziv, kratkiO, opis, proizvajalec, orgLink, kategorije, kategorije2, cena, skrij, slike, navodila, opozorila, sestavine, odgOseba, certifikati, video, barva, volumen):
        self.sifra = sifra
        self.naziv = naziv
        self.kratkiO = kratkiO
        self.opis = opis
        self.proizvajalec = proizvajalec
        self.orgLink = orgLink
        self.kategorije = kategorije
        self.kategorije2 = kategorije2
        self.cena = cena
        self.skrij = skrij
        self.slike = slike
        self.navodila = navodila
        self.opozorila = opozorila
        self.sestavine = sestavine
        self.odgOseba = odgOseba
        self.certifikati = certifikati
        self.video = video
        self.barva = barva
        self.volumen = volumen

    def preimenujSlike(self):
        data = self.naziv

        data = data.lower()
        data = data.replace("'", "")
        data = data.replace("-", "")
        data = data.replace(",", "")
        data = data.replace(".", "")
        data = data.replace(" ", "_")
        data = data.replace("__", "_")
        data = data.replace("š", "s")
        data = data.replace("č", "c")
        data = data.replace("ž", "z")
        data = data.replace("ć", "c")

        tmp = ""

        for i, ph in enumerate(self.slike):
            if ph.strip() == "":
                continue

            end = ph.split(".")[-1:][0]
            newF = str(data)+"_"+str(i)+"."+end

            os.system("wget --no-check-certificate -nc "+str(ph) +
                      " -O files/out/"+newF+" > /dev/null")

            tmp += "https://www.komelt.dev/akademija/"+newF+","

        # print(tmp)

        self.slike = tmp

        # print(self.slike)

    def zdruziKategorije(self):
        tmp = ""
        for kat in self.kategorije:
            if kat.strip() == "":
                continue
            tmp += kat.strip().capitalize()+">"

        if tmp[-1:] == ">":
            tmp = tmp[:-1]
        self.kategorije = tmp

        tmp = ""
        for kat in self.kategorije2:
            if kat.strip() == "":
                continue
            tmp += kat.strip()+">"

        if tmp[-1:] == ">":
            tmp = tmp[:-1]
        self.kategorije2 = tmp


def other(csv_reader: csv.reader):
    prodArr = []

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("")
        else:
            izd = Other(row[0], row[1], row[2], row[3], row[4], row[5], [row[6], row[7], row[8]], [row[9], row[10], row[11]], row[12], row[13], [
                row[14], row[15], row[16], row[17], row[18], row[19], row[20]], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28])

            izd.preimenujSlike()
            print("\n"+izd.naziv)
            print(izd.slike)
            izd.zdruziKategorije()

            prodArr.append(izd)

        line_count += 1

    return prodArr
