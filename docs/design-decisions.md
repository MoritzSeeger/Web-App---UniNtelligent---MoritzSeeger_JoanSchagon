---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Design Decisions

### Meta

Status
: **Decided

Updated
: 19.12.2025

### Problem statement

Für das Projekt "UniNtelligent" mussten wir eine technische Basis wählen, die sowohl die Anforderungen des Kurses erfüllt als auch eine faire, objektive Informationsgrundlage für Studierende schafft. Das Hauptproblem bei bestehenden Lösungen ist oft die Subjektivität: Studierende bewerten Dozenten schlecht, nur weil eine Prüfung schwer war. Unser Ziel war es, ein System zu schaffen, das Eigenschaften (Stil) statt Noten (Leistung) in den Vordergrund stellt und technisch simpel bleibt

### Decision

Wir haben uns für einen monolithischen Flask-Stack mit SQLite und Custom CSS entschieden. Die Entscheidung basiert auf folgenden Faktoren:

Vorgabe & Fokus: Flask und Jinja2 waren Kursvorgaben. Wir haben uns entschieden, die Komplexität niedrig zu halten, um uns auf die Logik des Matching-Algorithmus zu konzentrieren.

Datenhaltung: Wir nutzen Plain SQL statt SQLAlchemy. Da unsere Datenstruktur stabil ist und nur wenige Schreibzugriffe durch User erfolgen. 

Neutralität: Das System wurde gezielt so entworfen, dass es kein klassisches Sterne-Rating gibt. Wir nutzen vordefinierte Kategorien (z.B. Kursstil, Arbeitsaufwand), um eine objektive Einschätzung statt einer emotionalen Bewertung zu ermöglichen.

### Regarded options

| Option 1: Database | Criterion | Plain SQL (Chosen) | SQLAlchemy |
| --- | --- | --- | --- |
| | **Know-how** | ✔️ SQL-Kenntnisse vorhanden | ❌ ORM muss gelernt werden |
| | **Complexity** | ✔️ Schlankes System | ❌ Zu hoher Overhead |
| | **Schema** | ❌ Manuelle Updates nötig | ❔ Gut: Klassen-Struktur |

| Option 2: Styling | Criterion | Custom CSS (Chosen) | CSS Frameworks |
| --- | --- | --- | --- |
| | **Control** | ✔️ Volle Design-Freiheit | ❌ Standard-Komponenten |
| | **Performance** | ✔️ Kein unnötiger Code | ❌ Große Library-Files |

---

## 02: Design Decision HTML/CSS

### Meta

Status
: **Decided**

Updated
: 28.12.2025

### Problem statement
Während der Entwicklung der Website, kam oft eine sehr wichtige Frage auf: Wie soll die Website aussehen und warum? Das war eine sehr wichtige, aber auch gleichzeitig schwieriege Frage. Das Ziel des Projektes war ja klar, die Umsetzungsmethoden, wie z.B. HTML, CSS, Jinja2, Python und SQLite ( oder SQAlchemy ) auch, weil es vorgaben waren, die Idee für das Projekt war auch vorhanden. Das schwierigste war für uns dennoch die Entscheidung des Aussehens der Website. Das Design muss ansprechend sein, ein guten Überblick bieten und dennoch nicht zu viel sein.

### Decision
Da unser Projekt "UniNtelligent" eine klare Lösung bietet und kein Schnick-Schnack benötigt, haben wir uns für ein suaberes, aber auch gleichzeitig geordnetes und simples Design entschieden. Unsere Zielgruppe sind Studenten, besonders Studenten der HWR-Berlin. Das Design der HWR besteht dabei aus simplen Farbelementen, sauberes weiß als Hauptfarbe mit vielen roten Akzenten drin. Dieses Desgin bietet ein einfaches, sauberes Nutzererlebnis und sieht gleichzeitig modern aus. Da wir uns auf Dozenten/Studenten der HWR fokussieren wollen, nutzen auch wir dieses Farbschema für unsere Website, mit der roten durchgehenden Navigationsleiste im Header (siehe `base.html` und `syle.css`). Das symbolisiert auch auf unserer Website eine gewisse modernität und das Gefühl, dass wir selbst zur HWR-Berlin gehören, was Vertrauen bei der Kurswahl schafft.


## 03: Design Decision Datenbank Samples

### Meta

Status
: **Decided**

Updated
: 5.01.2025

### Problem statement
Unsere Website benötigt viele Daten, damit Studenten auch Kurse suchen, Dozenten suchen und Eigenschaften der Kurse + DOzenten finden können, sodass sie ihre Kurse besser wählen können. Die Entscheidung benötigt allein schon viele Daten, die unsere Datenbank dem NUtzer bieten muss. Woher bekommen wir die Daten? Wie viel Daten sind zu viel? Was wäre eine sinnvolle Mitte für das jetzige Ziel des Projektes.

### Decision
Sinnvoll wäre in unserer jetzigen Position, dass die Datenbank = `todos.sqlite` nur Daten für unseren Campus enthält, also dem Campus Schöneberg und somit nur Daten aus dem Fachbereich 1 . DIe HWR Website bietet glücklicherweise Informationen zu allen Dozenten der HWR und man kann sogar Filtern zu welchem Fachbereich sie gehören. Da Das trotzdem durch E-Mails und weitere für uns nutzlosen Daten wieder zu viele Daten wären (mehr als 1000 Excel Zeilen nur für 100 DOzenten aus dem Fachbereich 1), haben wir mit KI unnötige INformationen rausgefiltert, sodass 119 SQL smaple Zeilen übrig blieben (Dies Sample Rohdaten sind in `insert_sample.sql` zu finden. Hinzu kamen dann noch Informationen zu Kursen etc., dass macht aber im Vergleich zu den Dozenten nicht viel aus.


