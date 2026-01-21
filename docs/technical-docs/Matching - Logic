# Matching Algorithm

## Goal
To compute a compatibility score between a student and each professor based on five traits.

## Traits
1. Teaching Style  
2. Self-Study  
3. Character  
4. Digital  
5. AI Usage  

EACH TRAIT IS SCORED 1-10

-------

The matching logic is based on a points differential system. On an absolute level, it compares the 5 “Traits” that are assigned to professors and those picked by the user.

This algorithm places a large focus on matching users to professors with exact value-matches and conversely tries to hide professors from the user which have an attribute far from the users own.

#Logic breakdown:

### Point Mapping

| Difference | Points | Interpretation |
|------------|--------|----------------|
0 | 10 | Exact
1 | 8 | Great
2 | 4 | Good
3 | 2 | Acceptable
4 | 0 | Indifferent
5 | -2 | Unsatisfactory
6 | -4 | Bad
7 | -6 | Poor
8 | -8 | Terrible
9 | -10 | Worst

## Final Score

The final compatibility score is the sum of the points from all five traits.

## Example

Student: `5 | 3 | 9 | 1 | 4`

Professor A: `3 | 4 | 6 | 6 | 2`
→ 4 + 8 + 2 + 8 + 8 = **30 (Good Match)**

Professor B: `1 | 4 | 6 | 6 | 6`
→ 0 + 8 + 2 - 1 + 4 = **13 (Acceptable Match)**

Professor C: `9 | 5 | 1 | 10 | 7`
→ 0 + 4 - 8 - 10 + 2 = **-12 (Bad Match)**

## Limitations
- Linear scoring
- No weighting
- Trait scale is subjective
## Future imporvements
- Weighted traits
- Machine learning-based matching
- User-adjustable priorities

I realise this system is not perfect and may change in the future. If you have any improvement suggestions please let me know :) - Joan Schagon
