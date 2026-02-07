import pandas as pd
import numpy as np
import db

MATCH_COLUMNS = [         #[2] Mit hilfe von ChatGPT. Es was unklar das die benötigt wurde
    "teaching_style",
    "self_study",
    "character_style",
    "digital",
    "ai_usage"
]


def get_user_df(user_id):
    con = db.get_db_con()
    query = """
    SELECT teaching_style, self_study, character_style, digital, ai_usage
    FROM users
    WHERE id = ?
    """
    return pd.read_sql_query(query, con, params=(user_id,))




def get_professors_df():
    db_con = db.get_db_con()

    query = """
    SELECT  id,  surname, name, teaching_style, self_study, character_style, digital, ai_usage, theses_is_supervisor
    FROM professors
    """

    prof_df = pd.read_sql_query(query, db_con) 
    return prof_df



    def points_system():
        
        conditions = [diff == 0, diff == 1, diff == 2, diff == 3, diff == 4, diff == 5, diff == 6, diff == 7, diff == 8, diff == 9,]        #This was my original Logic for calculating matches
        points = [10, 8, 4, 2, 0, -2, -4, -6, -8, -10]
        return pd.Series(np.select(conditions, choices, default=-10), index=diff.index)     

#[2] This is the adjusted Logic given by ChatGPT 

POINTS = np.array([10, 8, 4, 2, 0, -2, -4, -6, -8, -10])

def diff_to_points(diff):       
    d = diff.to_numpy(dtype=int)
    d = np.clip(d, 0, 9)               #
    return pd.Series(POINTS[d], index=diff.index)      

def compute_matching_scores(user, prof_df):
    # Compute absolute differences per column
    diffs = prof_df[MATCH_COLUMNS].subtract(user[MATCH_COLUMNS], axis=1).abs()

    # Convert differences to points
    points = diffs.apply(diff_to_points)

    # Sum across dimensions
    prof_df["match_score"] = points.sum(axis=1)

    return prof_df.sort_values("match_score", ascending=False)



    
