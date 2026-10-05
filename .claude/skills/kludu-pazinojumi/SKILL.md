---
name: kludu-pazinojumi
description: Kļūdu paziņojumu noteikumi HTML formām. Izmanto vienmēr, kad veido vai maini formas mapē ui/, arī kad maini, kā forma rāda API kļūdas.
---

# Kļūdu paziņojumi

## Noteikumi
- Visi paziņojumi latviešu valodā.
- Uzruna "jūs" (Ievadiet, Pārbaudiet, Izvēlieties).
- Skaidri paskaidro, kurš lauks ir nepareizs. Lauku sauc tā, kā tas rakstīts formā (etiķete), nevis API nosaukumā.
- Paskaidro, kā kļūdu labot.
- Nekad neatkārto lietotāja ievadītu personas kodu: ne paziņojumā, ne konsolē, ne URL.
- Nerāda kļūdu kodus, HTTP statusus, API lauku nosaukumus vai tehniskus paziņojumus (piem., "INVALID_FORMAT", "HTTP 400", "personalCode").
- Kļūdas formulē cilvēkam saprotamā valodā.
- Validāciju dara API. Forma tikai pārvērš API kļūdu (`details[].field` + `details[].issue`) saprotamā tekstā.
- Ja kļūdas veids vai lauks nav zināms: "Pārbaudiet ievadītos datus un mēģiniet vēlreiz."
- Servera vai tīkla kļūdai: "Neizdevās nosūtīt iesniegumu. Mēģiniet vēlreiz."

## Paraugteksti
| Lauks | REQUIRED | INVALID_FORMAT | TOO_LONG |
|---|---|---|---|
| Personas kods | Ievadiet personas kodu. | Personas kods nav pareizs. Ievadiet 11 ciparus, piemēram, 123456-12345 vai 12345612345. | – |
| Vārds, uzvārds | Ievadiet vārdu un uzvārdu. | – | – |
| E-pasts | Ievadiet e-pasta adresi. | E-pasta adrese nav pareiza. Ievadiet adresi formā vards@piemers.lv. | – |
| Tēma | Izvēlieties tēmu. | – | – |
| Temats | Ievadiet iesnieguma tematu. | – | Temats ir pārāk garš. Saīsiniet to. |
| Teksts | Ievadiet iesnieguma tekstu. | – | Teksts ir pārāk garš. Saīsiniet to līdz 2000 rakstzīmēm. |
| Atbildes kanāls | Izvēlieties, kā vēlaties saņemt atbildi. | – | – |

## Nedrīkst
- "Nepareizs formāts" bez norādes, kā labot.
- "Iesniegums nav pieņemts (HTTP 400, VALIDATION_ERROR)".
- "Personas kods 32000000001 nav derīgs".
