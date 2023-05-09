"""
Structuri de date = zone de adrese de memorie care pot stoca mai multe valori
Exista patru tipuri de structuri de date:
- liste
- seturi
- tupluri
- dictionare
Atentie!!! nu incurcati tipurile de date cu structurile de date
tipuri de date = proprietati ale unui spatiu de memorie
structuri de date = adrese de memorie
"""

"""
1. Listele
Listele reprezinta adrese de memorie neomogene (pot stoca valori avand diverse tipuri de date)
care sunt ordonate pe baza de index si mutabile
mutabilitate = proprietatea unei structuri de date de a putea sa isi schimbe elementele
(exemplu: vreau sa mut elevul popescu in banca langa elevul ionescu)
Actiuni care se pot face asupra unei liste:
- adaugare elemente
- stergere elemente
- modificare element la un anumit index
- mutare element la un anumit index
Definirea listei se face pe baza unei perechi de paranteze patrate []
Se poate initializa si o lista goala
"""

# 1. Declararea si initializarea unei liste goale

# varianta 1
lista_studenti = []
print(f"Lista goala este: {lista_studenti}")

# varianta 2
lista_studenti = list()
print(f"Lista goala este: {lista_studenti}")

print(f"Dimensiunea listei goale este: {len(lista_studenti)}")

# 2. Declararea si intializarea unei liste (omogene) populate
lista_studenti_prezenti = ["Andreea", "Rene", "Florin", "Maria", "Alex", "Damian", "Alex", "Diana", "Dani", "Paula"]
lista_studenti_absenti = ["Vasi", "Rodica", "Catalin"]

# Observatie: pot sa initializez o lista plecand de la un string prin apelarea functiei split()
string_test = "Astazi invatam despre liste"
lista_split = string_test.split()
print(lista_split)

# 3.a. Accesarea primului element din lista
# putem sa ne referim la un element cu un anumit index folosind paranteze drepte nume_lista[nr_index]
print(f"Primul element din lista este: {lista_studenti_prezenti[0]}")

# 3.b Accesarea ultimului element din lista
print(f"Ultimul element din lista este: {lista_studenti_prezenti[len(lista_studenti) - 1]}")
print(f"Ultimul element din lista este: {lista_studenti_prezenti[-1]}")

# 4. Functii care pot sa fie folosite cu listele
# Functiile se pot apela prin intermediul numele listei urmat de punct

# 4.a Functia append() -> Adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Gabriela")
print(f"Lista de studenti dupa append este: {lista_studenti_prezenti}")

# 4.b Functia insert() -> Adauga un element in lista intr-o anumita pozitie
lista_studenti_prezenti.insert(3, "Cosmin")
print(f"Lista de studenti dupa adaugarea lui Cosmin este: {lista_studenti_prezenti}")

# 4.c Functia index() -> Returneaza indexul unui anumit element
print(f"Studentul Damian se afla in lista la indexul {lista_studenti_prezenti.index('Damian')}")

# 4.d Functia remove() -> Sterge un element pe baza numelui sau
lista_studenti_prezenti.remove("Cosmin")
print(f"Lista studenti prezenti dupa inlaturarea lui Cosmin este: {lista_studenti_prezenti}")

# 4.e Functia pop() -> Sterge un element pe baza de index
lista_studenti_prezenti.pop(len(lista_studenti_prezenti) - 1)
print(f"Lista studenti dupa scoaterea ultimului element este: {lista_studenti_prezenti}")

# 4.f Functia count() numara de cate ori apare un element intr-o lista
print(lista_studenti_prezenti.count("George"))

# 4.g. Functia reverse() -> inverseaza elementele listei
lista_studenti_prezenti.reverse()
print(f"Lista de studenti inversata este: {lista_studenti_prezenti}")
#
# 4.h Functia extend() uneste listele prin comasare
lista_studenti_prezenti.extend(lista_studenti_absenti)
print(f"Lista dupa extend() >>>>  {lista_studenti_prezenti}")

