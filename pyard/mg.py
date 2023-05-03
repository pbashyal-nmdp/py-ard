from itertools import product

import pyard

ard = pyard.init()


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
        f"{allele_gl_1}/{allele_gl_2} => {allele_set_1}/{allele_set_2} = {i}/{u} => jc = {jc}"
    )
    if jc == 1:
        if len(allele_set_1) > 1 or len(allele_set_2) > 1:
            return "IM"
        else:
            return "HM"

    if 0 < jc < 1:
        return "IM"

    if jc == 0:
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

    cwd_redux_allele1 = ard.cwd_redux(ard.redux(allele1, "lgx"))
    cwd_redux_allele2 = ard.cwd_redux(ard.redux(allele2, "lgx"))

    return calculate_research_mg(cwd_redux_allele1, cwd_redux_allele2)


if __name__ == "__main__":
    p = list(product(["A*02:01"], ["A*02:01", "A*02:05"]))
    for i in p:
        print(research_mg(i[0], i[1]))
