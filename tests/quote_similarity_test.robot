*** settings ***
Documentation    General test case for checking similarity betweeen two quotes as to avoid duplicate or similar quotes
Library  ${CURDIR}${/}..\\scripts\\string_comparison.py
Library  ${CURDIR}${/}..\\scripts\\load_quotes.py

*** test cases ***
Duplicate quote test
    Set Tags    similarity check    duplicate check
    Set Test Documentation    Fails if it finds duplicate quotes

    ${quotes}=   Load Quotes                download=False  get_authors=False  get_quotes=True
    Set Suite Variable      ${quotes}

    ${duplicate}=  Filter By Similarity         ${quotes}       tolerance=1.
    Should Be Empty         ${duplicate}
    [Teardown]  Run Keywords
    ...         Run Keyword If Test Failed      Log             Duplicate quotes found!
    ...  AND    Run Keyword If Test Failed      Log             Found the following duplicate quotes:       ERROR
    ...  AND    Run Keyword If Test Failed      Log             quote ID 1 | quote ID 2 | similarity [0-1]
    ...  AND    Run Keyword If Test Failed      Log             ${duplicate}                                ERROR

quote similarity test
    Set Tags    similarity check
    Set Test Documentation    Fails if it finds too similar quotes, logs all the bad quotes as well as suspiciously similoar quotes

    ${similar}          Filter By Similarity    ${quotes}   tolerance=.50   upper_bound_ignore=.70
    ${very similar}     Filter By Similarity    ${quotes}   tolerance=.70   upper_bound_ignore=1.0

    IF  '@{similar}' != '@{EMPTY}'
    Run Keywords
    ...         Log     Some similar quotes were found              WARN
    ...  AND    Log     quote ID 1 | quote ID 2 | similarity [0-1]
    ...  AND    Log     ${similar}                                  WARN
    END

    [Teardown]  Run Keywords
    ...         Run Keyword If Test Failed      log     Found the following very similar quotes:                   ERROR
    ...  AND    Run Keyword If Test Failed      log     quote ID 1 | quote ID 2 | similarity [0-1]
    ...  AND    Run Keyword If Test Failed      Log     ${very_similar}                             ERROR

    Should Be Empty     ${very similar}