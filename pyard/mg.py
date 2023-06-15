from itertools import product

import pyard

ard = pyard.init()

mg_hierarchy = {"HM": 4, "Hmm": 3, "IM": 2, "Imm": 1}

mg_reverse = {4: "HM", 3: "Hmm", 2: "IM", 1: "Imm"}


def find_antigen_group(allele_set):
    """
    Find unique antigen groups of allele set

    @param allele_set: A set of alleles
    @return: set of antigen group
    """
    return {allele.split(":")[0] for allele in allele_set}


def calculate_research_mg(allele_gl_1, allele_gl_2) -> str:
    """
    Research Match Grade is based on [Jaccard Index](https://en.wikipedia.org/wiki/Jaccard_index).

    The following table describes the Jaccard index value and
    the corresponding *Research Match Grade*

    | Jaccard Index | Research MG |
    |---------------|-------------|
    | J = 1         | HM          |
    | 0 < J < 1     | IM          |
    | J = 0         | Hmm/Imm     |

    Exception:
    If J = 1 and
        if len(allele_set_1) > 1 or len(allele_set_2) > 1
        then Research MG = IM

    :param allele_gl_1: Ambiguous allele list of an allele in GL String format
    :param allele_gl_2: Ambiguous allele list of an allele in GL String format
    """
    allele_set_1 = set(allele_gl_1.split("/"))
    allele_set_2 = set(allele_gl_2.split("/"))
    # find length of intersection and unions of the elements of the set(alleles)
    i = len(allele_set_1.intersection(allele_set_2))
    u = len(allele_set_1.union(allele_set_2))
    # Jaccard coefficient is defined as a ratio of length of intersection
    # over length of union
    jc = i / u

    print(
        f"\t{allele_gl_1}÷{allele_gl_2} => {allele_set_1}÷{allele_set_2} = {i}÷{u} => jc = {jc}"
    )
    if jc == 1:
        if len(allele_set_1) > 1 or len(allele_set_2) > 1:
            return "IM"
        else:
            return "HM"

    if 0 < jc < 1:
        return "IM"

    if jc == 0:
        antigen_group_1 = find_antigen_group(allele_set_1)
        antigen_group_2 = find_antigen_group(allele_set_2)
        if antigen_group_1 == antigen_group_2:
            print(f"\tSame antigen group: {antigen_group_1} vs {antigen_group_2}")
            return "Hmm"
        return "Imm"

    raise ValueError(
        f"Unable to calculate match grade for {allele_gl_1} and {allele_gl_2}"
    )


def research_mg(allele1, allele2) -> str:
    if not allele1 and not allele2:
        raise ValueError(f"Unable to calculate match grade for {allele1} and {allele2}")

    # Make a blank allele be homozygous
    if allele1 and not allele2:
        allele2 = allele1
    elif allele2 and not allele1:
        allele1 = allele2

    cwd_redux_allele1 = ard.cwd_redux(allele1)
    cwd_redux_allele2 = ard.cwd_redux(allele2)

    return calculate_research_mg(cwd_redux_allele1, cwd_redux_allele2)


def research_mg_slug(recipient, donor) -> str:
    r_typ_1, r_typ_2 = recipient
    # If recipient typing is missing, it's N:N
    if not r_typ_1 and not r_typ_2:
        return "N:N"
    # Homozygous if the other one is missing
    if not r_typ_2:
        r_typ_2 = r_typ_1
    elif not r_typ_1:
        r_typ_1 = r_typ_2

    d_typ_1, d_typ_2 = donor
    # If donor's typing is missing, it's N:N
    if not d_typ_1 and not d_typ_2:
        return "N:N"
    # Homozygous if the other one is missing
    if not d_typ_2:
        d_typ_2 = d_typ_1
    elif not d_typ_1:
        d_typ_1 = d_typ_2

    recip1_donor = product([r_typ_1], [d_typ_1, d_typ_2])
    match_grades = []
    for r_d_pair in recip1_donor:
        print(f"Pair:{r_d_pair}")
        mg = research_mg(r_d_pair[0], r_d_pair[1])
        match_grades.append(mg)
        print(f"\t{mg}")

    mg_val1 = max(mg_hierarchy[match_grades[0]], mg_hierarchy[match_grades[1]])
    print(f"{match_grades} Match Grade: {mg_reverse[mg_val1]} Index: {mg_val1}")
    print()

    recip2_donor = product([r_typ_2], [d_typ_1, d_typ_2])
    match_grades = []
    for r_d_pair in recip2_donor:
        print(f"Pair:{r_d_pair}")
        mg = research_mg(r_d_pair[0], r_d_pair[1])
        match_grades.append(mg)
        print(f"\t{mg}")

    mg_val2 = max(mg_hierarchy[match_grades[0]], mg_hierarchy[match_grades[1]])
    print(f"{match_grades} Match Grade: {mg_reverse[mg_val2]} Index: {mg_val2}")

    final_mg = f"{mg_reverse[mg_val1]}:{mg_reverse[mg_val2]}"
    return final_mg


if __name__ == "__main__":
    """
    A row from HLA SAVE
      | R_TYP1        | R_TYP2        | D_TYP1        | D_TYP2        | DNA_MG   |
      | A*01:01       | A*68:01       | A*02:01:01    | A*68:01:02:01 | Imm:HM   |

      13:02,35:03,35:03,15:XX
    """

    # recipient = {"R_TYP1": "B*13:01", "R_TYP2": "B*35:03"}
    recipient = {"R_TYP1": "A*30:01", "R_TYP2": "A*30:02"}

    # donor = {"D_TYP1": "B*35:03", "D_TYP2": "B*15:XX"}
    donor = {"D_TYP1": "A*30:AB", "D_TYP2": "A*74:XX"}

    final_mg = research_mg_slug(
        (recipient["R_TYP1"], recipient["R_TYP2"]), (donor["D_TYP1"], donor["D_TYP2"])
    )
    # recip1_donor = list(
    #     product([recipient["R_TYP1"]], [donor["D_TYP1"], donor["D_TYP2"]])
    # )
    # match_grades = []
    # for r_d_pair in recip1_donor:
    #     print(r_d_pair)
    #     mg = research_mg(r_d_pair[0], r_d_pair[1])
    #     match_grades.append(mg)
    #     print(mg)
    #
    # mg_val1 = max(mg_hierarchy[match_grades[0]], mg_hierarchy[match_grades[1]])
    # print(f"{match_grades} Match Grade: {mg_val1}")
    #
    # recip2_donor = list(
    #     product([recipient["R_TYP2"]], [donor["D_TYP1"], donor["D_TYP2"]])
    # )
    # match_grades = []
    # for r_d_pair in recip2_donor:
    #     print(r_d_pair)
    #     mg = research_mg(r_d_pair[0], r_d_pair[1])
    #     match_grades.append(mg)
    #     print(mg)
    # mg_val2 = max(mg_hierarchy[match_grades[0]], mg_hierarchy[match_grades[1]])
    # print(f"{match_grades} Match Grade: {mg_val2}")

    # final_mg = f"{mg_reverse[mg_val1]}:{mg_reverse[mg_val2]}"
    print(final_mg)
