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
: **Work in progress** - Decided - Obsolete

Updated
: 19.12.2025

### Problem statement

Für das Projekt "ProfMatch" mussten wir eine technische Basis wählen, die sowohl die Anforderungen des Kurses erfüllt als auch eine faire, objektive Informationsgrundlage für Studierende schafft. Das Hauptproblem bei bestehenden Lösungen ist oft die Subjektivität: Studierende bewerten Dozenten schlecht, nur weil eine Prüfung schwer war. Unser Ziel war es, ein System zu schaffen, das Eigenschaften (Stil) statt Noten (Leistung) in den Vordergrund stellt und technisch simpel bleibt

### Decision

Wir haben uns für einen monolithischen Flask-Stack mit SQLite und Custom CSS entschieden. Die Entscheidung basiert auf folgenden Faktoren:

Vorgabe & Fokus: Flask und Jinja2 waren Kursvorgaben. Wir haben uns entschieden, die Komplexität niedrig zu halten, um uns auf die Logik des Matching-Algorithmus zu konzentrieren.

Datenhaltung: Wir nutzen Plain SQL statt SQLAlchemy. Da unsere Datenstruktur stabil ist und nur wenige Schreibzugriffe durch User erfolgen. 

Neutralität: Das System wurde gezielt so entworfen, dass es kein klassisches Sterne-Rating gibt. Wir nutzen vordefinierte Kategorien (z.B. Kursstil, Arbeitsaufwand), um eine objektive Einschätzung statt einer emotionalen Bewertung zu ermöglichen.

### Regarded options

Option 1: Database Access - Plain SQL vs. SQLAlchemy | Criterion | Plain SQL (Chosen) | SQLAlchemy | | --- | --- | --- | | Know-how | ✔️ Vorhandene SQL-Kenntnisse konnten direkt genutzt werden | ❌ Hohe Lernkurve für ORM-Konzepte & Syntax | | Complexity | ✔️ Schlankes System ohne zusätzlichen Abstraktionslayer | ❌ Overkill für ein Projekt mit stabilen Datenstrukturen | | Change DB schema | ❌ SQL über den Code verteilt; manuelle Updates nötig | ❔ Gut: Klassen-Struktur, bad: braucht Alembic |

Option 2: Styling - Custom CSS vs. Bootstrap | Criterion | Custom CSS (Chosen) | CSS Frameworks | | --- | --- | --- | | Control | ✔️ Volle Freiheit über das Branding und Layout | ❌ Eingeschränkt durch Standard-Komponenten | | Performance | ✔️ Minimaler Code; kein Laden ungenutzter Klassen | ❌ Große Libraries verursachen unnötigen Overhead |

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
