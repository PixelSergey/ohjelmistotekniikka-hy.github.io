---
layout: page
permalink: /java/harjoitustyon-aloittaminen
title: Aiheen valinta ja harjoitustyön aloittaminen
---

Kurssilla seurataan Helsingin yliopiston opintokäytäntöjä. Plagiarismi ja opintovilppi, eli esimerkiksi netissä olevien tai kaverilta saatujen vastausten kopiointi ja niiden palauttaminen omana työnä on kiellettyä. Todettu opintovilppi johtaa kurssisuorituksen hylkäämiseen ja toistuva opintovilppi voi johtaa opinto-oikeuden määräaikaiseen menettämiseen. Lue lisää osoitteessa https://guide.student.helsinki.fi/fi/artikkeli/mita-ovat-vilppi-ja-plagiointi

Mitä plagiointi tarkoittaa harjoitustyön yhteydessä? Idean saa luonnollisesti lainata, mutta koodin suora kopioiminen on kiellettyä poikkeuksena muutaman rivin mittaiset algoritmit. Myös koodin rakenteen suora kopioiminen esim. siten että muuttujien ja funktioiden nimet muutetaan lasketaan plagioinniksi. Esim. kuvia saa toki lainata muualta, mutta näin tehtävessä tulee työn dokumentaatioon tehdä "lähdeviite", eli mainita mistä lainaus on tehty.

Samat plagiaattisäännöt koskevat työn dokumentaatiota, esityisen kiellettyä on copy pasteta referenssisovelluksen dokumentaatiota.

## Yleistä

