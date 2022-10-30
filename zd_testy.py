# zad 1 Napisz klase ktora bedzie posiadala metode obliczajaca nww i nwd,
# napisz do tej klasy klase testowa sprawdzajaca NWD i nww
# zad 2 Napisz klase posiadajaca liste ulubionych aut,
# napisz mchanizm sortowania, wypisywania duplikatow, usuwania duplikatow
# napisz niezbedne testy pod zadane funkcjonalnosci
# zad 3 Calosc zamiesc na gitHub

class NwdNww:
    @classmethod
    def nwd(cls,a,b):
        if not isinstance(a,int) or not isinstance(b, int):
            raise TypeError('Błędny typ danych')
        a = abs(a)
        b = abs(b)
        while b!=0:
            tmp = b
            b = a % b
            a = tmp
        return a
    @classmethod
    def nww(cls,a,b):
        if not isinstance(a,int) or not isinstance(b, int):
            raise TypeError('Błędny typ danych')
        return (a * b) / cls.nwd(a,b)

class auto:
    _auta = []
    @classmethod
    def dodaj_auto(cls, marka):
        cls._auta.append(marka)

    @classmethod
    def sortuj_auta(cls):
        cls._auta.sort()

    @classmethod
    def wypisz_auta(cls):
        print('-'*40)
        for a in cls._auta:
            print(a)

    @classmethod
    def znajdz_duplikaty(cls):
        d = []
        start = 1
        for s in cls._auta:
            for i in range(start, len(cls._auta)):
                if s == cls._auta[i]:
                    d.append(s)
            start+=1
        return d

    @classmethod
    def usun_duplikaty(cls):
        z = set()
        for a in cls._auta:
            z.add(a)
        cls._auta=[]
        for a in z:
            cls._auta.append(a)

