import requests
api_key = "842b08e0-7dee-4b92-967e-973eaea6cacb"
url = "https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke="
kjennemerke = input("Skriv inn kjennemerke: ")
endpoint = f"{url}{kjennemerke}"
response = requests.get(endpoint, headers={'SVV-Authorization': api_key})

if response.status_code == 200:
     understellsnummer = response.json()["kjoretoydataListe"][0]["kjoretoyId"]["understellsnummer"]
     registreringsstatus = response.json()["kjoretoydataListe"][0]["registrering"]["registreringsstatus"]["kodeBeskrivelse"]
     forstegangRegistrertDato = response.json()["kjoretoydataListe"][0]["godkjenning"]["forstegangsGodkjenning"]["forstegangRegistrertDato"]
     kjoretoyklassifisering = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["kjoretoyklassifisering"]["beskrivelse"]
     karosseritype = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["karosseriOgLasteplan"]["karosseritype"]["kodeNavn"]
     plasseringAvDorer = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["karosseriOgLasteplan"]["plasseringAvDorer"]["kodeBeskrivelse"]
     rFarge = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["karosseriOgLasteplan"]["rFarge"][0]["kodeNavn"]
     rFarge_beskrivelse = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["karosseriOgLasteplan"]["rFarge"][0]["kodeBeskrivelse"]
     drivstoff = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["motorOgDrivverk"]["motor"][0]["drivstoff"][0]["drivstoffKode"]["kodeNavn"]
     girkassetype = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["motorOgDrivverk"]["girkassetype"]["kodeNavn"]
     motorkode = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["motorOgDrivverk"]["motor"][0]["motorKode"]
     merke = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["generelt"]["merke"][0]["merke"]
     handelsbetegnelse = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["generelt"]["handelsbetegnelse"][0]
     sitteplasser_foran = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["persontall"]["sitteplasserForan"]
     sitteplasser_Totalt = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["persontall"]["sitteplasserTotalt"]
     
     bil_dimensjoner = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["dimensjoner"]
     bil_bredde = bil_dimensjoner["bredde"]
     bil_lengde = bil_dimensjoner["lengde"]
     
     vekter = response.json()["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["vekter"]
     egenvekt = vekter["egenvekt"]
     egenvekMinimum = vekter["egenvektMinimum"]
     nyttelast = vekter["nyttelast"]
     tillattTotalvekt = vekter["tillattTotalvekt"]
     tillattVogntogvekt = vekter["tillattVogntogvekt"]
     
     sist_eierskifte = response.json()["kjoretoydataListe"][0]["registrering"]["fomTidspunkt"]
     sist_EU_godkjent = response.json()["kjoretoydataListe"][0]["periodiskKjoretoyKontroll"]["sistGodkjent"]
     neste_EU_Kontroll = response.json()["kjoretoydataListe"][0]["periodiskKjoretoyKontroll"]["kontrollfrist"]
     
     print("\nReg_status         |", registreringsstatus)
     print("Først Registrert   |", forstegangRegistrertDato)
     print("Sist Eierskifte    |", sist_eierskifte[:10])
     print("===================|====================")
     print("Sist EU godkjent   |", sist_EU_godkjent)
     print("Neste EU kontroll  |", neste_EU_Kontroll)
     print("===================|====================")
     print("Merke              |", merke, "|", handelsbetegnelse)
     print("===================|====================")
     print("Farge              |", rFarge)
     print("===================|====================")
     print("Drivstoff          |", drivstoff)
     print("Girkassetype       |", girkassetype)
     print("===================|====================")
     print("klassifisering     |", kjoretoyklassifisering)
     print("Karosseri_type     |", karosseritype)
     print("Antall_Dører       |", plasseringAvDorer)
     print("Sitteplasser       |", sitteplasser_Totalt, "plasser")
     print("===================|====================")
     print("Understellsnummer  |",understellsnummer)
     print("Motorkode          |", motorkode)
     print("===================|====================")
     print("Bredde             |", bil_bredde, "cm")
     print("Lengde             |", bil_lengde, "cm")
     print("Egenvekt           |", egenvekt, "kg")
     print("Egenvekt_min       |", egenvekMinimum, "kg")
     print("Nyttelast          |", nyttelast, "kg")
     print("Tillatt_totalvekt  |", tillattTotalvekt, "kg")
     print("Tillat_vogntogvekt |", tillattVogntogvekt, "kg")
     print("===================|====================\n")
else:
     print("Error:", response.status_code)