Kurssin pääpainon muodostaa viikolla 2 aloitettava harjoitustyö. Harjoitustyössä toteutetaan itsenäisesti ohjelmisto omavalintaisesta aiheesta. Tavoitteena on soveltaa ja syventää ohjelmoinnin perus- ja jatkokursseilla opittuja taitoja ja harjoitella tiedon omatoimista etsimistä. Harjoitustyötä tehdään itsenäisesti, mutta tarjolla on runsaasti [pajaohjausta](/#ajankohtaista).

Harjoitustyön on edettävä [viikottaisten tavoitteiden mukaan](/#aikataulu). Työ on saatava valmiiksi kurssin aikana ja sitä on toteutettava tasaisesti, muuten kurssi katsotaan keskeytetyksi. Samaa ohjelmaa ei voi jatkaa seuraavalla kurssilla, vaan työ on aloitettava uudella aiheella alusta. Muista varata riittävästi aikaa (10-15h viikossa) koko periodin ajaksi.

Koko kurssin arvostelu perustuu pääasiassa harjoitustyöstä saataviin pisteisiin. Osa pisteistä kertyy [aikatauluun](/#aikataulu) määriteltyjen viikoittaisten välitavoitteiden kautta, osa taas perustuu työn lopulliseen palautukseen.

{% include fi_practical_work_works.md %}

## Harjoitustyön kieli ja ohjelmointikieli

Harjoitustyön ohjelmointikieli on Java tai Python. Pythoniin liittyvät ohjeet ovat [täällä](/python/viikko2#harjoitustyö).

Web-sovelluksia kurssilla ei sallita. Sovelluksissa sallitaan toki webissä olevat komponentit, mutta sovelluksen käyttöliittymän tulee olla ns. desktop-sovellus.

**Ohjelmakoodin muuttujat, luokat ja metodit kirjoitetaan englanniksi.** Dokumentaatio voidaan kirjoittaa joko suomeksi tai englanniksi.

## Ohjelman toteutus

Toteutus etenee "iteratiivisesti ja inkrementaalisesti". Tämä tarkoittaa, että heti alussa toteutetaan pieni osa ohjelman toiminnallisuudesta. Ohjelman ydin pidetään koko ajan toimivana, uutta toiminnallisuutta lisäten, kunnes tavoiteltu ohjelman laajuus on saavutettu. Ohjelman rakenteeseen kannattaa kysyä vinkkejä pajasta, sekä ottaa mallia ohjelmoinnin jatkokurssin harjoitustehtävistä ja materiaalista. Muutamia vihjeitä on myös kurssin [referenssiprojektissa](https://github.com/mluukkai/OtmTodoApp) sekä [täällä](/java/toteutus).

Iteratiiviseen tapaan tehdä ohjelma liittyy kiinteästi automatisoitu testaus. Aina uutta toiminnallisuutta lisättäessä ja vanhaa muokatessa täytyy varmistua, että kaikki vanhat ominaisuudet toimivat edelleen. Kaiken testaaminen käsin uudelleen ja uudelleen ei ole ajankäytöllisesti järkevää, ja siksi ohjelmakoodille onkin syytä laatia jatkuvasti testejä ohjelmoinnin edetessä. Testit on syytä pitää kattavina ja ajan tasalla.

Jotta ohjelmaa pystyisi testaamaan, on tärkeää että sovelluslogiikkaa [ei kirjoiteta käyttöliittymän sekaan](/java/toteutus)!

Eräs mahdollisuus on tehdä aluksi tekstikäyttöliittymän ja vasta saatuasi ohjelman perustoiminnallisuuden toteutettua voit siirtyä graafisen käyttöliittymän toteutukseen. Graafinen käyttöliittymä on mahdollista myös jättää pois, mutta tämä [vaikuttaa arvosanaan](/java/arvosteluperusteet).

Graafisen käyttöliittymän toteuttamiseen kannattaa oletusarvoisesti käyttää JavaFX:ää, jonka käytön perusteet esitellään [Ohjelmoinnin jatkokurssilla](https://materiaalit.github.io/ohjelmointi-s17/part11/). Muutamia vihjeitä liittyen JavaFX:ään [täällä](/java/toteutus).

[Arvosanan kannalta suositeltavaa](/java/arvosteluperusteet) on, että ohjelmasi tallettaa dataa joko tiedostoon tai tietokantaan. Vihjeitä tiedon tallettamiseen [täällä](/java/toteutus).

Harjoitustyön tavoitteena on tuottaa ohjelma, joka voitaisiin antaa toiselle opiskelijalle ylläpidettäväksi ja täydennettäväksi. Lopullisessa palautuksessa on oltava lähdekoodin lisäksi dokumentaatio ja automaattiset testit sekä jar-tiedosto, joka mahdollistaa ohjelman suorittamisen NetBeansin ulkopuolella.

Toivottava dokumentaation taso käy ilmi [referenssiprojektissa](https://github.com/mluukkai/OtmTodoApp).

## Esimerkkejä aiheista

### Hyvän aiheen ominaisuudet

- **Itseäsi kiinnostava aihe**

  - Innostava aihe auttaa huonoinakin hetkinä

- "Riittävän laaja"

  - Vältä eeppisiä aiheita, aloita riittävän pienestä. Yksi periodi on yllättävän lyhyt aika
  - Valitse kuitenkin aihe, jonka perustoiminnallisuuden saa toteutettua nopeasti, mutta jota saa myös laajennettua helposti
  - Hyvässä aiheessa on muutamia logiikkaluokkia, tiedoston tai tietokannankäsittelyä ja logiikasta eriytetty käyttöliittymä

- Kurssilla pääpaino on Ohjelmoinnin Perusteissa ja Jatkokurssilla opituissa asioissa

  - Käytettävyys
  - Toimivuus ja varautuminen virhetilanteisiin
  - Luokkien vastuut
  - Ohjelman selkeä rakenne
  - Laajennettavuus ja ylläpidettävyys

- **Tällä kurssilla ei ole tärkeää:**

  - Tekoäly
  - Grafiikka
  - Tietoturva
  - Tehokkuus

- **HUOMIO!** Kannattaa yrittää välttää aiheita, joissa pääpaino on tiedon säilömisessä tai käyttöliittymässä. Paljon tietoa säilövät, esim. yli 3 tietokantataulua tarvitsevat sovellukset ovat vaikeita testata tämän kurssin esitietovaatimusten puitteissa, ja ne sopivat yleensä paremmin Tietokantasovellus-kurssille. Käyttöliittymäkeskeisissä aiheissa (esim. tekstieditori) voi olla vaikea keksiä sovelluslogiikkaa, joka on enemmän tämän kurssin painopiste (myös siksi koska käyttöliittymää ei tällä kurssilla testata ja testaus on kurssin keskeinen aihe - jos ei ole sovelluslogiikkaa, on vaikea myös kirjoittaa sille testejä)

### Esimerkkejä aiheista

Oman aiheen ei ole pakko olla allaolevasta listasta. Listassa on kuitenkin erilaisia esimerkkejä, joista voi toteuttaa oman versionsa.

- Hyötyohjelmat

  - Aritmetiikan harjoittelua
  - Tehtävägeneraattori, joka antaa käyttäjälle tehtävän sekä mallivastauksen (esim. matematiikkaa, fysiikkaa, kemiaa, ...)
  - Opintojen seurantajärjestelmä
  - Code Snippet Manageri
  - Laskin, funktiolaskin, graafinen laskin
  - Budjetointisovellus
  - HTML WYSIWYG-editor (What you see is what you get)

- Reaaliaikaiset pelit

  - Tetris
  - Pong
  - Pacman
  - Tower Defence
  - Asteroids
  - Space Invaders
  - Yksinkertainen tasohyppypeli, esimerkiksi The Impossible Game

- Vuoropohjaiset pelit

  - Tammi
  - Yatzy
  - Miinaharava
  - Laivanupotus
  - Yksinkertainen roolipeli tai luolastoseikkailu
  - Sudoku
  - Muistipeli
  - Ristinolla (mielivaltaisen kokoisella ruudukolla?)
  - 2048

- Korttipelit

  - En Garde
  - Pasianssi
  - UNO
  - Texas Hold'em

- Omaan tieteenalaan, sivuaineeseen tai harrastukseen liittyvät hyötyohjelmat
  - Yksinkertainen fysiikkasimulaattori
  - DNA-ketjujen tutkija
  - Keräilykorttien hallintajärjestelmä
  - Pelin hahmogeneraattori, joka tallentaa tiedostoon (esim. D&D hahmolomake)
  - Fraktaaligeneraattori

## Harjoitustyön aloitus

Harjoitustyö siis aloitetaan kurssin [toisella viikolla](/java/viikko2).

Työ tehdään samaan repositorioon, jonka olet rekisteröinyt Labtooliin ja johon olet jo tehnyt [viikon 1 laskareiden](/java/viikko1) palautuksen.

### GitHubissa olevan repositorion kloonaaminen

Jos haluat tehdä harjoitustyötä eri koneella, kuin mille teit repositoriosi alunperin, saat koodin siirrettyä toiselle koneelle kloonaamalla repositorion.

Koneeseesi täytyy luonnollisesti [ensin asentaa](https://git-scm.com/downloads) git jos se ei ole jo koneellasi.

- Muista myös [oleellisten konfiguraatioiden](/java/viikko1#konfiguraatioita) tekeminen

Koneesi julkinen avain on talletettava GitHubiin. Ohje avaimen generointiin ja tallettamiseen [täällä](/java/viikko1#julkinen-avain).

Kloonaus tapahtuu seuraavasti

- avaa palautusrepositoriosi
- klikkaa kohtaa _clone or download_ ja kopioi kloonausurl
  - varmista että valittuna on "clone with SSH"

![](/assets/images/a-1.png)

- mene sopivaan hakemistoon paikallisella koneella
  - **ÄLÄ** kuitenkaan mene minkään git-repositorion sisälle
- anna kloonauskomento _git clone_ parametrina kloonausurl

```
mluukkai@melkinkari:~$ git clone git@github.com:mluukkai/otm-harjoitustyo.git
Cloning into 'otm-harjoitustyo'...
remote: Counting objects: 29, done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 29 (delta 5), reused 17 (delta 2), pack-reused 0
Receiving objects: 100% (29/29), 4.83 KiB | 0 bytes/s, done.
Resolving deltas: 100% (5/5), done.
```

Hakemistoosi syntyy uusi hakemisto, esimerkissä nimeltään _otm-harjoitustyo_, eli oletusarvoisesti nimi päätellään kloonausurlista. Uuden hakemiston nimen voi myös määritellä itse antamalla komennolle lisäparametrin:

```
git clone git@github.com:mluukkai/otm-harjoitustyo.git hakemiston_nimi
```

Syntynyt hakemisto on nyt git-repositorio, jonka sisältö on sama kuin etärepositoriossa.

- tee repositorioon jokin muutos, lisää ja committoi
- pushaa muutokset githubiin ja varmista GitHubista että muutos menee perille

**HUOM** jos _git push_ ei toimi, eli saat seuraavan virheilmoituksen

```
ERROR: Permission to mluukkai/otm-harjoitustyo.git denied to mluukkai.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

niin voit siirtyä käyttämään _HTTPS_-muotoista kloonausurlia:

![](/assets/images/a-2.png)

joudut poistamaan ensin vanhan kloonausurlin ja lisäämään uuden antamalla seuraavat komennot:

```
git remote rm origin
git remote add origin https://github.com/mluukkai/otm-harjoitustyo.git
```

Ikävä seuraus tästä on se, että GitHub kysyy jokaisen pushaamisen yhteydessä salasanaasi.

### Työskentely usealla koneella

Jos työskentelet monella koneella niin huomioi seuraavat

- GitHubissa oleva repositorion tulee olla kloonattuna kaikille koneille
- Oletusarvoisesti kaikkien koneiden julkiset avaimet kannattaa olla määritelty GitHubiin
- [oleelliset konfiguraatiot](/java/viikko1#konfiguraatioita) kannattaa olla tehtynä kaikilla koneilla
- **TÄRKEÄÄ** aina kun lopetat työskentelyn koneella, pushaa muutokset githubiin
- kun aloitat työskentelyn koneelta, pullaa muutokset githubista
- jos (ja kun) törmäät seuraavaan virheeseen

```
mluukkai@melkki:~/otm-harjoitustyo$ git push
To git@github.com:mluukkai/otm-harjoitustyo.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:mluukkai/otm-harjoitustyo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
mluukkai@melkki:~/otm-harjoitustyo$
```

- tilanne korjautuu kun ensin pullaat githubin sisällön

### Maven-projektin luominen

Harjoitustyössä tehtävä ohjelmisto tehdään maven-projektina. Projektin luominen onnistuu NetBeansin avulla seuraavasti:

- valitse _new project_ ja tee seuraavat valinnat:
  <img src="https://raw.githubusercontent.com/mluukkai/ohjelmistotekniikka-syksy-2020/main/web/images/a-3.png">

- Vaikka käyttäisit JavaFX:ää, kannattaa projektia varten silti luoda "normaali" maven-projekti ellet päätä käyttää [FXML:ää](/java/toteutus#fxml)

- määrittele kentän _Project location_ arvoksi repositoriosi juuri
  <img src="https://raw.githubusercontent.com/mluukkai/ohjelmistotekniikka-syksy-2020/main/web/images/a-4.png" width="600">

- luo repositoriosi juureen tiedosto _.gitignore_ ja lisää sinne rivi, joka ignoroi luodun projektin hakemiston alle tulevan hakemiston _target_. Omassa esimerkissäni rivi olisi

```
Pokemontietokanta/target
```

- lisää muutokset versionhallintaan, commitoi ja pushaa
- varmista että GitHub-näkymä näyttää suunilleen seuraavalta
  <img src="https://raw.githubusercontent.com/mluukkai/ohjelmistotekniikka-syksy-2020/main/web/images/a-5.png" width="600">

Pääset oletusarvoisella konfiguraatiolla alkuun. Lisää ohjeita mavenin konfigurointiin [täällä](/java/maven)

## Työaikakirjanpito

Pidä säännöllisesti kirjaa käyttämistäsi työtunneista. Käytettyjen työtuntien määrä ei vaikuta arvosanaan, _mutta_ vajavaisesti pidetty työaikakirjanpito alentaa työn arvosanaa.

Lisää repositorioon linkki [työaikakirjanpitoon](https://github.com/mluukkai/OtmTodoApp/blob/master/dokumentaatio/tuntikirjanpito.md).
