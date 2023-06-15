import pandas as pd
from pyard import mg

# "BMT_CASE", "R_A_TYP1", "R_A_TYP2", "D_A_TYP1", "D_A_TYP2", "A_RES_MG"
# "BMT_CASE", "R_B_TYP1", "R_B_TYP2", "D_B_TYP1", "D_B_TYP2", "B_RES_MG"
columns_to_read = [
    "BMT_CASE",
    "R_A_TYP1",
    "R_A_TYP2",
    "D_A_TYP1",
    "D_A_TYP2",
    "A_RES_MG",
]


def row_mg(locus, id, r_typ1, r_typ2, d_typ1, d_typ2):
    print("*" * 30)
    print(f"Processing: {id}")
    r_typ1 = add_locus(locus, r_typ1)
    r_typ2 = add_locus(locus, r_typ2)
    d_typ1 = add_locus(locus, d_typ1)
    d_typ2 = add_locus(locus, d_typ2)

    final_mg = mg.research_mg_slug((r_typ1, r_typ2), (d_typ1, d_typ2))
    print(f"id: {id} => {final_mg}")
    return final_mg


def add_locus(locus, typing):
    if str(typing) != "nan":
        if ":" in typing:
            typing = f"{locus}*{typing}"
        else:  # serology
            typing = f"{locus}{typing}"
    else:
        typing = ""
    return typing


if __name__ == "__main__":
    df = pd.read_csv(
        "Q1_2023_HLA_SAVE.csv", usecols=columns_to_read, dtype={"BMT_CASE": str}
    )

    locus = "A"
    df[f"{locus}_NEW_mg"] = df.apply(
        lambda row: row_mg(locus, row[0], row[1], row[2], row[3], row[4]), axis=1
    )
    # sample = df.head(10).apply(lambda row: row_mg(locus, row[1], row[2], row[3], row[4]), axis=1)
    df.head()
    diff_df = df[df["A_RES_MG"] != df[f"{locus}_NEW_mg"]]
    diff_df.reset_index(drop=True).to_csv(f"{locus}_hlasave_diff.csv", index=False)
