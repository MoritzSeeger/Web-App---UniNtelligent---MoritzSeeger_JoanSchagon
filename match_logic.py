import pandas as pd
import db

MATCH_COLUMNS = [         #[2] ChatGPT
    "teaching_style",
    "self_study",
    "character_style",
    "digital",
    "ai_usage"
]


def get_user_df(db_path):

    db_con = db.get_db_con()
    query = """
    SELECT teaching_style, selfstudy AS self_study, character_Style AS character_style, digital, ai_usage
    FROM users
    WHERE id = ?
    """
    df = pd.read_sql_query(query, db_con, params=(id,))

    return df.iloc[0]   # Help from ChatGPT




def get_professors_df():
    db_con = db.get_db_con()

    query = """
    SELECT  id,  surname, name, teaching_style, self_study, character_style, digital, ai_usage, theses_is_supervisor
    FROM professors
    """

    prof_df = pd.read_sql_query(query, db_con) #Help from ChatGPT
    return prof_df



    def points_system():
        
        conditions = [diff == 0, diff == 1, diff == 2, diff == 3, diff == 4, diff == 5, diff == 6, diff == 7, diff == 8, diff == 9,]        #This was my original Logic for calculating matches
        points = [10, 8, 4, 2, 0, -2, -4, -6, -8, -10]
        return pd.Series(np.select(conditions, choices, default=-10), index=diff.index)     



def diff_to_points(diff):
    bins = [-1,0,1,2,3,4,5,6,7,8,9,100]
    scores = [10,8,4,2,0,-2,-4,-6,-8,-10,-10]
    return pd.cut(diff, bins=bins, labels=scores).astype(int)           #[2] This is the adjusted Logic given by ChatGPT 

def compute_matching_scores(user, prof_df):
    # Compute absolute differences per column
    diffs = prof_df[MATCH_COLUMNS].subtract(user[MATCH_COLUMNS], axis=1).abs()

    # Convert differences to points
    points = diffs.apply(diff_to_points)

    # Sum across dimensions
    prof_df["match_score"] = points.sum(axis=1)

    return prof_df.sort_values("match_score", ascending=False)



    