# 4.i Functia append() adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Gabriela")
print(f"Lista dupa append()  >>>> {lista_studenti_prezenti}")

# urmatoarea varianta creaza o lista imbricata
# lista imbricata (embedded list) = lista in lista
lista_studenti_prezenti.append(lista_studenti_absenti)
print(f"Lista dupa append() cu alta lista >>>> {lista_studenti_prezenti}")

#eliminam lista de studenti absenti
lista_studenti_prezenti.pop(len(lista_studenti_prezenti) - 1)

# 4.j Functia clear() -> sterge continutul listei
lista_studenti_prezenti.clear()
print(f"Lista studenti dupa apelarea metodei clear este: {lista_studenti_prezenti}")

# 4.k Functia sort() -> sorteaza lista in ordine alfabetica
lista_studenti_prezenti.sort()

print(f"Lista studenti dupa sortare este: {lista_studenti_prezenti}")
lista_studenti_prezenti.append("Cosmin")
lista_studenti_prezenti.sort()
print(f"Lista studenti dupa adaugarea lui Cosmin este: {lista_studenti_prezenti}")
# sortarea se va face in ordine alfabetica in functie de codul ASCII:
# https://infoas.ro/lectie/90/codul-ascii-tabel-complet

# 5. Crearea unei liste neomogene:
lista_neomogena = ["Andreea", 23, True, "Vasi", 28, False, "Felix", 45, True, "Rares", 38, False]

# 5.a Accesarea elementelor prin slicing (exact ca la stringuri)
# lista[index_start : index_stop : pas]
print(f"Persoanele din lista neomogena sunt: {lista_neomogena[::3]}")
print(f"Varsta lor este: {lista_neomogena[1::3]}")

"""
2. Seturi
Seturile reprezinta structuri de date neordonate, immutabile
Operatii care se pot face intr-un set:
- accesare elemente
- adaugare elemente
- stergere elemente
Definirea unui set se face cu o pereche de acolade
"""

# 1. Definirea unui set gol
set_gol = set()
print(type(set_gol))

# 2. Definirea unui set populat
set_pisici = {"tom", "garfield", "felix"}
set_catei = {"spike", "bethowen", "goofy", "pluto"}

# 3. Accesarea unui element din set
# Avand in vedere ca setul nu este indexat, NU putem accesa direct elementele din set
# Putem sa facem in schimb doua operatii similare:
# - parcurgerea setului cu for (vom face la cursul urmator)
# - putem sa verificam daca un element se afla in set cu operatorul IN
print("tom" in set_pisici)
assert "tom" in set_pisici, "Error: Tom nu exista in set_pisici"

# 4. Functii care pot fi folosite cu seturile
# 4.a functia add care adauga un nou element in set
set_pisici.add("Jinx")
set_pisici.add("Jinx")
print(f"Set pisici dupa adaugarea lui Jinx: {set_pisici}")

# 4.b Functia pop() sterge un element la intamplare
item_sters = set_pisici.pop()
print(f"Setul dupa stergerea elementului cu pop() este: {set_pisici}")
print(f"Elementul sters cu pop() este: {item_sters}")

# 4.c Functia remove() sterge un element specificat
set_pisici.add("meow")
set_pisici.remove("meow")
print(f"Setul dupa stergerea elementului 'meow' cu remove() este: {set_pisici}")

set_pisici.discard("meow")
# print("am trecut pe aici")

# Diferenta intre remove() si discard() este ca remove da eroare daca elementul nu exista
# si discard executa instructiunea dar nu da eroare daca elementul nu exista

# 4.c Functia update si functia union concateneaza doua seturi
set_pisici.update(set_catei)
print(f"Set pisici dupa update(): {set_pisici}")
set_rezultat = set_pisici.union(set_catei)
print(f"Set pisici dupa union(): {set_rezultat}")

# Diferenta intre update() si union() este ca update modifica lista de la care se pleaca direct,
# in schimb union creaza o a treia lista
# care reprezinta concatenarea celor doua liste implicate

# 4.c Functia clear() sterge continutul setului
set_pisici.clear()
print(f"Set pisici dupa clear(): {set_pisici}")


