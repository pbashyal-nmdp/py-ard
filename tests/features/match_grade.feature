@wip
Feature: Match Grade
  # Enter feature description here

  Scenario Outline: Research Match Grade

    Given The first typing for a recipient is <R_TYP1>
    And The second typing for a recipient is <R_TYP2>
    And The first typing for a donor is <D_TYP1>
    And The second typing for a donor is <D_TYP2>
    When We calculate the research match grade
    Then The research match grade is <DNA_MG>

    Examples:

      | R_TYP1        | R_TYP2        | D_TYP1        | D_TYP2        | DNA_MG   |
      | A*01:01       | A*68:01       | A*02:01:01    | A*68:01:02:01 | Imm:HM   |
      | A*01:01       | A*03:02       | A*01:CAVHH    | A*03:YXPV     | HM:HM    |
      | A*03:01:01    | A*11:01:01    | A*03:01       | A*11:01       | HM:HM    |
      | A*02:01:01    | A*03:01:01    | A*02:AAFWZ    | A*03:AAGYA    | IM:HM    |
      | A*03:01       | A*31:01       | A*03:01       | A*31:01       | HM:HM    |
      | A*02:01       |               | A*02:01       | A*02:01       | HM:HM    |
      | A*31:01:02    | A*33:03:01    | A*31:01:02    | A*33:03:01    | HM:HM    |
      | A*02:05:01:01 | A*29:01:01:01 | A*02:01:01:01 | A*02:05:01:01 | HM:Imm   |
      | A*02:03:01    | A*30:01:01    | A*02:03:01G   | A*30:01:01G   | HM:HM    |