"""
Tupluri (tuples)
Tuplurile reprezinta structuri de date ordonate si identificabile
pe baza de index care accepta duplicate si este imutabil (immutable)
"""
# 1. Definirea unui tuplu gol:
# varianta 1
tuplu_gol = ()
print(tuplu_gol)

# varianta 2
tuplu_gol = tuple()
print(tuplu_gol)

# 2. Definirea unui tuplu populat:
tuplu_populat = ("mere", "pere", "nuci", "covrigi", "si-o bucata de sorici", "mere", "si gutui amarui")

# sau fara paranteze
greutate = 15, 6  # Daca definim o variabila in felul asta, va fi identifica automat ca si tuplu

print(greutate)

# 3. Functii care se pot folosi cu un tuplu
# 3.a Functia index returneaza indexul primului element dat ca parametru
print(f"Indexul fructului mere este: {tuplu_populat.index('mere')}")

# 3.b Functia count returneaza de cate ori apare un anumit element in tuplu
print(f"Fructul mar apare de {tuplu_populat.count('mere')} ori")

"""
4. Dictionarele
Un dictionar este o structura de date ordonata care contine mai multe perechi cheie: valoare
Cheile trebuie sa fie unice. Ele servesc drept inlocuitor pentru indexul de la liste
Operatii care se pot face intr-un dictionar:
- adaugare perechi
- stergere perechi
- modificare valoare cheie
- accesare elemente
"""

# 1. Creare dictionar gol:
# varianta 1
dict_gol = {}
print(dict_gol)

# varianta 2
dict_gol = dict()
print(dict_gol)

# 2. Creare dictionar populat:
masini = {
    "nume": "bmw",
    "model": "x5",
    "an_fabricatie": 2010,
    "tip_tractiune": "spate",
    "norme_euro": "euro4",
    "combustibil": "benzina"
}

# 3. Accesarea elementelor dintr-un dictionar.
# Sintaxa: nume_dict["cheie"] sau nume_dict.get("cheie")
print(f"Numele masinii este: {masini['nume']}")
print(f"Modelul masinii este: {masini.get('model')}")

# 4. Adaugarea elementelor in dictionar
# Sintaxa: nume_dict["proprietate_noua"] = valoare
masini["numar_locuri"] = 5
print(f"Masina are  {masini['numar_locuri']} locuri")

# 5.Actualizarea elementelor din dictionar
#varianta 1
masini.update({"norme_euro": "euro6"})
print(f"Norma europeana curenta este: {masini['norme_euro']}")

#varianta 2
masini["an_fabricatie"] = 2012
print(f"Am corectat anul de fabricatie al masinii la valoarea {masini['an_fabricatie']}")

# 6.Stergerea elementelor din dictionar
masini.pop("nume")
print(f"Dictionarul curent este {masini}")

# 7. Accesarea cheilor din dictionar
print(f"Proprietatile masinii mele sunt: {masini.keys()}")

# 8. Accesarea valorilor din dictionar:
print(f"Valorile proprietatilor masinii mele sunt: {masini.values()}")

# 9. Accesarea perechilor cheie: valoare
print(f"Dictionarul este format din urmatoarele elemente: {masini.items()}")

# 10. Dictionar imbricat
sucuri = {
    "pepsi": {
        "nume": "Pepsi",
        "producator": "Pepsi SRL",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "cola": {
        "nume": "Coke SRL",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "fanta":
        {
            "nume": "fanta",
            "producator": "Fanta Co",
            "impachetare": "bax",
            "promovare":
                {
                    "reclama": "Suc cu spirit tanar!"
                },
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}
print(sucuri["pepsi"]["impachetare"])
print(sucuri["fanta"]["promovare"]["reclama"])
print(sucuri["fanta"]["televiziune promovare"][2])


"""
pip install pylint
cd <calea la care se afla fisierul pe care vreau sa il analizez>
ls (list) -> pentru a vedea toate fisierele din folderul curent
 pylint curs_03.py -> evaluare fisier
"""